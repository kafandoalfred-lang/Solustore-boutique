import re

with open('produit-cat.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('CAT-capacite.jpg', 'cat-sac-interieur.jpg')

with open('produit-cat.html', 'w', encoding='utf-8') as f:
    f.write(html)
