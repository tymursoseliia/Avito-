import re
import json

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the grid
grid_match = re.search(r'<div class="ProfileItemsGrid-module-root-wq8JY">(.*?)<div class="ExtendedProfileStickyContainer-module-sidebar-oF2w3">', content, re.DOTALL)
if grid_match:
    grid_content = grid_match.group(1)
else:
    # try another way
    grid_match = re.search(r'(<div class="ProfileItemsGrid-module-root-wq8JY">.*?)<div class="styles-module-root-auHUM', content, re.DOTALL)
    grid_content = grid_match.group(1) if grid_match else content

items = re.findall(r'<div data-marker="item_list_with_filters.*?itemtype="http://schema.org/Product">(.*?)</div></div></div></div></div></div></div>', grid_content, re.DOTALL)
print(f"Found {len(items)} items")

cars_data = []

for item in items:
    title_match = re.search(r'<a itemprop="url".*?title="(.*?)"', item)
    title = title_match.group(1) if title_match else ""
    
    price_match = re.search(r'<meta itemprop="price" content="(.*?)">', item)
    price = int(price_match.group(1)) if price_match else 0
    
    img_match = re.search(r'<img.*?itemprop="image".*?src="(.*?)"', item)
    img_url = img_match.group(1) if img_match else ""
    
    loc_match = re.search(r'<div class="geo-root-ltL41".*?<span title="".*?</span>(.*?)</span>', item, re.DOTALL)
    loc = loc_match.group(1).strip() if loc_match else ""
    
    date_match = re.search(r'data-marker="item-date">(.*?)</p>', item)
    date_str = date_match.group(1).strip() if date_match else ""
    
    badge_match = re.search(r'<div class="styles-module-content-huG62".*?>(.*?)</div>', item)
    badge = badge_match.group(1).strip() if badge_match else ""
    
    year = 0
    mileage = 0
    # Title parse "..., 2025, 11 км"
    parts = title.split(',')
    if len(parts) >= 3:
        try:
            year = int(parts[-2].strip())
            mileage = int(parts[-1].replace('км', '').replace(' ', '').strip())
        except:
            pass

    cars_data.append({
        "title": title,
        "price": price,
        "image_url": img_url,
        "image_urls": [img_url] if img_url else [],
        "location": loc,
        "date_str": date_str,
        "badge_text": badge,
        "year": year,
        "mileage": mileage
    })

with open('cars_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(cars_data, f, ensure_ascii=False, indent=2)
print("Saved to cars_extracted.json")
