with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

# I will update the logic for "11. Force avatar replace" to be cleaner
old_code = """            // 11. Force avatar replace
            const avatars = document.querySelectorAll('[data-marker="seller-info/avatar"], [data-marker="seller-info/avatar-link"]');
            avatars.forEach(avatar => {
                // The avatar might be the element itself or an img/div inside it
                // We'll just force the background on the container and any child divs
                avatar.style.backgroundImage = 'url("logo.jpg")';
                avatar.style.backgroundSize = 'cover';
                avatar.style.backgroundPosition = 'center';
                
                const children = avatar.querySelectorAll('div, span, img');
                children.forEach(child => {
                    if (child.tagName === 'IMG') {
                        child.src = 'logo.jpg';
                        child.style.objectFit = 'cover';
                        child.style.borderRadius = '50%';
                    } else {
                        child.style.backgroundImage = 'url("logo.jpg")';
                        child.style.backgroundSize = 'cover';
                        child.style.backgroundPosition = 'center';
                    }
                });
            });"""

new_code = """            // 11. Force avatar replace
            const avatars = document.querySelectorAll('[data-marker="seller-info/avatar"], [data-marker="seller-info/avatar-link"]');
            avatars.forEach(avatar => {
                // Clear any weird backgrounds on the avatar link wrapper itself
                avatar.style.background = 'transparent';
                
                // Usually Avito puts an img inside. Let's find it.
                const img = avatar.querySelector('img');
                if (img) {
                    img.src = 'logo.jpg';
                    img.style.objectFit = 'contain';
                    img.style.backgroundColor = 'white';
                    img.style.borderRadius = '50%';
                    // remove any background from siblings/parents to prevent ghosting
                    const allInner = avatar.querySelectorAll('div, span');
                    allInner.forEach(el => el.style.background = 'transparent');
                } else {
                    // If there's no img tag, apply it to the first div child or the avatar itself
                    const innerDiv = avatar.querySelector('div') || avatar;
                    innerDiv.style.backgroundImage = 'url("logo.jpg")';
                    innerDiv.style.backgroundSize = 'contain';
                    innerDiv.style.backgroundPosition = 'center';
                    innerDiv.style.backgroundRepeat = 'no-repeat';
                    innerDiv.style.backgroundColor = 'white';
                    innerDiv.style.borderRadius = '50%';
                }
            });"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed avatar styling logic")
else:
    print("Old avatar logic not found")
