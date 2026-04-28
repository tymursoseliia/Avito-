import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('photo-slider-slider-')
start = max(0, idx - 100)
end = min(len(html), idx + 200)
print(html[start:end])
