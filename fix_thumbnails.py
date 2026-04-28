with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("th.style.display = 'none';", "th.remove();")

with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated update_car_page.py to use th.remove() for extra thumbnails")
