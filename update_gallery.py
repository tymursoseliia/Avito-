import re

with open('car_page.html', 'r', encoding='utf-8') as f:
    content = f.read()

# First remove the previously injected script entirely
content = re.sub(r'<!-- Supabase JS -->.*?</script>', '', content, flags=re.DOTALL)

js_code = """
<!-- Supabase JS -->
<style>
.avito-gallery { width: 100%; display: flex; flex-direction: column; gap: 8px; margin-bottom: 24px; }
.avito-main-img-wrap { position: relative; width: 100%; aspect-ratio: 4/3; background: #000; border-radius: 8px; overflow: hidden; cursor: zoom-in; }
.avito-main-img-wrap img { width: 100%; height: 100%; object-fit: cover; }
.ag-nav { position: absolute; top: 50%; transform: translateY(-50%); background: rgba(0,0,0,0.3); color: white; padding: 16px 12px; cursor: pointer; user-select: none; font-size: 24px; transition: 0.2s; z-index: 5; }
.ag-nav:hover { background: rgba(0,0,0,0.7); }
.ag-prev { left: 0; border-radius: 0 4px 4px 0; }
.ag-next { right: 0; border-radius: 4px 0 0 4px; }
.avito-thumbs-wrap { display: flex; gap: 8px; overflow-x: auto; padding-bottom: 4px; scrollbar-width: none; }
.avito-thumbs-wrap::-webkit-scrollbar { display: none; }
.ag-thumb { width: 80px; height: 60px; flex-shrink: 0; object-fit: cover; border-radius: 4px; cursor: pointer; opacity: 0.5; transition: 0.2s; box-sizing: border-box; }
.ag-thumb:hover { opacity: 0.8; }
.ag-thumb.active { opacity: 1; border: 2px solid #00AAFF; }

/* Modal */
.avito-modal { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; background: rgba(0,0,0,0.9); z-index: 999999; display: none; flex-direction: column; font-family: Manrope, sans-serif; }
.avito-modal.active { display: flex; }
.ag-modal-close { position: absolute; top: 20px; right: 30px; color: white; font-size: 40px; cursor: pointer; z-index: 10; opacity: 0.7; transition: 0.2s; }
.ag-modal-close:hover { opacity: 1; }
.ag-modal-content { flex: 1; display: flex; justify-content: center; align-items: center; position: relative; padding: 0 60px; }
.ag-modal-content img { max-width: 100%; max-height: 100%; object-fit: contain; }
.ag-modal-content .ag-nav { padding: 30px 20px; font-size: 40px; background: transparent; opacity: 0.5; }
.ag-modal-content .ag-nav:hover { opacity: 1; background: rgba(255,255,255,0.1); }
.ag-modal-footer { background: #fff; display: flex; justify-content: center; align-items: center; gap: 16px; padding: 24px; }
.ag-modal-btn { padding: 14px 40px; border-radius: 8px; font-weight: 600; font-size: 16px; color: white; cursor: pointer; text-align: center; line-height: 1.2; }
.ag-modal-btn small { font-weight: 400; font-size: 13px; display: block; opacity: 0.9; margin-top: 4px; }
.ag-btn-green { background: #16c644; transition: 0.2s; }
.ag-btn-green:hover { background: #13ad3c; }
.ag-btn-blue { background: #00AAFF; transition: 0.2s; }
.ag-btn-blue:hover { background: #0099e5; }
</style>
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js"></script>
<script>
    const supabaseUrl = 'https://yjhjthhirxjxkbokycat.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqaGp0aGhpcnhqeGtib2t5Y2F0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NDQ4MjcsImV4cCI6MjA5MjUyMDgyN30.yXO_zbZgTT-oAJOkvnPsrF_YLnK49Cbpl7sn8ioFvOg';
    const supabaseClient = supabase.createClient(supabaseUrl, supabaseKey);

    let galleryImages = [];
    let currentImgIndex = 0;

    function formatPrice(price) {
        return price ? price.toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g, " ") : "0";
    }
    
    function agSetImage(index) {
        if (galleryImages.length === 0) return;
        if (index < 0) index = galleryImages.length - 1;
        if (index >= galleryImages.length) index = 0;
        currentImgIndex = index;
        
        // Update main photo
        const mainImg = document.getElementById('ag-main-img');
        if(mainImg) mainImg.src = galleryImages[currentImgIndex];
        
        // Update modal photo
        const modalImg = document.getElementById('ag-modal-img');
        if(modalImg) modalImg.src = galleryImages[currentImgIndex];
        
        // Update thumbs active state
        document.querySelectorAll('.ag-thumb').forEach((th, i) => {
            if (i === currentImgIndex) th.classList.add('active');
            else th.classList.remove('active');
        });
    }

    window.agPrev = function(e) {
        e.stopPropagation();
        agSetImage(currentImgIndex - 1);
    };

    window.agNext = function(e) {
        e.stopPropagation();
        agSetImage(currentImgIndex + 1);
    };

    window.agOpenModal = function() {
        document.getElementById('ag-modal').classList.add('active');
    };

    window.agCloseModal = function() {
        document.getElementById('ag-modal').classList.remove('active');
    };

    async function loadCarDetails() {
        const urlParams = new URLSearchParams(window.location.search);
        const carId = urlParams.get('id');
        if (!carId) return;

        const { data: car, error } = await supabaseClient.from('cars').select('*').eq('id', carId).single();
        if (error || !car) return;

        document.title = car.title + ' - Купить в ' + car.location;
        
        const titleEl = document.querySelector('[data-marker="item-view/title-info"]');
        if (titleEl) titleEl.innerHTML = car.title;

        const priceEl = document.querySelector('[data-marker="item-view/item-price"]');
        if (priceEl) {
            priceEl.setAttribute('content', car.price);
            priceEl.innerHTML = formatPrice(car.price) + '&nbsp;₽';
        }
        
        // Setup Gallery
        galleryImages = car.image_urls && car.image_urls.length > 0 ? car.image_urls : [car.image_url];
        
        const galleryEl = document.querySelector('[data-marker="item-view/gallery"]');
        if (galleryEl && galleryImages.length > 0) {
            
            // Build custom gallery HTML
            let thumbsHtml = '';
            galleryImages.forEach((url, i) => {
                thumbsHtml += `<img src="${url}" class="ag-thumb ${i===0?'active':''}" onclick="agSetImage(${i})">`;
            });
            
            galleryEl.innerHTML = `
                <div class="avito-gallery">
                    <div class="avito-main-img-wrap" onclick="agOpenModal()">
                        <img id="ag-main-img" src="${galleryImages[0]}" alt="Photo">
                        ${galleryImages.length > 1 ? `
                            <div class="ag-nav ag-prev" onclick="agPrev(event)">&#10094;</div>
                            <div class="ag-nav ag-next" onclick="agNext(event)">&#10095;</div>
                        ` : ''}
                    </div>
                    ${galleryImages.length > 1 ? `
                        <div class="avito-thumbs-wrap" id="ag-thumbs">
                            ${thumbsHtml}
                        </div>
                    ` : ''}
                </div>
            `;
            
            // Inject modal into body
            if(!document.getElementById('ag-modal')) {
                const modalHtml = `
                <div class="avito-modal" id="ag-modal">
                    <div class="ag-modal-close" onclick="agCloseModal()">&#10005;</div>
                    <div class="ag-modal-content">
                        <img id="ag-modal-img" src="${galleryImages[0]}" alt="Fullscreen photo">
                        ${galleryImages.length > 1 ? `
                            <div class="ag-nav ag-prev" onclick="agPrev(event)">&#10094;</div>
                            <div class="ag-nav ag-next" onclick="agNext(event)">&#10095;</div>
                        ` : ''}
                    </div>
                    <div class="ag-modal-footer">
                        <div class="ag-modal-btn ag-btn-green">Показать телефон<br><small>8 XXX XXX-XX-XX</small></div>
                        <div class="ag-modal-btn ag-btn-blue">Написать сообщение<br><small>Отвечает около часа</small></div>
                    </div>
                </div>
                `;
                document.body.insertAdjacentHTML('beforeend', modalHtml);
            }
        }
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', loadCarDetails);
    } else {
        loadCarDetails();
    }
</script>
</body>
"""

content = content.replace('</body>', js_code)
with open('car_page.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated gallery in car_page.html")
