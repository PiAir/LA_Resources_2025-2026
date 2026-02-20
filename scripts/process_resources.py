import os
import requests
import fitz  # PyMuPDF
from urllib.parse import urlparse
import json
import time

# Configuration
BASE_DIR = r"c:\Users\nswap\OneDrive - HAN\HAN\MOVEL\LA 2025-2026\processed_content"
PDF_DIR = os.path.join(BASE_DIR, "pdfs")
MEDIA_DIR = os.path.join(BASE_DIR, "media")
THUMBNAIL_DIR = os.path.join(MEDIA_DIR, "thumbnails")
TEXT_EXTRACT_FILE = os.path.join(BASE_DIR, "pdf_texts.json")

# Ensure directories exist
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(THUMBNAIL_DIR, exist_ok=True)

def download_file(url, target_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(target_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {url} -> {target_path}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def generate_pdf_thumbnail(pdf_path, thumbnail_path):
    try:
        doc = fitz.open(pdf_path)
        page = doc.load_page(0)  # number of page
        pix = page.get_pixmap(matrix=fitz.Matrix(0.5, 0.5)) # Scale down to 50%
        pix.save(thumbnail_path)
        print(f"Thumbnail generated: {thumbnail_path}")
        return True
    except Exception as e:
        print(f"Failed to generate thumbnail for {pdf_path}: {e}")
        return False

def extract_pdf_text(pdf_path, max_words=500):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
            if len(text.split()) > max_words:
                break
        return " ".join(text.split()[:max_words])
    except Exception as e:
        print(f"Failed to extract text from {pdf_path}: {e}")
        return ""

def process_pdfs():
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.endswith(".pdf")]
    extracted_texts = {}

    for pdf_file in pdf_files:
        pdf_path = os.path.join(PDF_DIR, pdf_file)
        thumbnail_name = f"{pdf_file}.jpg"
        thumbnail_path = os.path.join(THUMBNAIL_DIR, thumbnail_name)

        # Generate Thumbnail
        if not os.path.exists(thumbnail_path):
            generate_pdf_thumbnail(pdf_path, thumbnail_path)
        
        # Extract Text
        extracted_texts[pdf_file] = extract_pdf_text(pdf_path)

    # Save extracted text for the Agent to read
    with open(TEXT_EXTRACT_FILE, "w", encoding="utf-8") as f:
        json.dump(extracted_texts, f, indent=4)
        print(f"Saved extracted texts to {TEXT_EXTRACT_FILE}")

if __name__ == "__main__":
    print("Starting PDF processing...")
    process_pdfs()
    print("Done.")
