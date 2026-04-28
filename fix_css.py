import os

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

css = """
<style id="custom-dropdown-styles">
.custom-mega-dropdown {
    display: none;
    position: absolute;
    width: 800px;
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    padding: 32px 24px;
    z-index: 99999;
    box-sizing: border-box;
    cursor: default;
    text-align: left;
}
.custom-mega-dropdown.show { display: flex; gap: 40px; }
.mega-dropdown-col { flex: 1; display: flex; flex-direction: column; gap: 24px; }
.mega-dropdown-section h3 { font-size: 16px; font-weight: 700; margin: 0 0 12px 0; font-family: Manrope, sans-serif; color: #000; }
.mega-dropdown-section a { display: block; color: #000; text-decoration: none; font-size: 14px; margin-bottom: 8px; font-family: Manrope, sans-serif; }
.mega-dropdown-section a:hover { color: #00a8ff; }
.mega-dropdown-all-cats { font-size: 16px; font-weight: 700; color: #00a8ff; cursor: pointer; font-family: Manrope, sans-serif; margin-bottom: 24px; }
</style>
<style id="custom-filters-styles">
.custom-filter-select, .custom-filter-input {
    background-color: #F2F2F2;
    border-radius: 8px;
    height: 40px;
    display: flex;
    align-items: center;
    padding: 0 12px;
    box-sizing: border-box;
    cursor: pointer;
}
.custom-filter-select { justify-content: space-between; }
.custom-filter-text { color: #8f8f8f; font-size: 14px; font-family: Manrope, sans-serif; }
.custom-filter-arrow { color: #8f8f8f; font-size: 16px; }
.custom-filter-input input { border: none; background: transparent; width: 100%; outline: none; font-size: 14px; font-family: Manrope, sans-serif; color: #000; }
.custom-filter-input input::placeholder { color: #8f8f8f; }
</style>
"""

if 'custom-mega-dropdown.show' not in text:
    text = text.replace('</head>', css + '\n</head>')
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('CSS restored.')
else:
    print('CSS already present.')
