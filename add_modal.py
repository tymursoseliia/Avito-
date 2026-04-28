with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

modal_html_js = """            // 6. Add Custom Modal for "Под заказ"
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
                                <button style="background: #1a1a1a; color: white; border: none; border-radius: 8px; padding: 12px 24px; font-size: 15px; font-weight: 600; cursor: pointer;">Подробнее</button>
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
            }"""

if '// 6. Add Custom Modal for "Под заказ"' not in text:
    text = text.replace("// 4. Update Native Gallery", modal_html_js + "\n\n            // 4. Update Native Gallery")
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added modal logic")
else:
    print("Modal logic already exists")
