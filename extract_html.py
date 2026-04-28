import re

html = open('car_page.html', encoding='utf-8').read()

with open('extracted_chunks.txt', 'w', encoding='utf-8') as f:
    for li_match in re.finditer(r'<li[^>]*>.*?Год выпуска.*?</li>', html, re.IGNORECASE | re.DOTALL):
        f.write("LI MATCH:\n" + li_match.group(0) + "\n\n")
    
    for breadcrumb in re.finditer(r'<[a-z]+[^>]*data-marker="breadcrumbs"[^>]*>.*?</[a-z]+>', html, re.IGNORECASE | re.DOTALL):
        f.write("BREADCRUMBS MATCH:\n" + breadcrumb.group(0)[:500] + "\n\n")

