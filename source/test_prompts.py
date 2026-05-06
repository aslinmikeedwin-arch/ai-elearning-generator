"""
test_prompts.py
---------------
This file tests 5 different types of AI responses from Ollama.
Think of it as a "sanity check" — before building the full course,
we make sure the AI is working correctly for each type of output.

The 5 types tested are:
1. Story      — Can the AI write creative content?
2. List       — Can the AI return a simple formatted list?
3. Summary    — Can the AI summarise a topic clearly?
4. Q&A        — Can the AI answer a direct question?
5. JSON       — Can the AI return clean structured data?
"""

from ai_engine import ask_ollama  # Our custom AI messenger
import json                        # Used to validate JSON output


# ── Test 1: Story Generation ──────────────────────────────────────────────────

def generate_story():
    """
    Test if the AI can write a short creative story.
    We ask for exactly 2 sentences about a robot.
    """
    prompt = "Write a 2 sentence short story about a robot."
    response = ask_ollama(prompt)
    print("📖 STORY:")
    print(response)
    print()


# ── Test 2: List Generation ───────────────────────────────────────────────────

def generate_list():
    """
    Test if the AI can return a simple formatted list.
    We ask for 3 fruits, one per line.
    """
    prompt = "Give me a list of 3 fruits. One per line."
    response = ask_ollama(prompt)
    print("📋 LIST:")
    print(response)
    print()


# ── Test 3: Summary Generation ────────────────────────────────────────────────

def generate_summary():
    """
    Test if the AI can summarise a topic in 2 sentences.
    We ask about the Python programming language.
    """
    prompt = "Summarize what Python programming language is in 2 sentences."
    response = ask_ollama(prompt)
    print("📝 SUMMARY:")
    print(response)
    print()


# ── Test 4: Q&A Generation ────────────────────────────────────────────────────

def generate_qa():
    """
    Test if the AI can answer a direct factual question.
    We use a simple geography question with a clear answer.
    """
    prompt = "Q: What is the capital of France? A:"
    response = ask_ollama(prompt)
    print("❓ Q&A:")
    print(response)
    print()


# ── Test 5: JSON Generation ───────────────────────────────────────────────────

def generate_json():
    """
    Test if the AI can return clean, valid JSON data.
    This is important because our quiz generator (generate_cyu) relies
    on the AI returning valid JSON for the question and answer options.

    We check if the response is valid JSON using json.loads().
    If it passes — the AI is ready for the full pipeline.
    If it fails — we need to improve the prompt.
    """
    prompt = """Return ONLY a JSON object with no extra text, no explanation, no markdown.
Just raw JSON like this: {"name": "Alice", "age": 25, "city": "Paris"}
Now return a JSON object for a fictional person."""

    response = ask_ollama(prompt)
    print("🔧 JSON:")
    print(response)

    # Try to parse the response as JSON
    try:
        parsed = json.loads(response)
        print("✅ JSON is clean and valid!")
    except:
        print("❌ JSON is messy - needs fixing")
    print()


# ── Run all 5 tests ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== Testing all 5 functions ===\n")
    generate_story()    # Test 1: Creative writing
    generate_list()     # Test 2: Formatted list
    generate_summary()  # Test 3: Topic summary
    generate_qa()       # Test 4: Direct Q&A
    generate_json()     # Test 5: Clean JSON output
    print("=== Done! ===")
