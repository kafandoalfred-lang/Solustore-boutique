import re

with open('produit-cat.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all case-insensitive "essentials" text
html = re.sub(r'ESSENTIALS', 'CAT', html, flags=re.IGNORECASE)

# Fix specific accents and titles
html = html.replace('SAC  DOS CAT', 'SAC À DOS CAT')
html = html.replace('SAC À DOS CAT', 'SAC À DOS CAT') 

# Replace image paths
html = re.sub(r'essentials-etudiant\.jpg', 'cat-sac-face.jpg', html)
html = re.sub(r'essentials-pluie\.jpg', 'cat-sac-profil.jpg', html)
html = re.sub(r'essentials-capacite\.jpg', 'cat-sac-details.jpg', html)
html = re.sub(r'essentials-etudiant-campus\.jpg', 'cat-sac-face.jpg', html)

# Replace old prices
html = html.replace('20 000 FCFA', '15 000 FCFA')

with open('produit-cat.html', 'w', encoding='utf-8') as f:
    f.write(html)
