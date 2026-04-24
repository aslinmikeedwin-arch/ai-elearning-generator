
import fitz
from ai_engine import ask_ollama

def read_pdf_chunks(filepath: str) -> list:
    doc = fitz.open(filepath)
    chunks = []
    for page in doc:
        text = page.get_text().strip()
        if text:
            chunks.append(text)
    return chunks

def generate_content_screen(chunk: str) -> str:
    prompt = f"""You are an eLearning content designer.
Convert the following text into a learning screen.
You MUST follow this EXACT format or your response is wrong:

Title: [short title here]

- [bullet point 1]
- [bullet point 2]
- [bullet point 3]
- [bullet point 4]
- [bullet point 5]

CRITICAL Rules:
- Line 1 MUST start with "Title:" — this is mandatory
- ALWAYS use the • symbol for bullets, NEVER use - or *
- ALWAYS write exactly 5 bullet points
- Title must be short, no chapter numbers or prefixes
- Each bullet must be one short simple sentence
- Do NOT skip the Title line under any circumstances

Text:
{chunk}"""
    return ask_ollama(prompt)

if __name__ == "__main__":
    chunks = read_pdf_chunks("sample.pdf")
    print(f"Total chunks found: {len(chunks)}\n")
    for i, chunk in enumerate(chunks[:3]):
        print(f"=== Screen {i+1} ===\n")
        result = generate_content_screen(chunk)
        print(result)
        print()
    print("✅ Done!")
