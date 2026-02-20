import markdown
import os
from bs4 import BeautifulSoup
import re

BASE_DIR = r"c:\Users\nswap\OneDrive - HAN\HAN\MOVEL\LA 2025-2026\processed_content"
MARKDOWN_FILE = os.path.join(BASE_DIR, "LA-2025-2026 bronnen.md")
OUTPUT_HTML = os.path.join(BASE_DIR, "index.html")
THUMB_DIR = "thumbnails" # Relative to index.html

CSS = """
<style>
    :root {
        --primary-color: #E60005; /* HAN Red */
        --primary-dark: #b30004;
        --secondary-color: #333;
        --bg-color: #F4F6F8;
        --text-color: #212529;
        --card-bg: #FFFFFF;
        --sidebar-width: 280px;
        --transition-speed: 0.3s;
    }
    
    body {
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
        margin: 0;
        padding: 0;
        display: flex;
        background-color: var(--bg-color);
        color: var(--text-color);
        height: 100vh;
        overflow: hidden;
    }
    
    /* Sidebar */
    #sidebar {
        width: var(--sidebar-width);
        background: white;
        border-right: 1px solid #e0e0e0;
        display: flex;
        flex-direction: column;
        height: 100%;
        box-shadow: 2px 0 5px rgba(0,0,0,0.05);
        z-index: 10;
    }
    
    .sidebar-header {
        padding: 20px;
        border-bottom: 1px solid #eee;
        background: var(--primary-color);
        color: white;
    }
    
    .sidebar-header h2 {
        margin: 0;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    #search-container {
        padding: 20px;
        border-bottom: 1px solid #eee;
    }
    
    #search-box {
        width: 100%;
        padding: 12px;
        border: 1px solid #ddd;
        border-radius: 6px;
        font-size: 1rem;
        box-sizing: border-box;
        transition: border-color var(--transition-speed);
    }
    
    #search-box:focus {
        outline: none;
        border-color: var(--primary-color);
        box-shadow: 0 0 0 3px rgba(230, 0, 5, 0.1);
    }
    
    #toc {
        flex: 1;
        overflow-y: auto;
        padding: 10px 0;
    }
    
    .toc-item {
        display: block;
        padding: 10px 20px;
        color: #555;
        text-decoration: none;
        transition: background-color 0.2s, color 0.2s;
        border-left: 3px solid transparent;
        font-size: 0.95rem;
    }
    
    .toc-item:hover {
        background-color: #f8f9fa;
        color: var(--primary-color);
        border-left-color: var(--primary-color);
    }

    /* Main Content */
    #content {
        flex: 1;
        overflow-y: auto;
        padding: 40px;
        scroll-behavior: smooth;
    }
    
    .container {
        max-width: 1200px;
        margin: 0 auto;
    }
    
    h1 {
        color: var(--secondary-color);
        font-size: 2.5rem;
        margin-bottom: 10px;
        padding-bottom: 15px;
        border-bottom: 3px solid var(--primary-color);
    }
    
    h2 {
        color: var(--secondary-color);
        font-size: 1.8rem;
        margin-top: 50px;
        margin-bottom: 25px;
        padding-bottom: 10px;
        border-bottom: 1px solid #e0e0e0;
        display: flex;
        align-items: center;
    }
    
    p {
        line-height: 1.6;
        color: #4a4a4a;
        margin-bottom: 20px;
    }

    /* Card Grid */
    .resource-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 25px;
    }
    
    .card {
        background: var(--card-bg);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: transform var(--transition-speed), box-shadow var(--transition-speed);
        display: flex;
        flex-direction: column;
        border: 1px solid #eee;
        overflow: hidden;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border-color: #ddd;
    }
    
    .card-thumb {
        height: 180px;
        overflow: hidden;
        background-color: #f0f0f0;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .card-thumb img {
        width: 100%;
        height: 100%;
        object-fit: cover; /* or contain for PDFs? Cover looks better usually */
        object-position: top;
        transition: transform 0.5s;
    }
    
    .card:hover .card-thumb img {
        transform: scale(1.05);
    }
    
    .card-body {
        padding: 20px;
        flex: 1;
        display: flex;
        flex-direction: column;
    }
    
    .card-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0 0 10px 0;
        line-height: 1.4;
    }
    
    .card-title a {
        color: var(--secondary-color);
        text-decoration: none;
        transition: color 0.2s;
    }
    
    .card-title a:hover {
        color: var(--primary-color);
    }
    
    .card-desc {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 20px;
        flex: 1;
        line-height: 1.5;
    }
    
    .card-footer {
        margin-top: auto;
        padding-top: 15px;
        border-top: 1px solid #f0f0f0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .btn {
        display: inline-block;
        padding: 8px 16px;
        background-color: var(--primary-color);
        color: white;
        text-decoration: none;
        border-radius: 4px;
        font-size: 0.9rem;
        font-weight: 500;
        transition: background-color 0.2s;
    }
    
    .btn:hover {
        background-color: var(--primary-dark);
        text-decoration: none;
    }
    
    .badge {
        font-size: 0.75rem;
        padding: 4px 8px;
        border-radius: 4px;
        background-color: #eee;
        color: #555;
        font-weight: 600;
        text-transform: uppercase;
    }
    
    .badge.pdf { background-color: #ffebee; color: #c62828; }
    .badge.link { background-color: #e3f2fd; color: #1565c0; }

    /* Images in content */
    img.content-img {
        max-width: 100%;
        border-radius: 8px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        display: block;
        margin: 20px auto;
    }

    /* Responsive */
    @media (max-width: 900px) {
        body {
            flex-direction: column;
            overflow: auto;
            height: auto;
        }
        #sidebar {
            width: 100%;
            height: auto;
            border-right: none;
            position: relative;
        }
        #content {
            padding: 20px;
        }
        .sidebar-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        #toc {
            display: none; /* Hide TOC on mobile initially, or make expandable */
        }
        
        #sidebar.expanded #toc {
            display: block;
        }
    }
</style>
"""

