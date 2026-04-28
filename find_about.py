with open('car_page.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
idx = text.find('О компании')
if idx != -1:
    print(text[max(0, idx-500):min(len(text), idx+1000)])
