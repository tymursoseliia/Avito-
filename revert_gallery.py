import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# Original slider code
original_code = """<a class="iva-item-sliderLink-hO7qj" data-marker="item-photo-sliderLink" itemprop="url" href="#" target="_blank" rel="noopener noreferrer"><div class="photo-slider-root-_kL8M photo-slider-roundCorners-j8Wrb" data-marker="item-photo"><div class="photo-slider-photoSlider-b9P07 photo-slider-aspect-ratio-1-1-aIB4A"><ul class="photo-slider-list-PxsU9" style="display:flex; overflow-x:auto; scroll-snap-type:x mandatory; scrollbar-width:none;">
${(car.image_urls && car.image_urls.length > 0 ? car.image_urls : [car.image_url]).map((url, idx) => `
<li onclick="event.stopPropagation(); window.open('car_page.html?id=${car.id}&img=${idx}', '_blank')" class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; scroll-snap-align: start; cursor:pointer;"><div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73">
<img alt="${car.title}" class="photo-slider-image-PWbIy" itemprop="image" importance="high" src="${url}" loading="${idx === 0 ? 'eager' : 'lazy'}"></div></li>
`).join('')}</ul></div></div></a>"""

# Let's find the current block
start_str = '<div class="iva-item-sliderLink-hO7qj"'
end_str = '</div></div></div>\n${badgeHtml}'

idx1 = text.find(start_str)
idx2 = text.find(end_str, idx1)

if idx1 != -1 and idx2 != -1:
    current_block = text[idx1:idx2]
    text = text.replace(current_block, original_code + '\n')
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Reverted to original gallery")
else:
    print("Could not find current block")

