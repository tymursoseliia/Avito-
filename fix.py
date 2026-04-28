with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

old_str = "window.open(`car_page.html?id=${car.id}&img=${idx}`, `_blank`)"
new_str = "window.open('car_page.html?id=${car.id}&img=${idx}', '_blank')"

content = content.replace(old_str, new_str)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed syntax error in JS template string!")
