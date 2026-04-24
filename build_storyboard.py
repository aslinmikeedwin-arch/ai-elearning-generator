
import fitz
import json
import re
from ai_engine import ask_ollama

def read_pdf(filepath: str) -> str:
    doc = fitz.open(filepath)
    return " ".join(page.get_text().strip() for page in doc)

def read_pdf_chunks(filepath: str) -> list:
    doc = fitz.open(filepath)
    return [page.get_text().strip() for page in doc if page.get_text().strip()]

def generate_introduction(filepath: str) -> str:
    content = read_pdf(filepath)
    prompt = f"""Based on the following document, write a clear professional introduction of 4-5 sentences.
Return only the introduction, nothing else.
Document: {content}"""
    return ask_ollama(prompt)

def generate_objectives(filepath: str) -> str:
    content = read_pdf(filepath)
    prompt = f"""Based on the following document, list exactly 5 learning objectives as a numbered list 1-5.
Return only the numbered list, nothing else.
Document: {content}"""
    return ask_ollama(prompt)

def generate_content_screen(chunk: str) -> str:
    prompt = f"""You are an eLearning content designer.
Convert the following text into a learning screen.
You MUST follow this EXACT format:

Title: [short title here]

- [bullet point 1]
- [bullet point 2]
- [bullet point 3]
- [bullet point 4]
- [bullet point 5]

CRITICAL Rules:
- Line 1 MUST start with "Title:"
- ALWAYS use • symbol, NEVER use - or *
- ALWAYS write exactly 5 bullet points
- Each bullet must be one short simple sentence

Text: {chunk}"""
    return ask_ollama(prompt)

def generate_cyu(chunk: str) -> dict:
    prompt = f"""Create a multiple choice question based on the text below.
Respond with ONLY this JSON and absolutely nothing else:

{{"question": "Write question here?", "options": {{"A": "option 1", "B": "option 2", "C": "option 3", "D": "option 4"}}, "correct_answer": "A"}}

Replace values with your actual question and options.
The correct_answer must be A, B, C, or D only.

Text: {chunk}"""
    response = ask_ollama(prompt).strip()
    match = re.search(r'\{.*\}', response, re.DOTALL)
    if match:
        response = match.group()
    return json.loads(response)

def generate_summary(filepath: str) -> str:
    content = read_pdf(filepath)
    prompt = f"""Based on the following document, write a short closing summary of 3-4 sentences.
It should recap the key points a learner should remember.
Return only the summary, nothing else.
Document: {content}"""
    return ask_ollama(prompt)

def build_storyboard(filepath: str) -> dict:
    print("📄 Reading PDF...")
    chunks = read_pdf_chunks(filepath)

    print("✍️  Generating Introduction...")
    intro = generate_introduction(filepath)

    print("🎯 Generating Objectives...")
    objectives = generate_objectives(filepath)

    screens = []
    for i, chunk in enumerate(chunks[:3]):
        print(f"🖥️  Generating Screen {i+1}...")
        screen = generate_content_screen(chunk)
        print(f"❓ Generating CYU {i+1}...")
        cyu = generate_cyu(chunk)
        screens.append({"screen": screen, "cyu": cyu})

    print("📝 Generating Summary...")
    summary = generate_summary(filepath)

    return {
        "introduction": intro,
        "objectives": objectives,
        "screens": screens,
        "summary": summary
    }

if __name__ == "__main__":
    print("=== Building Full Storyboard ===\n")
    storyboard = build_storyboard("sample.pdf")

    print("\n=============================")
    print("📖 INTRODUCTION")
    print("=============================")
    print(storyboard["introduction"])

    print("\n=============================")
    print("🎯 OBJECTIVES")
    print("=============================")
    print(storyboard["objectives"])

    for i, item in enumerate(storyboard["screens"]):
        print(f"\n=============================")
        print(f"🖥️  SCREEN {i+1}")
        print("=============================")
        print(item["screen"])
        print(f"\n❓ CYU {i+1}:")
        cyu = item["cyu"]
        print(f"Q: {cyu['question']}")
        for k, v in cyu["options"].items():
            print(f"   {k}) {v}")
        print(f"   ✅ Correct: {cyu.get('correct_answer', cyu.get('correctAnswer', 'N/A'))}")

    print("\n=============================")
    print("📝 SUMMARY")
    print("=============================")
    print(storyboard["summary"])
    print("\n✅ Storyboard complete!")
