# ⚡ CodePath AI

A multi-agent programming and learning assistant built with Streamlit, CrewAI, and Google's Gemini API.

## Features
- Personalized learning roadmap generation
- Beginner-friendly programming concept explanations
- Code generation
- Basic code/output review
- Separate modules for each agent
- Tool-enabled agent workflow
- Live agent-stage indicators in the UI
- Download results as Markdown

## Project structure

```text
CodePath_AI/
├── app.py
├── settings.py
├── requirements.txt
├── agents/
│   ├── __init__.py
│   ├── requirement_agent.py
│   ├── roadmap_agent.py
│   ├── code_agent.py
│   └── reviewer_agent.py
├── tools/
│   ├── __init__.py
│   └── learning_tools.py
└── .streamlit/
    └── config.toml
```

## Setup on Streamlit Community Cloud

1. Upload these files to a GitHub repository, preserving the folder paths.
2. Open https://share.streamlit.io and create an app.
3. Select the repository, branch `main`, and main file path `app.py`.
4. In Advanced settings, choose Python 3.12 if available.
5. Add this in the Secrets box:

```toml
GEMINI_API_KEY = "paste-your-Gemini-API-key-here"
```

6. Deploy the app.

## API key
Create a key through Google AI Studio: https://aistudio.google.com/apikey

Never commit your API key to GitHub. Use Streamlit Community Cloud Secrets.

## Important notes
- Each workflow explicitly runs its assigned custom tool to produce a preflight checklist/report, then passes that result to the specialist agent. The same tool is also attached to the CrewAI agent for additional use when needed.
- The Output Validation Tool uses Python's built-in `ast` parser for Python syntax only; it does not execute code.
- For non-Python languages, the tool performs a simple delimiter check, not compilation.
- Generated code can be incorrect. Review and test it in a safe environment before using it.
- The app does not execute user-submitted or AI-generated code.
- This code has been organized for cloud deployment, but package resolution and Gemini API access must still be confirmed in the deployed app. Check Streamlit logs if deployment fails.
