with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """            const priceEl = document.querySelector('[data-marker="item-view/item-price"]');
            if (priceEl) {
                priceEl.setAttribute('content', car.price);
                priceEl.innerHTML = formatPrice(car.price) + '&nbsp;₽';
            }"""

new_code = """            const priceEls = document.querySelectorAll('[data-marker="item-view/item-price"]');
            priceEls.forEach(priceEl => {
                priceEl.setAttribute('content', car.price);
                priceEl.innerHTML = formatPrice(car.price) + '&nbsp;₽';
            });"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated price update logic in update_car_page.py")
else:
    print("Could not find old price logic in update_car_page.py")
