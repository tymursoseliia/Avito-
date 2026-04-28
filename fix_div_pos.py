with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

old_div = """<div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73">"""
new_div = """<div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73" style="position:relative; width:100%; height:100%;">"""

if old_div in text:
    text = text.replace(old_div, new_div)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed div positioning")
else:
    print("Div positioning HTML not found")