JS = """
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const searchBox = document.getElementById('search-box');
        
        searchBox.addEventListener('input', function(e) {
            const term = e.target.value.toLowerCase();
            const cards = document.querySelectorAll('.card');
            
            cards.forEach(card => {
                const title = card.querySelector('.card-title').textContent.toLowerCase();
                const desc = card.querySelector('.card-desc').textContent.toLowerCase();
                
                if (title.includes(term) || desc.includes(term)) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
            
            // Also filter list items if any remain
            // ...
        });
    });
</script>
"""

def generate_web_app():
    with open(MARKDOWN_FILE, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    # 1. Convert initial markdown to HTML
    html_raw = markdown.markdown(md_text, extensions=['toc', 'tables', 'fenced_code'])
    soup = BeautifulSoup(html_raw, 'html.parser')
    
    # 2. Transform headers (add IDs manually if TOC extension didn't do it well, but it usually does)
    # We will assume TOC extension added IDs.
    
    # 3. Transform Lists into Grid Cards
    # We look for <ul> that follow a header or paragraph, containing items with links.
    
    # Strategy:
    # Iterate over all <ul> elements. 
    # Check if children <li> contain a link <a> as the first prominent element.
    # If so, transform the <ul> into <div class="resource-grid">
    # And <li> into <div class="card">
    
    for ul in soup.find_all('ul'):
        # Simple heuristic: If the list has items with links, treat it as a resource list
        # Check first item
        first_li = ul.find('li')
        if not first_li: continue
        
        link = first_li.find('a')
        if link:
            # Create a Grid Div
            grid_div = soup.new_tag('div', **{'class': 'resource-grid'})
            
            # Process all items
            for li in ul.find_all('li', recursive=False): # Only direct children
                
                # Check for link
                a_tag = li.find('a')
                if not a_tag:
                    # Just keep it as is, or maybe wrap in a simple card?
                    continue
                
                href = a_tag['href']
                title = a_tag.get_text()
                
                # Description: look for nested <ul> or text after link
                desc_text = ""
                # Check for nested list
                nested_ul = li.find('ul')
                if nested_ul:
                    desc_text = nested_ul.get_text().strip()
                    nested_ul.decompose() # Remove it from DOM
                else:
                    # Try to get text after the link
                    # This is tricky in BS4 as text is a NavigableString sibling
                    # We can get all text and subtract title?
                    full_text = li.get_text().strip()
                    if full_text.startswith(title):
                        desc_text = full_text[len(title):].strip(" -:,\n")
                
                # Determine type
                is_pdf = href.lower().endswith('.pdf')
                file_type = "PDF" if is_pdf else "Link"
                badge_class = "pdf" if is_pdf else "link"
                
                # Thumbnail
                thumb_src = ""
                if is_pdf:
                    filename = os.path.basename(href).replace("%20", " ") # Decode URL
                    thumb_filename = f"{filename}.png"
                    # Check if exists (assuming script runs in correct dir)
                    # We just assume it exists for now based on previous script
                    thumb_src = f"thumbnails/{thumb_filename}"
                else:
                    # Default icon for external links
                    # We can use a placeholder or relevant image if we had one
                    thumb_src = "media/image(2).png" # Fallback to generic image
                
                # Create Card HTML
                card = soup.new_tag('div', **{'class': 'card'})
                
                # Thumb
                thumb_div = soup.new_tag('div', **{'class': 'card-thumb'})
                img = soup.new_tag('img', src=thumb_src, alt=title,  loading="lazy")
                # Handle missing images gracefully via JS? Or just let it break?
                # Best to use a default error handler in JS
                img['onerror'] = "this.src='media/image.png'" # Fallback
                thumb_div.append(img)
                card.append(thumb_div)
                
                # Body
                body_div = soup.new_tag('div', **{'class': 'card-body'})
                
                # Title
                title_h3 = soup.new_tag('h3', **{'class': 'card-title'})
                title_link = soup.new_tag('a', href=href, target="_blank")
                title_link.string = title
                title_h3.append(title_link)
                body_div.append(title_h3)
                
                # Desc
                if desc_text:
                    p_desc = soup.new_tag('p', **{'class': 'card-desc'})
                    p_desc.string = desc_text
                    body_div.append(p_desc)
                else:
                     # Add empty filler to push footer down
                    filler = soup.new_tag('div', **{'class': 'card-desc'})
                    body_div.append(filler)

                # Footer
                footer_div = soup.new_tag('div', **{'class': 'card-footer'})
                badge = soup.new_tag('span', **{'class': f'badge {badge_class}'})
                badge.string = file_type
                footer_div.append(badge)
                
                btn = soup.new_tag('a', href=href, **{'class': 'btn'})
                if is_pdf:
                    btn.string = "Download PDF"
                    btn['download'] = "" # Hint to download
                else:
                    btn.string = "Open Link"
                    btn['target'] = "_blank"
                
                footer_div.append(btn)
                body_div.append(footer_div)
                
                card.append(body_div)
                grid_div.append(card)
            
            # Replace UL with the Grid Div
            ul.replace_with(grid_div)
            
    # Modify Images
    for img in soup.find_all('img'):
        if 'card-thumb' not in img.parent.get('class', []):
            img['class'] = img.get('class', []) + ['content-img']

    # Generate TOC for sidebar
    # We can parse H1, H2 from soup
    toc_html = ""
    for h2 in soup.find_all('h2'):
        text = h2.get_text()
        if not h2.get('id'):
            # Generate ID if missing
            new_id = re.sub(r'[^a-zA-Z0-9]', '-', text.lower())
            h2['id'] = new_id
        
        toc_html += f'<a href="#{h2["id"]}" class="toc-item">{text}</a>'
        
    # Build Final HTML
    final_html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learning Analytics Bronnen 2025-2026</title>
    {CSS}
</head>
<body>
    <div id="sidebar">
        <div class="sidebar-header">
            <h2>LA Bronnen</h2>
        </div>
        <div id="search-container">
            <input type="text" id="search-box" placeholder="Zoeken..." aria-label="Zoeken">
        </div>
        <div id="toc">
            {toc_html}
        </div>
    </div>
    
    <div id="content">
        <div class="container">
             {str(soup)}
        </div>
    </div>
    
    {JS}
</body>
</html>
"""
    
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print(f"Generated {OUTPUT_HTML}")

if __name__ == "__main__":
    generate_web_app()
