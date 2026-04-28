with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('data-marker="item-view/seller-info"')
if idx != -1:
    with open('seller_debug.txt', 'w', encoding='utf-8') as out:
        out.write(text[max(0, idx-100):min(len(text), idx+1500)])
