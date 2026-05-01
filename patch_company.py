with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

js_addition = """
            // 9. Replace Company Name and Logo
            // Replace text
            const allElementsText = document.querySelectorAll('a, p, span, div');
            allElementsText.forEach(el => {
                if (el.children.length === 0 && el.textContent) {
                    if (el.textContent.includes('Автомиг')) {
                        el.textContent = el.textContent.replace(/Автомиг/g, 'Автомиг');
                    }
                    if (el.textContent.includes('Газтормоз')) {
                        el.textContent = el.textContent.replace(/Газтормоз/g, 'Автомиг');
                    }
                    if (el.textContent.includes('ГазТормоз')) {
                        el.textContent = el.textContent.replace(/ГазТормоз/g, 'Автомиг');
                    }
                }
            });

            // Replace logo
            // The gaztormoz logo is usually a specific img tag
            const allImages = document.querySelectorAll('img');
            allImages.forEach(img => {
                if (img.src && (img.src.includes('avatar') || img.src.includes('logo') || img.src.includes('gaztormoz') || img.src === 'https://40.img.avito.st/image/1/1.k0QhGba102vP29z7NIf2E26_021P01z.p9tI3XW5mJ_B_8zFQQHkOOTa7M54qK2w2R2B6U99oKk' || img.src.includes('k0QhGba102vP29z7NIf2E26_021P01z.p9tI3XW5mJ_B_8zFQQHkOOTa7M54qK2w2R2B6U99oKk'))) {
                    // Let's replace the avatar/logo with Avtomig's logo
                    // Avtomig logo is https://i.ibb.co/68ZJ2F9/111.jpg
                    if (img.parentElement && img.parentElement.tagName === 'DIV' && img.parentElement.classList.contains('_9275a4968c2dc72b')) {
                        // This is likely the seller avatar wrapper or near it
                    }
                }
            });
            
            // Just specifically target the seller logo image
            // We can look for the seller link href
            const sellerLinks = document.querySelectorAll('a[href*="gaztormoz"]');
            sellerLinks.forEach(link => {
                // If it contains an image, it's the logo link
                const img = link.querySelector('img');
                if (img) {
                    img.src = 'https://i.ibb.co/68ZJ2F9/111.jpg';
                    // also fix style to ensure it fits well
                    img.style.objectFit = 'cover';
                    img.style.borderRadius = '50%';
                }
            });
"""

if '// 9. Replace Company Name and Logo' not in text:
    text = text.replace("// 4. Update Native Gallery", js_addition + "\n\n            // 4. Update Native Gallery")
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added Company Name logic")
else:
    print("Company Name logic already exists")
