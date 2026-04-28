with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

limit = text.find('<!-- Supabase JS -->')
if limit != -1:
    text = text[:limit]

idx = text.find('data-marker="image-frame/thumbnail"')
if idx != -1:
    with open('thumb_debug.txt', 'w', encoding='utf-8') as f:
        f.write(text[idx-200:idx+400])
    print("Thumb written at", idx)
else:
    print("Thumb not found in HTML body")
