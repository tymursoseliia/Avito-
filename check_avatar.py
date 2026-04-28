import re

with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'data-marker="seller-info/avatar[^"]*"', text)
for m in matches:
    idx = m.start()
    print(text[max(0, idx-200):min(len(text), idx+500)])
