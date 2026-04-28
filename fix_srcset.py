with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('if (img) img.src = url;', 'if (img) { img.src = url; img.removeAttribute("srcset"); }')
text = text.replace('if (img) img.src = galleryImages[idx];', 'if (img) { img.src = galleryImages[idx]; img.removeAttribute("srcset"); }')

with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated update_car_page.py to remove srcset')
