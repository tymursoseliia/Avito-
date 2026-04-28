import sys
import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Transcribe columns
col1 = """
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
"""

col2 = """
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
"""

col3 = """
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
"""

col4 = """
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
"""

dropdown_html = f"""
<div id="custom-mega-dropdown" class="custom-mega-dropdown">
    {col1}
    {col2}
    {col3}
    {col4}
</div>
"""

css = """
<style>
.custom-mega-dropdown {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    width: 800px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    padding: 32px 24px;
    z-index: 9999;
    box-sizing: border-box;
    cursor: default;
    text-align: left;
}
.custom-mega-dropdown.show {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;
}
.mega-dropdown-col {
    display: flex;
    flex-direction: column;
    gap: 24px;
}
.mega-dropdown-section {
    display: flex;
    flex-direction: column;
    gap: 12px;
}
.mega-dropdown-section h3 {
    font-size: 14px;
    font-weight: 600;
    color: #009cf0;
    margin: 0;
    cursor: pointer;
    line-height: 1.2;
}
.mega-dropdown-section h3:hover {
    color: #0077c2;
}
.mega-dropdown-section a {
    font-size: 12px;
    color: #009cf0;
    text-decoration: none;
    line-height: 1.4;
    transition: color 0.1s ease-in-out;
}
.mega-dropdown-section a:hover {
    color: #0077c2;
}
.mega-dropdown-all-cats {
    font-size: 15px;
    font-weight: 700;
    color: #009cf0;
    margin-bottom: -10px;
    cursor: pointer;
}
.mega-dropdown-all-cats:hover {
    color: #0077c2;
}
.dc04365ae03852a3 {
    position: relative; /* Context for absolute dropdown */
}
</style>
"""

js = """
<script>
document.addEventListener('DOMContentLoaded', function() {
    var moreBtn = document.getElementById('btn-more-dropdown');
    var dropdown = document.getElementById('custom-mega-dropdown');
    
    if(moreBtn && dropdown) {
        moreBtn.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            dropdown.classList.toggle('show');
        });
        
        document.addEventListener('click', function(e) {
            if(!dropdown.contains(e.target) && e.target !== moreBtn && !moreBtn.contains(e.target)) {
                dropdown.classList.remove('show');
            }
        });
    }
});
</script>
"""

# Insert CSS before </head>
html = html.replace('</head>', css + '\n</head>')

# Insert JS before </body>
html = html.replace('</body>', js + '\n</body>')

# Find the "Ещё" button and insert the dropdown HTML
idx = html.find('>Ещё<!-- -->')
if idx != -1:
    a_start = html.rfind('<a ', 0, idx)
    
    # We need to add an ID to the <a> tag so JS can find it
    a_tag_str = html[a_start:html.find('>', a_start)+1]
    new_a_tag = a_tag_str.replace('<a ', '<a id="btn-more-dropdown" ')
    
    html = html[:a_start] + new_a_tag + html[a_start+len(a_tag_str):]
    
    # Find the closing </a>
    a_end = html.find('</a>', idx) + 4
    
    # We want to insert the dropdown right after the </a>
    # Wait, the parent is <div class="dc04365ae03852a3">
    # We should ensure this <div> wraps the <a> and the dropdown.
    # The current DOM is: <div class="dc04365ae03852a3"><a ...>Ещё</a></div>
    # We will insert dropdown right before the closing </div>
    
    # Check if the next tag is </div>
    div_close = html.find('</div>', a_end)
    html = html[:div_close] + dropdown_html + html[div_close:]
    print("Dropdown HTML injected successfully.")
else:
    print("Error: Could not find 'Ещё' button.")

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done.")
