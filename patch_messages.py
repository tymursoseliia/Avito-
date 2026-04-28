with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

js_addition = """
            // 12. Telegram redirect for messages
            const tgUsername = 'Automigsup';
            
            // Handle quick replies
            const quickReplies = document.querySelectorAll('[data-marker^="icebreakers/icebreaker-"]');
            quickReplies.forEach(btn => {
                // Remove existing click handlers if possible by replacing clone, but simpler is to use capture
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const msgText = btn.textContent.trim();
                    window.open(`https://t.me/${tgUsername}?text=${encodeURIComponent(msgText)}`, '_blank');
                }, true);
            });
            
            // Handle the send button
            const sendBtnMarker = document.querySelector('[data-marker="icebreakers/send-message"]');
            if (sendBtnMarker) {
                // The actual clickable area might be the parent wrapper
                let sendBtn = sendBtnMarker.closest('div');
                if (!sendBtn) sendBtn = sendBtnMarker;
                
                // Also make the textarea trigger it on Enter if we want, but a click is enough for now
                sendBtn.style.cursor = 'pointer';
                sendBtn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const textarea = document.querySelector('[data-marker="icebreakers/textarea"]');
                    let msgText = textarea ? textarea.value.trim() : '';
                    if (!msgText) {
                        msgText = textarea ? textarea.placeholder : '';
                    }
                    if (msgText) {
                        window.open(`https://t.me/${tgUsername}?text=${encodeURIComponent(msgText)}`, '_blank');
                    }
                }, true);
            }
"""

if '// 12. Telegram redirect for messages' not in text:
    text = text.replace("// 4. Update Native Gallery", js_addition + "\n\n            // 4. Update Native Gallery")
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Added Telegram message redirect logic")
else:
    print("Telegram logic already exists")
