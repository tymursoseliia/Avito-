import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Change padding to 16px to align perfectly with the top search bar.
html = html.replace('padding: 0 6px;', 'padding: 0 16px;')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated padding to 16px for perfect left-edge alignment.")
