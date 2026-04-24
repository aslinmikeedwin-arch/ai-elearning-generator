"""
ai_engine.py
------------
This is the core AI engine of the project.
It connects Python to Ollama (a local AI model running on your Mac).
Think of it as the "messenger" between your code and the AI.
"""

import requests


def ask_ollama(prompt: str, model: str = "llama3.2", host: str = "http://localhost:11434") -> str:
    """
    Send a question (prompt) to Ollama and get a text response back.

    Parameters:
    - prompt: The question or instruction you want to send to the AI
    - model:  The AI model to use (default: llama3.2)
    - host:   The address where Ollama is running (default: localhost)

    Returns:
    - The AI's response as a plain string
    """

    # The URL where Ollama listens for requests
    url = f"{host}/api/generate"

    # Package the prompt and model name into a request
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False  # Get the full response at once, not word by word
    }

    # Try to send the request to Ollama
    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()  # Raise an error if something went wrong
    except requests.exceptions.ConnectionError:
        # This happens when Ollama is not running
        raise ConnectionError(
            f"Could not connect to Ollama at {host}. "
            "Make sure Ollama is installed and running (`ollama serve`)."
        )
    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"Ollama API returned an error: {e}")

    # Extract the response text from the JSON reply
    data = response.json()
    if "response" not in data:
        raise RuntimeError(f"Unexpected response format from Ollama: {data}")

    return data["response"].strip()


# ── Quick test ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_prompt = "What is 2 + 2? Answer in one sentence."
    print(f"Prompt : {test_prompt}")
    print("Sending to Ollama...\n")

    try:
        answer = ask_ollama(test_prompt)
        print(f"Response: {answer}")
        print("\n✅ Ollama is responding correctly.")
    except ConnectionError as e:
        print(f"\n❌ Connection failed: {e}")
    except RuntimeError as e:
        print(f"\n❌ API error: {e}")
