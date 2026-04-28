with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

old_slider_code = """<a class="iva-item-sliderLink-hO7qj" data-marker="item-photo-sliderLink" itemprop="url" href="#" target="_blank" rel="noopener noreferrer"><div class="photo-slider-root-_kL8M photo-slider-roundCorners-j8Wrb" data-marker="item-photo"><div class="photo-slider-photoSlider-b9P07 photo-slider-aspect-ratio-1-1-aIB4A"><ul class="photo-slider-list-PxsU9" style="display:flex; overflow-x:auto; scroll-snap-type:x mandatory; scrollbar-width:none;">
${(car.image_urls && car.image_urls.length > 0 ? car.image_urls : [car.image_url]).map((url, idx) => `
<li onclick="event.stopPropagation(); window.open('car_page.html?id=${car.id}&img=${idx}', '_blank')" class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; scroll-snap-align: start; cursor:pointer;"><div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73">
<img alt="${car.title}" class="photo-slider-image-PWbIy" itemprop="image" importance="high" src="${url}" loading="${idx === 0 ? 'eager' : 'lazy'}"></div></li>
`).join('')}</ul></div></div></a>"""

new_slider_code = """<div class="iva-item-sliderLink-hO7qj" data-marker="item-photo-sliderLink" style="position:relative;">
<div class="photo-slider-root-_kL8M photo-slider-roundCorners-j8Wrb" data-marker="item-photo"><div class="photo-slider-photoSlider-b9P07 photo-slider-aspect-ratio-1-1-aIB4A">
<ul class="photo-slider-list-PxsU9" id="slider-${car.id}" style="display:flex; overflow-x:hidden; scrollbar-width:none; width: 100%; height: 100%;">
${(car.image_urls && car.image_urls.length > 0 ? car.image_urls : [car.image_url]).map((url, idx) => `
<li class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; cursor:pointer; width: 100%; height: 100%;"><div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73">
<img alt="${car.title}" class="photo-slider-image-PWbIy" itemprop="image" importance="high" src="${url}" loading="${idx === 0 ? 'eager' : 'lazy'}" style="width:100%;height:100%;object-fit:cover;"></div></li>
`).join('')}</ul>
<div style="position:absolute; top:0; left:0; width:100%; height:100%; display:flex; z-index:10;">
${(car.image_urls && car.image_urls.length > 0 ? car.image_urls : [car.image_url]).map((url, idx) => `
<div style="flex: 1; height: 100%; cursor:pointer;" 
     onmouseover="document.getElementById('slider-${car.id}').scrollLeft = document.getElementById('slider-${car.id}').offsetWidth * ${idx};"
     onclick="window.open('car_page.html?id=${car.id}&img=${idx}', '_blank')">
</div>
`).join('')}
</div>
</div></div></div>"""

if old_slider_code in text:
    text = text.replace(old_slider_code, new_slider_code)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed hover gallery logic")
else:
    print("Hover gallery logic not found")
