with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add the new tab button
old_tabs = """<div class="tabs">
        <div class="tab active" onclick="switchTab('cars', this)">🚘 Автомобили</div>
        <div class="tab" onclick="switchTab('reviews', this)">💬 Отзывы</div>
    </div>"""

new_tabs = """<div class="tabs">
        <div class="tab active" onclick="switchTab('cars', this)">🚘 Автомобили</div>
        <div class="tab" onclick="switchTab('reviews', this)">💬 Отзывы</div>
        <div class="tab" onclick="switchTab('company', this)">🏢 Настройки компании</div>
    </div>"""

if old_tabs in text:
    text = text.replace(old_tabs, new_tabs)
else:
    print("Could not find tabs HTML")

# 2. Add the company-tab content
# We need to insert it right before the scripts, or at the end of the body container.
# Let's find `<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>`

company_html = """
    <div id="company-tab" class="tab-content">
        <div class="container" style="max-width: 800px;">
            <h1>Настройки компании</h1>
            <form id="company-form">
                <div class="form-group">
                    <label class="form-label" for="company-name">Название компании</label>
                    <input type="text" id="company-name" class="form-input" required>
                </div>
                
                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label" for="company-rating">Рейтинг (например: 5,0)</label>
                        <input type="text" id="company-rating" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="company-reviews-count">Количество отзывов</label>
                        <input type="text" id="company-reviews-count" class="form-input" required>
                    </div>
                </div>

                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label" for="company-subscribers">Подписчиков</label>
                        <input type="text" id="company-subscribers" class="form-input" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="company-subscriptions">Подписок</label>
                        <input type="text" id="company-subscriptions" class="form-input" required>
                    </div>
                </div>

                <div class="form-group">
                    <label class="form-label" for="company-address">Адрес</label>
                    <input type="text" id="company-address" class="form-input" required>
                </div>

                <div class="form-group">
                    <label class="form-label">Аватар / Логотип</label>
                    <div class="file-upload-wrapper">
                        <div class="file-upload-text">+ Загрузить новый логотип</div>
                        <input type="file" id="company-logo" accept="image/*" class="file-upload-input">
                    </div>
                    <div id="logo-preview" class="image-list"></div>
                </div>

                <div class="form-group">
                    <label class="form-label">Фотографии "О компании"</label>
                    <div class="file-upload-wrapper">
                        <div class="file-upload-text">+ Выбрать фото</br>(до 10 шт)</div>
                        <input type="file" id="company-about-photos" accept="image/*" multiple class="file-upload-input">
                    </div>
                    <div id="about-photos-list" class="image-list"></div>
                </div>

                <button type="submit" class="submit-btn" id="company-submit-btn" style="width:100%; margin-top:20px;">Сохранить настройки</button>
            </form>
        </div>
    </div>
"""

idx = text.find('<!-- Supabase JS -->')
if idx != -1:
    text = text[:idx] + company_html + '\n    ' + text[idx:]
else:
    print("Could not find Supabase JS comment")

# Write changes back
with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated admin.html HTML structure")
