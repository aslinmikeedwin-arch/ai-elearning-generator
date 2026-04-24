"""
e2e_test.py
-----------
This is the main pipeline file — the "brain" of the project.
It reads a PDF document and uses AI to generate all course content:
- Introduction, Objectives, Content Screens, Quizzes, Summary

Think of it like a factory:
PDF goes in → Full eLearning course comes out
"""

import fitz      # PyMuPDF — used to read PDF files
import json      # Used to parse JSON responses from the AI
import re        # Used to find patterns in text (like JSON inside a response)
from ai_engine import ask_ollama  # Our custom AI messenger


# ── PDF Reading Functions ─────────────────────────────────────────────────────

def read_pdf(filepath):
    """
    Read the entire PDF and return all text as one big string.
    Used when we need the full document (intro, objectives, summary).
    """
    doc = fitz.open(filepath)
    return " ".join(page.get_text().strip() for page in doc)


def read_pdf_chunks(filepath):
    """
    Read the PDF and return a list where each item is one page's text.
    Used when we need to process the document page by page.
    Example: ["Page 1 text...", "Page 2 text...", "Page 3 text..."]
    """
    doc = fitz.open(filepath)
    return [page.get_text().strip() for page in doc if page.get_text().strip()]


# ── Helper: Clean AI Responses ────────────────────────────────────────────────

def clean_response(text):
    """
    Remove common AI preamble phrases from the start of a response.
    For example, Ollama sometimes starts with "Here is..." or "Based on..."
    This function strips those unnecessary introductions.
    """
    lines = text.strip().split("\n")
    skip = ["here is", "here are", "based on", "certainly", "sure!", "below is", "of course"]

    # If the first line starts with a preamble phrase, remove it
    if lines and any(lines[0].lower().startswith(p) for p in skip):
        lines = lines[1:]

    return "\n".join(lines).strip()


# ── Content Generation Functions ──────────────────────────────────────────────

def generate_introduction(filepath):
    """
    Read the PDF and ask the AI to write a professional introduction.
    Returns a 4-5 sentence paragraph about the document's topic.
    """
    content = read_pdf(filepath)
    prompt = f"Write a clear professional introduction of 4-5 sentences. Return only the text, no preamble.\nDocument: {content}"
    return clean_response(ask_ollama(prompt))


def generate_objectives(filepath):
    """
    Read the PDF and ask the AI to write 5 learning objectives.
    Returns a numbered list of what the learner will achieve.
    """
    content = read_pdf(filepath)
    prompt = f"List exactly 5 learning objectives numbered 1-5. Return only the list, no preamble.\nDocument: {content}"
    return clean_response(ask_ollama(prompt))


def generate_content_screen(chunk):
    """
    Take one page of text and ask the AI to convert it into a learning screen.
    Returns a Title + 5 bullet points summarising the key facts.
    """
    prompt = f"""Convert this text into 5 bullet points about the topic.
Respond in this format only - no other text:

Title: [3-5 word topic title]
- [one fact about the topic]
- [one fact about the topic]
- [one fact about the topic]
- [one fact about the topic]
- [one fact about the topic]

Text: {chunk}"""
    return ask_ollama(prompt)


def extract_title(screen_text, chunk=""):
    """
    Find and return the title from a content screen.
    The AI should return "Title: ..." as the first line.
    If it doesn't, we ask the AI separately for a title.
    If that also fails, we return "Content Screen" as a fallback.
    """
    # Look for a line that starts with "Title:"
    for line in screen_text.splitlines():
        line = line.strip()
        if line.lower().startswith("title:"):
            return line.split(":", 1)[1].strip()

    # If no title found, ask the AI directly
    if chunk:
        try:
            t = ask_ollama(f"Give a 3-5 word title for this. Reply ONLY with the title:\n{chunk[:300]}")
            return t.strip().strip('"').strip("'")[:50]
        except:
            pass

    # Last resort fallback
    return "Content Screen"


