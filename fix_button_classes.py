import re

with open('produit-sac.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the double class attribute issue
# It currently looks like: <a href="javascript:void(0)" class="trigger-order" class="lp-btn-primary">
# or <a href="javascript:void(0)" class="trigger-order" class="lp-btn-secondary">

html = html.replace('class="trigger-order" class="lp-btn-primary"', 'class="lp-btn-primary trigger-order"')
html = html.replace('class="trigger-order" class="lp-btn-secondary"', 'class="lp-btn-secondary trigger-order"')

with open('produit-sac.html', 'w', encoding='utf-8') as f:
    f.write(html)
