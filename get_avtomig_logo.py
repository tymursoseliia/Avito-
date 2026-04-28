import re
with open('clean_avito (1).html', encoding='utf-8') as f:
    text = f.read()

images = re.findall(r'<img[^>]*src=[\"\']([^\'\"]+)[\"\'][^>]*>', text)
for img in set(images):
    if 'ibb' in img or 'avtomig' in img.lower() or 'avatar' in img:
        print("Found possible logo:", img)
