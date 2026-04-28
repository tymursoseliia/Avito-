with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('data-marker="image-preview/item"')
if idx != -1:
    print(text[max(0, idx-50):min(len(text), idx+500)])
