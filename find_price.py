with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('item-price')
if idx != -1:
    with open('price_debug.txt', 'w', encoding='utf-8') as out:
        out.write(text[max(0, idx-100):min(len(text), idx+300)])
    print('Found item-price')
else:
    print('Not found')
