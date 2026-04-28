with open('admin.html', 'r', encoding='utf-8') as f:
    text = f.read()

js_code = """
        // --- COMPANY PROFILE LOGIC ---
        let companyAboutPhotos = [];
        let companyLogoUrl = '';

        async function loadCompanyProfile() {
            const { data, error } = await supabaseClient.from('company_profile').select('*').eq('id', 1).single();
            if (error) {
                console.error("Error loading company profile:", error);
                return;
            }
            if (data) {
                document.getElementById('company-name').value = data.name || '';
                document.getElementById('company-rating').value = data.rating || '';
                document.getElementById('company-reviews-count').value = data.reviews_count || '';
                document.getElementById('company-subscribers').value = data.subscribers || '';
                document.getElementById('company-subscriptions').value = data.subscriptions || '';
                document.getElementById('company-address').value = data.address || '';
                
                companyLogoUrl = data.logo_url || '';
                if (companyLogoUrl) {
                    const preview = document.getElementById('logo-preview');
                    preview.innerHTML = `<div class="image-preview" style="background-image: url('${companyLogoUrl}')"></div>`;
                }

                companyAboutPhotos = data.about_photos || [];
                renderCompanyAboutPhotos();
            }
        }

        function renderCompanyAboutPhotos() {
            const list = document.getElementById('about-photos-list');
            list.innerHTML = '';
            companyAboutPhotos.forEach((url, index) => {
                const div = document.createElement('div');
                div.className = 'image-preview';
                div.style.backgroundImage = `url('${url}')`;
                
                const removeBtn = document.createElement('div');
                removeBtn.className = 'remove-image';
                removeBtn.innerHTML = '×';
                removeBtn.onclick = () => {
                    companyAboutPhotos.splice(index, 1);
                    renderCompanyAboutPhotos();
                };
                
                div.appendChild(removeBtn);
                list.appendChild(div);
            });
        }

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
            loadCompanyProfile();
        });
        // --- END COMPANY PROFILE LOGIC ---
"""

idx = text.find('function switchTab')
if idx != -1:
    text = text[:idx] + js_code + '\n        ' + text[idx:]
    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Injected company profile JS")
else:
    print("Could not find switchTab function")
