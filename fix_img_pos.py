with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# I will replace the <li> to remove position: relative
old_li = """<li class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; cursor:pointer; width: 100%; height: 100%; position:relative;">"""
new_li = """<li class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; cursor:pointer; width: 100%; height: 100%;">"""

# The img is inside <div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73">
# By default, photo-slider-image-PWbIy has position absolute in Avito CSS!
# Let's remove our inline position absolute, or change it to ensure it targets the right wrapper.
# Actually, the original HTML had no inline styles on the img.
old_img = """style="width:100%;height:100%;object-fit:cover;position:absolute;top:0;left:0;">"""
new_img = """style="width:100%;height:100%;object-fit:cover;position:absolute;top:0;left:0;">"""

if old_li in text:
    text = text.replace(old_li, new_li)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed image positioning")
else:
    print("Image positioning HTML not found")
