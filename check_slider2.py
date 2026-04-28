import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the second occurrence
idx = html.find('photo-slider-item-Zbpsa', html.find('photo-slider-item-Zbpsa') + 100)

start = max(0, idx - 300)
end = min(len(html), idx + 300)
print(html[start:end])
