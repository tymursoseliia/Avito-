import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('data-marker="review(1)"')
if idx != -1:
    # Get 500 chars before and 2000 chars after to see full structure
    print(html[max(0, idx-1000):idx+2500])
