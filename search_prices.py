with open('car_page.html', encoding='utf-8') as f:
    text = f.read()

print('data-marker item-price count:', text.count('data-marker="item-view/item-price"'))

# Let's also search for anything that looks like a price with the ruble sign
import re
prices = set(re.findall(r'>([^<]*13[^<]*199[^<]*000[^<]*)<', text.replace('&nbsp;', ' ')))
print('Price formats found in text nodes:', prices)
