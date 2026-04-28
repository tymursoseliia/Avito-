import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the JS code block for the cardHtml and replace the photo-slider-list-PxsU9 content.

old_img_code = '''<ul class="photo-slider-list-PxsU9"><li class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX"><div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73">
<img alt="${car.title}" class="photo-slider-image-PWbIy" itemprop="image" importance="high" src="${car.image_url}"></div></li></ul>'''

new_img_code = '''<ul class="photo-slider-list-PxsU9" style="display:flex; overflow-x:auto; scroll-snap-type:x mandatory; scrollbar-width:none;">
${(car.image_urls && car.image_urls.length > 0 ? car.image_urls : [car.image_url]).map((url, idx) => `
<li class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; scroll-snap-align: start;"><div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73">
<img alt="${car.title}" class="photo-slider-image-PWbIy" itemprop="image" importance="high" src="${url}" loading="${idx === 0 ? 'eager' : 'lazy'}"></div></li>
`).join('')}</ul>'''

if old_img_code in content:
    content = content.replace(old_img_code, new_img_code)
    
    # Also hide webkit scrollbar for slider
    css_to_add = '''<style>
.photo-slider-list-PxsU9::-webkit-scrollbar { display: none; }
</style>
'''
    if 'photo-slider-list-PxsU9::-webkit-scrollbar' not in content:
        content = content.replace('</head>', css_to_add + '</head>')
        
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Replaced slider code successfully')
else:
    print('Could not find the old image code')
