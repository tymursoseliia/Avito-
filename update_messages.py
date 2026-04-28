with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """            // 12. Telegram redirect for messages
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
            }"""

new_code = """            // 12. Telegram redirect for messages
            const tgUsername = 'Automigsup';
            const textarea = document.querySelector('[data-marker="icebreakers/textarea"]');
            
            // Handle quick replies
            const quickReplies = document.querySelectorAll('[data-marker^="icebreakers/icebreaker-"]');
            quickReplies.forEach(btn => {
                btn.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const msgText = btn.textContent.trim();
                    
                    // Update the textarea visually first
                    if (textarea) {
                        textarea.value = msgText;
                    }
                    
                    // Small delay to let the user see the text change before redirecting
                    setTimeout(() => {
                        window.open(`https://t.me/${tgUsername}?text=${encodeURIComponent(msgText)}`, '_blank');
                    }, 300);
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
            }"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed telegram message logic to update textarea first")
else:
    print("Telegram logic not found")
