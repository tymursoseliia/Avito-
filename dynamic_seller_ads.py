with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """            // 7. Redirect Seller Ads Button
            const allLinks = document.querySelectorAll('a');
            allLinks.forEach(link => {
                if (link.textContent && link.textContent.includes('объявлений пользователя')) {
                    link.href = 'clean_avito (1).html';
                }
            });"""

new_code = """            // 7. Redirect Seller Ads Button
            function getPlural(number, one, two, five) {
                let n = Math.abs(number);
                n %= 100;
                if (n >= 5 && n <= 20) return five;
                n %= 10;
                if (n === 1) return one;
                if (n >= 2 && n <= 4) return two;
                return five;
            }

            const { count, error: countError } = await supabaseClient
                .from('cars')
                .select('*', { count: 'exact', head: true });
            
            let totalAds = count || 0;
            let adsText = `${totalAds} ${getPlural(totalAds, 'объявление', 'объявления', 'объявлений')} пользователя`;

            const allLinks = document.querySelectorAll('a');
            allLinks.forEach(link => {
                if (link.textContent && (link.textContent.includes('объявлени') || link.textContent.includes('пользователя'))) {
                    // Check if it's the specific seller ads button
                    if (link.classList.contains('css-1cm6pik') || link.textContent.includes('65')) {
                        link.href = 'clean_avito (1).html';
                        const span = link.querySelector('span');
                        if (span) {
                            span.textContent = adsText;
                        } else {
                            link.textContent = adsText;
                        }
                    }
                }
            });"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated Seller Ads dynamic count")
else:
    print("Could not find old Seller Ads logic")
