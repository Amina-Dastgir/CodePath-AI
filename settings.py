import streamlit as st
from crewai import LLM

MODEL_NAME = "openai/gpt-oss-120b"


def create_llm(model_name: str = MODEL_NAME):
    """Create the Groq LLM used by CodePath AI agents."""

    api_key = st.secrets.get("GROQ_API_KEY", "")

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is missing from Streamlit Secrets."
        )

    return LLM(
        model=model_name,
        api_key=api_key,
        temperature=0.2,
        num_retries=3,
    )
