import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Активные')
if idx != -1:
    print("Found 'Активные' at", idx)
    print(text[max(0, idx-50):min(len(text), idx+100)])
else:
    print("Not found")
