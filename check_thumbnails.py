with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

# find first index that is NOT in the <script>
idx = text.find('data-marker="image-frame/thumbnail"')
if idx != -1:
    print(text[idx-200:idx+400])
