with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

js_addition = """
            // 7. Redirect Seller Ads Button
            const allLinks = document.querySelectorAll('a');
            allLinks.forEach(link => {
                if (link.textContent && link.textContent.includes('объявлений пользователя')) {
                    link.href = 'clean_avito (1).html';
                }
            });"""

if '// 7. Redirect Seller Ads Button' not in text:
    text = text.replace("// 4. Update Native Gallery", js_addition + "\n\n            // 4. Update Native Gallery")
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added Seller Ads link logic")
else:
    print("Seller Ads link logic already exists")
