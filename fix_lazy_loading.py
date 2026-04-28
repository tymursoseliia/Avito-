with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will replace the loading logic in hover_gallery.py
old_img = """<img alt="${car.title}" class="photo-slider-image-PWbIy" itemprop="image" importance="high" src="${url}" loading="${idx === 0 ? 'eager' : 'lazy'}" style="width:100%;height:100%;object-fit:cover;">"""
new_img = """<img alt="${car.title}" class="photo-slider-image-PWbIy" itemprop="image" importance="high" src="${url}" style="width:100%;height:100%;object-fit:cover;position:absolute;top:0;left:0;">"""

# Also ensure the parent container maintains the aspect ratio. The class photo-slider-keepImageRatio-BgO73 usually uses padding-bottom.
# We'll just make sure the li is relative.
old_li = """<li class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; cursor:pointer; width: 100%; height: 100%;">"""
new_li = """<li class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; cursor:pointer; width: 100%; height: 100%; position:relative;">"""

if old_img in text:
    text = text.replace(old_img, new_img)
    text = text.replace(old_li, new_li)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed lazy loading and positioning for gallery images")
else:
    print("Image HTML not found")
