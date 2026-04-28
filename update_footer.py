import re

links_map = {
    "Помощь": "https://support.avito.ru/",
    "Безопасность": "https://www.avito.ru/safety",
    "Реклама на сайте": "https://www.avito.ru/business",
    "О компании": "https://www.avito.ru/company",
    "Карьера": "https://avito.career/",
    "Авито Журнал": "https://auto.avito.ru/",
    "Блог": "https://www.avito.ru/blog",
    "Авито помогает": "https://www.avito.ru/avito-care",
    "Приложение Авито": "https://www.avito.ru/info/app",
    "Авито Кредит": "https://www.avito.ru/credits/buyer",
    "Каталог автомобилей": "https://www.avito.ru/catalog/avtomobili",
    "ВКонтакте": "https://vk.com/avito",
    "Одноклассники": "https://ok.ru/avito",
    "Telegram": "https://t.me/avito",
    "YouTube": "https://www.youtube.com/avito",
    "RuTube": "https://rutube.ru/channel/24446549/"
}

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

for text, url in links_map.items():
    # Replace the href of the specific link
    # We will find the pattern <a ... href="..." ...>Text</a>
    # Or simply: re.sub(r'(<a[^>]*?href=)["\'][^"\']*?["\']([^>]*?>\s*' + re.escape(text) + r'\s*</a>)', r'\g<1>"' + url + r'"\g<2>', html)
    html = re.sub(
        r'(<a[^>]*?href=)["\'][^"\']*?["\']([^>]*?>\s*' + re.escape(text) + r'\s*</a>)',
        r'\1"' + url + r'"\2',
        html,
        flags=re.IGNORECASE
    )

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Footer links updated successfully.")
