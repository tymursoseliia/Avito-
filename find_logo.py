import re

with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

idx = text.find('Автомиг')
if idx != -1:
    snippet = text[max(0, idx-2000):min(len(text), idx+500)]
    images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', snippet)
    print('Images near Автомиг:', images)
