from crewai import LLM

MODEL_NAME = "gemini/gemini-3.8-flash"


def create_llm(api_key: str) -> LLM:
    """Create the Gemini language model used by all agents."""
    if not api_key or not api_key.strip():
        raise ValueError("A Gemini API key is required.")
    return LLM(
        model=MODEL_NAME,
        api_key=api_key.strip(),
        temperature=1.0,
    )
