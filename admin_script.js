
        const supabaseUrl = 'https://yjhjthhirxjxkbokycat.supabase.co';
        const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqaGp0aGhpcnhqeGtib2t5Y2F0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NDQ4MjcsImV4cCI6MjA5MjUyMDgyN30.yXO_zbZgTT-oAJOkvnPsrF_YLnK49Cbpl7sn8ioFvOg';
        const supabaseClient = supabase.createClient(supabaseUrl, supabaseKey);

        const form = document.getElementById('add-car-form');
        const submitBtn = document.getElementById('submit-btn');
        const toast = document.getElementById('toast');
        const fileInput = document.getElementById('images');
        const fileList = document.getElementById('file-list');
        const carsListEl = document.getElementById('cars-list');
        
        
        let selectedFiles = [];
        let allCars = [];

        // Загрузка машин
        async function loadAdminCars() {
            const { data, error } = await supabaseClient.from('cars').select('*').order('created_at', { ascending: false });
            if (error) {
                carsListEl.innerHTML = '<span style="color:red">Ошибка загрузки объявлений</span>';
                return;
            }
            allCars = data || [];
            renderCars();
        }

        function formatPrice(price) {
            return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") : "0";
        }

        function renderCars() {
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
        }

        // Удаление
        async function deleteCar(id) {
            if(!confirm('Вы уверены, что хотите удалить это объявление?')) return;
            const { error } = await supabaseClient.from('cars').delete().eq('id', id);
            if (error) {
                showToast('Ошибка удаления', true);
            } else {
                showToast('Объявление удалено!');
                loadAdminCars();
                if(document.getElementById('edit_car_id').value === id) cancelEdit();
            }
        }

        // Редактирование
        function startEdit(id) {
            const car = allCars.find(c => c.id === id);
            if(!car) return;

            document.getElementById('edit_car_id').value = car.id;
            document.getElementById('title').value = car.title || '';
            document.getElementById('year').value = car.year || '';
            document.getElementById('mileage').value = car.mileage || '';
            document.getElementById('price').value = car.price || '';
            document.getElementById('location').value = car.location || '';
            document.getElementById('date_str').value = car.date_str || '';
            document.getElementById('badge_text').value = car.badge_text || '';
            
            // Настройка UI
            document.getElementById('form-title').childNodes[0].nodeValue = 'Редактирование ';
            document.getElementById('cancel-edit-btn').style.display = 'block';
            submitBtn.textContent = 'Сохранить изменения';
            
            // Сброс файлов (фото необязательны при редактировании)
            fileInput.required = false;
            document.getElementById('photo-label').textContent = 'Новые фотографии (оставьте пустым, чтобы сохранить старые)';
            document.getElementById('photo-subtext').textContent = 'При выборе новых фото старые будут удалены';
            selectedFiles = [];
            fileList.innerHTML = '';
            
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function cancelEdit() {
            form.reset();
            document.getElementById('edit_car_id').value = '';
            document.getElementById('form-title').childNodes[0].nodeValue = 'Новое объявление ';
            document.getElementById('cancel-edit-btn').style.display = 'none';
            submitBtn.textContent = 'Опубликовать';
            fileInput.required = true;
            document.getElementById('photo-label').textContent = 'Фотографии (до 10 шт)';
            document.getElementById('photo-subtext').textContent = 'Водяной знак добавится автоматически';
            selectedFiles = [];
            fileList.innerHTML = '';
        }

        fileInput.addEventListener('change', (e) => {
            selectedFiles = Array.from(e.target.files).slice(0, 10);
            fileList.innerHTML = '';
            selectedFiles.forEach((f, i) => {
                fileList.innerHTML += `<div>📷 ${f.name} (${(f.size / 1024 / 1024).toFixed(2)} MB)</div>`;
            });
        });

        function showToast(message, isError = false) {
            toast.textContent = message;
            if(isError) toast.classList.add('error');
            else toast.classList.remove('error');
            
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 5000);
        }

        // Функция наложения водяного знака
        function applyWatermark(file) {
            return new Promise((resolve, reject) => {
                const img = new Image();
                const url = URL.createObjectURL(file);
                
                img.onload = () => {
                    const MAX_WIDTH = 1200;
                    const MAX_HEIGHT = 900;
                    let width = img.width;
                    let height = img.height;
                    
                    if (width > height) {
                        if (width > MAX_WIDTH) { height *= MAX_WIDTH / width; width = MAX_WIDTH; }
                    } else {
                        if (height > MAX_HEIGHT) { width *= MAX_HEIGHT / height; height = MAX_HEIGHT; }
                    }
                    
                    const canvas = document.createElement('canvas');
                    canvas.width = width;
                    canvas.height = height;
                    const ctx = canvas.getContext('2d');
                    
                    // Рисуем основное фото
                    ctx.drawImage(img, 0, 0, width, height);
                    
                    // Обновляем img.width для расчетов водяного знака
                    Object.defineProperty(img, 'width', {value: width});
                    Object.defineProperty(img, 'height', {value: height});
                    
                    // Оригинальный водяной знак Авито (4 круга + текст)
                    const scale = Math.max(img.width / 1000, 0.3); // Масштаб относительно размера фото
                    const padding = img.width * 0.03;
                    
                    // Радиусы кругов
                    const rCenter = 12 * scale;
                    const rTop = 5 * scale;
                    const rBottomLeft = 6.5 * scale;
                    const rBottomRight = 8.5 * scale;
                    
                    const logoWidth = rCenter * 2.5;
                    
                    ctx.font = `bold ${50 * scale}px Manrope, Arial`;
                    const text = "Avito";
                    const textWidth = ctx.measureText(text).width;
                    
                    // Высчитываем правый нижний угол
                    const startX = img.width - logoWidth - textWidth - padding * 2;
                    const startY = img.height - rCenter * 3 - padding;
                    
                    const cx = startX + rCenter * 1.5;
                    const cy = startY + rCenter * 1.5;
                    
                    ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
                    
                    // Тень для читаемости на любых фото
                    ctx.shadowColor = 'rgba(0, 0, 0, 0.4)';
                    ctx.shadowBlur = 6 * scale;
                    ctx.shadowOffsetX = 1 * scale;
                    ctx.shadowOffsetY = 2 * scale;
                    
                    // Центральный круг
                    ctx.beginPath();
                    ctx.arc(cx - rCenter * 0.5, cy, rCenter, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Верхний круг
                    ctx.beginPath();
                    ctx.arc(cx - rCenter * 0.8, cy - rCenter * 1.1, rTop, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Нижний левый круг
                    ctx.beginPath();
                    ctx.arc(cx - rCenter * 1.6, cy + rCenter * 0.9, rBottomLeft, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Нижний правый круг
                    ctx.beginPath();
                    ctx.arc(cx + rCenter * 0.4, cy + rCenter * 1.1, rBottomRight, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Текст
                    ctx.textBaseline = 'middle';
                    ctx.fillText(text, startX + logoWidth + 8 * scale, cy + rCenter * 0.2);
                    
                    // Сбрасываем тень
                    ctx.shadowColor = 'transparent';
                    
                    canvas.toBlob((blob) => {
                        URL.revokeObjectURL(url);
                        resolve(blob);
                    }, 'image/jpeg', 0.9);
                };
                img.onerror = reject;
                img.src = url;
            });
        }

        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const editId = document.getElementById('edit_car_id').value;
            
            if (!editId && selectedFiles.length === 0) {
                showToast('Выберите хотя бы одно фото', true);
                return;
            }

            submitBtn.disabled = true;
            submitBtn.textContent = 'Обработка...';

            try {
                let uploadedUrls = [];

                // Загружаем фото только если выбраны новые
                if (selectedFiles.length > 0) {
                    for (let i = 0; i < selectedFiles.length; i++) {
                        submitBtn.textContent = `Загрузка фото ${i + 1} из ${selectedFiles.length}...`;
                        
                        const watermarkedBlob = await applyWatermark(selectedFiles[i]);
                        const fileName = `${Date.now()}_${Math.random().toString(36).substring(7)}.jpg`;
                        
                        const { data: uploadData, error: uploadError } = await supabaseClient.storage
                            .from('cars')
                            .upload(fileName, watermarkedBlob, {
                                contentType: 'image/jpeg',
                                cacheControl: '3600',
                                upsert: false
                            });

                        if (uploadError) throw new Error('Ошибка загрузки фото: ' + uploadError.message);

                        const { data: { publicUrl } } = supabaseClient.storage
                            .from('cars')
                            .getPublicUrl(fileName);
                            
                        uploadedUrls.push(publicUrl);
                    }
                }

                submitBtn.textContent = 'Сохранение объявления...';

                const carData = {
                    title: document.getElementById('title').value.trim(),
                    year: parseInt(document.getElementById('year').value),
                    mileage: parseInt(document.getElementById('mileage').value),
                    price: parseInt(document.getElementById('price').value),
                    description: document.getElementById('description').value,
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
                };

                // Обновляем URL только если загрузили новые фото
                if (uploadedUrls.length > 0) {
                    carData.image_url = uploadedUrls[0];
                    carData.image_urls = uploadedUrls;
                }

                let error = null;
                
                if (editId) {
                    const res = await supabaseClient.from('cars').update(carData).eq('id', editId);
                    error = res.error;
                } else {
                    const res = await supabaseClient.from('cars').insert([carData]);
                    error = res.error;
                }

                if (error) throw new Error('Ошибка БД: ' + error.message);

                showToast(editId ? 'Изменения сохранены!' : 'Объявление опубликовано!');
                cancelEdit();
                loadAdminCars();
            } catch (err) {
                console.error(err);
                showToast(err.message, true);
            } finally {
                submitBtn.disabled = false;
                submitBtn.textContent = editId ? 'Сохранить изменения' : 'Опубликовать';
            }
        });

        // Запуск
        loadAdminCars();
        loadAdminReviews();

        
        

        document.getElementById('company-logo').addEventListener('change', async (e) => {
            const file = e.target.files[0];
            if (!file) return;
            showToast("Загрузка логотипа...");
            try {
                const fileName = `logo_${Date.now()}_${Math.random().toString(36).substring(7)}.jpg`;
                const { data: uploadData, error: uploadError } = await supabaseClient.storage
                    .from('cars')
                    .upload(fileName, file, { contentType: file.type || 'image/jpeg', cacheControl: '3600' });

                if (uploadError) throw new Error(uploadError.message);

                const { data: { publicUrl } } = supabaseClient.storage.from('cars').getPublicUrl(fileName);
                companyLogoUrl = publicUrl;
                
                const preview = document.getElementById('logo-preview');
                preview.innerHTML = `<div class="image-preview" style="background-image: url('${companyLogoUrl}')"></div>`;
                showToast("Логотип загружен!");
            } catch(e) {
                console.error(e);
                showToast("Ошибка загрузки логотипа", true);
            }
        });

        document.getElementById('company-about-photos').addEventListener('change', async (e) => {
            const files = Array.from(e.target.files);
            if (!files.length) return;
            
            showToast("Загрузка фотографий...");
            try {
                for (let file of files) {
                    const fileName = `about_${Date.now()}_${Math.random().toString(36).substring(7)}.jpg`;
                    const { data: uploadData, error: uploadError } = await supabaseClient.storage
                        .from('cars')
                        .upload(fileName, file, { contentType: file.type || 'image/jpeg', cacheControl: '3600' });

                    if (uploadError) throw new Error(uploadError.message);

                    const { data: { publicUrl } } = supabaseClient.storage.from('cars').getPublicUrl(fileName);
                    companyAboutPhotos.push(publicUrl);
                }
                renderCompanyAboutPhotos();
                showToast("Фотографии загружены!");
            } catch(e) {
                console.error(e);
                showToast("Ошибка загрузки фотографий", true);
            }
        });

        document.getElementById('company-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('company-submit-btn');
            btn.innerText = 'Сохранение...';
            btn.disabled = true;

            const profileData = {
                name: document.getElementById('company-name').value,
                rating: document.getElementById('company-rating').value,
                reviews_count: document.getElementById('company-reviews-count').value,
                subscribers: document.getElementById('company-subscribers').value,
                subscriptions: document.getElementById('company-subscriptions').value,
                address: document.getElementById('company-address').value,
                logo_url: companyLogoUrl,
                about_photos: companyAboutPhotos
            };

            try {
                const { error } = await supabaseClient.from('company_profile').update(profileData).eq('id', 1);
                if (error) throw error;
                showToast('Настройки компании успешно сохранены!');
            } catch(err) {
                console.error(err);
                showToast('Ошибка при сохранении настроек', true);
            } finally {
                btn.innerText = 'Сохранить настройки';
                btn.disabled = false;
            }
        });

        // Load profile on start
        document.addEventListener('DOMContentLoaded', () => {
                    });
        // --- END COMPANY PROFILE LOGIC ---

        function switchTab(tabId, el) {
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.getElementById(tabId + '-tab').classList.add('active');
            el.classList.add('active');
            if (tabId === 'reviews') {
                loadAdminReviews();
            } else {
                loadAdminCars();
            }
        }

        const reviewForm = document.getElementById('add-review-form');
        const reviewSubmitBtn = document.getElementById('review-submit-btn');
        const reviewsListEl = document.getElementById('reviews-list');
        
        let selectedReviewFiles = [];
        let currentReviewPhotos = [];
        let currentReplyPhotos = [];

        let selectedReplyFiles = [];
        let allReviews = [];

        
        document.getElementById('author_avatar').addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                document.getElementById('author-avatar-name').textContent = '📷 ' + e.target.files[0].name;
            } else {
                document.getElementById('author-avatar-name').textContent = '';
            }
        });

        document.getElementById('review_images').addEventListener('change', (e) => {
            selectedReviewFiles = Array.from(e.target.files).slice(0, 5);
            const list = document.getElementById('review-file-list');
            renderExistingReviewPhotos();
        });

        document.getElementById('reply_images').addEventListener('change', (e) => {
            selectedReplyFiles = Array.from(e.target.files).slice(0, 5);
            const list = document.getElementById('reply-file-list');
            renderExistingReplyPhotos();
        });

        async function loadAdminReviews() {
            const { data, error } = await supabaseClient.from('reviews').select('*').order('created_at', { ascending: false });
            if (error) {
                reviewsListEl.innerHTML = '<span style="color:red">Ошибка загрузки отзывов</span>';
                return;
            }
            allReviews = data || [];
            renderReviews();
        }

        function renderReviews() {
            if (allReviews.length === 0) {
                reviewsListEl.innerHTML = '<p>Пока нет отзывов.</p>';
                return;
            }
            reviewsListEl.innerHTML = allReviews.map(r => `
                <div class="car-item">
                    <div class="car-item-info">
                        <div class="car-item-title">${r.author_name} - ${r.rating} ⭐</div>
                        <div style="font-size: 13px; color: #666;">${r.date_text} • ${r.car_title}</div>
                        <div style="margin-top: 8px; font-size: 14px;">${r.comment_text.substring(0, 100)}...</div>
                        ${r.reply_text ? `<div style="margin-top: 4px; font-size: 13px; color: #00AAFF;">Ответ: ${r.reply_text.substring(0, 50)}...</div>` : ''}
                    </div>
                    <div class="car-item-actions">
                        <button class="action-btn edit" onclick="startReviewEdit('${r.id}')">Редактировать</button>
                        <button class="action-btn delete" onclick="deleteReview('${r.id}')">Удалить</button>
                    </div>
                </div>
            `).join('');
        }

        async function deleteReview(id) {
            if(!confirm('Вы уверены, что хотите удалить этот отзыв?')) return;
            const { error } = await supabaseClient.from('reviews').delete().eq('id', id);
            if (error) {
                showToast('Ошибка удаления', true);
            } else {
                showToast('Отзыв удален!');
                loadAdminReviews();
                if(document.getElementById('edit_review_id').value === id) cancelReviewEdit();
            }
        }

        
        function renderExistingReviewPhotos() {
            const list = document.getElementById('review-file-list');
            let html = currentReviewPhotos.map((url, i) => `
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <img src="${url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px; margin-right: 12px;">
                    <span onclick="removeExistingReviewPhoto(${i})" style="color:red; cursor:pointer; font-size: 14px;">❌ Удалить</span>
                </div>
            `).join('');
            
            let newFilesHtml = selectedReviewFiles.map(f => `<div>📷 Новый файл: ${f.name}</div>`).join('');
            list.innerHTML = html + newFilesHtml;
        }

        function removeExistingReviewPhoto(index) {
            currentReviewPhotos.splice(index, 1);
            renderExistingReviewPhotos();
        }

        function renderExistingReplyPhotos() {
            const list = document.getElementById('reply-file-list');
            let html = currentReplyPhotos.map((url, i) => `
                <div style="display: flex; align-items: center; margin-bottom: 8px;">
                    <img src="${url}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px; margin-right: 12px;">
                    <span onclick="removeExistingReplyPhoto(${i})" style="color:red; cursor:pointer; font-size: 14px;">❌ Удалить</span>
                </div>
            `).join('');
            
            let newFilesHtml = selectedReplyFiles.map(f => `<div>📷 Новый файл: ${f.name}</div>`).join('');
            list.innerHTML = html + newFilesHtml;
        }

        function removeExistingReplyPhoto(index) {
            currentReplyPhotos.splice(index, 1);
            renderExistingReplyPhotos();
        }

        function startReviewEdit(id) {
            const r = allReviews.find(x => x.id === id);
            if(!r) return;

            document.getElementById('edit_review_id').value = r.id;
            document.getElementById('review_author').value = r.author_name || '';
            document.getElementById('author_avatar').value = '';
            document.getElementById('author-avatar-name').textContent = r.author_avatar ? '📷 Установлен текущий аватар' : '';
            document.getElementById('review_rating').value = r.rating || '5';
            document.getElementById('review_date').value = r.date_text || '';
            document.getElementById('review_car_title').value = r.car_title || '';
            document.getElementById('review_comment').value = r.comment_text || '';
            document.getElementById('review_reply').value = r.reply_text || '';
            
            document.getElementById('review-form-title').childNodes[0].nodeValue = 'Редактирование отзыва ';
            document.getElementById('review-cancel-edit-btn').style.display = 'block';
            reviewSubmitBtn.textContent = 'Сохранить изменения';
            
            selectedReviewFiles = [];
            selectedReplyFiles = [];
            
            let reviewFilesHtml = '';
            if (r.comment_photos && r.comment_photos.length > 0) {
                reviewFilesHtml = r.comment_photos.map(url => `<div>📷 <a href="${url}" target="_blank" style="color:#00AAFF;">Уже загружено фото</a></div>`).join('');
            }
            document.getElementById('review-file-list').innerHTML = reviewFilesHtml;
            
            let replyFilesHtml = '';
            if (r.reply_photos && r.reply_photos.length > 0) {
                replyFilesHtml = r.reply_photos.map(url => `<div>📷 <a href="${url}" target="_blank" style="color:#52c41a;">Уже загружено фото</a></div>`).join('');
            }
            document.getElementById('reply-file-list').innerHTML = replyFilesHtml;
            
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        function cancelReviewEdit() {
            reviewForm.reset();
            document.getElementById('edit_review_id').value = '';
            document.getElementById('review-form-title').childNodes[0].nodeValue = 'Новый отзыв ';
            document.getElementById('review-cancel-edit-btn').style.display = 'none';
            reviewSubmitBtn.textContent = 'Опубликовать отзыв';
            selectedReviewFiles = [];
            selectedReplyFiles = [];
            document.getElementById('review-file-list').innerHTML = '';
            document.getElementById('reply-file-list').innerHTML = '';
        }

        reviewForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const editId = document.getElementById('edit_review_id').value;
            
            reviewSubmitBtn.disabled = true;
            reviewSubmitBtn.textContent = 'Обработка...';

            try {
                let reviewPhotoUrls = [...currentReviewPhotos];
                let replyPhotoUrls = [...currentReplyPhotos];
                let author_avatar_url = null;
                
                // Upload author avatar if selected
                const avatarFile = document.getElementById('author_avatar').files[0];
                if (avatarFile) {
                    const ext = avatarFile.name.split('.').pop();
                    const path = `reviews/${Date.now()}_avatar.${ext}`;
                    const { data, error } = await supabaseClient.storage.from('cars').upload(path, avatarFile);
                    if (error) throw new Error('Ошибка загрузки аватара автора');
                    author_avatar_url = supabaseClient.storage.from('cars').getPublicUrl(path).data.publicUrl;
                } else if (editId) {
                    const existingReview = allReviews.find(r => r.id === editId);
                    if (existingReview) author_avatar_url = existingReview.author_avatar;
                }

                // Upload Review Photos
                if (selectedReviewFiles.length > 0) {
                    for (let i = 0; i < selectedReviewFiles.length; i++) {
                        reviewSubmitBtn.textContent = `Загрузка фото клиента ${i + 1}...`;
                        const fileName = `reviews/${Date.now()}_rev_${Math.random().toString(36).substring(7)}.jpg`;
                        const { error: uploadError } = await supabaseClient.storage.from('cars').upload(fileName, selectedReviewFiles[i]);
                        if (!uploadError) {
                            const { data: { publicUrl } } = supabaseClient.storage.from('cars').getPublicUrl(fileName);
                            reviewPhotoUrls.push(publicUrl);
                        }
                    }
                }

                // Upload Reply Photos
                if (selectedReplyFiles.length > 0) {
                    for (let i = 0; i < selectedReplyFiles.length; i++) {
                        reviewSubmitBtn.textContent = `Загрузка фото ответа ${i + 1}...`;
                        const fileName = `reviews/${Date.now()}_rep_${Math.random().toString(36).substring(7)}.jpg`;
                        const { error: uploadError } = await supabaseClient.storage.from('cars').upload(fileName, selectedReplyFiles[i]);
                        if (!uploadError) {
                            const { data: { publicUrl } } = supabaseClient.storage.from('cars').getPublicUrl(fileName);
                            replyPhotoUrls.push(publicUrl);
                        }
                    }
                }

                reviewSubmitBtn.textContent = 'Сохранение отзыва...';

                const revData = {
                    author_name: document.getElementById('review_author').value.trim(),
                    author_avatar: author_avatar_url,
                    rating: parseInt(document.getElementById('review_rating').value),
                    date_text: document.getElementById('review_date').value.trim(),
                    car_title: document.getElementById('review_car_title').value.trim(),
                    comment_text: document.getElementById('review_comment').value.trim(),
                    reply_text: document.getElementById('review_reply').value.trim()
                };

                revData.comment_photos = reviewPhotoUrls;
                revData.reply_photos = replyPhotoUrls;

                let error = null;
                
                if (editId) {
                    const res = await supabaseClient.from('reviews').update(revData).eq('id', editId);
                    error = res.error;
                } else {
                    const res = await supabaseClient.from('reviews').insert([revData]);
                    error = res.error;
                }

                if (error) throw new Error('Ошибка БД: ' + error.message);

                showToast(editId ? 'Отзыв изменен!' : 'Отзыв добавлен!');
                cancelReviewEdit();
                loadAdminReviews();
            } catch (err) {
                console.error(err);
                showToast(err.message, true);
            } finally {
                reviewSubmitBtn.disabled = false;
                reviewSubmitBtn.textContent = editId ? 'Сохранить изменения' : 'Опубликовать отзыв';
            }
        });
        
        loadAdminReviews();

    