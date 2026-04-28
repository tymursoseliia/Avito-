with open('update_car_page.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_code = """            // 12. Telegram redirect for messages
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
            }"""

if old_code in text:
    text = text.replace(old_code, new_code)
    with open('update_car_page.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed telegram message logic to only send on send-button click")
else:
    print("Telegram logic not found")
