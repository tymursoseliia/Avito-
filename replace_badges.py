import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'<div><div class="ProfileBadge-root-xZasE.*?12 покупок.*?Реквизиты проверены.*?</div></div></div></div>', re.DOTALL)

replacement = '''<div style="display: flex; flex-direction: column; gap: 8px; margin-bottom: 16px; width: 100%;">
  <div style="display: flex; align-items: center; background-color: #E6F6FF; border-radius: 12px; padding: 12px 16px; gap: 12px;">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
    <span style="font-size: 14px; font-weight: 500; color: #000; font-family: Manrope, sans-serif;">12 покупок с Авито Доставкой</span>
  </div>
  <div style="display: flex; align-items: center; background-color: #E6F6FF; border-radius: 12px; padding: 12px 16px; gap: 12px;">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="3" width="15" height="13"></rect><polygon points="16 8 20 8 23 11 23 16 16 16 16 8"></polygon><circle cx="5.5" cy="18.5" r="2.5"></circle><circle cx="18.5" cy="18.5" r="2.5"></circle></svg>
    <span style="font-size: 14px; font-weight: 500; color: #000; font-family: Manrope, sans-serif;">37 продаж с Авито Доставкой</span>
  </div>
  <div style="display: flex; align-items: center; background-color: #E6F6FF; border-radius: 12px; padding: 12px 16px; gap: 12px;">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
    <span style="font-size: 14px; font-weight: 500; color: #000; font-family: Manrope, sans-serif;">Реквизиты проверены</span>
  </div>
</div>'''

new_content, count = pattern.subn(replacement, content)

if count > 0:
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'Replaced {count} occurrences.')
else:
    print('Pattern not found!')
