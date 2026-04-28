import re

with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'data-marker="[^"]*avatar[^"]*"', text)
print('Avatar markers:', set(matches))

logo_matches = re.findall(r'data-marker="[^"]*logo[^"]*"', text)
print('Logo markers:', set(logo_matches))
