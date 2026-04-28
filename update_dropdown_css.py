import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

new_css = """
<style>
.custom-brand-dropdown {
    position: absolute;
    top: calc(100% + 4px);
    left: 0;
    width: 100%;
    background: #ffffff;
    border-radius: 6px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    z-index: 1000;
    font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
    font-size: 14px;
    color: #000;
    overflow-y: auto;
    max-height: 280px;
    border: 1px solid #e0e0e0;
}
.custom-brand-dropdown::-webkit-scrollbar {
    width: 8px;
}
.custom-brand-dropdown::-webkit-scrollbar-thumb {
    background-color: #c4c4c4;
    border-radius: 4px;
}
.brand-item {
    padding: 10px 16px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
    line-height: 1.4;
}
.brand-item:hover {
    background-color: #f2f2f2;
}
.brand-title {
    padding: 12px 16px 8px;
    font-weight: 700;
    color: #000;
}
.brand-item.not-selected {
    background-color: #e8e5df;
}
.brand-item.not-selected:hover {
    background-color: #e8e5df;
}
</style>
"""

# Let's find exactly `<style>\n.custom-brand-dropdown {`
start_idx = html.find('<style>\n.custom-brand-dropdown {')
if start_idx != -1:
    end_idx = html.find('</style>', start_idx) + 8
    html = html[:start_idx] + new_css.strip() + html[end_idx:]
else:
    # Maybe it was written differently
    start_idx = html.find('.custom-brand-dropdown {')
    if start_idx != -1:
        # find the <style> before it
        style_idx = html.rfind('<style>', 0, start_idx)
        end_idx = html.find('</style>', start_idx) + 8
        html = html[:style_idx] + new_css.strip() + html[end_idx:]

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

print("CSS updated.")
