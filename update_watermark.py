import re

with open('admin.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_watermark = '''                    // Рисуем водяной знак Авито
                    const padding = img.width * 0.05;
                    const fontSize = Math.max(img.width * 0.08, 20);
                    
                    ctx.fillStyle = 'rgba(255, 255, 255, 0.7)';
                    ctx.font = `bold ${fontSize}px Manrope, Arial`;
                    const text = "Авито";
                    const textWidth = ctx.measureText(text).width;
                    const textHeight = fontSize;
                    
                    const rectWidth = textWidth + padding;
                    const rectHeight = textHeight + padding;
                    
                    const rectX = img.width - rectWidth - padding;
                    const rectY = img.height - rectHeight - padding;
                    
                    ctx.beginPath();
                    ctx.roundRect(rectX, rectY, rectWidth, rectHeight, fontSize * 0.3);
                    ctx.fill();
                    
                    ctx.fillStyle = '#00AAFF';
                    ctx.textBaseline = 'middle';
                    ctx.fillText(text, rectX + padding/2, rectY + rectHeight/2 + fontSize * 0.1);'''

new_watermark = '''                    // Оригинальный водяной знак Авито (4 круга + текст)
                    const scale = Math.max(img.width / 1000, 0.3); // Масштаб относительно размера фото
                    const padding = img.width * 0.03;
                    
                    // Радиусы кругов
                    const rCenter = 12 * scale;
                    const rTop = 5 * scale;
                    const rBottomLeft = 6.5 * scale;
                    const rBottomRight = 8.5 * scale;
                    
                    const logoWidth = rCenter * 2.5;
                    
                    ctx.font = `bold ${50 * scale}px Manrope, Arial`;
                    const text = "Avito";
                    const textWidth = ctx.measureText(text).width;
                    
                    // Высчитываем правый нижний угол
                    const startX = img.width - logoWidth - textWidth - padding * 2;
                    const startY = img.height - rCenter * 3 - padding;
                    
                    const cx = startX + rCenter * 1.5;
                    const cy = startY + rCenter * 1.5;
                    
                    ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
                    
                    // Тень для читаемости на любых фото
                    ctx.shadowColor = 'rgba(0, 0, 0, 0.4)';
                    ctx.shadowBlur = 6 * scale;
                    ctx.shadowOffsetX = 1 * scale;
                    ctx.shadowOffsetY = 2 * scale;
                    
                    // Центральный круг
                    ctx.beginPath();
                    ctx.arc(cx - rCenter * 0.5, cy, rCenter, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Верхний круг
                    ctx.beginPath();
                    ctx.arc(cx - rCenter * 0.8, cy - rCenter * 1.1, rTop, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Нижний левый круг
                    ctx.beginPath();
                    ctx.arc(cx - rCenter * 1.6, cy + rCenter * 0.9, rBottomLeft, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Нижний правый круг
                    ctx.beginPath();
                    ctx.arc(cx + rCenter * 0.4, cy + rCenter * 1.1, rBottomRight, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // Текст
                    ctx.textBaseline = 'middle';
                    ctx.fillText(text, startX + logoWidth + 8 * scale, cy + rCenter * 0.2);
                    
                    // Сбрасываем тень
                    ctx.shadowColor = 'transparent';'''

if old_watermark in content:
    content = content.replace(old_watermark, new_watermark)
    with open('admin.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Watermark updated!')
else:
    print('Could not find old watermark logic')
