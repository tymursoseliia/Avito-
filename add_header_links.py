with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

js_addition = """
            // 5. Update Header Links to return to catalog
            const topLinks = document.querySelectorAll('a');
            topLinks.forEach(a => {
                if (['Для бизнеса', 'Карьера в Авито', 'Помощь', 'Каталоги', '#яПомогаю'].some(text => a.textContent.includes(text))) {
                    a.href = 'clean_avito (1).html';
                    a.onclick = (e) => { e.preventDefault(); e.stopPropagation(); window.location.href = 'clean_avito (1).html'; };
                }
            });
            // Also Avito logo
            const logo = document.querySelector('a[href="/"]');
            if (logo) {
                logo.href = 'clean_avito (1).html';
                logo.onclick = (e) => { e.preventDefault(); window.location.href = 'clean_avito (1).html'; };
            }
"""

text = text.replace('// 4. Update Native Gallery', js_addition + '\n            // 4. Update Native Gallery')

with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated update_car_page.py to include header links logic")
