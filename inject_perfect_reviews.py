import re

html_file = 'clean_avito (1).html'
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

with open('js_template.js', 'r', encoding='utf-8') as f:
    template_str = f.read()

# Since we reverted, the `clean_avito (1).html` does NOT have the JS script anymore.
# We will append it to the end of the file.

# But wait! We need to add the logic that hides the static reviews dynamically so we don't flash.
# Actually, the user wants the dynamic ones to REPLACE the static ones without layout breaks.
# The code in `fix_review_styles.py` handled hiding them.

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
        const { data, error } = await window.supabaseClient.from('reviews').select('*').order('created_at', { ascending: false });
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
            
            // Replace the hardcoded template string
            html += `''' + template_str + '''`;
        });
        
        container.innerHTML = html;
        
    } catch(err) {
        console.error('Failed to load reviews', err);
    }
}
</script>
'''

# Wait, `window.supabaseClient`? I must ensure supabaseClient is defined.
# I included supabaseClient definition in `add_supabase.py` which was injected to `clean_avito (1).html`.
# Let's check if `clean_avito (1).html` has `supabaseClient`. It does.

if '// --- DYNAMIC REVIEWS SCRIPT ---' not in html:
    final_html = html.replace('</body>', new_script + '\n</body>')
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print("Injected perfect 1:1 dynamic reviews script.")
else:
    print("Script already present")
