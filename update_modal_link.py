with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_button = '<button style="background: #1a1a1a; color: white; border: none; border-radius: 8px; padding: 12px 24px; font-size: 15px; font-weight: 600; cursor: pointer;">Подробнее</button>'
new_button = '<button onclick="window.open(\'https://www.avito.ru/journal/articles/kak-kupit-avto-na-zakaz-iz-drugoy-strany\', \'_blank\')" style="background: #1a1a1a; color: white; border: none; border-radius: 8px; padding: 12px 24px; font-size: 15px; font-weight: 600; cursor: pointer;">Подробнее</button>'

if old_button in text:
    text = text.replace(old_button, new_button)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated button link in update_car_page.py")
else:
    print("Could not find old button in update_car_page.py")
