with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """            // 11. Force avatar replace
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
                
                // Add padding so the logo doesn't touch the edges, like the original
                newImg.style.boxSizing = 'border-box';
                newImg.style.padding = '15%'; 
                
                // Optional subtle border like avito usually has
                newImg.style.border = '1px solid rgba(0, 0, 0, 0.1)';
                
                avatar.appendChild(newImg);
            });"""

new_code = """            // 11. Force avatar replace
            // Revert to a much safer approach: just change the background of the existing A tag
            const avatarLinks = document.querySelectorAll('[data-marker="seller-info/avatar-link"]');
            avatarLinks.forEach(link => {
                // The link is already perfectly sized and rounded by Avito's CSS
                link.style.backgroundImage = 'url("logo.jpg")';
                link.style.backgroundSize = '70%'; // Make the logo slightly smaller inside the circle
                link.style.backgroundPosition = 'center';
                link.style.backgroundRepeat = 'no-repeat';
                link.style.backgroundColor = 'white';
                
                // Remove any inner text or images that might interfere
                link.innerHTML = '';
            });"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Reverted to safe background replace")
else:
    print("Avatar logic not found")
