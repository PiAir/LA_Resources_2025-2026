import os
import fitz  # PyMuPDF

BASE_DIR = r"c:\Users\nswap\OneDrive - HAN\HAN\MOVEL\LA 2025-2026\processed_content"
PDF_DIR = os.path.join(BASE_DIR, "pdfs")
THUMB_DIR = os.path.join(BASE_DIR, "thumbnails")

if not os.path.exists(THUMB_DIR):
    os.makedirs(THUMB_DIR)

def generate_thumbnails():
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith('.pdf')]
    print(f"Found {len(pdf_files)} PDFs.")

    for pdf_file in pdf_files:
        pdf_path = os.path.join(PDF_DIR, pdf_file)
        thumb_name = f"{pdf_file}.png"
        thumb_path = os.path.join(THUMB_DIR, thumb_name)
        
        # Skip if already exists? Maybe force overwrite to be sure
        # if os.path.exists(thumb_path):
        #    continue

        try:
            doc = fitz.open(pdf_path)
            if len(doc) > 0:
                page = doc[0]
                pix = page.get_pixmap(matrix=fitz.Matrix(0.5, 0.5)) # Scale down to 50%
                pix.save(thumb_path)
                print(f"Generated thumbnail for {pdf_file}")
            doc.close()
        except Exception as e:
            print(f"Failed to generate thumbnail for {pdf_file}: {e}")

if __name__ == "__main__":
    generate_thumbnails()
