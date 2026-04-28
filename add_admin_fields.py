with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

fields_html = """
                <!-- Specifications Section -->
                <div style="margin-top: 30px; border-top: 1px solid #e0e0e0; padding-top: 20px; margin-bottom: 20px;">
                    <h3 style="margin-bottom: 15px; font-family: 'Manrope', sans-serif;">Характеристики</h3>
                    
                    <div class="form-group">
                        <label class="form-label" for="spec_generation">Поколение</label>
                        <input type="text" id="spec_generation" class="form-input" placeholder="Например: I (2025-2026)">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_pts">ПТС</label>
                        <input type="text" id="spec_pts" class="form-input" placeholder="Например: Не оформлен">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_condition">Состояние</label>
                        <input type="text" id="spec_condition" class="form-input" placeholder="Например: Не битый">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_modification">Модификация</label>
                        <input type="text" id="spec_modification" class="form-input" placeholder="Например: 2.0hyb 4WD DHT (1176 л.с.)">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_engine_volume">Объём двигателя</label>
                        <input type="text" id="spec_engine_volume" class="form-input" placeholder="Например: 2 л">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_engine_type">Тип двигателя</label>
                        <input type="text" id="spec_engine_type" class="form-input" placeholder="Например: Гибрид">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_transmission">Коробка передач</label>
                        <input type="text" id="spec_transmission" class="form-input" placeholder="Например: Робот">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_drive">Привод</label>
                        <input type="text" id="spec_drive" class="form-input" placeholder="Например: Полный">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_equipment">Комплектация</label>
                        <input type="text" id="spec_equipment" class="form-input" placeholder="Например: 70 kWh Yaoying">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_body_type">Тип кузова</label>
                        <input type="text" id="spec_body_type" class="form-input" placeholder="Например: Внедорожник 5-дверный">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_color">Цвет</label>
                        <input type="text" id="spec_color" class="form-input" placeholder="Например: Серый">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_wheel">Руль</label>
                        <input type="text" id="spec_wheel" class="form-input" placeholder="Например: Левый">
                    </div>
                    <div class="form-group">
                        <label class="form-label" for="spec_vin">VIN или номер кузова</label>
                        <input type="text" id="spec_vin" class="form-input" placeholder="Например: LSV2*************">
                    </div>
                </div>

                <button type="submit"
"""

if 'id="spec_generation"' not in text:
    text = text.replace('<button type="submit"', fields_html.strip())
    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added specification fields to admin.html")
else:
    print("Fields already exist in admin.html")
