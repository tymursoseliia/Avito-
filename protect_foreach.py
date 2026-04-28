with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("if (aboutSection && data.about_photos && data.about_photos.length > 0)", "if (aboutSection && Array.isArray(data.about_photos) && data.about_photos.length > 0)")
with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("if (aboutSection && data.about_photos && data.about_photos.length > 0)", "if (aboutSection && Array.isArray(data.about_photos) && data.about_photos.length > 0)")
with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Protected about_photos.forEach")
