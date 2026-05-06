import requests

def ask_ollama(prompt, model="llama3.2", host="http://localhost:11434"):
    url = f"{host}/api/generate"
    payload = {"model": model, "prompt": prompt, "stream": False}
    try:
        response = requests.post(url, json=payload, timeout=120)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Could not connect to Ollama. Make sure it is running.")
    data = response.json()
    return data["response"].strip()
