import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the previous JS with a completely synchronous one
new_js = """
<script>
(function() {
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

    // Append to body immediately
    var div = document.createElement('div');
    div.innerHTML = dropdownHTML;
    document.body.appendChild(div.firstElementChild);
    
    var dropdown = document.getElementById('custom-mega-dropdown');
    
    // Global click handler, using capture phase
    window.addEventListener('click', function(e) {
        // Is it the button or inside the button?
        var isBtn = false;
        var btnElement = null;
        
        var target = e.target;
        while (target && target !== document.body) {
            // Check by exact class OR by text content containing "Ещё"
            if ((target.classList && target.classList.contains('beeccf01c8a9fa23')) || 
                (target.textContent && target.textContent.includes('Ещё') && target.tagName === 'A')) {
                isBtn = true;
                btnElement = target;
                break;
            }
            target = target.parentNode;
        }

        if (isBtn) {
            e.preventDefault();
            e.stopPropagation();
            
            if (dropdown.classList.contains('show')) {
                dropdown.classList.remove('show');
            } else {
                var rect = btnElement.getBoundingClientRect();
                dropdown.style.top = (rect.bottom + window.scrollY + 10) + 'px';
                
                var leftPos = rect.left - 500;
                if (leftPos < 20) leftPos = 20;
                dropdown.style.left = leftPos + 'px';
                
                dropdown.classList.add('show');
            }
        } else if (dropdown && !dropdown.contains(e.target)) {
            dropdown.classList.remove('show');
        }
    }, true);
})();
</script>
"""

# Extract current script block
idx1 = html.rfind('<script>')
if idx1 != -1:
    html = html[:idx1] + new_js + '\n</body>\n</html>'

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated script to IIFE.")
