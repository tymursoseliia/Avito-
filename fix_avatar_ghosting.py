with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """            // 11. Force avatar replace
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

new_code = """            // 11. Force avatar replace
            const avatars = document.querySelectorAll('[data-marker="seller-info/avatar"], [data-marker="seller-info/avatar-link"]');
            avatars.forEach(avatar => {
                // Clear the parent completely
                avatar.style.background = 'transparent';
                
                // Find all elements inside
                const allElements = avatar.querySelectorAll('*');
                allElements.forEach(el => {
                    if (el.tagName === 'IMG') {
                        // VERY IMPORTANT: remove srcset or the browser will load the old HD image!
                        el.removeAttribute('srcset');
                        el.src = 'logo.jpg';
                        el.style.objectFit = 'contain';
                        el.style.backgroundColor = 'white';
                        el.style.borderRadius = '50%';
                        el.style.width = '100%';
                        el.style.height = '100%';
                    } else {
                        // Strip background from all wrappers to avoid ghosting
                        el.style.background = 'none';
                        el.style.backgroundImage = 'none';
                    }
                });
                
                // If it's pure CSS (no img tag)
                if (!avatar.querySelector('img')) {
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
    print("Fixed avatar srcset ghosting")
else:
    print("Avatar logic not found")
