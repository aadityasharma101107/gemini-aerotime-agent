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
├── .env.example          # Environment template
├── requirements.txt      # Dependency specification
└── README.md             # Project documentation


## 🚀 Getting Started
# 1. Prerequisites
Python 3.10 to 3.13

A Gemini API Key from Google AI Studio

# 2. Setup Virtual EnvironmentBash# Clone the repository
git clone [https://github.com/your-username/my-first-agent.git](https://github.com/your-username/my-first-agent.git)
cd my-first-agent

# Create and activate virtual environment
python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# Linux / macOS
source .venv/bin/activate
3. Install DependenciesBashpip install -r requirements.txt
4. Configure Environment VariablesCreate a .env file in the project root:
Code snippetGEMINI_API_KEY="your_actual_gemini_api_key_here"
GOOGLE_GENAI_USE_VERTEXAI="false"
GOOGLE_GENAI_CLIENT_TRANSPORT="rest"
💻 Running the AgentTerminal Interactive Mode (CLI)Bashadk run app
Visual Web Inspector UITo inspect function calling traces, payloads, and tokens visually:Bashadk web app
Navigate to http://localhost:8000 in your browser.

🛠️ Built WithGoogle Agent Development Kit (ADK)  Google GenAI SDKGemini Flash
📄 LicenseThis project is licensed under the Apache 2.0 License.
---

### Recommended `.gitignore` Check

Make sure your `.gitignore` includes the following lines before running `git add .` and committing:

```gitignore
.venv/
__pycache__/
*.pyc
.env
.adk/