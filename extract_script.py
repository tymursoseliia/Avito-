import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<script>(.*)</script>', html, re.DOTALL)
if m:
    with open('admin_script.js', 'w', encoding='utf-8') as fw:
        fw.write(m.group(1))
    print("Extracted to admin_script.js")
