import re

with open('produit-cat.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('CAT-etudiant.jpg', 'cat-sac-face.jpg')

with open('produit-cat.html', 'w', encoding='utf-8') as f:
    f.write(html)
