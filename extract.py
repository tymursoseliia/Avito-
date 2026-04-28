import re
f=open('clean_avito (1).html', 'r', encoding='utf-8')
content=f.read()
match=re.search(r'<div[^>]*class=.styles-module-flex-mJzcB styles-module-flex-col-zuXfL styles-module-child-width-full-26DGJ styles-module-child-height-full-clwo0.*?</public-profile-desktoppublicprofile>', content, re.DOTALL)
open('sidebar.txt', 'w', encoding='utf-8').write(match.group(0) if match else 'not found')
