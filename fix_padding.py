import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# I previously removed padding completely: style="display: none; margin-bottom: 24px; padding: 0;"
# Let's change it to match the standard Avito left/right padding. Let's try 16px, which is standard.
pattern = re.compile(r'style="display: none; margin-bottom: 24px; padding: 0;"')
html = pattern.sub('style="display: none; margin-bottom: 24px; padding: 0 16px;"', html)

# If it was still padding: 0 10px; (maybe the previous replacement failed or something?)
html = html.replace('style="display: none; margin-bottom: 24px; padding: 0 10px;"', 'style="display: none; margin-bottom: 24px; padding: 0 16px;"')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated padding to 16px to align with search bar.")
