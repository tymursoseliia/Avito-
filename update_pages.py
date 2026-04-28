import re

# Update clean_avito (1).html to link to car_page.html
with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add onclick to the card container
if "onclick=\"window.open('car_page.html?id=${car.id}', '_blank')\"" not in content:
    content = content.replace('<div class="iva-item-root-Kcj9I', '<div onclick="window.open(\\\'car_page.html?id=${car.id}\\\', \\\'_blank\\\')" style="cursor:pointer" class="iva-item-root-Kcj9I')
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(content)

# Now inject JS into car_page.html
with open('car_page.html', 'r', encoding='utf-8') as f:
    car_page = f.read()

js_code = """
<!-- Supabase JS -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>
<script>
    const supabaseUrl = 'https://yjhjthhirxjxkbokycat.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqaGp0aGhpcnhqeGtib2t5Y2F0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NDQ4MjcsImV4cCI6MjA5MjUyMDgyN30.yXO_zbZgTT-oAJOkvnPsrF_YLnK49Cbpl7sn8ioFvOg';
    const supabaseClient = supabase.createClient(supabaseUrl, supabaseKey);

    function formatPrice(price) {
        return price ? price.toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g, " ") : "0";
    }

    async function loadCarDetails() {
        const urlParams = new URLSearchParams(window.location.search);
        const carId = urlParams.get('id');
        if (!carId) return;

        const { data: car, error } = await supabaseClient.from('cars').select('*').eq('id', carId).single();
        if (error || !car) {
            console.error('Car not found', error);
            return;
        }

        document.title = car.title + ' - Купить в ' + car.location;
        
        const titleEl = document.querySelector('[data-marker="item-view/title-info"]');
        if (titleEl) titleEl.innerHTML = car.title;

        const priceEl = document.querySelector('[data-marker="item-view/item-price"]');
        if (priceEl) {
            priceEl.setAttribute('content', car.price);
            priceEl.innerHTML = formatPrice(car.price) + '&nbsp;₽';
        }
        
        // Update images in gallery
        const galleryEl = document.querySelector('[data-marker="item-view/gallery"]');
        if (galleryEl && car.image_urls && car.image_urls.length > 0) {
            const firstImg = galleryEl.querySelector('img');
            if (firstImg) {
                // If there's an image, replace it. For a proper slider, it's more complex,
                // but at least setting the first image makes it show the right car.
                firstImg.src = car.image_urls[0];
            }
            
            // Try to replace all image srcs in the gallery block to the first image 
            // (or cycle through them if possible)
            const allImgs = galleryEl.querySelectorAll('img');
            allImgs.forEach((img, idx) => {
                img.src = car.image_urls[idx % car.image_urls.length];
                img.srcset = ""; // Remove srcset to force src usage
            });
            
            // Also update any other background images or source tags
            galleryEl.querySelectorAll('source').forEach(s => s.remove());
        } else if (galleryEl && car.image_url) {
             const allImgs = galleryEl.querySelectorAll('img');
             allImgs.forEach(img => { img.src = car.image_url; img.srcset = ""; });
             galleryEl.querySelectorAll('source').forEach(s => s.remove());
        }
        
        // Hide the loading or specific text elements if necessary
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadCarDetails);
    } else {
        loadCarDetails();
    }
</script>
</body>
"""

if '<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>' not in car_page:
    car_page = car_page.replace('</body>', js_code)
    with open('car_page.html', 'w', encoding='utf-8') as f:
        f.write(car_page)
    print("Injected script into car_page.html")
else:
    print("Already injected into car_page.html")