def generate_cyu(chunk):
    """
    Take one page of text and ask the AI to create a multiple choice question.
    Returns a dictionary with:
    - question: The question text
    - options: A, B, C, D answer choices
    - correct_answer: The correct letter (A, B, C, or D)
    """
    prompt = f"""Create a multiple choice question. Return ONLY valid JSON on a single line like this:
{{"question": "Your question?", "options": {{"A": "option1", "B": "option2", "C": "option3", "D": "option4"}}, "correct_answer": "B"}}

No extra text. No line breaks inside JSON. Just one line of JSON.
Text: {chunk}"""

    response = ask_ollama(prompt).strip()

    # Try to find a valid JSON object in the response
    match = re.search(r'\{[^{}]*"question"[^{}]*"options"[^{}]*\}', response, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except:
            pass

    # Try each line to find valid JSON
    for line in response.splitlines():
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            try:
                return json.loads(line)
            except:
                pass

    # If all else fails, return a default question
    return {
        "question": "What is the main topic of this content?",
        "options": {"A": "Option A", "B": "Option B", "C": "Option C", "D": "Option D"},
        "correct_answer": "A"
    }


def generate_summary(filepath):
    """
    Read the PDF and ask the AI to write a closing summary.
    Returns a 3-4 sentence recap of the key points.
    """
    content = read_pdf(filepath)
    prompt = f"Write a 3-4 sentence closing summary. Return only the text, no preamble.\nDocument: {content}"
    return clean_response(ask_ollama(prompt))


# ── Main Pipeline ─────────────────────────────────────────────────────────────

def build_storyboard(filepath):
    """
    The main pipeline function — runs all generators in order.
    Takes a PDF file path and returns a list of screen dictionaries.

    Each screen dictionary looks like:
    {
        "type": "introduction",   ← what kind of screen it is
        "title": "Introduction",  ← the screen title
        "content": "..."          ← the actual text content
    }

    The full storyboard order is:
    1. Introduction
    2. Objectives
    3. Content Screen 1 + Quiz 1
    4. Content Screen 2 + Quiz 2
    5. Content Screen 3 + Quiz 3
    6. Summary
    """
    screens = []  # This list will hold all our generated screens
    print("📄 Reading PDF...")
    chunks = read_pdf_chunks(filepath)  # Split PDF into pages

    # ── Generate Introduction ─────────────────────────────────────────────────
    print("✍️  Generating Introduction...")
    try:
        screens.append({
            "type": "introduction",
            "title": "Introduction",
            "content": generate_introduction(filepath)
        })
    except Exception as e:
        print(f"❌ Introduction failed: {e}")

    # ── Generate Objectives ───────────────────────────────────────────────────
    print("🎯 Generating Objectives...")
    try:
        screens.append({
            "type": "objectives",
            "title": "Objectives",
            "content": generate_objectives(filepath)
        })
    except Exception as e:
        print(f"❌ Objectives failed: {e}")

    # ── Generate Content Screens + Quizzes (one per page) ────────────────────
    for i, chunk in enumerate(chunks[:3]):  # Process first 3 pages only

        # Content Screen
        print(f"🖥️  Generating Screen {i+1}...")
        try:
            screen = generate_content_screen(chunk)
            title = extract_title(screen, chunk)
            screens.append({
                "type": "screen",
                "title": title,
                "content": screen
            })
        except Exception as e:
            print(f"❌ Screen {i+1} failed: {e}")

        # Quiz (Check Your Understanding)
        print(f"❓ Generating CYU {i+1}...")
        try:
            cyu = generate_cyu(chunk)
            screens.append({
                "type": "cyu",
                "title": "Check Your Understanding",
                "question": cyu.get("question", ""),
                "options": cyu.get("options", {}),
                "correct_answer": cyu.get("correct_answer", "")
            })
        except Exception as e:
            print(f"❌ CYU {i+1} failed: {e}")

    # ── Generate Summary ──────────────────────────────────────────────────────
    print("📝 Generating Summary...")
    try:
        screens.append({
            "type": "summary",
            "title": "Summary",
            "content": generate_summary(filepath)
        })
    except Exception as e:
        print(f"❌ Summary failed: {e}")

    return screens  # Return the complete list of screens


# ── Run as standalone test ────────────────────────────────────────────────────
if __name__ == "__main__":
    # Test the full pipeline on the AI sample PDF
    storyboard = build_storyboard("sample.pdf")

    print("\n=== All Screens ===\n")
    for i, s in enumerate(storyboard):
        print(f"{i+1}. [{s['type']}] {s['title']}")

    print(f"\n✅ Total: {len(storyboard)} screens")
