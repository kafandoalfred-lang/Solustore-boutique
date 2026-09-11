import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <div class="features-grid"> with slider structure
content = content.replace('<div class="features-grid">', '''<div class="slider-container" id="catalogSlider">
                <button class="slider-btn slider-btn-prev" onclick="moveSlider(-1)"><i class="fa-solid fa-chevron-left"></i></button>
                <button class="slider-btn slider-btn-next" onclick="moveSlider(1)"><i class="fa-solid fa-chevron-right"></i></button>
                <div class="slider-track" id="sliderTrack">''')

# Close the slider track instead of features-grid
pattern = re.compile(r'</div>\s*</section>\s*<!-- Offre Duo -->', re.DOTALL)
content = pattern.sub('''</div>\n            </div>\n        </section>\n\n        <!-- Offre Duo -->''', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
