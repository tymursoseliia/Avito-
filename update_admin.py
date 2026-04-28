import re

with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS for the complete button
css_to_add = """
        .action-btn.complete {
            background: #f6ffed;
            color: #52c41a;
        }

        .action-btn.complete:hover { background: #d9f7be; }
        
        .action-btn.activate {
            background: #fffbe6;
            color: #faad14;
        }

        .action-btn.activate:hover { background: #fff1b8; }
        
        .car-item-status {
            font-size: 12px;
            padding: 2px 8px;
            border-radius: 4px;
            display: inline-block;
            margin-top: 4px;
            font-weight: 600;
        }
        
        .status-active { background: #e6f7ff; color: #1890ff; }
        .status-completed { background: #f5f5f5; color: #8c8c8c; }
"""

html = html.replace('.action-btn.delete {', css_to_add + '\n        .action-btn.delete {')

# Replace renderCars()
old_render_cars = """        function renderCars() {
            if (allCars.length === 0) {
                carsListEl.innerHTML = '<p>Пока нет объявлений.</p>';
                return;
            }

            carsListEl.innerHTML = allCars.map(car => `
                <div class="car-item">
                    <img src="${car.image_url || 'https://via.placeholder.com/80'}" alt="${car.title}">
                    <div class="car-item-info">
                        <div class="car-item-title">${car.title}</div>
                        <div class="car-item-price">${formatPrice(car.price)} ₽</div>
                    </div>
                    <div class="car-item-actions">
                        <button class="action-btn edit" onclick="startEdit('${car.id}')">Редактировать</button>
                        <button class="action-btn delete" onclick="deleteCar('${car.id}')">Удалить</button>
                    </div>
                </div>
            `).join('');
        }"""

new_render_cars = """        function renderCars() {
            if (allCars.length === 0) {
                carsListEl.innerHTML = '<p>Пока нет объявлений.</p>';
                return;
            }

            carsListEl.innerHTML = allCars.map(car => {
                const status = car.status || 'active';
                const statusLabel = status === 'completed' ? 'Завершено' : 'Активно';
                const statusClass = status === 'completed' ? 'status-completed' : 'status-active';
                
                const toggleBtnClass = status === 'completed' ? 'activate' : 'complete';
                const toggleBtnText = status === 'completed' ? 'В активные' : 'В завершённые';
                const newStatus = status === 'completed' ? 'active' : 'completed';

                return `
                <div class="car-item" style="${status === 'completed' ? 'opacity: 0.7' : ''}">
                    <img src="${car.image_url || 'https://via.placeholder.com/80'}" alt="${car.title}">
                    <div class="car-item-info">
                        <div class="car-item-title">${car.title}</div>
                        <div class="car-item-price">${formatPrice(car.price)} ₽</div>
                        <div class="car-item-status ${statusClass}">${statusLabel}</div>
                    </div>
                    <div class="car-item-actions">
                        <button class="action-btn ${toggleBtnClass}" onclick="toggleStatus('${car.id}', '${newStatus}')">${toggleBtnText}</button>
                        <button class="action-btn edit" onclick="startEdit('${car.id}')">Редактировать</button>
                        <button class="action-btn delete" onclick="deleteCar('${car.id}')">Удалить</button>
                    </div>
                </div>
                `;
            }).join('');
        }

        async function toggleStatus(id, newStatus) {
            const { error } = await supabaseClient.from('cars').update({ status: newStatus }).eq('id', id);
            if (error) {
                showToast('Ошибка изменения статуса: ' + error.message, true);
            } else {
                showToast(newStatus === 'completed' ? 'Перенесено в завершенные' : 'Возвращено в активные');
                loadAdminCars();
            }
        }"""

html = html.replace(old_render_cars, new_render_cars)

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("admin.html updated")
