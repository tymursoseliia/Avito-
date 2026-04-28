with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacement = """                const carData = {
                    title: document.getElementById('title').value.trim(),
                    year: parseInt(document.getElementById('year').value),
                    mileage: parseInt(document.getElementById('mileage').value),
                    price: parseInt(document.getElementById('price').value),
                    location: document.getElementById('location').value.trim(),
                    date_str: document.getElementById('date_str').value.trim(),
                    badge_text: document.getElementById('badge_text').value.trim(),
                    specs: {
                        generation: document.getElementById('spec_generation').value.trim(),
                        pts: document.getElementById('spec_pts').value.trim(),
                        condition: document.getElementById('spec_condition').value.trim(),
                        modification: document.getElementById('spec_modification').value.trim(),
                        engine_volume: document.getElementById('spec_engine_volume').value.trim(),
                        engine_type: document.getElementById('spec_engine_type').value.trim(),
                        transmission: document.getElementById('spec_transmission').value.trim(),
                        drive: document.getElementById('spec_drive').value.trim(),
                        equipment: document.getElementById('spec_equipment').value.trim(),
                        body_type: document.getElementById('spec_body_type').value.trim(),
                        color: document.getElementById('spec_color').value.trim(),
                        wheel: document.getElementById('spec_wheel').value.trim(),
                        vin: document.getElementById('spec_vin').value.trim()
                    }
                };"""

text = text.replace("""                const carData = {
                    title: document.getElementById('title').value.trim(),
                    year: parseInt(document.getElementById('year').value),
                    mileage: parseInt(document.getElementById('mileage').value),
                    price: parseInt(document.getElementById('price').value),
                    location: document.getElementById('location').value.trim(),
                    date_str: document.getElementById('date_str').value.trim(),
                    badge_text: document.getElementById('badge_text').value.trim()
                };""", replacement)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated admin.html to include specs in carData")
