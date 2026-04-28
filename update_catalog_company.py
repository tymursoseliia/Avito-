with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

js_code = """
        // --- DYNAMIC COMPANY PROFILE ---
        async function loadCompanyProfile() {
            const { data, error } = await supabaseClient.from('company_profile').select('*').eq('id', 1).single();
            if (error) {
                console.error("Error loading company profile:", error);
                return;
            }
            if (data) {
                // Name
                const nameElements = document.querySelectorAll('.styles-module-root-neN_7.styles-module-size_xl-s7Xn6');
                nameElements.forEach(el => {
                    if (el.textContent.includes('Автомиг') || el.textContent.trim().length > 0) {
                        el.textContent = data.name || 'Автомиг';
                    }
                });
                const breadcrumbNames = document.querySelectorAll('.breadcrumbs-link-Z5E11');
                breadcrumbNames.forEach(el => {
                    if (el.textContent.includes('Автомиг')) el.textContent = data.name || 'Автомиг';
                });

                // Rating
                const ratingEl = document.querySelector('.desktop-1m0o6d6');
                if (ratingEl) ratingEl.textContent = data.rating || '5,0';

                // Reviews
                const reviewsEl = document.querySelector('.desktop-l06xve');
                if (reviewsEl) reviewsEl.textContent = (data.reviews_count || '175') + ' отзывов';

                // Subscribers
                const subEl = document.querySelector('[data-marker="public-profile/followers-info"] .desktop-1kch6u5');
                if (subEl) subEl.textContent = data.subscribers || '420';

                // Subscriptions
                const subEl2 = document.querySelectorAll('.desktop-1kch6u5');
                if (subEl2.length > 1) {
                    subEl2[1].textContent = data.subscriptions || '12';
                }

                // Logo
                const logoEl = document.querySelector('.styles-module-image-vF1Z_');
                if (logoEl && data.logo_url) {
                    logoEl.src = data.logo_url;
                }

                // Update title
                document.title = (data.name || 'Автомиг') + ' - Авито';
            }
        }
"""

# Insert right after supabaseClient initialization
idx = text.find('const supabaseClient = supabase.createClient(supabaseUrl, supabaseKey);')
if idx != -1:
    end_idx = text.find('\n', idx)
    text = text[:end_idx] + '\n' + js_code + text[end_idx:]

# Call loadCompanyProfile at the bottom
idx_end = text.find('loadCars();')
if idx_end != -1:
    text = text[:idx_end] + 'loadCompanyProfile();\n            ' + text[idx_end:]

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Injected loadCompanyProfile to clean_avito (1).html")
