with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

# We need to inject the fetch for company_profile inside the js_code of update_car_page.py
# The easiest way is to add it right after loadCarDetails() is called or inside it.
# Let's find loadCarDetails()

js_addition = """
    async function loadCompanyProfile() {
        const { data, error } = await supabaseClient.from('company_profile').select('*').eq('id', 1).single();
        if (error || !data) return;
        
        // Replace name
        const allElementsText = document.querySelectorAll('a, p, span, div, h1, h2, h3, h4, h5');
        allElementsText.forEach(el => {
            if (el.children.length === 0 && el.textContent) {
                if (el.textContent.includes('Автомиг')) el.textContent = el.textContent.replace(/Автомиг/g, data.name || 'Автомиг');
                if (el.textContent.includes('Автомиг')) el.textContent = el.textContent.replace(/Автомиг/g, data.name || 'Автомиг');
                if (el.textContent.includes('Газтормоз')) el.textContent = el.textContent.replace(/Газтормоз/g, data.name || 'Автомиг');
            }
        });

        // Replace logo
        if (data.logo_url) {
            const avatarLink = document.querySelector('[data-marker="seller-info/avatar-link"]');
            if (avatarLink) {
                avatarLink.innerHTML = `<img src="${data.logo_url}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">`;
            }
        }
        
        // About photos (if "О компании" exists on this page)
        const aboutSection = document.getElementById('about_v2');
        if (aboutSection && data.about_photos && data.about_photos.length > 0) {
            let galleryHtml = '<div style="display:flex; overflow-x:auto; gap:10px; margin-top:20px; padding-bottom:10px;">';
            data.about_photos.forEach(url => {
                galleryHtml += `<img src="${url}" style="height:200px; border-radius:8px; object-fit:cover;">`;
            });
            galleryHtml += '</div>';
            
            // Check if we already added it
            if (!document.getElementById('dynamic-about-gallery')) {
                const galleryWrapper = document.createElement('div');
                galleryWrapper.id = 'dynamic-about-gallery';
                galleryWrapper.innerHTML = galleryHtml;
                aboutSection.appendChild(galleryWrapper);
            }
        }
    }
"""

if 'loadCompanyProfile()' not in text:
    # Inject it before window.onload
    idx = text.find('window.onload = () => {')
    if idx != -1:
        text = text[:idx] + js_addition + '\n    ' + text[idx:]
        # Call it inside window.onload
        idx2 = text.find('loadCarDetails();', idx)
        if idx2 != -1:
            text = text[:idx2] + 'loadCompanyProfile();\n        ' + text[idx2:]
        with open('update_car_page.py', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Updated update_car_page.py with company profile logic")
    else:
        print("Could not find window.onload")
else:
    print("loadCompanyProfile already in update_car_page.py")
