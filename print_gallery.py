with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('item-view/gallery')
if idx != -1:
    with open('gallery_debug.txt', 'w', encoding='utf-8') as f:
        f.write(text[idx-200:idx+2000])
