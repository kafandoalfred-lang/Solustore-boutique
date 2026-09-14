import re

with open('produit-cat.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Titles and Meta
html = html.replace('Sac à Dos ESSENTIALS', 'Sac à Dos CAT')
html = html.replace('Sac à dos officiel ESSENTIALS', 'Sac à dos CAT très résistant en tissu Jean')
html = html.replace('sac-essentials', 'sac-cat')
html = html.replace('12500', '10000')
html = html.replace('12.500', '10.000')
html = html.replace('12 500', '10 000')

# Replace Images in Gallery
gallery_pattern = r'<div class="gallery-thumbnails">.*?</div>'
new_gallery = '''<div class="gallery-thumbnails">
                    <img src="cat-sac-face.jpg" class="thumbnail active" onclick="changeImage('cat-sac-face.jpg', this)">
                    <img src="cat-sac-profil.jpg" class="thumbnail" onclick="changeImage('cat-sac-profil.jpg', this)">
                    <img src="cat-sac-details.jpg" class="thumbnail" onclick="changeImage('cat-sac-details.jpg', this)">
                </div>'''
html = re.sub(gallery_pattern, new_gallery, html, flags=re.DOTALL)

# Main Image
html = re.sub(r'src="essentials-vert-nouveau.jpg"', 'src="cat-sac-face.jpg"', html)

# Description and Features
features_pattern = r'<div class="tab-pane active" id="tab-description">.*?</div>'
new_features = '''<div class="tab-pane active" id="tab-description">
                        <h3>Détails du Produit</h3>
                        <p>Le <strong>Sac à Dos CAT</strong> est conçu pour la durabilité et le voyage. Assez gros pour vos déplacements, il offre une protection maximale et un style unique avec son tissu en jean très résistant.</p>
                        <ul class="features-list">
                            <li><i class="fa-solid fa-check text-green"></i> <strong>Tissu en Jean</strong> ultra-résistant</li>
                            <li><i class="fa-solid fa-check text-green"></i> <strong>Grande Capacité</strong> idéal pour voyager</li>
                            <li><i class="fa-solid fa-check text-green"></i> <strong>Cadenas à code</strong> intégré pour la sécurité</li>
                            <li><i class="fa-solid fa-check text-green"></i> <strong>Poches Multiples</strong> pour une organisation optimale</li>
                        </ul>
                    </div>'''
html = re.sub(features_pattern, new_features, html, flags=re.DOTALL)

with open('produit-cat.html', 'w', encoding='utf-8') as f:
    f.write(html)
