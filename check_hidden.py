import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('Реквизиты проверены')
start = max(0, idx - 800)
end = min(len(html), idx + 200)
print(html[start:end])
