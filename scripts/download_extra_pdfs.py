import os
import re
import requests
from urllib.parse import unquote, urlparse

BASE_DIR = r"c:\Users\nswap\OneDrive - HAN\HAN\MOVEL\LA 2025-2026\processed_content"
PDF_DIR = os.path.join(BASE_DIR, "pdfs")
MARKDOWN_FILE = os.path.join(BASE_DIR, "LA-2025-2026 bronnen.md")

def download_external_pdfs():
    with open(MARKDOWN_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all http(s) links ending in .pdf
    # Regex for [text](url)
    links = re.findall(r'\((https?://[^)]+\.pdf)\)', content)
    
    print(f"Found {len(links)} external PDF links.")

    for url in links:
        filename = os.path.basename(urlparse(url).path)
        filename = unquote(filename)
        target_path = os.path.join(PDF_DIR, filename)
        
        if not os.path.exists(target_path):
            print(f"Downloading {url} to {filename}...")
            try:
                response = requests.get(url, stream=True)
                if response.status_code == 200:
                    with open(target_path, 'wb') as f:
                        for chunk in response.iter_content(chunk_size=8192):
                            f.write(chunk)
                    print("Success.")
                else:
                    print(f"Failed: Status {response.status_code}")
            except Exception as e:
                print(f"Error downloading {url}: {e}")
        else:
            print(f"Skipping {filename}, already exists.")

if __name__ == "__main__":
    download_external_pdfs()
