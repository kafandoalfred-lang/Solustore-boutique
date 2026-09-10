import re

files = ['produit-sac.html', 'produit-landkaidi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to match the city block
    city_pattern = re.compile(r'\s*<div class="form-group">\s*<label for="city">Ville & Quartier \(Adresse de livraison\)</label>\s*<div class="input-wrapper">\s*<i class="fa-solid fa-location-dot"></i>\s*<input type="text" id="city" name="city" placeholder="Ex: Ouagadougou, Zone 1" required>\s*</div>\s*</div>', re.DOTALL)
    
    replacement = '''
                            <div class="info-message" style="background: rgba(30, 58, 138, 0.1); padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem; text-align: center; border: 1px dashed rgba(30, 58, 138, 0.3);">
                                <i class="fa-solid fa-truck" style="color: var(--primary-accent); margin-bottom: 0.5rem; font-size: 1.2rem;"></i>
                                <p style="font-size: 0.9rem; font-weight: 500; margin: 0; color: var(--text-color);">Une personne de l'équipe vous contactera pour organiser la livraison.</p>
                            </div>'''
                            
    content = city_pattern.sub(replacement, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
