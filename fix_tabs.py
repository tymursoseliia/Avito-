import re

with open('clean_avito (1).html', 'r', encoding='utf-8') as f:
    html = f.read()

# We need to replace async function loadCars() { ... } with our new logic.
# Since it's at the end of the file, we can use regex or string manipulation.

start_str = "async function loadCars() {"
end_str = "if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',loadCars);}else{loadCars();}"

start_idx = html.find(start_str)
end_idx = html.find(end_str)

if start_idx != -1 and end_idx != -1:
    old_logic = html[start_idx:end_idx]
    
    # We will extract the cardHtml generation part and wrap it in a new logic.
    new_logic = """let completedCarsHtml = '';
let activeCarsHtml = '';

async function loadCars() {
  const grid = document.querySelector('.ProfileItemsGrid-module-root-wq8JY');
  if (!grid) return;
  
  if (!completedCarsHtml) {
      completedCarsHtml = grid.innerHTML;
  }

  const { data: cars, error } = await supabaseClient.from('cars').select('*').order('created_at', { ascending: false });
  if (error) { console.error('Ошибка:', error); return; }

  activeCarsHtml = '';

  if (!cars || cars.length === 0) { 
      activeCarsHtml = '<p style="padding: 20px; font-family: Manrope, sans-serif; font-size: 16px;">Нет активных объявлений.</p>'; 
  } else {
      cars.forEach(car => {
        let badgeHtml = '';
        if (car.badge_text) {
            badgeHtml = `<div class="iva-item-badgeBarStep-M10pn iva-item-ivaItemRedesign-emu4_"><div class=""><div><div class="SnippetLayout-root-rWpNO SnippetLayout-rootVertical-QewdW SnippetLayout-rootDocking-kGTyv"><div class="SnippetLayout-item-ntHD2"><div class="SnippetBadgeV2-root-oZw6k"><div class="styles-module-root-XQv5I styles-module-root_size_m-RVAzG styles-module-root_preset_green-aAvUr" data-marker="iva-item/2232"><div class="styles-module-corner-D5aFi styles-module-corner_left-RFgMw" style="color:#00AAFF"><svg width="13" height="28" viewBox="0 0 13 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="M0 28V0h9.25c.68 0 1.34.17 1.92.5.57.33 1.05.8 1.37 1.37a3.49 3.49 0 0 1-.14 3.68l-3.47 5.2a5.83 5.83 0 0 0 0 6.5l3.47 5.2a3.5 3.5 0 0 1-1.23 5.04c-.58.33-1.23.5-1.9.51H0Z"></path></svg></div><div class="styles-module-content-huG62" style="color:#FFFFFF;background-color:#00AAFF">${car.badge_text}</div><div class="styles-module-corner-D5aFi styles-module-corner_right-lw0vp" style="color:#00AAFF"><svg width="12" height="28" viewBox="0 0 12 28" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill="currentColor" d="m4.92 1.84 6.4 9.89a4.18 4.18 0 0 1 0 4.54l-6.4 9.9A4.02 4.02 0 0 1 1.53 28H0V0h1.53a4.06 4.06 0 0 1 3.39 1.84Z"></path></svg></div></div></div></div></div></div></div></div></div>`;
        }

        const priceFormatted = car.price ? car.price.toString().replace(/\\B(?=(\\d{3})+(?!\\d))/g, " ") : "0";
        
        const cardHtml = `<div onclick="window.open('car_page.html?id=${car.id}', '_blank')" style="cursor:pointer" class="iva-item-root-Kcj9I photo-slider-slider-igVxt iva-item-gallery-Xzeib iva-item-ivaItemRedesign-emu4_ iva-item-responsive-QUMlk iva-item-xl-DqPVY  js-catalog-item-enum" itemscope="" itemtype="http://schema.org/Product">
<div class="styles-module-theme-q6maA tokens-light-module-theme-Jt9YA styles-module-theme-Xik12"><div class="styles-module-theme-q6maA tokens-light-module-theme-Jt9YA styles-module-theme-Xik12"><div class="iva-item-content-caL0w"><div class="iva-item-slider-OwE2I" data-marker="item-image"><div class="styles-redesignGalleryBadgesWrapper-Iw7Mp"><div class="styles-module-root-jjade styles-module-margin-top_none-ncPHM styles-module-margin-bottom_none-Umlp4" style="--module-spacer-column-gap:var(--theme-gap-8)"></div></div>
<a class="iva-item-sliderLink-hO7qj" data-marker="item-photo-sliderLink" itemprop="url" href="#" target="_blank" rel="noopener noreferrer"><div class="photo-slider-root-_kL8M photo-slider-roundCorners-j8Wrb" data-marker="item-photo"><div class="photo-slider-photoSlider-b9P07 photo-slider-aspect-ratio-1-1-aIB4A"><ul class="photo-slider-list-PxsU9" style="display:flex; overflow-x:auto; scroll-snap-type:x mandatory; scrollbar-width:none;">
${(car.image_urls && car.image_urls.length > 0 ? car.image_urls : [car.image_url]).map((url, idx) => `
<li onclick="event.stopPropagation(); window.open('car_page.html?id=${car.id}&img=${idx}', '_blank')" class="photo-slider-list-item-X8gjp photo-slider-dotsCounter-XHmkX" style="flex: 0 0 100%; scroll-snap-align: start; cursor:pointer;"><div class="photo-slider-item-Zbpsa photo-slider-keepImageRatio-BgO73">
<img alt="${car.title}" class="photo-slider-image-PWbIy" itemprop="image" importance="high" src="${url}" loading="${idx === 0 ? 'eager' : 'lazy'}"></div></li>
`).join('')}</ul></div></div></a>
${badgeHtml}
</div><div class="iva-item-body-D1zaw"><div class="iva-item-favoriteCartIcons-ozfQY iva-item-ivaItemRedesign-emu4_"><div class="iva-item-ivaItemRedesign-emu4_"><span hidden=""></span><div data-marker="favorites-add" data-state="empty" class="favorites-rootRedesign-MrHIV" title="Добавить в избранное и в сравнение" aria-haspopup="true" aria-expanded="false"><svg class="favorites-favoritesOutlineIcon-W5gir" width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M9.98204 16.867L3.28133 10.1643C1.69523 8.57776 1.69534 6.00549 3.28133 4.41902C4.86733 2.83255 7.43879 2.83252 9.02478 4.41902L9.98204 5.37656L10.9393 4.41902C12.5253 2.83255 15.0968 2.83252 16.6829 4.41902C18.2688 6.00553 18.2688 8.5778 16.6829 10.1643L9.98204 16.867Z" stroke-width="2.2" stroke-linejoin="round"></path></svg></div><span data-resolver-terminal="true" hidden=""></span></div></div><div class="iva-item-titleStep-kuovU iva-item-ivaItemRedesign-emu4_"><div class="iva-item-titleWrapper-a3mcT"><div class="iva-item-title-mxG7F"><h2 itemprop="name" class="styles-module-root-neN_7 styles-module-root-myocF styles-module-size_m-YQSwg styles-module-size_m_dense-Wn03w styles-module-size_m_compensated-F6Ij8 styles-module-size_m-ObXjj styles-module-ellipsis-J1hvZ styles-module-weight_normal-DI6c9 styles-module-size_dense-HHKZg stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-header-m-oJjlT" style="--module-max-lines-size:2"><a itemprop="url" rel="noopener" target="_blank" title="${car.title}" data-marker="item-title" href="#" class="styles-module-root-u1LzV styles-module-root_underlineOffset_size-m-MlPEm styles-module-root_noVisited-PHSAu styles-module-root_preset_black-mfhgC">${car.title}</a></h2></div></div></div><div class="iva-item-priceStep-lpXsl iva-item-ivaItemRedesign-emu4_"><span class="price-root-HNqwR"><div class="price-price-l1xq6"><div class="price-priceContent-tSFM8"><p data-marker="item-price" itemprop="offers" itemscope="" itemtype="http://schema.org/Offer" class="styles-module-root-myocF styles-module-size_s-UNZNT styles-module-size_s-tDgq2 stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-s-T9Os5"><meta itemprop="priceCurrency" content="RUB"><meta itemprop="price" content="${car.price}"><meta itemprop="availability" content="https://schema.org/LimitedAvailability"><strong class="styles-module-root-caRWu"><span data-marker="item-price-value" class="styles-module-size_xm-RKzt0 styles-module-size_xm_dense-OkKrJ">${priceFormatted}<!-- -->&nbsp;₽</span></strong></p></div></div></span></div><div class="iva-item-ivaItemRedesign-emu4_"><div class="geo-root-ltL41" data-marker="item-location"><p class="styles-module-root-myocF styles-module-size_m-YQSwg styles-module-size_m_dense-Wn03w styles-module-size_m-ObXjj styles-module-size_dense-HHKZg stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-m-dense-aiTyL"><span title="" class=""><span class="geo-pinIcon-PNCMG"><svg width="10" height="12" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="4.59927" cy="4.6" r="1.25455" fill="black"></circle><path d="M0.5 4.44318C0.5 2.27871 2.31612 0.5 4.6 0.5C6.88388 0.5 8.7 2.27871 8.7 4.44318C8.7 5.36368 8.36741 6.19394 7.84004 6.84334L5.44405 9.71032C5.22744 9.96951 5.08532 10.1389 4.96726 10.2575C4.8524 10.373 4.7979 10.4006 4.77138 10.4103C4.6607 10.4507 4.5393 10.4507 4.42862 10.4103C4.4021 10.4006 4.3476 10.373 4.23274 10.2575C4.11468 10.1389 3.97256 9.96951 3.75595 9.71032L1.35996 6.84335C0.832595 6.19395 0.5 5.36369 0.5 4.44318Z" stroke="black" stroke-linejoin="round"></path></svg></span>${car.location || ''}</span></p></div></div><div class="iva-item-dateInfoStep-rNddc iva-item-ivaItemRedesign-emu4_"><span hidden=""></span><div data-marker="item-date/tooltip/reference" aria-haspopup="true" aria-expanded="false"><p class="styles-module-root-myocF styles-module-size_m-YQSwg styles-module-size_m_dense-Wn03w styles-module-size_m-ObXjj styles-module-size_dense-HHKZg stylesMarningNormal-module-root-oPKUh stylesMarningNormal-module-paragraph-m-dense-aiTyL styles-module-noAccent-jqVSj" data-marker="item-date">${car.date_str || ''}</p></div><span data-resolver-terminal="true" hidden=""></span><div class="styles-arrowRoot-uNr2A"><span hidden=""></span><div class="styles-arrowRoot-uNr2A" aria-haspopup="true" aria-expanded="false"><div class="styles-arrow-uuBWa"><i class="style-vas-icon-g3NFP style-vas-icon_type-promoted-CTu39 style-vas-icon_size-xxs-UFxCO style-vas-icon_muted-dhTwO"></i></div></div><span data-resolver-terminal="true" hidden=""></span></div></div></div></div></div></div></div>`;
        activeCarsHtml += cardHtml;
      });
  }

  // Update counters
  const activeTabCounter = document.querySelector('[data-marker="extended_profile_tabs/tab(active)"] .styles-module-counter-uAip7');
  if (activeTabCounter && cars) activeTabCounter.innerText = cars.length;

  const completedTabCounter = document.querySelector('[data-marker="extended_profile_tabs/tab(closed)"] .styles-module-counter-uAip7');
  if (completedTabCounter) completedTabCounter.innerText = "12";

  // Init grid
  grid.innerHTML = activeCarsHtml;
  grid.id = 'cars-grid';

  // Setup Tabs
  const tabActive = document.querySelector('[data-marker="extended_profile_tabs/tab(active)"]');
  const tabClosed = document.querySelector('[data-marker="extended_profile_tabs/tab(closed)"]');
  
  if (tabActive && tabClosed) {
      tabActive.onclick = () => {
          tabActive.classList.add('styles-module-tab-button_active-mZotZ');
          tabActive.setAttribute('aria-selected', 'true');
          tabClosed.classList.remove('styles-module-tab-button_active-mZotZ');
          tabClosed.setAttribute('aria-selected', 'false');
          grid.innerHTML = activeCarsHtml;
      };
      
      tabClosed.onclick = () => {
          tabClosed.classList.add('styles-module-tab-button_active-mZotZ');
          tabClosed.setAttribute('aria-selected', 'true');
          tabActive.classList.remove('styles-module-tab-button_active-mZotZ');
          tabActive.setAttribute('aria-selected', 'false');
          grid.innerHTML = completedCarsHtml;
      };
  }
}
"""

    html = html[:start_idx] + new_logic + html[end_idx:]
    with open('clean_avito (1).html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Tabs updated successfully.")
else:
    print("Could not find loadCars function.")
