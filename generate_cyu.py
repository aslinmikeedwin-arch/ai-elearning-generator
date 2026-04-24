
import fitz
import json
import re
from ai_engine import ask_ollama

def read_pdf_chunks(filepath: str) -> list:
    doc = fitz.open(filepath)
    chunks = []
    for page in doc:
        text = page.get_text().strip()
        if text:
            chunks.append(text)
    return chunks

def generate_cyu(chunk: str) -> dict:
    prompt = f"""Create a multiple choice question based on the text below.
Respond with ONLY this JSON and absolutely nothing else before or after it:

{{"question": "Write question here?", "options": {{"A": "option 1", "B": "option 2", "C": "option 3", "D": "option 4"}}, "correct_answer": "A"}}

Replace the values with your actual question and options.
The correct_answer must be A, B, C, or D only.
Do not add any text before or after the JSON.

Text:
{chunk}"""
    response = ask_ollama(prompt)
    response = response.strip()
    
    # Extract JSON using regex
    match = re.search(r'\{{.*\}}', response, re.DOTALL)
    if match:
        response = match.group()
    
    return json.loads(response)

def verify_cyu(cyu: dict) -> bool:
    print("--- Verifying fields ---")
    all_good = True
    fields = [
        ("question", cyu.get("question")),
        ("Option A", cyu.get("options", {}).get("A")),
        ("Option B", cyu.get("options", {}).get("B")),
        ("Option C", cyu.get("options", {}).get("C")),
        ("Option D", cyu.get("options", {}).get("D")),
        ("correct_answer", cyu.get("correct_answer")),
    ]
    for name, value in fields:
        if value:
            print(f"✅ {name}: {value}")
        else:
            print(f"❌ {name}: MISSING!")
            all_good = False
    return all_good

if __name__ == "__main__":
    chunks = read_pdf_chunks("sample.pdf")
    print(f"Total chunks: {len(chunks)}\n")
    for i, chunk in enumerate(chunks[:3]):
        print(f"=== CYU Screen {i+1} ===\n")
        try:
            cyu = generate_cyu(chunk)
            valid = verify_cyu(cyu)
            print(f"\nResult: {'✅ All fields populated!' if valid else '❌ Some fields missing!'}\n")
        except Exception as e:
            print(f"❌ Error parsing JSON: {e}\n")
    print("✅ Done!")
