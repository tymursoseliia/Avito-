with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix the counter
old_counter = """            const completedTabCounter = document.querySelector('[data-marker="extended_profile_tabs/tab(closed)"] .styles-module-counter-uAip7');
            if (completedTabCounter) completedTabCounter.innerText = "0";"""

new_counter = """            const completedTabCounter = document.querySelector('[data-marker="extended_profile_tabs/tab(closed)"] .styles-module-counter-uAip7');
            if (completedTabCounter) completedTabCounter.innerText = dbCompletedCount;"""

# 2. Add opacity if completed.
# In loadCars(), the cardHtml is generated inside a loop.
# We need to change the generation logic to apply styles if status is completed.
# Actually, it's easier to just do a string replace in the loadCars function where it checks status.

old_loop = """                    if (car.status === 'completed') {
                        dbCompletedCarsHtml += cardHtml;
                        dbCompletedCount++;
                    } else {
                        activeCarsHtml += cardHtml;
                        activeCount++;
                    }"""

new_loop = """                    if (car.status === 'completed') {
                        // Make completed cars look gray and semi-transparent
                        let completedCardHtml = cardHtml.replace('class="iva-item-root-Kcj9I', 'style="opacity: 0.5; filter: grayscale(100%);" class="iva-item-root-Kcj9I');
                        dbCompletedCarsHtml += completedCardHtml;
                        dbCompletedCount++;
                    } else {
                        activeCarsHtml += cardHtml;
                        activeCount++;
                    }"""

if old_counter in text and old_loop in text:
    text = text.replace(old_counter, new_counter)
    text = text.replace(old_loop, new_loop)
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed counters and grayed out completed cars")
else:
    print("Logic not found in HTML")
