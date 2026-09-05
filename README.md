# AeroTime — Weather & Local Time AI Agent 🌤️🕒

A lightweight, specialized AI agent built with **Google Agent Development Kit (ADK)** and powered by **Gemini Flash**. AeroTime handles live weather queries and timezone-aware local time conversions using autonomous function calling and strict behavioral guardrails.

---

## 🌟 Key Features

- **Autonomous Tool Routing:** Dynamic schema extraction and parameter binding for custom Python tools (`get_weather`, `get_current_time`).
- **Strict Guardrails:** Configured system instructions prevent generic LLM hallucinations and enforce domain specialization (weather & time only).
- **Fast Execution:** Configured for low-latency REST transport over standard Google GenAI endpoints.
- **Multi-Interface Access:** Interactive command-line chat (`adk run`) and a visual evaluation playground (`adk web`).

---

## 📁 Project Structure

```text
my-first-agent/
├── app/
│   ├── __init__.py
│   ├── agent.py          # Core Agent definition, tools, and system prompt
│   └── fastapiapp.py     # Optional FastAPI integration layer
├── .env.example          # Environment template (safe for Git)
├── .gitignore            # Excludes secrets & virtual envs
├── requirements.txt      # Dependency specification
└── README.md             # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.10 to 3.13
- A Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/apikey)

### 2. Setup Virtual Environment

```bash
# Clone the repository
git clone https://github.com/aadityasharma101107/gemini-aerotime-agent.git
cd gemini-aerotime-agent

# Create virtual environment
python -m venv .venv

# Activate on Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate on Linux / macOS
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root based on `.env.example`:

```env
GEMINI_API_KEY="your_actual_gemini_api_key_here"
GOOGLE_GENAI_USE_VERTEXAI="false"
GOOGLE_GENAI_CLIENT_TRANSPORT="rest"
```

---

## 💻 Running the Agent

### Terminal Interactive Mode (CLI)

```bash
adk run app
```

### Visual Web Inspector UI

To inspect function calling traces, payloads, and tokens visually:

```bash
adk web app
```

Navigate to `http://localhost:8000` in your browser.

---

## 🧪 Example Test Prompts

| Intent | Sample Prompt | Expected Behavior |
|---|---|---|
| **Capability Check** | `Hi, what can you do?` | Introduces itself strictly as a weather and time assistant. |
| **Tool Execution** | `What is the weather in San Francisco?` | Calls `get_weather(location="San Francisco")` and returns conditions. |
| **Multi-Tool Chaining** | `Give me the time and weather for Delhi.` | Sequentially calls both tools and synthesizes the answer. |
| **Guardrail Boundary** | `Write a Python script for binary search.` | Refuses off-topic task and reaffirms its weather/time focus. |

---

## 🛠️ Built With

- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python)
- [Google GenAI SDK](https://github.com/googleapis/python-genai)
- [Gemini Flash](https://aistudio.google.com/)

---

## 📄 License

This project is licensed under the Apache 2.0 License.
