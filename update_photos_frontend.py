import re

html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to extract the existing static part from js_template.js or just write the script clean
with open('js_template.js', 'r', encoding='utf-8') as f:
    template_str = f.read()

new_script = '''<script>
// --- DYNAMIC REVIEWS SCRIPT ---
document.addEventListener('DOMContentLoaded', async () => {
    // Hide static reviews
    const staticReviews = document.querySelectorAll('[data-marker^="review("]');
    let lastSnippet = null;
    if (staticReviews.length > 0) {
        staticReviews.forEach(el => {
            const snippet = el.closest('.styles-module-snippet-JUn6v') || el;
            snippet.style.display = 'none'; // hide it
            lastSnippet = snippet;
        });
        
        let dynList = document.createElement('div');
        dynList.id = 'dynamic-reviews-list';
        if (lastSnippet && lastSnippet.parentElement) {
            lastSnippet.parentElement.appendChild(dynList);
        } else {
            const ratingSummary = document.querySelector('[data-marker="ratingSummary"]');
            if (ratingSummary) ratingSummary.parentElement.parentElement.appendChild(dynList);
        }
        
        fetchAndRenderReviews();
    }
});

function buildPhotosHtml(photos, markerPrefix) {
    if (!photos || photos.length === 0) return '';
    let imgs = photos.map((url, i) => `
        <div data-marker="${markerPrefix}/image(${i})" class="styles-module-image-IJiTw" tabindex="0" role="button" aria-label="Нажмите, чтобы увеличить">
            <img src="${url}" alt="Фото из отзыва" style="width:100%; height:100%; object-fit: cover; border-radius: inherit;" draggable="false" data-marker="${markerPrefix}/image(${i})/image">
        </div>
    `).join('');
    
    return `
    <div class="" style="margin-top:12px; margin-bottom:12px;"><div class="styles-module-images-ycitL"><div class="styles-module-root-aix8z" data-marker="${markerPrefix}"><div data-marker="${markerPrefix}" class="styles-module-root-Ie3Kv" style="--thumbnail-size:60px;--thumbnail-gap:2px;--thumbnail-border-radius:2px;--thumbnail-edge-border-radius:12px">
        ${imgs}
    </div></div></div></div>
    `;
}

async function fetchAndRenderReviews() {
    try {
        const { data, error } = await supabaseClient.from('reviews').select('*').order('created_at', { ascending: false });
        if (error) throw error;
        
        const container = document.getElementById('dynamic-reviews-list');
        if (!container) return;
        
        if (!data || data.length === 0) {
            container.innerHTML = '<p class="stylesMarningNormal-module-paragraph-m-ZXEoT">Нет отзывов.</p>';
            return;
        }

        let allReviewsData = data;
        let currentReviewsPage = 1;
        const REVIEWS_PER_PAGE = 10;
        const colors = ['#00AAFF', '#FF5500', '#00CC66', '#9900FF', '#FF0055'];

        function renderReviews(startIndex, count) {
            const dataToShow = allReviewsData.slice(startIndex, startIndex + count);
            let html = '';
            
            dataToShow.forEach((r, idxOffset) => {
                const index = startIndex + idxOffset;
                let starsHtml = '';
                for (let i = 1; i <= 5; i++) {
                    if (i <= r.rating) {
                        starsHtml += `<div data-marker="review(${index+1})/score/star-${i}" tabindex="-1" role="button" aria-label="★ ${i}" class="styles-module-star-euNED"><svg class="styles-module-root-qQ0wp styles-module-filled-YWV4W" style="height:16px;width:16px" width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="m10 14.99-4.92 3.26a.55.55 0 0 1-.83-.6l1.58-5.7L1.2 8.29a.55.55 0 0 1 .31-.98l5.9-.25 2.07-5.53a.55.55 0 0 1 1.02 0l2.07 5.53 5.9.25a.55.55 0 0 1 .31.98l-4.62 3.68 1.58 5.69a.55.55 0 0 1-.83.6z"></path></svg></div>`;
                    } else {
                        starsHtml += `<div data-marker="review(${index+1})/score/star-${i}" tabindex="-1" role="button" aria-label="★ ${i}" class="styles-module-star-euNED"><svg class="styles-module-root-qQ0wp styles-module-empty-B0hps" style="height:16px;width:16px" width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="m10 14.99-4.92 3.26a.55.55 0 0 1-.83-.6l1.58-5.7L1.2 8.29a.55.55 0 0 1 .31-.98l5.9-.25 2.07-5.53a.55.55 0 0 1 1.02 0l2.07 5.53 5.9.25a.55.55 0 0 1 .31.98l-4.62 3.68 1.58 5.69a.55.55 0 0 1-.83.6z"></path></svg></div>`;
                    }
                }
                
                let authorAvatarHtml = '';
                if (r.author_avatar) {
                    authorAvatarHtml = `<img src="${r.author_avatar}" class="styles-module-image-gA0c_" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;">`;
                } else {
                    const color = colors[index % colors.length];
                    const initial = r.author_name ? r.author_name.charAt(0).toUpperCase() : '?';
                    authorAvatarHtml = `<div class="styles-module-letter-qgO4h styles-module-letter_size_m-m97vE" style="background-color: ${color}; color: white; border-radius: 50%; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-weight: bold;">${initial}</div>`;
                }
                
                let commentPhotosHtml = buildPhotosHtml(r.comment_photos, `review(${index+1})`);
                let replyPhotosHtml = buildPhotosHtml(r.reply_photos, `review(${index+1})`);
                
                let itemHtml = `''' + template_str + '''`;
                
                itemHtml = itemHtml.replace('<img src="./logo.jpg" class="styles-module-image-gA0c_" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;">', authorAvatarHtml);
                
                html += itemHtml;
            });
            
            if (startIndex === 0) {
                container.innerHTML = html;
            } else {
                container.insertAdjacentHTML('beforeend', html);
            }
        }
        
        renderReviews(0, REVIEWS_PER_PAGE);
        
        const moreBtn = document.querySelector('[data-marker="rating-list/moreReviewsButton"]');
        if (moreBtn) {
            const newBtn = moreBtn.cloneNode(true);
            moreBtn.parentNode.replaceChild(newBtn, moreBtn);
            
            newBtn.addEventListener('click', () => {
                const startIndex = currentReviewsPage * REVIEWS_PER_PAGE;
                renderReviews(startIndex, REVIEWS_PER_PAGE);
                currentReviewsPage++;
                
                if (currentReviewsPage * REVIEWS_PER_PAGE >= allReviewsData.length) {
                    newBtn.style.display = 'none';
                }
            });
            
            if (REVIEWS_PER_PAGE >= allReviewsData.length) {
                newBtn.style.display = 'none';
            } else {
                newBtn.style.display = '';
            }
        }
        
    } catch(err) {
        console.error('Failed to load reviews', err);
    }
}
</script>
'''

js_start = html.find('// --- DYNAMIC REVIEWS SCRIPT ---')
if js_start != -1:
    script_start = html.rfind('<script>', 0, js_start)
    script_end = html.find('</script>', js_start) + 9
    final_html = html[:script_start] + new_script + html[script_end:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Injected updated script for photos support.")
else:
    body_end = html.rfind('</body>')
    if body_end != -1:
        final_html = html[:body_end] + new_script + html[body_end:]
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print("Injected new script at the end of the body.")
    else:
        print("Could not find body block either.")
