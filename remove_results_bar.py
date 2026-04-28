import re
with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<div id="results-count-bar".*?</div>\s*</div>', '', text, flags=re.DOTALL)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(text)
print('results-count-bar removed.')
