import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the CSS to use !important just in case
css_update = """
.custom-mega-dropdown {
    display: none !important;
    position: absolute;
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
.custom-mega-dropdown.show {
    display: grid !important;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
}
"""
html = re.sub(r'\.custom-mega-dropdown \{.*?\.custom-mega-dropdown\.show \{.*?\}', css_update.strip(), html, flags=re.DOTALL)

# 2. Update the JS to use a simple click listener with closest() and NOT touch React DOM
new_js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
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
    
    // We use window level click, capture phase
    window.addEventListener('click', function(e) {
        // Find if they clicked the exact "Ещё" button wrapper class
        var btn = e.target.closest('.beeccf01c8a9fa23');
        
        // Or if they clicked a span that contains 'Ещё'
        if (!btn && e.target.textContent && e.target.textContent.includes('Ещё')) {
            btn = e.target;
        }

        if (btn) {
            e.preventDefault();
            e.stopPropagation();
            
            if (dropdown.classList.contains('show')) {
                dropdown.classList.remove('show');
            } else {
                var rect = btn.getBoundingClientRect();
                dropdown.style.top = (rect.bottom + window.scrollY + 5) + 'px';
                
                var leftPos = rect.left - 500;
                if (leftPos < 20) leftPos = 20;
                dropdown.style.left = leftPos + 'px';
                
                dropdown.classList.add('show');
            }
        } else if (dropdown && !dropdown.contains(e.target)) {
            dropdown.classList.remove('show');
        }
    }, true);
    
});
</script>
"""

# Replace old script
idx = html.rfind('<script>')
if idx != -1:
    html = html[:idx] + new_js + '\n</body>\n</html>'

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated script to use closest() class matching.")
