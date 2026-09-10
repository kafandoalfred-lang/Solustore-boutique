import re

files = ['produit-sac.html', 'produit-landkaidi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to remove quantity block
    q_pattern = re.compile(r'\s*<div class="form-group">\s*<label for="quantity">Quantité & Offres</label>\s*<div class="input-wrapper">\s*<i class="fa-solid fa-layer-group"></i>\s*<select id="quantity" name="quantity">.*?</select>\s*</div>\s*</div>', re.DOTALL)
    
    # regex to remove total block
    t_pattern = re.compile(r'\s*<div class="total-display">\s*<span>Total à régler :</span>\s*<strong id="totalPrice">.*?</strong>\s*</div>', re.DOTALL)
    
    content = q_pattern.sub('', content)
    content = t_pattern.sub('', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
