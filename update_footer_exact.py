import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    (r'(?i)(href=")[^"]*("[^>]*>\s*Помощь\s*</a>)', r'\g<1>https://support.avito.ru/\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Безопасность\s*</a>)', r'\g<1>https://www.avito.ru/safety\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Реклама на сайте\s*</a>)', r'\g<1>https://www.avito.ru/business\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*О компании\s*</a>)', r'\g<1>https://www.avito.ru/company\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Карьера\s*</a>)', r'\g<1>https://avito.career/\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Журнал\s*</a>)', r'\g<1>https://auto.avito.ru/\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Авито Журнал\s*</a>)', r'\g<1>https://auto.avito.ru/\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Блог\s*</a>)', r'\g<1>https://www.avito.ru/blog\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*#яПомогаю\s*</a>)', r'\g<1>https://www.avito.ru/avito-care/crisis-help\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Приложение\s*</a>)', r'\g<1>https://www.avito.ru/info/app\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Займы\s+онлайн\s*</a>)', r'\g<1>https://www.avito.ru/finance/zaimy\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Каталог\s+автомобилей\s*</a>)', r'\g<1>https://www.avito.ru/catalog/avtomobili\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Каталог\s+новостроек\s*</a>)', r'\g<1>https://www.avito.ru/moskva/kvartiry/catalog/novostroyki\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Карта\s+сайта\s*</a>)', r'\g<1>https://www.avito.ru/links\g<2>'),
    (r'(?i)(href=")[^"]*("[^>]*>\s*Свежие\s+объявления\s*</a>)', r'\g<1>https://www.avito.ru/links/items\g<2>')
]

count = 0
for pattern, repl in replacements:
    old_html = html
    html = re.sub(pattern, repl, html)
    if html != old_html:
        count += 1

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Updated {count} different types of links.')
