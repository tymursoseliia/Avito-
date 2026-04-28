import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'<span class="styles-module-counter-uAip7">[^<]*</span>', text)
for m in matches:
    idx = m.start()
    print(text[max(0, idx-50):min(len(text), idx+50)])
