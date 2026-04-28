import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('photo-slider-item-Zbpsa')
# Find the start of the <ul class="photo-slider-list-PxsU9"> or whatever wrapper it is
start = max(0, idx - 300)
end = min(len(html), idx + 300)
print(html[start:end])
