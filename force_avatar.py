with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

js_addition = """
            // 11. Force avatar replace
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

if '// 11. Force avatar replace' not in text:
    text = text.replace("// 4. Update Native Gallery", js_addition + "\n\n            // 4. Update Native Gallery")
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added Aggressive Avatar replace logic")
else:
    print("Avatar replace logic already exists")
