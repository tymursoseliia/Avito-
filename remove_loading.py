import re

html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Let's just remove the class from the file!
html = html.replace('styles-module-loading-_VPeU', '')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Removed loading class from images.")
