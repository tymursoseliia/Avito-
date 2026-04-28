with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

# I will update the logic for "11. Force avatar replace" to target data-marker="seller-info/avatar"
old_code = """            // 11. Force avatar replace
            const sellerInfos = document.querySelectorAll('[data-marker="item-view/seller-info"]');
            sellerInfos.forEach(info => {
                // Find all divs/spans that have a background image
                const elementsWithBg = info.querySelectorAll('*');
                elementsWithBg.forEach(el => {
                    const bg = el.style.backgroundImage;
                    if (bg && bg.includes('url')) {
                        // It's likely the avatar
                        el.style.backgroundImage = 'url("https://i.ibb.co/68ZJ2F9/111.jpg")';
                        el.style.backgroundSize = 'cover';
                    }
                    if (el.tagName === 'IMG' && !el.src.includes('avatar')) {
                        // Check if it's the avatar img
                        if (el.classList.contains('css-1i6k59z')) return; // gallery image
                        el.src = 'https://i.ibb.co/68ZJ2F9/111.jpg';
                        el.style.objectFit = 'cover';
                    }
                });
            });"""

new_code = """            // 11. Force avatar replace
            const avatars = document.querySelectorAll('[data-marker="seller-info/avatar"], [data-marker="seller-info/avatar-link"]');
            avatars.forEach(avatar => {
                // The avatar might be the element itself or an img/div inside it
                // We'll just force the background on the container and any child divs
                avatar.style.backgroundImage = 'url("https://i.ibb.co/68ZJ2F9/111.jpg")';
                avatar.style.backgroundSize = 'cover';
                avatar.style.backgroundPosition = 'center';
                
                const children = avatar.querySelectorAll('div, span, img');
                children.forEach(child => {
                    if (child.tagName === 'IMG') {
                        child.src = 'https://i.ibb.co/68ZJ2F9/111.jpg';
                        child.style.objectFit = 'cover';
                        child.style.borderRadius = '50%';
                    } else {
                        child.style.backgroundImage = 'url("https://i.ibb.co/68ZJ2F9/111.jpg")';
                        child.style.backgroundSize = 'cover';
                        child.style.backgroundPosition = 'center';
                    }
                });
            });"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed avatar targeting logic")
else:
    print("Old avatar logic not found")
