import re

html_file = 'clean_avito (1).html'

with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace the avatar image specifically inside the seller answers.
# The answers have class="styles-module-answer-UU7zu"
# The avatar container inside them is <div class="styles-module-avatar-_ScJK">...</div>
# We can find all occurrences of <div class="styles-module-avatar-_ScJK"> and replace the span/img inside it if it's within an answer.
# Actually, styles-module-avatar-_ScJK might only be used for answer avatars! Let's check how many there are.

count = 0
def repl(match):
    global count
    count += 1
    # Replace the entire <div class="styles-module-avatar-_ScJK">...</div> 
    # with the new logo.
    new_content = '<div class="styles-module-avatar-_ScJK"><span style="width:40px;height:40px" class="styles-module-root-pAYM0 styles-module-icon-q5sRd"><img src="./logo.jpg" class="styles-module-image-gA0c_" style="width: 100%; height: 100%; border-radius: 50%; object-fit: cover;"></span></div>'
    return new_content

# Match <div class="styles-module-avatar-_ScJK"> and everything until the next </div> that closes it
# Note: since it contains <span...><img...></span></div>, we can match up to </span></div></div>
# A safer way:
new_html = re.sub(r'<div class="styles-module-avatar-_ScJK">.*?</span></div>', repl, html, flags=re.DOTALL)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Replaced {count} answer avatars with logo.jpg")
