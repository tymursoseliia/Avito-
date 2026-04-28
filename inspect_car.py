import re

with open('car_page.html', 'r', encoding='utf-8') as f:
    content = f.read()

def find_tag(marker):
    match = re.search(f'[^>]*data-marker="{marker}"[^>]*>(.*?)</', content)
    if match:
        print(f"Found {marker}:", match.group(0)[:100])
    else:
        print(f"Not found: {marker}")

find_tag('item-view/title-info')
find_tag('item-view/item-price')
find_tag('item-view/address')
find_tag('item-view/gallery')
find_tag('item-properties-item')
