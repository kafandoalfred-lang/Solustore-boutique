import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Header Button
content = content.replace('<a href="produit-sac.html" class="btn-header">Voir les Sacs</a>', '<a href="#catalogue" class="btn-header">Voir nos Modèles</a>')

# 2. Update Hero Banner Text & Buttons
old_hero = '''<div class="poster-content">
                    <span class="badge-tag-minimal" style="width: fit-content; margin-bottom: 1rem;">Collection 2026</span>
                    <h2>Le compagnon de vos journées intenses.</h2>
                    <p class="subtitle">Sac à dos ESSENTIALS</p>
                    <p class="desc">Design épuré, conception imperméable haute densité et compartiment matelassé pour votre ordinateur 15.6". L'élégance minimaliste sans aucun compromis sur la solidité.</p>
                    
                    <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; margin-bottom: 2rem;">
                        <a href="produit-sac.html" class="btn-header" style="padding: 1rem 2rem;">Découvrir la collection</a>
                        <a href="#catalogue" class="btn-outline" style="padding: 1rem 2rem;">Voir les couleurs</a>
                    </div>
                </div>'''

new_hero = '''<div class="poster-content">
                    <span class="badge-tag-minimal" style="width: fit-content; margin-bottom: 1rem;">Boutique Officielle</span>
                    <h2>L'excellence au quotidien.</h2>
                    <p class="subtitle">Boutique SoluStore Burkina</p>
                    <p class="desc">Découvrez notre collection exclusive de sacs haut de gamme et d'équipements innovants. Livraison express gratuite et paiement à la livraison à Ouagadougou.</p>
                    
                    <div style="display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; margin-bottom: 2rem;">
                        <a href="#catalogue" class="btn-header" style="padding: 1rem 2rem;">Découvrir notre catalogue</a>
                    </div>
                </div>'''

# Re-read and write string replacement for hero
if old_hero in content:
    content = content.replace(old_hero, new_hero)
else:
    # Use regex if exact match fails
    hero_pattern = re.compile(r'<div class="poster-content">.*?</div>\s*</div>', re.DOTALL)
    content = hero_pattern.sub(new_hero + '\n            </div>', content, count=1)


# 3. Update Catalog Section Title
old_catalog = '''<div class="section-title">
                <h2>Les Éditions ESSENTIALS</h2>
                <p>Choisissez la teinte qui vous correspond. Chaque modèle bénéficie de la livraison gratuite sous 2h à Ouagadougou.</p>
            </div>'''
            
new_catalog = '''<div class="section-title">
                <h2>Notre Catalogue</h2>
                <p>Découvrez tous nos modèles disponibles. Chaque produit bénéficie de la livraison gratuite sous 2h à Ouagadougou.</p>
            </div>'''

if old_catalog in content:
    content = content.replace(old_catalog, new_catalog)
else:
    cat_pattern = re.compile(r'<div class="section-title">\s*<h2>Les Éditions ESSENTIALS</h2>.*?</p>\s*</div>', re.DOTALL)
    content = cat_pattern.sub(new_catalog, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
