import streamlit as st
from crewai import LLM


MODEL_NAME = "gemini/gemini-2.5-flash"


def create_llm(model_name: str = MODEL_NAME):
    """Create the Gemini LLM used by CodePath AI agents."""

    api_key = st.secrets.get("GEMINI_API_KEY", "")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing from Streamlit Secrets."
        )

    return LLM(
        model=model_name,
        api_key=api_key,
        temperature=0.2,
    )
