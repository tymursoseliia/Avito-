import sys
import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the previously injected HTML dropdown
start_idx = html.find('<div id="custom-mega-dropdown"')
if start_idx != -1:
    end_idx = html.find('</div>\n</div>\n</div>', start_idx)
    # The dropdown HTML ends with 4 columns. We need to be careful to remove the whole block.
    # A safer way is to use regex or find the exact block.
    # Let's just find the end of the <div id="custom-mega-dropdown"...> block
    # It has 4 mega-dropdown-col divs. Let's just remove the exact string.
    
    # Actually, it's easier to find the script and style tags, and the div
    pass

# We can just run a python script to strip out everything between <style> custom-mega-dropdown and the script.
# But it's easier to just use regex to clean it up.
html = re.sub(r'<div id="custom-mega-dropdown".*?</div>\n</div>\n</div>\n</div>\n</div>', '', html, flags=re.DOTALL)

# Clean up the inline onclick we added
html = re.sub(r'id="btn-more-dropdown" onclick="[^"]+" ', '', html)

# Clean up the previous <script> block
html = re.sub(r'<script>\ndocument\.addEventListener\(\'DOMContentLoaded\', function\(\) {\n    var moreBtn = document\.getElementById.*?</script>', '', html, flags=re.DOTALL)

# Keep the CSS, but update it to be body-relative
css_update = """
.custom-mega-dropdown {
    display: none;
    position: absolute; /* Relative to body */
    width: 800px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    padding: 32px 24px;
    z-index: 99999;
    box-sizing: border-box;
    cursor: default;
    text-align: left;
}
"""
html = re.sub(r'\.custom-mega-dropdown \{.*?\}', css_update.strip(), html, flags=re.DOTALL)

