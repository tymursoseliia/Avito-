import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all occurrences of GAZTORMOZ (case-insensitive) with Автомиг
new_html = re.sub(r'GAZTORMOZ', 'Автомиг', html, flags=re.IGNORECASE)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Replacement complete.")
