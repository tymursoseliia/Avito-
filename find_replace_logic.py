with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// 9. Replace Company Name and Logo')
if idx != -1:
    print(text[max(0, idx):min(len(text), idx+2000)])
