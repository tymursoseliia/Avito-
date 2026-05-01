
    const supabaseUrl = 'https://yjhjthhirxjxkbokycat.supabase.co';
    const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlqaGp0aGhpcnhqeGtib2t5Y2F0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzY5NDQ4MjcsImV4cCI6MjA5MjUyMDgyN30.yXO_zbZgTT-oAJOkvnPsrF_YLnK49Cbpl7sn8ioFvOg';
    const supabaseClient = supabase.createClient(supabaseUrl, supabaseKey);

    function formatPrice(price) {
        return price ? price.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ") : "0";
    }

    async function loadCarDetails() {
        const urlParams = new URLSearchParams(window.location.search);
        const carId = urlParams.get('id');
        
        if (!carId) {
            document.body.style.opacity = '1';
            return;
        }

        try {
            const { data: car, error } = await supabaseClient.from('cars').select('*').eq('id', carId).single();
            if (error || !car) {
                console.error('Car not found', error);
                document.body.style.opacity = '1';
                return;
            }

            // 1. Update Title & Price
            document.title = car.title + ' - Купить в ' + (car.location || 'Москве') + ' | Авито';
            
            const titleEl = document.querySelector('[data-marker="item-view/title-info"]');
            if (titleEl) titleEl.innerHTML = car.title;

            const priceEls = document.querySelectorAll('[data-marker="item-view/item-price"]');
            priceEls.forEach(priceEl => {
                priceEl.setAttribute('content', car.price);
                priceEl.innerHTML = formatPrice(car.price) + '&nbsp;₽';
            });

            // 2. Update Characteristics (Year, Mileage)
            const listItems = document.querySelectorAll('li');
            listItems.forEach(li => {
                if (li.textContent.includes('Год выпуска') && car.year) {
                    if (li.innerHTML.includes('2026')) {
                         li.innerHTML = li.innerHTML.replace('2026', car.year);
                    } else {
                         li.childNodes.forEach(node => {
                             if(node.nodeType === 3 && node.textContent.trim().length > 0) {
                                 node.textContent = car.year;
                             }
                         });
                    }
                }
                if (li.textContent.includes('Пробег') && car.mileage) {
                    if (li.innerHTML.includes('1 км') || li.innerHTML.includes('1&nbsp;км')) {
                         li.innerHTML = li.innerHTML.replace(/1(?:&nbsp;|\s)км/, `${car.mileage} км`);
                    } else {
                         li.childNodes.forEach(node => {
                             if(node.nodeType === 3 && node.textContent.trim().length > 0) {
                                 node.textContent = `${car.mileage} км`;
                             }
                         });
                    }
                }
            });

            // 3. Update Breadcrumbs
            const breadcrumbItems = document.querySelectorAll('[data-marker="breadcrumbs"] span[itemprop="itemListElement"]');
            breadcrumbItems.forEach(item => {
                const text = item.textContent;
                if (text.includes('Zeekr') || text.includes('8X')) {
                    item.remove();
                }
            });
            
            // Also update the last breadcrumb to the car title
            const breadcrumbs = document.querySelectorAll('[data-marker="breadcrumbs"] a, [data-marker="breadcrumbs"] span');
            if (breadcrumbs.length >= 2) {
                const lastBreadcrumb = breadcrumbs[breadcrumbs.length - 1];
                if (lastBreadcrumb) {
                    lastBreadcrumb.textContent = car.title;
                }
            }
            
            // Redirect breadcrumb links to the main catalog
            const breadcrumbLinks = document.querySelectorAll('[data-marker="breadcrumbs"] a');
            breadcrumbLinks.forEach(link => {
                link.href = 'clean_avito (1).html';
            });
            
            
            // Update Specifications
            const specHeaders = Array.from(document.querySelectorAll('h2')).filter(h2 => h2.textContent.includes('Характеристики'));
            if (specHeaders.length > 0) {
                const specUl = specHeaders[0].nextElementSibling;
                if (specUl && specUl.tagName === 'UL') {
                    // Start building HTML based on car properties
                    let html = '';
                    
                    const specMapping = [
                        { key: 'year', label: 'Год выпуска', val: car.year },
                        { key: 'mileage', label: 'Пробег', val: car.mileage ? car.mileage + ' км' : '' }
                    ];
                    
                    if (car.specs) {
                        const s = car.specs;
                        if (s.generation) specMapping.push({ label: 'Поколение', val: s.generation });
                        if (s.pts) specMapping.push({ label: 'ПТС', val: s.pts });
                        if (s.condition) specMapping.push({ label: 'Состояние', val: s.condition });
                        if (s.modification) specMapping.push({ label: 'Модификация', val: s.modification });
                        if (s.engine_volume) specMapping.push({ label: 'Объём двигателя', val: s.engine_volume });
                        if (s.engine_type) specMapping.push({ label: 'Тип двигателя', val: s.engine_type });
                        if (s.transmission) specMapping.push({ label: 'Коробка передач', val: s.transmission });
                        if (s.drive) specMapping.push({ label: 'Привод', val: s.drive });
                        if (s.equipment) specMapping.push({ label: 'Комплектация', val: s.equipment });
                        if (s.body_type) specMapping.push({ label: 'Тип кузова', val: s.body_type });
                        if (s.color) specMapping.push({ label: 'Цвет', val: s.color });
                        if (s.wheel) specMapping.push({ label: 'Руль', val: s.wheel });
                        if (s.vin) specMapping.push({ label: 'VIN или номер кузова', val: s.vin });
                    }
                    
                    specMapping.forEach(item => {
                        if (item.val) {
                            html += `<li class="d2936d013c910379"><span class="d6e8fd2e3d52b32a">${item.label}<span>: </span></span>${item.val}</li>`;
                        }
                    });
                    
                    specUl.innerHTML = html;
                }
            }

            // 5. Update Header Links
            const topLinks = document.querySelectorAll('a');
            topLinks.forEach(a => {
                

                if (a.textContent.includes('#яПомогаю')) {
                    a.href = 'https://www.avito.ru/avito-care/crisis-help?from=mp_header';
                    a.target = '_blank';
                }
            });

                        // 6. Add Custom Modal for "Под заказ"
            const badges = document.querySelectorAll('[data-marker="badge-2232"]');
            if (badges.length > 0) {
                // Create modal HTML if it doesn't exist
                if (!document.getElementById('custom-order-modal')) {
                    const modalHTML = `
                        <div id="custom-order-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 10000; align-items: center; justify-content: center;">
                            <div style="background: white; border-radius: 16px; padding: 32px; max-width: 400px; width: 90%; position: relative; font-family: 'Manrope', sans-serif;">
                                <button id="custom-order-modal-close" style="position: absolute; top: 16px; right: 16px; background: none; border: none; font-size: 24px; cursor: pointer; color: #000;">&times;</button>
                                <h2 style="font-size: 24px; font-weight: 700; margin-bottom: 16px; margin-top: 0;">Под заказ</h2>
                                <p style="font-size: 15px; line-height: 1.5; color: #000; margin-bottom: 24px;">Автомобиль привезут из другой страны, поэтому цена и сроки могут увеличиться без вашего согласия.</p>
                                <button onclick="window.open('https://www.avito.ru/journal/articles/kak-kupit-avto-na-zakaz-iz-drugoy-strany', '_blank')" style="background: #1a1a1a; color: white; border: none; border-radius: 8px; padding: 12px 24px; font-size: 15px; font-weight: 600; cursor: pointer;">Подробнее</button>
                            </div>
                        </div>
                    `;
                    document.body.insertAdjacentHTML('beforeend', modalHTML);
                    
                    const modal = document.getElementById('custom-order-modal');
                    const closeBtn = document.getElementById('custom-order-modal-close');
                    
                    closeBtn.addEventListener('click', () => {
                        modal.style.display = 'none';
                    });
                    
                    modal.addEventListener('click', (e) => {
                        if (e.target === modal) {
                            modal.style.display = 'none';
                        }
                    });
                }
                
                // Attach click listener to all badges
                badges.forEach(badge => {
                    badge.style.cursor = 'pointer';
                    badge.addEventListener('click', () => {
                        document.getElementById('custom-order-modal').style.display = 'flex';
                    });
                });
            }

            
            // 7. Redirect Seller Ads Button
            function getPlural(number, one, two, five) {
                let n = Math.abs(number);
                n %= 100;
                if (n >= 5 && n <= 20) return five;
                n %= 10;
                if (n === 1) return one;
                if (n >= 2 && n <= 4) return two;
                return five;
            }

            const { count, error: countError } = await supabaseClient
                .from('cars')
                .select('*', { count: 'exact', head: true });
            
            let totalAds = count || 0;
            let adsText = `${totalAds} ${getPlural(totalAds, 'объявление', 'объявления', 'объявлений')} пользователя`;

            const allLinks = document.querySelectorAll('a');
            allLinks.forEach(link => {
                if (link.textContent && (link.textContent.includes('объявлени') || link.textContent.includes('пользователя'))) {
                    // Check if it's the specific seller ads button
                    if (link.classList.contains('css-1cm6pik') || link.textContent.includes('65')) {
                        link.href = 'clean_avito (1).html';
                        const span = link.querySelector('span');
                        if (span) {
                            span.textContent = adsText;
                        } else {
                            link.textContent = adsText;
                        }
                    }
                }
            });

            
            // 8. Fix Basta Ad Link
            const adTitles = document.querySelectorAll('strong');
            adTitles.forEach(el => {
                if (el.textContent && (el.textContent.includes('БАСТА') || el.textContent.includes('СИНЕРГИЯ'))) {
                    // Find the closest ad container (go up ~4 levels)
                    let container = el;
                    for (let i = 0; i < 4; i++) {
                        if (container.parentElement && container.parentElement.tagName !== 'BODY') {
                            container = container.parentElement;
                        }
                    }
                    
                    // Make the container clickable
                    container.style.cursor = 'pointer';
                    container.onclick = function(e) {
                        e.preventDefault();
                        e.stopPropagation();
                        window.open('https://xn--80aac8afrzi0cyb.xn--p1ai/?aviclid=c4095ce4-7c11-44ca-ab0b-e6bcc84d98ab&marketer=zvv&produkt=393998515&utm_campaign=202604204&utm_gen=3&utm_medium=cpc&utm_source=avito-ads&utm_term=basta_s_textom_capitals', '_blank');
                    };
                }
            });

            
            // 9. Replace Company Name and Logo
            // Replace text
            const allElementsText = document.querySelectorAll('a, p, span, div');
            allElementsText.forEach(el => {
                if (el.children.length === 0 && el.textContent) {
                    if (el.textContent.includes('Автомиг')) {
                        el.textContent = el.textContent.replace(/Автомиг/g, 'Автомиг');
                    }
                    if (el.textContent.includes('Газтормоз')) {
                        el.textContent = el.textContent.replace(/Газтормоз/g, 'Автомиг');
                    }
                    if (el.textContent.includes('ГазТормоз')) {
                        el.textContent = el.textContent.replace(/ГазТормоз/g, 'Автомиг');
                    }
                }
            });

            // Replace logo
            // The gaztormoz logo is usually a specific img tag
            const allImages = document.querySelectorAll('img');
            allImages.forEach(img => {
                if (img.src && (img.src.includes('avatar') || img.src.includes('logo') || img.src.includes('gaztormoz') || img.src === 'https://40.img.avito.st/image/1/1.k0QhGba102vP29z7NIf2E26_021P01z.p9tI3XW5mJ_B_8zFQQHkOOTa7M54qK2w2R2B6U99oKk' || img.src.includes('k0QhGba102vP29z7NIf2E26_021P01z.p9tI3XW5mJ_B_8zFQQHkOOTa7M54qK2w2R2B6U99oKk'))) {
                    // Let's replace the avatar/logo with Avtomig's logo
                    // Avtomig logo is logo.jpg
                    if (img.parentElement && img.parentElement.tagName === 'DIV' && img.parentElement.classList.contains('_9275a4968c2dc72b')) {
                        // This is likely the seller avatar wrapper or near it
                    }
                }
            });
            
            // Just specifically target the seller logo image
            // We can look for the seller link href
            const sellerLinks = document.querySelectorAll('a[href*="gaztormoz"]');
            sellerLinks.forEach(link => {
                // If it contains an image, it's the logo link
                const img = link.querySelector('img');
                if (img) {
                    img.src = 'logo.jpg';
                    // also fix style to ensure it fits well
                    img.style.objectFit = 'cover';
                    img.style.borderRadius = '50%';
                }
            });


            
            // 10. Replace avatar backgrounds
            const allDivs = document.querySelectorAll('div, span');
            allDivs.forEach(div => {
                const bg = div.style.backgroundImage;
                if (bg && (bg.includes('gaztormoz') || bg.includes('54F-uLa4S2hIEYltPNug80IYSW7AGclgCBxJas4RQ2LI'))) {
                    div.style.backgroundImage = 'url("logo.jpg")';
                }
            });

            
            // 11. Force avatar replace
            // Revert to a much safer approach: just change the background of the existing A tag
            const avatarLinks = document.querySelectorAll('[data-marker="seller-info/avatar-link"]');
            avatarLinks.forEach(link => {
                // The link is already perfectly sized and rounded by Avito's CSS
                link.style.backgroundImage = 'url("logo.jpg")';
                link.style.backgroundSize = '70%'; // Make the logo slightly smaller inside the circle
                link.style.backgroundPosition = 'center';
                link.style.backgroundRepeat = 'no-repeat';
                link.style.backgroundColor = 'white';
                
                // Remove any inner text or images that might interfere
                link.innerHTML = '';
            });

            
            // 12. Telegram redirect for messages
            const tgUsername = 'Automigsup';
            const textarea = document.querySelector('[data-marker="icebreakers/textarea"]');
            
            // Handle quick replies
            const quickReplies = document.querySelectorAll('[data-marker^="icebreakers/icebreaker-"]');
            quickReplies.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const msgText = btn.textContent.trim();
                    
                    // ONLY update the textarea, do NOT redirect yet.
                    if (textarea) {
                        textarea.value = msgText;
                    }
                }, true);
            });
            
            // Handle the send button
            const sendBtnMarker = document.querySelector('[data-marker="icebreakers/send-message"]');
            if (sendBtnMarker) {
                let sendBtn = sendBtnMarker.closest('div');
                if (!sendBtn) sendBtn = sendBtnMarker;
                
                sendBtn.style.cursor = 'pointer';
                sendBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    let msgText = textarea ? textarea.value.trim() : '';
                    
                    // Fallback to placeholder or inner text if value is empty
                    if (!msgText && textarea) {
                        msgText = textarea.placeholder || textarea.textContent.trim();
                    }
                    
                    if (msgText) {
                        window.open(`https://t.me/${tgUsername}?text=${encodeURIComponent(msgText)}`, '_blank');
                    }
                }, true);
            }


            // 4. Update Native Gallery
            const galleryImages = car.image_urls && car.image_urls.length > 0 ? car.image_urls : [car.image_url];
            if (galleryImages.length > 0 && galleryImages[0]) {
                const galleryEl = document.querySelector('[data-marker="item-view/gallery"]');
                if (galleryEl) {
                    const mainImgWrap = galleryEl.querySelector('[data-marker="image-frame/image-wrapper"]');
                    const thumbnails = galleryEl.querySelectorAll('[data-marker="image-preview/item"]');
                    
                    let currentIndex = 0;
                    
                    function setMainImage(idx) {
                        currentIndex = idx;
                        const url = galleryImages[idx];
                        if(!url) return;
                        if (mainImgWrap) {
                            const span = mainImgWrap.querySelector('span');
                            if (span) span.style.backgroundImage = `url("${url}")`;
                            const img = mainImgWrap.querySelector('img');
                            if (img) { img.src = url; img.removeAttribute("srcset"); }
                        }
                        
                        thumbnails.forEach((th, i) => {
                            if (i === idx) {
                                th.style.opacity = '1';
                                th.style.border = '2px solid #00AAFF';
                            } else {
                                th.style.opacity = '0.5';
                                th.style.border = 'none';
                            }
                        });
                    }

                    thumbnails.forEach((th, idx) => {
                        if (galleryImages[idx]) {
                            const span = th.querySelector('span');
                            if (span) span.style.backgroundImage = `url("${galleryImages[idx]}")`;
                            const img = th.querySelector('img');
                            if (img) { img.src = galleryImages[idx]; img.removeAttribute("srcset"); }
                             
                            
                            th.onclick = function(e) {
                                e.preventDefault();
                                e.stopPropagation();
                                setMainImage(idx);
                            };
                        } else {
                            th.remove();
                        }
                    });

                    setMainImage(0);

                    const leftBtn = galleryEl.querySelector('[data-marker="image-frame/left-button"]');
                    const rightBtn = galleryEl.querySelector('[data-marker="image-frame/right-button"]');
                    
                    if (leftBtn) {
                        leftBtn.onclick = function(e) {
                            e.preventDefault();
                            e.stopPropagation();
                            let newIdx = currentIndex - 1;
                            if (newIdx < 0) {
                                newIdx = Math.min(thumbnails.length - 1, galleryImages.length - 1);
                            }
                            setMainImage(newIdx);
                        }
                    }
                    if (rightBtn) {
                        rightBtn.onclick = function(e) {
                            e.preventDefault();
                            e.stopPropagation();
                            let newIdx = currentIndex + 1;
                            if (newIdx >= galleryImages.length || newIdx >= thumbnails.length) newIdx = 0;
                            setMainImage(newIdx);
                        }
                    }
                }
            }
        } catch (err) {
            console.error(err);
        } finally {

            // Replace description
            if (car.description) {
                const descEl = document.querySelector('[data-marker="item-view/item-description"] p');
                if (descEl) {
                    descEl.innerHTML = car.description.replace(/
/g, '<br>');
                } else {
                    const descContainer = document.querySelector('[data-marker="item-view/item-description"]');
                    if (descContainer) {
                        descContainer.innerHTML = `<p>${car.description.replace(/
/g, '<br>')}</p>`;
                    }
                }
            }

            // Unhide the body when everything is loaded
            document.body.style.opacity = '1';
            const styleTag = document.getElementById('dynamic-hide');
            if (styleTag) styleTag.remove();
        }
    }
    

    async function loadCompanyProfile() {
        const { data, error } = await supabaseClient.from('company_profile').select('*').eq('id', 1).single();
        if (error || !data) return;
        
        // Replace name
        const allElementsText = document.querySelectorAll('a, p, span, div, h1, h2, h3, h4, h5');
        allElementsText.forEach(el => {
            if (el.children.length === 0 && el.textContent) {
                if (el.textContent.includes('Автомиг')) el.textContent = el.textContent.replace(/Автомиг/g, data.name || 'Автомиг');
                if (el.textContent.includes('Автомиг')) el.textContent = el.textContent.replace(/Автомиг/g, data.name || 'Автомиг');
                if (el.textContent.includes('Газтормоз')) el.textContent = el.textContent.replace(/Газтормоз/g, data.name || 'Автомиг');
            }
        });

        // Replace rating & reviews if they exist near seller block
        const ratingEls = document.querySelectorAll('.seller-info-rating-M0A3b, .seller-info-ratingScore-qWvGz');
        ratingEls.forEach(el => el.textContent = data.rating || '5,0');

        // Replace logo
        if (data.logo_url) {
            const avatarLink = document.querySelector('[data-marker="seller-info/avatar-link"]');
            if (avatarLink) {
                avatarLink.innerHTML = `<img src="${data.logo_url}" style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">`;
            }
            
            // Re-run the logo patch for <img> tags
            const allImages = document.querySelectorAll('img');
            allImages.forEach(img => {
                if (img.src && (img.src.includes('avatar') || img.src.includes('logo') || img.src.includes('gaztormoz') || img.src === 'https://40.img.avito.st/image/1/1.k0QhGba102vP29z7NIf2E26_021P01z.p9tI3XW5mJ_B_8zFQQHkOOTa7M54qK2w2R2B6U99oKk')) {
                    if (img.parentElement && img.parentElement.tagName === 'DIV' && img.parentElement.classList.contains('_9275a4968c2dc72b')) {
                        img.src = data.logo_url;
                    }
                }
            });
        }
        
        // About photos
        const aboutSection = document.getElementById('about_v2');
        if (aboutSection && data.about_photos && data.about_photos.length > 0) {
            let galleryHtml = '<div style="display:flex; overflow-x:auto; gap:10px; margin-top:20px; padding-bottom:10px;">';
            data.about_photos.forEach(url => {
                galleryHtml += `<img src="${url}" style="height:200px; border-radius:8px; object-fit:cover; flex-shrink: 0;">`;
            });
            galleryHtml += '</div>';
            
            if (!document.getElementById('dynamic-about-gallery')) {
                const galleryWrapper = document.createElement('div');
                galleryWrapper.id = 'dynamic-about-gallery';
                galleryWrapper.innerHTML = galleryHtml;
                aboutSection.appendChild(galleryWrapper);
            }
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => { loadCarDetails(); loadCompanyProfile(); });
    } else {
        loadCarDetails();
        loadCompanyProfile();
    }

