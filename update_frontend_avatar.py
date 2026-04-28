import re

html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

with open('js_template.js', 'r', encoding='utf-8') as f:
    template_str = f.read()

# We need to change the template to use author_avatar if available
# The current template has:
# <div class="styles-module-letter-qgO4h styles-module-letter_size_m-m97vE" style="background-color: #00AAFF; color: white; border-radius: 50%; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; font-weight: bold;">${r.author_name.charAt(0).toUpperCase()}</div>
# Wait, js_template.js still has `<img src="./logo.jpg"...` because it was generated from original_review.html which had logo.jpg!
# Let me look at my previous inject_perfect_reviews.py to see how I generated new_script.

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
        const colors = ['#00AAFF', '#FF5500', '#00CC66', '#9900FF', '#FF0055'];
        
        data.forEach((r, index) => {
            let starsHtml = '';
            for (let i = 1; i <= 5; i++) {
                if (i <= r.rating) {
                    starsHtml += `<div data-marker="review(${index+1})/score/star-${i}" tabindex="-1" role="button" aria-label="Рейтинг ${i}" class="styles-module-star-euNED"><svg class="styles-module-root-qQ0wp styles-module-filled-YWV4W" style="height:16px;width:16px" width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="m10 14.99-4.92 3.26a.55.55 0 0 1-.83-.6l1.58-5.7L1.2 8.29a.55.55 0 0 1 .31-.98l5.9-.25 2.07-5.53a.55.55 0 0 1 1.02 0l2.07 5.53 5.9.25a.55.55 0 0 1 .31.98l-4.62 3.68 1.58 5.69a.55.55 0 0 1-.83.6z"></path></svg></div>`;
                } else {
                    starsHtml += `<div data-marker="review(${index+1})/score/star-${i}" tabindex="-1" role="button" aria-label="Рейтинг ${i}" class="styles-module-star-euNED"><svg class="styles-module-root-qQ0wp styles-module-empty-B0hps" style="height:16px;width:16px" width="20" height="20" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path d="m10 14.99-4.92 3.26a.55.55 0 0 1-.83-.6l1.58-5.7L1.2 8.29a.55.55 0 0 1 .31-.98l5.9-.25 2.07-5.53a.55.55 0 0 1 1.02 0l2.07 5.53 5.9.25a.55.55 0 0 1 .31.98l-4.62 3.68 1.58 5.69a.55.55 0 0 1-.83.6z"></path></svg></div>`;
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
            
            let itemHtml = `''' + template_str + '''`;
            
            // Replace the hardcoded author avatar from template with authorAvatarHtml
            // We know the template has <img src="./logo.jpg" class="styles-module-image-gA0c_" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;">
            // But wait, the reply ALSO has logo.jpg!
            // We must only replace the FIRST occurrence of logo.jpg per review block for the author.
            // Let's do it like this:
            itemHtml = itemHtml.replace('<img src="./logo.jpg" class="styles-module-image-gA0c_" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;">', authorAvatarHtml);
            
            html += itemHtml;
        });
        
        container.innerHTML = html;
        
    } catch(err) {
        console.error('Failed to load reviews', err);
    }
}
</script>
'''

# Replace the existing script in html
js_start = html.find('// --- DYNAMIC REVIEWS SCRIPT ---')
if js_start != -1:
    script_start = html.rfind('<script>', 0, js_start)
    script_end = html.find('</script>', js_start) + 9
    final_html = html[:script_start] + new_script + html[script_end:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Injected updated script for author avatars.")
else:
    final_html = html.replace('</body>', new_script + '\n</body>')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Injected script for author avatars (new).")
