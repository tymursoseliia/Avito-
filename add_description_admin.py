with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add description field to the form
old_price_html = """                <div class="form-group">
                    <label class="form-label" for="price">Цена (₽)</label>
                    <input type="number" id="price" class="form-input" placeholder="9185400" required>
                </div>"""

new_price_html = """                <div class="form-group">
                    <label class="form-label" for="price">Цена (₽)</label>
                    <input type="number" id="price" class="form-input" placeholder="9185400" required>
                </div>
                
                <div class="form-group">
                    <label class="form-label" for="description">Описание автомобиля</label>
                    <textarea id="description" class="form-input" style="height: 150px; resize: vertical;" placeholder="Пример: В наличии в Москве! Идеальное состояние, один владелец."></textarea>
                </div>"""

if old_price_html in text:
    text = text.replace(old_price_html, new_price_html)
else:
    print("Could not find price HTML")

# 2. Update submit logic to include description
old_submit = """                const carData = {
                    title: document.getElementById('title').value,
                    year: parseInt(document.getElementById('year').value),
                    mileage: parseInt(document.getElementById('mileage').value),
                    price: parseInt(document.getElementById('price').value),
                    location: 'Москва',
                    date_str: 'Сегодня',
                    badge_text: 'В наличии',
                    image_url: selectedFiles.length > 0 ? selectedFiles[0].publicUrl : '',
                    image_urls: selectedFiles.map(f => f.publicUrl)
                };"""

new_submit = """                const carData = {
                    title: document.getElementById('title').value,
                    year: parseInt(document.getElementById('year').value),
                    mileage: parseInt(document.getElementById('mileage').value),
                    price: parseInt(document.getElementById('price').value),
                    description: document.getElementById('description').value,
                    location: 'Москва',
                    date_str: 'Сегодня',
                    badge_text: 'В наличии',
                    image_url: selectedFiles.length > 0 ? selectedFiles[0].publicUrl : '',
                    image_urls: selectedFiles.map(f => f.publicUrl)
                };"""

if old_submit in text:
    text = text.replace(old_submit, new_submit)
else:
    print("Could not find submit logic")

# 3. Update edit logic to load description
old_edit = """            document.getElementById('title').value = car.title;
            document.getElementById('year').value = car.year;
            document.getElementById('mileage').value = car.mileage;
            document.getElementById('price').value = car.price;"""

new_edit = """            document.getElementById('title').value = car.title;
            document.getElementById('year').value = car.year;
            document.getElementById('mileage').value = car.mileage;
            document.getElementById('price').value = car.price;
            document.getElementById('description').value = car.description || '';"""

if old_edit in text:
    text = text.replace(old_edit, new_edit)
else:
    print("Could not find edit logic")

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated admin.html with description field")
