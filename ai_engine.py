import requests
import os

CLAUDE_MODEL = "claude-haiku-4-5-20251001"

def get_api_key():
    try:
        import streamlit as st
        return st.secrets["ANTHROPIC_API_KEY"]
    except:
        return os.environ.get("ANTHROPIC_API_KEY", "")

def ask_ollama(prompt, model=None, host=None):
    api_key = get_api_key()
    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        },
        json={
            "model": CLAUDE_MODEL,
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}]
        },
        timeout=60
    )
    data = response.json()
    return data["content"][0]["text"].strip()
