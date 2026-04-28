with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

js_addition = """
            // 5. Update Header Links
            const topLinks = document.querySelectorAll('a');
            topLinks.forEach(a => {
                if (a.textContent.includes('#яПомогаю')) {
                    a.href = 'https://www.avito.ru/avito-care/crisis-help?from=mp_header';
                    a.target = '_blank';
                }
            });
"""

text = text.replace('// 4. Update Native Gallery', js_addition + '\n            // 4. Update Native Gallery')

with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated update_car_page.py to include link for #яПомогаю")
