import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the previous JS with the cloneNode approach
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

        // Add dropdown to body
        if (!document.getElementById('custom-mega-dropdown')) {
            var div = document.createElement('div');
            div.innerHTML = dropdownHTML;
            document.body.appendChild(div.firstElementChild);
        }
        
        var dropdown = document.getElementById('custom-mega-dropdown');
        
        // Find the "Ещё" button
        var allLinks = document.querySelectorAll('a');
        var oldBtn = null;
        for (var i = 0; i < allLinks.length; i++) {
            if (allLinks[i].textContent && allLinks[i].textContent.includes('Ещё') && allLinks[i].getBoundingClientRect().top < 200) {
                oldBtn = allLinks[i];
                break;
            }
        }
        
        if (oldBtn) {
            // CLONE the button to strip all React event listeners
            var newBtn = oldBtn.cloneNode(true);
            newBtn.style.cursor = 'pointer'; // Ensure it looks clickable
            oldBtn.parentNode.replaceChild(newBtn, oldBtn);
            
            // Add our own raw event listener
            newBtn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                
                // Toggle logic
                if (dropdown.classList.contains('show')) {
                    dropdown.classList.remove('show');
                } else {
                    var rect = newBtn.getBoundingClientRect();
                    dropdown.style.top = (rect.bottom + window.scrollY + 5) + 'px';
                    
                    var leftPos = rect.left - 500;
                    if (leftPos < 20) leftPos = 20;
                    dropdown.style.left = leftPos + 'px';
                    
                    dropdown.classList.add('show');
                }
            });
            
            // Global click to close
            document.addEventListener('click', function(e) {
                if (dropdown && !dropdown.contains(e.target) && !newBtn.contains(e.target)) {
                    dropdown.classList.remove('show');
                }
            });
            
            console.log("Custom dropdown successfully attached to cloned Ещё button!");
        } else {
            console.log("Error: Could not find Ещё button.");
        }
        
    }, 1500); 
});
</script>
"""

# Extract current script block
idx1 = html.find('<script>\ndocument.addEventListener(\'DOMContentLoaded\', function() {\n    setTimeout')
if idx1 != -1:
    idx2 = html.find('</script>', idx1) + 9
    html = html[:idx1] + new_js + html[idx2:]
else:
    # If not found, just replace before </body>
    html = html.replace('</body>', new_js + '\n</body>')


with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated script to cloneNode.")
