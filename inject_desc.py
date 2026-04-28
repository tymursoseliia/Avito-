with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace description
js_addition = """
            // Replace description
            if (car.description) {
                const descEl = document.querySelector('[data-marker="item-view/item-description"] p');
                if (descEl) {
                    descEl.innerHTML = car.description.replace(/\\n/g, '<br>');
                } else {
                    const descContainer = document.querySelector('[data-marker="item-view/item-description"]');
                    if (descContainer) {
                        descContainer.innerHTML = `<p>${car.description.replace(/\\n/g, '<br>')}</p>`;
                    }
                }
            }
"""

# Insert before "document.body.style.opacity = '1';"
text = text.replace("            // Unhide the body when everything is loaded", js_addition + "\n            // Unhide the body when everything is loaded")

with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected description replacement")
