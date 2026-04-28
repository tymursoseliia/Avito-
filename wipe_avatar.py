with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """            // 11. Force avatar replace
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

new_code = """            // 11. Force avatar replace
            const avatars = document.querySelectorAll('[data-marker="seller-info/avatar"], [data-marker="seller-info/avatar-link"]');
            avatars.forEach(avatar => {
                // Completely destroy everything inside the avatar container
                avatar.innerHTML = '';
                
                // Reset any styles on the container itself just in case
                avatar.style.background = 'transparent';
                avatar.style.backgroundImage = 'none';
                
                // Insert a brand new, clean image tag
                const newImg = document.createElement('img');
                newImg.src = 'logo.jpg';
                newImg.style.width = '100%';
                newImg.style.height = '100%';
                newImg.style.objectFit = 'contain';
                newImg.style.borderRadius = '50%';
                newImg.style.backgroundColor = 'white';
                newImg.style.display = 'block';
                
                avatar.appendChild(newImg);
            });"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed avatar with innerHTML wipe")
else:
    print("Avatar logic not found")
