import re

# 1. Update clean_avito (1).html
with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

slider_code_old = '''<li class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; scroll-snap-align: start;"><div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73">'''
slider_code_new = '''<li onclick="event.stopPropagation(); window.open(`car_page.html?id=${car.id}&img=${idx}`, `_blank`)" class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; scroll-snap-align: start; cursor:pointer;"><div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73">'''

if slider_code_old in content:
    content = content.replace(slider_code_old, slider_code_new)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated clean_avito (1).html')

# 2. Update car_page.html to read ?img=idx
with open('car_page.html', 'r', encoding='utf-8') as f:
    car_page = f.read()

if 'const initialImgStr = urlParams.get(\'img\');' not in car_page:
    car_page = car_page.replace('galleryImages = car.image_urls && car.image_urls.length > 0 ? car.image_urls : [car.image_url];',
    '''galleryImages = car.image_urls && car.image_urls.length > 0 ? car.image_urls : [car.image_url];
        const initialImgStr = urlParams.get('img');
        if (initialImgStr) {
            currentImgIndex = parseInt(initialImgStr);
            if (isNaN(currentImgIndex) || currentImgIndex < 0 || currentImgIndex >= galleryImages.length) currentImgIndex = 0;
        }''')
    car_page = car_page.replace('onclick="agOpenModal()"', 'onclick="agSetImage(currentImgIndex); agOpenModal()"')
    
    # Also fix agSetImage not being called initially
    if 'agSetImage(currentImgIndex);' not in car_page:
        car_page = car_page.replace("document.body.insertAdjacentHTML('beforeend', modalHtml);", 
        "document.body.insertAdjacentHTML('beforeend', modalHtml);\n            agSetImage(currentImgIndex);")
        
    with open('car_page.html', 'w', encoding='utf-8') as f:
        f.write(car_page)
    print('Updated car_page.html')

# 3. Update admin.html to compress images to speed up upload and page load
with open('admin.html', 'r', encoding='utf-8') as f:
    admin_page = f.read()

watermark_old = '''                    const canvas = document.createElement('canvas');
                    canvas.width = img.width;
                    canvas.height = img.height;
                    const ctx = canvas.getContext('2d');
                    
                    // Рисуем основное фото
                    ctx.drawImage(img, 0, 0);'''

watermark_new = '''                    const MAX_WIDTH = 1200;
                    const MAX_HEIGHT = 900;
                    let width = img.width;
                    let height = img.height;
                    
                    if (width > height) {
                        if (width > MAX_WIDTH) { height *= MAX_WIDTH / width; width = MAX_WIDTH; }
                    } else {
                        if (height > MAX_HEIGHT) { width *= MAX_HEIGHT / height; height = MAX_HEIGHT; }
                    }
                    
                    const canvas = document.createElement('canvas');
                    canvas.width = width;
                    canvas.height = height;
                    const ctx = canvas.getContext('2d');
                    
                    // Рисуем основное фото
                    ctx.drawImage(img, 0, 0, width, height);
                    
                    // Обновляем img.width для расчетов водяного знака
                    Object.defineProperty(img, 'width', {value: width});
                    Object.defineProperty(img, 'height', {value: height});'''

if watermark_old in admin_page:
    admin_page = admin_page.replace(watermark_old, watermark_new)
    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(admin_page)
    print('Updated admin.html (image compression)')
