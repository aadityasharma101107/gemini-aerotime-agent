

import os
import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

import urllib.parse
import urllib.request
import json


def get_weather(location: str) -> str:
    """Fetches real-time weather using Open-Meteo (no API key required)."""
    try:
        # Step A: Geocode city name to lat/lon
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={urllib.parse.quote(location)}&count=1&language=en&format=json"
        req = urllib.request.Request(geo_url, headers={"User-Agent": "AeroTimeAgent/1.0"})
        with urllib.request.urlopen(req, timeout=5) as res:
            geo_data = json.loads(res.read().decode())
        
        if not geo_data.get("results"):
            return f"Could not find coordinates for '{location}'."
        
        place = geo_data["results"][0]
        lat, lon = place["latitude"], place["longitude"]
        city_name = place.get("name", location)
        country = place.get("country", "")

        # Step B: Fetch current weather
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        with urllib.request.urlopen(weather_url, timeout=5) as res:
            w_data = json.loads(res.read().decode())
        
        curr = w_data["current_weather"]
        temp_c = curr["temperature"]
        wind = curr["windspeed"]
        return f"{city_name}, {country}: {temp_c}°C, Wind Speed: {wind} km/h."
    except Exception as e:
        return f"Weather lookup failed: {str(e)}"

def get_current_time(location: str) -> str:
    """Gets the current local time for a specified city.

    Args:
        location: The name of the city or region to query.

    Returns:
        The current local time formatted with timezone info.
    """
    loc = location.lower()

    tz_map = {
        "san francisco": "America/Los_Angeles",
        "sf": "America/Los_Angeles",
        "delhi": "Asia/Kolkata",
        "london": "Europe/London",
        "tokyo": "Asia/Tokyo",
        "new york": "America/New_York",
    }

    tz_identifier = None
    for city, tz in tz_map.items():
        if city in loc:
            tz_identifier = tz
            break

    if not tz_identifier:
        return f"Timezone data not found for '{location}'. Try cities like Delhi, London, Tokyo, or San Francisco."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"Current local time in {location.title()} is {now.strftime('%I:%M %p (%Z, %Y-%m-%d)')}."
    

root_agent = Agent(
    name="weather_time_agent",
    model=Gemini(
        model="gemini-3.6-flash",
        retry_options=types.HttpRetryOptions(attempts=1),
    ),
    instruction="""You are 'AeroTime', a focused Weather and Local Time AI Assistant.

Your capabilities:
1. Provide accurate weather conditions using the `get_weather` tool.
2. Provide the current local time using the `get_current_time` tool.

Guidelines:
- When greeted or asked about your capabilities, introduce yourself strictly as a Weather and Time assistant.
- Always call the corresponding tool when a user mentions a city, weather, or time. Never hallucinate forecasts without consulting tools.
- If a user asks for unrelated tasks (writing essays, solving DSA problems, generating general code), politely decline and state that you are specialized exclusively for weather and time inquiries.
""",
    tools=[get_weather, get_current_time],
)

app = App(
    root_agent=root_agent,
    name="app",
)
