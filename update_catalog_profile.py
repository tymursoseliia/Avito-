with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# I want to rewrite the loadCompanyProfile function completely
# First, extract everything from async function loadCompanyProfile() { to the end of that function.

import re

# Find start
match = re.search(r'async function loadCompanyProfile\(\)\s*\{', text)
if match:
    start_idx = match.start()
    
    # Simple brace counting to find end
    brace_count = 0
    end_idx = -1
    for i in range(start_idx, len(text)):
        if text[i] == '{':
            brace_count += 1
        elif text[i] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                break
                
    if end_idx != -1:
        old_func = text[start_idx:end_idx]
        
        new_func = """async function loadCompanyProfile() {
            try {
                const { data, error } = await supabaseClient.from('company_profile').select('*').eq('id', 1).single();
                if (error || !data) return;
                
                // Replace text dynamically
                const allElementsText = document.querySelectorAll('a, p, span, div, h1, h2, h3, h4, h5');
                allElementsText.forEach(el => {
                    if (el.children.length === 0 && el.textContent) {
                        if (el.textContent.includes('Автомиг')) el.textContent = el.textContent.replace(/Автомиг/g, data.name || 'Автомиг');
                        if (el.textContent.includes('GAZTORMOZ')) el.textContent = el.textContent.replace(/GAZTORMOZ/g, data.name || 'Автомиг');
                        if (el.textContent.includes('Газтормоз')) el.textContent = el.textContent.replace(/Газтормоз/g, data.name || 'Автомиг');
                    }
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
            } catch(e) { console.error('Error in loadCompanyProfile:', e); }
        }"""
        
        text = text[:start_idx] + new_func + text[end_idx:]
        
        with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Updated clean_avito (1).html loadCompanyProfile")
    else:
        print("Could not find end of function")
else:
    print("Could not find start of function")

