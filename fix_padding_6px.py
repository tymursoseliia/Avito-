import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Change padding to 6px because Avito's grid items have 6px padding (half of 12px gap)
html = html.replace('style="display: none; margin-bottom: 24px; padding: 0 16px;"', 'style="display: none; margin-bottom: 24px; padding: 0 6px;"')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated padding to 6px for perfect grid alignment.")
