import re
with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()
links = re.findall(r'href=\"(https://(vk\.com|ok\.ru|t\.me|www\.youtube\.com|rutube\.ru)[^\"]*)\"', html)
print("Social links found:", links)

# Let's check text links:
texts = ["Помощь", "Безопасность", "Реклама на сайте", "О компании", "Карьера", "Авито Журнал", "Блог", "Авито помогает", "Приложение Авито", "Авито Кредит", "Каталог автомобилей"]
for text in texts:
    match = re.search(r'<a[^>]*href=\"([^\"]*)\"[^>]*>.*?'+text+'.*?</a>', html, flags=re.IGNORECASE|re.DOTALL)
    if match:
        print(f"{text}: {match.group(1)}")
    else:
        print(f"{text}: NOT FOUND")
