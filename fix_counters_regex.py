import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any number inside the counter spans with '...'
new_text = re.sub(r'(<span class="styles-module-counter-uAip7[^>]*>)\d+(</span>)', r'\1...\2', text)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Replaced static counters with '...'")
