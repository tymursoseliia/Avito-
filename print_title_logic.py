with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('// 1. Update Title & Price')
if idx != -1:
    print(text[max(0, idx):min(len(text), idx+1000)].encode('utf-8'))
