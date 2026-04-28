with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('data-marker="seller-link/link"')
if idx != -1:
    with open('seller_html.txt', 'w', encoding='utf-8') as out:
        out.write(text[max(0, idx-2000):min(len(text), idx+1000)])
