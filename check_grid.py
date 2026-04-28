with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

# We want to clear the contents of <div class="ProfileItemsGrid-module-root-wq8JY">
# So it starts empty and doesn't flash old cars!
import re
grid_start = text.find('ProfileItemsGrid-module-root-wq8JY')
if grid_start != -1:
    div_start = text.rfind('<div', 0, grid_start)
    # We will just replace everything inside this div with empty string
    # Actually, let's just use regex to empty it out. But HTML regex is hard.
    # Let's find where the next container starts or just manually empty it
    
    # We can just change the class name so the JS finds it, but hide the original grid?
    # No, it's easier to just find the grid and wipe its children in HTML.
    
    # Let's find the closing tag of ProfileItemsGrid-module-root-wq8JY? It's huge.
    # What if we just use Python's html parser?
pass
