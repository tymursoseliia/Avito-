with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('data-marker="image-frame/thumbnail"', 'data-marker="image-preview/item"')

with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated thumbnail selector!")
