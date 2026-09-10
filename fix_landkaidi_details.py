import re

with open('produit-landkaidi.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Gallery
gallery_pattern = re.compile(r'<div class="gallery-thumbnails">.*?</div>', re.DOTALL)
new_gallery = '''<div class="gallery-thumbnails">
                        <img src="landkaidi-dimensions.jpg" alt="Dimensions du sac Landkaidi" class="thumbnail active" onclick="changeImage('landkaidi-dimensions.jpg', this)">
                        <img src="landkaidi-vert.jpg" alt="Sac LANDKAIDI Vert Olive" class="thumbnail" onclick="changeImage('landkaidi-vert.jpg', this)">
                        <img src="landkaidi-dos.jpg" alt="Sac LANDKAIDI Dos Renforcé" class="thumbnail" onclick="changeImage('landkaidi-dos.jpg', this)">
                        <img src="landkaidi-rose.jpg" alt="Sac LANDKAIDI Rose" class="thumbnail" onclick="changeImage('landkaidi-rose.jpg', this)">
                    </div>'''
content = gallery_pattern.sub(new_gallery, content)

# 2. Update Colors
color_pattern = re.compile(r'<select id="color" name="color" required>.*?</select>', re.DOTALL)
new_colors = '''<select id="color" name="color" required>
                                        <option value="Vert Olive" selected>Vert Olive</option>
                                        <option value="Kaki">Kaki</option>
                                    </select>'''
content = color_pattern.sub(new_colors, content)

# 3. Update Price display
price_pattern = re.compile(r'<div class="price-container">\s*<span class="price-new">10 000 FCFA</span>\s*<span class="price-old">20 000 FCFA</span>\s*</div>', re.DOTALL)
new_price = '''<div class="price-container" style="display: flex; flex-direction: column; align-items: flex-start; gap: 0.5rem; margin-bottom: 1.5rem; background: rgba(5, 150, 105, 0.05); padding: 1rem; border-radius: 12px; border-left: 5px solid var(--success-color);">
                        <div style="display: flex; align-items: baseline; gap: 1rem;">
                            <span class="price-new" style="font-size: 3rem; color: var(--primary-color); font-weight: 900; line-height: 1;">10 000 FCFA</span>
                            <span class="price-old" style="font-size: 1.2rem;">20 000 FCFA</span>
                        </div>
                        <div style="display: inline-flex; align-items: center; gap: 0.5rem; background: var(--success-color); color: white; padding: 0.4rem 1rem; border-radius: 50px; font-weight: bold; font-size: 1rem; margin-top: 0.5rem;">
                            <i class="fa-solid fa-truck-fast"></i> Livraison 100% Gratuite
                        </div>
                    </div>'''
content = price_pattern.sub(new_price, content)

with open('produit-landkaidi.html', 'w', encoding='utf-8') as f:
    f.write(content)
