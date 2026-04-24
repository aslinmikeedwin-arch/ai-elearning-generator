"""
ai_engine.py
------------
This is the core AI engine of the project.
It connects Python to Claude API (Anthropic) for online use.
The API key is stored securely in Streamlit secrets — not in the code!
"""

import requests
import os

# Get API key from environment variable or Streamlit secrets
def get_api_key():
    # Try Streamlit secrets first (for online deployment)
    try:
        import streamlit as st
        return st.secrets["ANTHROPIC_API_KEY"]
    except:
        pass
    # Fall back to environment variable (for local use)
    return os.environ.get("ANTHROPIC_API_KEY", "")

CLAUDE_MODEL = "claude-haiku-4-5-20251001"

def ask_ollama(prompt: s
