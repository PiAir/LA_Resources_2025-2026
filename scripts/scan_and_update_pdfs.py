import os
import re
import json
from urllib.parse import unquote, urlparse
from pypdf import PdfReader

BASE_DIR = r"c:\Users\nswap\OneDrive - HAN\HAN\MOVEL\LA 2025-2026\processed_content"
PDF_DIR = os.path.join(BASE_DIR, "pdfs")
MARKDOWN_FILE = os.path.join(BASE_DIR, "LA-2025-2026 bronnen.md")
SNIPPETS_FILE = os.path.join(BASE_DIR, "pdf_snippets.json")

def extract_text_from_pdf(pdf_path, max_chars=1500):
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages[:2]: # First 2 pages should contain abstract/intro
            text += page.extract_text() or ""
        return text[:max_chars]
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""

def main():
    with open(MARKDOWN_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update external links to local Relative paths if file exists
    # Regex to find links [text](http...)
    def replace_link(match):
        text = match.group(1)
        url = match.group(2)
        
        # Check if it's a PDF link
        path = urlparse(url).path
        if path.lower().endswith('.pdf'):
            filename = unquote(os.path.basename(path))
            local_path = os.path.join(PDF_DIR, filename)
            if os.path.exists(local_path):
                print(f"Updating link: {url} -> pdfs/{filename}")
                return f"[{text}](pdfs/{filename})"
        return match.group(0)

    # Use re.sub with callback
    # Pattern: [text](url)
    # Be careful not to mess up existing local links or images
    # We only target http/https links
    new_content = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', replace_link, content)
    
    with open(MARKDOWN_FILE, 'w', encoding='utf-8') as f:
        f.write(new_content)

    # 2. Extract snippets for ALL PDFs in the pdfs folder
    snippets = {}
    
    # Get all PDF files
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith('.pdf')]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(PDF_DIR, pdf_file)
        print(f"Extracting text from {pdf_file}...")
        text = extract_text_from_pdf(pdf_path)
        snippets[pdf_file] = text

    with open(SNIPPETS_FILE, 'w', encoding='utf-8') as f:
        json.dump(snippets, f, indent=2)

    print("Done. Snippets saved.")

if __name__ == "__main__":
    main()
