
import fitz  # pymupdf
from ai_engine import ask_ollama

def read_pdf(filepath: str) -> str:
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def generate_introduction(filepath: str) -> str:
    content = read_pdf(filepath)
    prompt = f"""Based on the following document content, write a clear and professional introduction paragraph of 4-5 sentences.
Only return the introduction, nothing else.

Document:
{content}"""
    return ask_ollama(prompt)

def generate_objectives(filepath: str) -> str:
    content = read_pdf(filepath)
    prompt = f"""Based on the following document content, list exactly 5 clear learning objectives.
Format them as a numbered list 1-5.
Only return the numbered list, nothing else.

Document:
{content}"""
    return ask_ollama(prompt)

if __name__ == "__main__":
    pdf = "sample.pdf"
    print("=== Testing generate_introduction() ===\n")
    intro = generate_introduction(pdf)
    print(intro)
    print("\n=== Testing generate_objectives() ===\n")
    objectives = generate_objectives(pdf)
    print(objectives)
    print("\n✅ Done!")