# Inject the new advanced JS that creates the dropdown dynamically outside the React root
new_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        var dropdownHTML = `
        <div id="custom-mega-dropdown" class="custom-mega-dropdown">
            <div class="mega-dropdown-col">
                <div class="mega-dropdown-all-cats">Все категории</div>
                <div class="mega-dropdown-section">
                    <h3>Транспорт</h3>
                    <a href="https://www.avito.ru/">Автомобили</a>
                    <a href="https://www.avito.ru/">Мотоциклы и мототехника</a>
                    <a href="https://www.avito.ru/">Грузовики и спецтехника</a>
                    <a href="https://www.avito.ru/">Аренда спецтехники</a>
                    <a href="https://www.avito.ru/">Водный транспорт</a>
                    <a href="https://www.avito.ru/">Запчасти и аксессуары</a>
                </div>
                <div class="mega-dropdown-section">
                    <h3>Для дома и дачи</h3>
                    <a href="https://www.avito.ru/">Ремонт и строительство</a>
                    <a href="https://www.avito.ru/">Мебель и интерьер</a>
                    <a href="https://www.avito.ru/">Бытовая техника</a>
                    <a href="https://www.avito.ru/">Продукты питания</a>
                    <a href="https://www.avito.ru/">Растения</a>
                    <a href="https://www.avito.ru/">Посуда и товары для кухни</a>
                </div>
                <div class="mega-dropdown-section">
                    <h3>Бизнес и оборудование</h3>
                    <a href="https://www.avito.ru/">Оборудование для бизнеса</a>
                    <a href="https://www.avito.ru/">Франшизы</a>
                    <a href="https://www.avito.ru/">Готовый бизнес</a>
                    <a href="https://www.avito.ru/">ПО для бизнеса</a>
                </div>
            </div>
            
            <div class="mega-dropdown-col">
                <div class="mega-dropdown-section">
                    <h3>Недвижимость</h3>
                    <a href="https://www.avito.ru/">Купить жильё</a>
                    <a href="https://www.avito.ru/">Путешествия</a>
                    <a href="https://www.avito.ru/">Снять долгосрочно</a>
                    <a href="https://www.avito.ru/">Коммерческая недвижимость</a>
                    <a href="https://www.avito.ru/">Другие категории</a>
                </div>
                <div class="mega-dropdown-section" style="margin-top: 10px;">
                    <h3>Электроника</h3>
                    <a href="https://www.avito.ru/">Телефоны</a>
                    <a href="https://www.avito.ru/">Аудио и видео</a>
                    <a href="https://www.avito.ru/">Товары для компьютера</a>
                    <a href="https://www.avito.ru/">Игры, приставки и программы</a>
                    <a href="https://www.avito.ru/">Ноутбуки</a>
                    <a href="https://www.avito.ru/">Настольные компьютеры</a>
                    <a href="https://www.avito.ru/">Фототехника</a>
                    <a href="https://www.avito.ru/">Планшеты и электронные книги</a>
                    <a href="https://www.avito.ru/">Оргтехника и расходники</a>
                </div>
            </div>
            
            <div class="mega-dropdown-col">
                <div class="mega-dropdown-section">
                    <h3>Работа</h3>
                    <a href="https://www.avito.ru/">Ищу работу</a>
                    <a href="https://www.avito.ru/">Ищу сотрудника</a>
                </div>
                <div class="mega-dropdown-section" style="margin-top: 10px;">
                    <h3>Услуги</h3>
                </div>
                <div class="mega-dropdown-section" style="margin-top: 10px;">
                    <h3>Хобби и отдых</h3>
                    <a href="https://www.avito.ru/">Билеты и путешествия</a>
                    <a href="https://www.avito.ru/">Велосипеды</a>
                    <a href="https://www.avito.ru/">Книги и журналы</a>
                    <a href="https://www.avito.ru/">Коллекционирование</a>
                    <a href="https://www.avito.ru/">Музыкальные инструменты</a>
                    <a href="https://www.avito.ru/">Охота и рыбалка</a>
                    <a href="https://www.avito.ru/">Спорт и отдых</a>
                </div>
            </div>
            
            <div class="mega-dropdown-col">
                <div class="mega-dropdown-section">
                    <h3>Личные вещи</h3>
                    <a href="https://www.avito.ru/">Как на праздник</a>
                    <a href="https://www.avito.ru/">Деловой стиль</a>
                    <a href="https://www.avito.ru/">Жизнь в движении</a>
                    <a href="https://www.avito.ru/">Время отдохнуть</a>
                    <a href="https://www.avito.ru/">Винтажные образы</a>
                    <a href="https://www.avito.ru/">Одежда, обувь, аксессуары</a>
                    <a href="https://www.avito.ru/">Детская одежда и обувь</a>
                    <a href="https://www.avito.ru/">Товары для детей и игрушки</a>
                    <a href="https://www.avito.ru/">Красота и здоровье</a>
                    <a href="https://www.avito.ru/">Часы и украшения</a>
                </div>
                <div class="mega-dropdown-section" style="margin-top: 10px;">
                    <h3>Животные</h3>
                    <a href="https://www.avito.ru/">Собаки</a>
                    <a href="https://www.avito.ru/">Кошки</a>
                    <a href="https://www.avito.ru/">Птицы</a>
                    <a href="https://www.avito.ru/">Аквариум</a>
                    <a href="https://www.avito.ru/">Другие животные</a>
                    <a href="https://www.avito.ru/">Товары для животных</a>
                </div>
            </div>
        </div>
        `;

        var div = document.createElement('div');
        div.innerHTML = dropdownHTML;
        document.body.appendChild(div.firstElementChild);
        
        var dropdown = document.getElementById('custom-mega-dropdown');
        
        document.addEventListener('click', function(e) {
            var target = e.target;
            var isMoreBtn = false;
            var btnElement = null;
            
            // Event delegation to catch clicks on "Ещё" even if React recreates it
            while (target && target !== document.body) {
                if (target.textContent && target.textContent.trim().startsWith('Ещё') && target.tagName === 'A') {
                    isMoreBtn = true;
                    btnElement = target;
                    break;
                }
                target = target.parentNode;
            }
            
            if (isMoreBtn && dropdown) {
                e.preventDefault();
                e.stopPropagation();
                
                // Position dropdown relative to the button exactly
                var rect = btnElement.getBoundingClientRect();
                dropdown.style.top = (rect.bottom + window.scrollY + 5) + 'px';
                
                // Center it generally under the navigation, max right screen bound
                var leftPos = rect.left - 500;
                if (leftPos < 20) leftPos = 20;
                dropdown.style.left = leftPos + 'px';
                
                dropdown.classList.toggle('show');
            } else if (dropdown && !dropdown.contains(e.target)) {
                dropdown.classList.remove('show');
            }
        });
    }, 1500); // Wait 1.5 seconds to ensure React finished hydrating and resetting DOM
});
</script>
"""

html = html.replace('</body>', new_js + '\n</body>')

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated script to bypass React hydration deletion.")
