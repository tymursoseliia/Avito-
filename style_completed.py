import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add CSS style
style_block = """
<style>
.completed-view .photo-slider-image-PWbIy {
    opacity: 0.5;
    filter: grayscale(20%);
}
.completed-view .styles-module-size_xm-RKzt0 {
    color: #8f8f8f !important;
}
.completed-view .styles-module-root-u1LzV {
    color: #8f8f8f !important;
}
.completed-view .geo-root-ltL41 p {
    color: #8f8f8f !important;
}
.completed-view .geo-pinIcon-PNCMG svg path,
.completed-view .geo-pinIcon-PNCMG svg circle {
    stroke: #8f8f8f !important;
    fill: #8f8f8f !important;
}
</style>
</head>
"""

if '.completed-view' not in html:
    html = html.replace('</head>', style_block)

# 2. Add class toggling in the JS
old_active_onclick = """      tabActive.onclick = () => {
          tabActive.classList.add('styles-module-tab-button_active-mZotZ');
          tabActive.setAttribute('aria-selected', 'true');
          tabClosed.classList.remove('styles-module-tab-button_active-mZotZ');
          tabClosed.setAttribute('aria-selected', 'false');
          grid.innerHTML = activeCarsHtml;
      };"""

new_active_onclick = """      tabActive.onclick = () => {
          tabActive.classList.add('styles-module-tab-button_active-mZotZ');
          tabActive.setAttribute('aria-selected', 'true');
          tabClosed.classList.remove('styles-module-tab-button_active-mZotZ');
          tabClosed.setAttribute('aria-selected', 'false');
          grid.innerHTML = activeCarsHtml;
          grid.classList.remove('completed-view');
      };"""

old_closed_onclick = """      tabClosed.onclick = () => {
          tabClosed.classList.add('styles-module-tab-button_active-mZotZ');
          tabClosed.setAttribute('aria-selected', 'true');
          tabActive.classList.remove('styles-module-tab-button_active-mZotZ');
          tabActive.setAttribute('aria-selected', 'false');
          grid.innerHTML = finalCompletedHtml;
      };"""

new_closed_onclick = """      tabClosed.onclick = () => {
          tabClosed.classList.add('styles-module-tab-button_active-mZotZ');
          tabClosed.setAttribute('aria-selected', 'true');
          tabActive.classList.remove('styles-module-tab-button_active-mZotZ');
          tabActive.setAttribute('aria-selected', 'false');
          grid.innerHTML = finalCompletedHtml;
          grid.classList.add('completed-view');
      };"""

html = html.replace(old_active_onclick, new_active_onclick)
html = html.replace(old_closed_onclick, new_closed_onclick)

with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Styles applied successfully")
