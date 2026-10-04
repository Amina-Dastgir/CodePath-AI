import streamlit as st
from crewai import LLM

# Gemini model used by all CodePath AI agents.

MODEL_NAME = "gemini/gemini-2.5-flash"

def create_llm(model_name: str = MODEL_NAME):
"""
Create and return a CrewAI LLM configured for Google Gemini.

```
model_name is optional so both of these work:

    create_llm()
    create_llm(MODEL_NAME)
"""

api_key = st.secrets.get("GEMINI_API_KEY", "")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. "
        "Add it in Streamlit Cloud → Manage app → Settings → Secrets."
    )

return LLM(
    model=model_name,
    api_key=api_key,
    temperature=0.2,
)
```
