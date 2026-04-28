import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the incomplete CSS with a more comprehensive one
old_css = """.completed-view .photo-slider-image-PWbIy {
    opacity: 0.5;
    filter: grayscale(20%);
}"""

new_css = """.completed-view .photo-slider-image-PWbIy,
.completed-view .native-video-thumbnail-kh15u,
.completed-view .native-video-video-pvydb,
.completed-view .photo-slider-item-Zbpsa {
    opacity: 0.5;
    filter: grayscale(100%);
}"""

if old_css in html:
    html = html.replace(old_css, new_css)
else:
    # If indentation is different, use regex
    html = re.sub(
        r'\.completed-view \.photo-slider-image-PWbIy\s*\{\s*opacity:\s*0\.5;\s*filter:\s*grayscale\(20\%\);\s*\}',
        new_css,
        html
    )

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("CSS updated.")
