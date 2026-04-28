with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '<div class="ProfileItemsGrid-module-root-wq8JY">'
start_idx = text.find(start_marker)

if start_idx != -1:
    # We need to find the matching closing div
    # Or simply, we know the next sibling or parent closing
    # The grid contains many iva-item-root-Kcj9I divs.
    # Let's just find the end of the grid by looking for a marker that comes after it.
    end_marker = '<div class="ProfileItemsList-module-action-c2I0I">'
    end_idx = text.find(end_marker, start_idx)
    
    if end_idx != -1:
        # Before end_marker, there should be a closing </div> for the grid
        # We will replace everything between start_marker + len(start_marker) and end_idx - 10
        # Let's be safe and use a simple regex or string replace if we can find the exact bounds.
        pass

# Actually, the easiest way to delete the old cars from the HTML without breaking tags is:
import bs4
soup = bs4.BeautifulSoup(text, 'html.parser')
grid = soup.find('div', class_='ProfileItemsGrid-module-root-wq8JY')
if grid:
    grid.clear()
    
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print("Cleared hardcoded cars using BeautifulSoup")
else:
    print("Grid not found")

