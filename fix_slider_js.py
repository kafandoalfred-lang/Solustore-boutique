import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_logic = '''    const offset = -(currentSlide * (100 / visibleCards));
    sliderTrack.style.transform = 	ranslateX(%);'''
    
new_logic = '''    const cardWidth = cards[0].offsetWidth;
    const gap = 32; // 2rem
    const shift = (cardWidth + gap) * currentSlide;
    sliderTrack.style.transform = 	ranslateX(-px);'''

content = content.replace(old_logic, new_logic)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
