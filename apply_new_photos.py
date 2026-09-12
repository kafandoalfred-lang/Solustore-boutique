import re

with open('produit-sac.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Hero Image
html = html.replace('src="essentials-etudiant.jpg"', 'src="essentials-etudiant-campus.jpg"')

# 2. Update Benefit 1 (Rain resistance)
html = html.replace('src="sac_dos_details_1788628077455.jpg"', 'src="essentials-pluie.jpg"')

# 3. Update Capacity Placeholder
old_placeholder = '<div class="lp-placeholder-img" style="margin-top: 1.5rem;">\\n                <span>[Photo du sac rempli - À venir]</span>\\n            </div>'
new_capacity_img = '<div style="margin-top: 1.5rem;">\\n                <img src="essentials-capacite.jpg" alt="Vue intérieure sac rempli" style="width:100%; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); display:block;">\\n            </div>'
html = html.replace(old_placeholder, new_capacity_img)
html = html.replace('<div class="lp-placeholder-img" style="margin-top: 1.5rem;">\n                <span>[Photo du sac rempli - À venir]</span>\n            </div>', new_capacity_img)

# 4. Add to gallery (if we can find the gallery-thumbnails div)
gallery_end = '</div>\\n            </div>\\n            \\n            <!-- Placeholders'
new_thumbs = '''
                    <img src="essentials-etudiant-campus.jpg" class="thumbnail" onclick="changeImage('essentials-etudiant-campus.jpg', this)">
                    <img src="essentials-pluie.jpg" class="thumbnail" onclick="changeImage('essentials-pluie.jpg', this)">
                    <img src="essentials-capacite.jpg" class="thumbnail" onclick="changeImage('essentials-capacite.jpg', this)">
'''
# I'll just append it to the gallery-thumbnails block using regex
gallery_pattern = r'(<div class="gallery-thumbnails">.*?)(</div>\s*</div>\s*<!-- Placeholders)'
match = re.search(gallery_pattern, html, re.DOTALL)
if match:
    updated_gallery = match.group(1) + new_thumbs + match.group(2)
    html = html.replace(match.group(0), updated_gallery)

with open('produit-sac.html', 'w', encoding='utf-8') as f:
    f.write(html)
