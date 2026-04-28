with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

js_addition = """
            // Update Specifications
            const specHeaders = Array.from(document.querySelectorAll('h2')).filter(h2 => h2.textContent.includes('Характеристики'));
            if (specHeaders.length > 0) {
                const specUl = specHeaders[0].nextElementSibling;
                if (specUl && specUl.tagName === 'UL') {
                    // Start building HTML based on car properties
                    let html = '';
                    
                    const specMapping = [
                        { key: 'year', label: 'Год выпуска', val: car.year },
                        { key: 'mileage', label: 'Пробег', val: car.mileage ? car.mileage + ' км' : '' }
                    ];
                    
                    if (car.specs) {
                        const s = car.specs;
                        if (s.generation) specMapping.push({ label: 'Поколение', val: s.generation });
                        if (s.pts) specMapping.push({ label: 'ПТС', val: s.pts });
                        if (s.condition) specMapping.push({ label: 'Состояние', val: s.condition });
                        if (s.modification) specMapping.push({ label: 'Модификация', val: s.modification });
                        if (s.engine_volume) specMapping.push({ label: 'Объём двигателя', val: s.engine_volume });
                        if (s.engine_type) specMapping.push({ label: 'Тип двигателя', val: s.engine_type });
                        if (s.transmission) specMapping.push({ label: 'Коробка передач', val: s.transmission });
                        if (s.drive) specMapping.push({ label: 'Привод', val: s.drive });
                        if (s.equipment) specMapping.push({ label: 'Комплектация', val: s.equipment });
                        if (s.body_type) specMapping.push({ label: 'Тип кузова', val: s.body_type });
                        if (s.color) specMapping.push({ label: 'Цвет', val: s.color });
                        if (s.wheel) specMapping.push({ label: 'Руль', val: s.wheel });
                        if (s.vin) specMapping.push({ label: 'VIN или номер кузова', val: s.vin });
                    }
                    
                    specMapping.forEach(item => {
                        if (item.val) {
                            html += `<li class="d2936d013c910379"><span class="d6e8fd2e3d52b32a">${item.label}<span>: </span></span>${item.val}</li>`;
                        }
                    });
                    
                    specUl.innerHTML = html;
                }
            }
"""

if '// Update Specifications' not in text:
    text = text.replace("// 5. Update Header Links", js_addition + "\n            // 5. Update Header Links")
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added specs rendering to update_car_page.py")
else:
    print("Specs rendering already in update_car_page.py")
