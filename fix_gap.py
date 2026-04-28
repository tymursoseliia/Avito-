import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Change padding and margin-top to fix the gap
html = html.replace('style="display: none; margin-bottom: 24px; padding: 0 6px;"', 'style="display: none; margin-top: -24px; margin-bottom: 24px; padding: 0 6px;"')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated margin-top to -24px to fix gap.")
