import re

# Read the HTML file
html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace the entire <script>...</script> block that contains `// --- DYNAMIC REVIEWS SCRIPT ---`
js_start = html.find('// --- DYNAMIC REVIEWS SCRIPT ---')
if js_start != -1:
    script_start = html.rfind('<script>', 0, js_start)
    script_end = html.find('</script>', js_start) + 9
    
    # We will replace it with the updated script.

    new_script = '''<script>
// --- DYNAMIC REVIEWS SCRIPT ---
document.addEventListener('DOMContentLoaded', async () => {
    // 1. Remove all static reviews
    const staticReviews = document.querySelectorAll('[data-marker^="review("]');
    if (staticReviews.length > 0) {
        staticReviews.forEach(el => {
            const snippet = el.closest('.styles-module-snippet-JUn6v') || el;
            snippet.style.display = 'none'; // We just hide them instead of removing to avoid breaking things, or remove them
            snippet.remove();
        });
        
        const ratingSummary = document.querySelector('[data-marker="ratingSummary"]');
        if (ratingSummary) {
            let dynList = document.createElement('div');
            dynList.id = 'dynamic-reviews-list';
            dynList.style.marginTop = '24px';
            ratingSummary.parentElement.parentElement.appendChild(dynList);
            fetchAndRenderReviews();
        }
    } else {
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
            let starsHtml = '';
            for (let i = 1; i <= 5; i++) {
                if (i <= r.rating) {
                    starsHtml += `<div data-marker="review(${index+1})/score/star-${i}" tabindex="-1" role="button" aria-label="Рейтинг ${i}" class="styles-module-star-euNED"><svg class="styles-module-root-qQ0wp styles-module-filled-YWV4W" style="height:16px;width:16px" width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="m10 14.99-4.92 3.26a.55.55 0 0 1-.83-.6l1.58-5.7L1.2 8.29a.55.55 0 0 1 .31-.98l5.9-.25 2.07-5.53a.55.55 0 0 1 1.02 0l2.07 5.53 5.9.25a.55.55 0 0 1 .31.98l-4.62 3.68 1.58 5.69a.55.55 0 0 1-.83.6z"></path></svg></div>`;
                } else {
                    starsHtml += `<div data-marker="review(${index+1})/score/star-${i}" tabindex="-1" role="button" aria-label="Рейтинг ${i}" class="styles-module-star-euNED"><svg class="styles-module-root-qQ0wp styles-module-empty-B0hps" style="height:16px;width:16px" width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="m10 14.99-4.92 3.26a.55.55 0 0 1-.83-.6l1.58-5.7L1.2 8.29a.55.55 0 0 1 .31-.98l5.9-.25 2.07-5.53a.55.55 0 0 1 1.02 0l2.07 5.53 5.9.25a.55.55 0 0 1 .31.98l-4.62 3.68 1.58 5.69a.55.55 0 0 1-.83.6z"></path></svg></div>`;
                }
            }

            let commentPhotosHtml = '';
            if (r.comment_photos && r.comment_photos.length > 0) {
                commentPhotosHtml = `<div class="styles-module-images-ycitL"><div class="styles-module-root-aix8z" data-marker="review(${index+1})"><div data-marker="review(${index+1})" class="styles-module-root-Ie3Kv" style="--thumbnail-size:60px;--thumbnail-gap:2px;--thumbnail-border-radius:2px;--thumbnail-edge-border-radius:12px">` + r.comment_photos.map((url, i) => `
                    <div data-marker="review(${index+1})/image(${i})" class="styles-module-image-IJiTw styles-module-loading-_VPeU" tabindex="0" role="button" aria-label="Нажмите, чтобы увеличить">
                        <img alt="Фото из отзыва" src="${url}" class="styles-module-root-lUe4R styles-module-root_object_fit_cover-Sdu0X" style="width:100%;height:100%" draggable="false" data-marker="review(${index+1})/image(${i})/image">
                    </div>
                `).join('') + `</div></div></div>`;
            }

            let replyHtml = '';
            if (r.reply_text) {
                let replyPhotosHtml = '';
                if (r.reply_photos && r.reply_photos.length > 0) {
                    replyPhotosHtml = `<div class="styles-module-images-ycitL"><div class="styles-module-root-aix8z" data-marker="review(${index+1})"><div data-marker="review(${index+1})" class="styles-module-root-Ie3Kv" style="--thumbnail-size:60px;--thumbnail-gap:2px;--thumbnail-border-radius:2px;--thumbnail-edge-border-radius:12px">` + r.reply_photos.map((url, i) => `
                        <div data-marker="review(${index+1})/image(${i})" class="styles-module-image-IJiTw styles-module-loading-_VPeU" tabindex="0" role="button" aria-label="Нажмите, чтобы увеличить">
                            <img alt="Фото из отзыва" src="${url}" class="styles-module-root-lUe4R styles-module-root_object_fit_cover-Sdu0X" style="width:100%;height:100%" draggable="false" data-marker="review(${index+1})/image(${i})/image">
                        </div>
                    `).join('') + `</div></div></div>`;
                }

                replyHtml = `
                <div data-marker="review(${index+1})/answer" class="styles-module-answer-UU7zu">
                    <header data-marker="review(${index+1})/header" itemprop="author" itemtype="https://schema.org/Person" itemscope="" class="styles-module-root-aC2w8">
                        <div class="styles-module-avatar-_ScJK">
                            <span style="width:40px;height:40px" class="styles-module-root-pAYM0 styles-module-icon-q5sRd">
                                <img src="./logo.jpg" class="styles-module-image-gA0c_" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;">
                            </span>
                        </div>
                        <div class="styles-module-root-jjade styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-root_direction_vertical-O76uB styles-module-root_fullWidth-ScjwN" style="--module-spacer-column-gap:var(--theme-gap-0);--module-spacer-row-gap:var(--theme-gap-0)">
                            <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-direction_vertical-xJdQV" style="--module-spacer-slot-width:auto">
                                <h5 data-marker="review(${index+1})/header/title" itemprop="name" class="styles-module-root-neN_7 styles-module-root-myocF styles-module-size_xm-RKzt0 styles-module-size_xm_dense-OkKrJ styles-module-size_xm_compensated-MV7t5 styles-module-size_xm-P71H7 styles-module-ellipsis-J1hvZ styles-module-ellipsis_oneLine-ZlKYu styles-module-size_dense-HHKZg stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-header-xm-qyz8Y" style="--module-max-lines-size:1">Автомиг | Авто со Всего Мира</h5>
                            </div>
                            <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-direction_vertical-xJdQV" style="--module-spacer-slot-width:auto">
                                <p data-marker="review(${index+1})/header/subtitle" class="styles-module-root-myocF styles-module-size_s-UNZNT styles-module-size_s_compensated-mu3RP styles-module-size_s-tDgq2 styles-module-ellipsis-J1hvZ styles-module-ellipsis_oneLine-ZlKYu stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-s-T9Os5 styles-module-noAccent-jqVSj" style="--module-max-lines-size:1">Официальный ответ</p>
                            </div>
                        </div>
                        <div class="styles-module-component-after-Y15nP"></div>
                    </header>
                    <div class="">
                        ${replyPhotosHtml}
                        <div class="styles-module-textSection-ivuRS">
                            <div class="styles-module-root-T9X8k">
                                <div class="styles-module-root-jjade styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-root_direction_vertical-O76uB styles-module-root_fullWidth-ScjwN" style="--module-spacer-column-gap:var(--theme-gap-4);--module-spacer-row-gap:var(--theme-gap-4)">
                                    <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-direction_vertical-xJdQV" style="--module-spacer-slot-width:auto">
                                        <div class="styles-module-cut-Xf0fk">
                                            <p class="styles-module-root-myocF styles-module-size_m-YQSwg styles-module-size_m-ObXjj stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-m-ZXEoT" style="white-space: pre-wrap;" data-marker="review(${index+1})/text-section/text">${r.reply_text}</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                `;
            }

            html += `
            <div class="styles-module-snippet-JUn6v">
                <div data-marker="review(${index+1})" itemtype="https://schema.org/Review" itemscope="" class="styles-module-root-eNKJJ">
                    <header data-marker="review(${index+1})/header" itemprop="author" itemtype="https://schema.org/Person" itemscope="" class="styles-module-root-aC2w8">
                        <div class="styles-module-avatar-_ScJK">
                            <span style="width:40px;height:40px" class="styles-module-root-pAYM0 styles-module-icon-q5sRd">
                                <div class="styles-module-letter-qgO4h styles-module-letter_size_m-m97vE" style="background-color: #00AAFF; color: white; border-radius: 50%; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-weight: bold;">
                                    ${r.author_name.charAt(0).toUpperCase()}
                                </div>
                            </span>
                        </div>
                        <div class="styles-module-root-jjade styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-root_direction_vertical-O76uB styles-module-root_fullWidth-ScjwN" style="--module-spacer-column-gap:var(--theme-gap-0);--module-spacer-row-gap:var(--theme-gap-0)">
                            <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-direction_vertical-xJdQV" style="--module-spacer-slot-width:auto">
                                <h5 data-marker="review(${index+1})/header/title" itemprop="name" class="styles-module-root-neN_7 styles-module-root-myocF styles-module-size_xm-RKzt0 styles-module-size_xm_dense-OkKrJ styles-module-size_xm_compensated-MV7t5 styles-module-size_xm-P71H7 styles-module-ellipsis-J1hvZ styles-module-ellipsis_oneLine-ZlKYu styles-module-size_dense-HHKZg stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-header-xm-qyz8Y" style="--module-max-lines-size:1">${r.author_name}</h5>
                            </div>
                            <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-direction_vertical-xJdQV" style="--module-spacer-slot-width:auto">
                                <p data-marker="review(${index+1})/header/subtitle" class="styles-module-root-myocF styles-module-size_s-UNZNT styles-module-size_s_compensated-mu3RP styles-module-size_s-tDgq2 styles-module-ellipsis-J1hvZ styles-module-ellipsis_oneLine-ZlKYu stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-s-T9Os5 styles-module-noAccent-jqVSj" style="--module-max-lines-size:1">${r.date_text}</p>
                            </div>
                        </div>
                        <div class="styles-module-component-after-Y15nP"></div>
                    </header>
                    <div data-marker="review(${index+1})/body">
                        <div class="">
                            <div class="styles-module-attributes-MWa1u">
                                <div class="styles-module-root-RaCL8">
                                    <div class="styles-module-score-eLAXV">
                                        <div data-marker="review(${index+1})/score" itemprop="reviewRating" itemtype="https://schema.org/Rating" itemscope="" style="--star-gap:0px;--star-color-filled:#ffb021;--star-color-empty:#e0e0e0;--star-color-invalid:#ffc5c6" class="styles-module-root-Tqjuo">
                                            <meta itemprop="ratingValue" content="${r.rating}">
                                            ${starsHtml}
                                        </div>
                                    </div>
                                    <p itemprop="itemReviewed" itemtype="https://schema.org/Product" itemscope="" class="styles-module-root-myocF styles-module-size_m-YQSwg styles-module-size_m_dense-Wn03w styles-module-size_m_compensated-F6Ij8 styles-module-size_m-ObXjj styles-module-ellipsis-J1hvZ styles-module-ellipsis_oneLine-ZlKYu styles-module-size_dense-HHKZg stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-m-dense-aiTyL styles-module-noAccent-jqVSj" style="--module-max-lines-size:1" data-marker="review(${index+1})/stage">Сделка состоялась<!-- --> · <span itemprop="name" class="styles-module-size_m-YQSwg" data-marker="review(${index+1})/itemTitle">${r.car_title}</span></p>
                                </div>
                            </div>
                            <div class="styles-module-text-sections-tKN7j">
                                <div class="styles-module-text-section-Tp2Pg">
                                    <div class="styles-module-root-T9X8k">
                                        <div class="styles-module-root-jjade styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-root_direction_vertical-O76uB styles-module-root_fullWidth-ScjwN" style="--module-spacer-column-gap:var(--theme-gap-4);--module-spacer-row-gap:var(--theme-gap-4)">
                                            <div class="styles-module-root-auHUM styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4 styles-module-direction_vertical-xJdQV" style="--module-spacer-slot-width:auto">
                                                <div class="styles-module-cut-Xf0fk">
                                                    <p class="styles-module-root-myocF styles-module-size_m-YQSwg styles-module-size_m-ObXjj stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-m-ZXEoT" style="white-space: pre-wrap;" data-marker="review(${index+1})/text-section/text">${r.comment_text}</p>
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
            </div>
            `;
        });
        
        container.innerHTML = html;
        
    } catch(err) {
        console.error('Failed to load reviews', err);
    }
}
</script>'''

    final_html = html[:script_start] + new_script + html[script_end:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Fixed review styles!")
else:
    print("Could not find dynamic JS block")
