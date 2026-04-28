with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

# I need to find the description logic and move it.
desc_logic = """
            // Replace description
            if (car.description) {
                const descEl = document.querySelector('[data-marker="item-view/item-description"] p');
                if (descEl) {
                    descEl.innerHTML = car.description.replace(/\\\\n/g, '<br>');
                } else {
                    const descContainer = document.querySelector('[data-marker="item-view/item-description"]');
                    if (descContainer) {
                        descContainer.innerHTML = `<p>${car.description.replace(/\\\\n/g, '<br>')}</p>`;
                    }
                }
            }
"""

# Let's remove it from wherever it is now
if desc_logic in text:
    text = text.replace(desc_logic, "")
else:
    # Try a more fuzzy removal
    import re
    text = re.sub(r'\s*// Replace description\s*if \(car\.description\) \{[\s\S]*?\}\s*\}\s*\}', '', text)

# Now inject it BEFORE the catch block.
# The catch block looks like:
#        } catch (err) {
idx = text.find('} catch (err) {')
if idx != -1:
    text = text[:idx] + desc_logic + text[idx:]
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Moved description logic into try block")
else:
    print("Could not find catch block")

