import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to find where the reviews start and end.
# They are typically marked with data-marker="review(1)", "review(2)", etc.
# We will find the parent container.
# The user's HTML might have them directly inside some div.
# Let's search for data-marker="review(2)" to see its parent.

# Let's just find the first data-marker="review(1)" and the last review's end.
# Actually, it's easier to just hide them using CSS and append our dynamic container,
# or dynamically remove all elements with data-marker starting with "review(" from JS!
# That way we don't risk breaking the HTML structure with regex!

js_code = '''
<script>
// --- DYNAMIC REVIEWS SCRIPT ---
document.addEventListener('DOMContentLoaded', async () => {
    // 1. Remove all static reviews
    const staticReviews = document.querySelectorAll('[data-marker^="review("]');
    if (staticReviews.length > 0) {
        // Find the parent container of the first review
        let container = staticReviews[0].parentElement;
        // Keep moving up if the container only has 1 review but there are multiple containers
        // Actually, in Avito, they are usually in a list.
        staticReviews.forEach(el => {
            // Find the closest snippet container and remove it
            const snippet = el.closest('.styles-module-snippet-JUn6v') || el;
            snippet.remove();
        });
        
        // Add our dynamic container after the rating summary
        const ratingSummary = document.querySelector('[data-marker="ratingSummary"]');
        if (ratingSummary) {
            let dynList = document.createElement('div');
            dynList.id = 'dynamic-reviews-list';
            dynList.style.marginTop = '24px';
            ratingSummary.parentElement.parentElement.appendChild(dynList);
            
            // 2. Fetch and render reviews from Supabase
            fetchAndRenderReviews();
        }
    } else {
        // If no static reviews found, just try to find where to put the dynamic ones
        const ratingSummary = document.querySelector('[data-marker="ratingSummary"]');
        if (ratingSummary && !document.getElementById('dynamic-reviews-list')) {
            let dynList = document.createElement('div');
            dynList.id = 'dynamic-reviews-list';
            dynList.style.marginTop = '24px';
            ratingSummary.parentElement.parentElement.appendChild(dynList);
            fetchAndRenderReviews();
        }
    }
});

async function fetchAndRenderReviews() {
    try {
        const { data, error } = await supabaseClient.from('reviews').select('*').order('created_at', { ascending: false });
        if (error) throw error;
        
        const container = document.getElementById('dynamic-reviews-list');
        if (!container) return;
        
        if (!data || data.length === 0) {
            container.innerHTML = '<p class="stylesMarningNormal-module-paragraph-m-ZXEoT">Пока нет отзывов.</p>';
            return;
        }

        let html = '';
        data.forEach((r, index) => {
            // Generate Stars
            let starsHtml = '';
            for (let i = 1; i <= 5; i++) {
                if (i <= r.rating) {
                    starsHtml += `<div tabindex="-1" role="button" aria-label="Рейтинг ${i}" class="styles-module-star-euNED"><svg class="styles-module-root-qQ0wp styles-module-filled-YWV4W" style="height:16px;width:16px" width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="m10 14.99-4.92 3.26a.55.55 0 0 1-.83-.6l1.58-5.7L1.2 8.29a.55.55 0 0 1 .31-.98l5.9-.25 2.07-5.53a.55.55 0 0 1 1.02 0l2.07 5.53 5.9.25a.55.55 0 0 1 .31.98l-4.62 3.68 1.58 5.69a.55.55 0 0 1-.83.6z"></path></svg></div>`;
                } else {
                    starsHtml += `<div tabindex="-1" role="button" aria-label="Рейтинг ${i}" class="styles-module-star-euNED"><svg class="styles-module-root-qQ0wp styles-module-empty-B0hps" style="height:16px;width:16px" width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="m10 14.99-4.92 3.26a.55.55 0 0 1-.83-.6l1.58-5.7L1.2 8.29a.55.55 0 0 1 .31-.98l5.9-.25 2.07-5.53a.55.55 0 0 1 1.02 0l2.07 5.53 5.9.25a.55.55 0 0 1 .31.98l-4.62 3.68 1.58 5.69a.55.55 0 0 1-.83.6z"></path></svg></div>`;
                }
            }

            // Generate Comment Photos
            let commentPhotosHtml = '';
            if (r.comment_photos && r.comment_photos.length > 0) {
                commentPhotosHtml = `<div class="styles-module-root-T9X8k" style="margin-top: 12px;"><div class="styles-module-images-yA0G_">` + r.comment_photos.map(url => `
                    <div class="styles-module-imageWrapper-Tz0H_">
                        <img src="${url}" class="styles-module-image-HnJ4P" style="width: 80px; height: 80px; object-fit: cover; border-radius: 4px; margin-right: 8px;">
                    </div>
                `).join('') + `</div></div>`;
            }

            // Generate Reply section
            let replyHtml = '';
            if (r.reply_text) {
                let replyPhotosHtml = '';
                if (r.reply_photos && r.reply_photos.length > 0) {
                    replyPhotosHtml = `<div class="styles-module-root-T9X8k" style="margin-top: 12px;"><div class="styles-module-images-yA0G_">` + r.reply_photos.map(url => `
                        <div class="styles-module-imageWrapper-Tz0H_">
                            <img src="${url}" class="styles-module-image-HnJ4P" style="width: 80px; height: 80px; object-fit: cover; border-radius: 4px; margin-right: 8px;">
                        </div>
                    `).join('') + `</div></div>`;
                }

                replyHtml = `
                <div data-marker="review(${index+1})/answer" class="styles-module-answer-UU7zu">
                    <header class="styles-module-root-aC2w8">
                        <div class="styles-module-avatar-_ScJK">
                            <span style="width:40px;height:40px" class="styles-module-root-pAYM0 styles-module-icon-q5sRd">
                                <img src="./logo.jpg" class="styles-module-image-gA0c_" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;">
                            </span>
                        </div>
                        <div class="styles-module-root-jjade styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-root_direction_vertical-O76uB styles-module-root_fullWidth-ScjwN" style="--module-spacer-column-gap:var(--theme-gap-0);--module-spacer-row-gap:var(--theme-gap-0)">
                            <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-direction_vertical-xJdQV" style="--module-spacer-slot-width:auto">
                                <h5 class="styles-module-root-neN_7 styles-module-root-myocF styles-module-size_xm-RKzt0 styles-module-size_xm_dense-OkKrJ styles-module-size_xm_compensated-gM6m2 styles-module-size_xm-fM_x5 styles-module-ellipsis-J1hvZ styles-module-weight_bold-K_Z3S styles-module-size_dense-HHKZg stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-header-xm-qyz8Y" style="--module-max-lines-size:1">Автосалон Автомиг - Автомобили со Всего Мира</h5>
                            </div>
                        </div>
                    </header>
                    <div class="styles-module-text-sections-tKN7j">
                        <div class="styles-module-text-section-Tp2Pg">
                            <div class="styles-module-root-T9X8k">
                                <div class="styles-module-cut-Xf0fk">
                                    <p class="styles-module-root-myocF styles-module-size_m-YQSwg styles-module-size_m-ObXjj stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-m-ZXEoT" style="white-space: pre-wrap;">${r.reply_text}</p>
                                </div>
                                ${replyPhotosHtml}
                            </div>
                        </div>
                    </div>
                </div>
                `;
            }

            // Build Review Block
            html += `
            <div class="styles-module-snippet-JUn6v" style="margin-bottom: 24px; border-bottom: 1px solid #e0e0e0; padding-bottom: 24px;">
                <div data-marker="review(${index+1})" class="styles-module-root-eNKJJ">
                    <header class="styles-module-root-aC2w8">
                        <div class="styles-module-avatar-_ScJK">
                            <span style="width:40px;height:40px" class="styles-module-root-pAYM0 styles-module-icon-q5sRd" data-marker="avatar">
                                <div class="styles-module-letter-qgO4h styles-module-letter_size_m-m97vE">${r.author_name.charAt(0).toUpperCase()}</div>
                            </span>
                        </div>
                        <div class="styles-module-root-jjade styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-root_direction_vertical-O76uB styles-module-root_fullWidth-ScjwN" style="--module-spacer-column-gap:var(--theme-gap-0);--module-spacer-row-gap:var(--theme-gap-0)">
                            <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-direction_vertical-xJdQV" style="--module-spacer-slot-width:auto">
                                <h5 class="styles-module-root-neN_7 styles-module-root-myocF styles-module-size_xm-RKzt0 styles-module-size_xm_dense-OkKrJ styles-module-size_xm_compensated-gM6m2 styles-module-size_xm-fM_x5 styles-module-ellipsis-J1hvZ styles-module-weight_bold-K_Z3S styles-module-size_dense-HHKZg stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-header-xm-qyz8Y" style="--module-max-lines-size:1">${r.author_name}</h5>
                            </div>
                            <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4" style="--module-spacer-slot-width:auto">
                                <p class="styles-module-root-myocF styles-module-size_s-UNZNT styles-module-size_s_dense-fh424 styles-module-size_s-tDgq2 styles-module-size_dense-HHKZg stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-s-dense-H7b3C">${r.date_text}</p>
                            </div>
                        </div>
                    </header>
                    <div class="styles-module-body-R_3m0">
                        <div class="styles-module-root-T9X8k">
                            <div class="styles-module-root-jjade styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-root_fullWidth-ScjwN" style="--module-spacer-column-gap:var(--theme-gap-8)">
                                <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4" style="--module-spacer-slot-width:auto">
                                    <div class="styles-module-root-Tqjuo" style="--star-gap:1px;--star-color-filled:#ffb021;--star-color-empty:#e0e0e0">
                                        ${starsHtml}
                                    </div>
                                </div>
                            </div>
                            <div class="styles-module-root-jjade styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-root_fullWidth-ScjwN" style="--module-spacer-column-gap:var(--theme-gap-8)">
                                <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-root_grow-q4mFN" style="--module-spacer-slot-width:auto">
                                    <p class="styles-module-root-myocF styles-module-size_m-YQSwg styles-module-size_m_dense-Wn03w styles-module-size_m_compensated-F6Ij8 styles-module-size_m-ObXjj styles-module-ellipsis-J1hvZ styles-module-weight_bold-K_Z3S styles-module-size_dense-HHKZg stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-header-m-oJjlT" style="--module-max-lines-size:1">
                                        ${r.car_title}
                                    </p>
                                </div>
                            </div>
                        </div>
                        <div class="styles-module-text-sections-tKN7j">
                            <div class="styles-module-text-section-Tp2Pg">
                                <div class="styles-module-root-T9X8k">
                                    <div class="styles-module-root-jjade styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-root_direction_vertical-O76uB styles-module-root_fullWidth-ScjwN" style="--module-spacer-column-gap:var(--theme-gap-4);--module-spacer-row-gap:var(--theme-gap-4)">
                                        <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-direction_vertical-xJdQV" style="--module-spacer-slot-width:auto">
                                            <div class="styles-module-cut-Xf0fk">
                                                <p class="styles-module-root-myocF styles-module-size_m-YQSwg styles-module-size_m-ObXjj stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-m-ZXEoT" style="white-space: pre-wrap;">${r.comment_text}</p>
                                            </div>
                                        </div>
                                    </div>
                                    ${commentPhotosHtml}
                                </div>
                            </div>
                        </div>
                        ${replyHtml}
                    </div>
                </div>
            </div>
            `;
        });
        
        container.innerHTML = html;
        
    } catch(err) {
        console.error('Failed to load reviews', err);
    }
}
</script>
'''

if '// --- DYNAMIC REVIEWS SCRIPT ---' not in html:
    html = html.replace('</body>', js_code + '\n</body>')
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Added dynamic reviews JS to clean_avito (1).html")
else:
    print("JS already present.")
