with open('admin.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix loadAdminCars
html = html.replace('''        async function loadAdminCars() {
            const { data, error } = await supabaseClient.from('cars').select('*').order('created_at', { ascending: false });
            if (error) {
                carsListEl.innerHTML = '<span style="color:red">Ошибка загрузки машин</span>';
                return;
            }
            allCars = data || [];
            renderCars();
        }''', '''        async function loadAdminCars() {
            try {
                const { data, error } = await supabaseClient.from('cars').select('*').order('created_at', { ascending: false });
                if (error) {
                    carsListEl.innerHTML = '<span style="color:red">Ошибка БД (машины): ' + error.message + '</span>';
                    return;
                }
                allCars = data || [];
                renderCars();
            } catch (err) {
                console.error(err);
                carsListEl.innerHTML = '<span style="color:red">Критическая ошибка (машины): ' + err.message + '</span>';
            }
        }''')

# Fix loadAdminReviews
html = html.replace('''        async function loadAdminReviews() {
            const { data, error } = await supabaseClient.from('reviews').select('*').order('created_at', { ascending: false });
            if (error) {
                reviewsListEl.innerHTML = '<span style="color:red">Ошибка загрузки отзывов</span>';
                return;
            }
            allReviews = data || [];
            renderReviews();
        }''', '''        async function loadAdminReviews() {
            try {
                const { data, error } = await supabaseClient.from('reviews').select('*').order('created_at', { ascending: false });
                if (error) {
                    reviewsListEl.innerHTML = '<span style="color:red">Ошибка БД (отзывы): ' + error.message + '</span>';
                    return;
                }
                allReviews = data || [];
                renderReviews();
            } catch (err) {
                console.error(err);
                reviewsListEl.innerHTML = '<span style="color:red">Критическая ошибка (отзывы): ' + err.message + '</span>';
            }
        }''')

with open('admin.html', 'w', encoding='utf-8') as f:
    f.write(html)
