with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace "loadCarDetails();" with "loadCarDetails(); loadCompanyProfile();"
# And add the loadCompanyProfile function just before it.

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

        // Replace rating & reviews if they exist near seller block
        const ratingEls = document.querySelectorAll('.seller-info-rating-M0A3b, .seller-info-ratingScore-qWvGz');
        ratingEls.forEach(el => el.textContent = data.rating || '5,0');

        // Replace logo
        if (data.logo_url) {
            const avatarLink = document.querySelector('[data-marker="seller-info/avatar-link"]');
            if (avatarLink) {
                avatarLink.innerHTML = `<img src="${data.logo_url}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">`;
            }
            
            // Re-run the logo patch for <img> tags
            const allImages = document.querySelectorAll('img');
            allImages.forEach(img => {
                if (img.src && (img.src.includes('avatar') || img.src.includes('logo') || img.src.includes('Автомиг') || img.src === 'https://70.img.avito.st/image/1/1.ogFkvLa5GOhSG4zuLN6wOkoeDO7WOYzu0hUu6tIfGOo.DD1WHCne7V9xcT0-BplTPVR-nMNUotlxjG7IidMeKtQ')) {
                    if (img.parentElement && img.parentElement.tagName === 'DIV' && img.parentElement.classList.contains('_9275a4968c2dc72b')) {
                        img.src = data.logo_url;
                    }
                }
            });
        }
        
        // About photos
        const aboutSection = document.getElementById('about_v2');
        if (aboutSection && data.about_photos && data.about_photos.length > 0) {
            let galleryHtml = '<div style="display:flex; overflow-x:auto; gap:10px; margin-top:20px; padding-bottom:10px;">';
            data.about_photos.forEach(url => {
                galleryHtml += `<img src="${url}" style="height:200px; border-radius:8px; object-fit:cover; flex-shrink: 0;">`;
            });
            galleryHtml += '</div>';
            
            if (!document.getElementById('dynamic-about-gallery')) {
                const galleryWrapper = document.createElement('div');
                galleryWrapper.id = 'dynamic-about-gallery';
                galleryWrapper.innerHTML = galleryHtml;
                aboutSection.appendChild(galleryWrapper);
            }
        }
    }
"""

text = text.replace("    if (document.readyState === 'loading') {", js_addition + "\n    if (document.readyState === 'loading') {")

text = text.replace("document.addEventListener('DOMContentLoaded', loadCarDetails);", "document.addEventListener('DOMContentLoaded', () => { loadCarDetails(); loadCompanyProfile(); });")
text = text.replace("        loadCarDetails();\n    }", "        loadCarDetails();\n        loadCompanyProfile();\n    }")

with open('update_car_page.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated update_car_page.py with loadCompanyProfile")
