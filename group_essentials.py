import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the 3 essentials cards with a single one
pattern = re.compile(r'<!-- Modèle 1 : Vert Kaki -->.*?<!-- Offre Duo -->', re.DOTALL)

single_essentials_card = '''<!-- Modèle Essentials Unique -->
                <div class="feature-card">
                    <div class="feature-image-wrapper">
                        <img src="essentials-poster-cyan.jpg" alt="Sac à dos Essentials">
                    </div>
                    <span class="badge-tag-minimal" style="background: rgba(30, 58, 138, 0.1); color: var(--primary-accent);">3 Couleurs Disponibles</span>
                    <h3>Sac à dos ESSENTIALS</h3>
                    <p>Design épuré, conception imperméable haute densité et compartiment matelassé pour votre ordinateur 15.6". L'excellence au quotidien.</p>
                    <div class="price-row">
                        <strong>12 500 FCFA</strong>
                        <a href="produit-sac.html" class="btn-outline" style="padding: 0.5rem 1.2rem; font-size: 0.85rem;">Découvrir</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Offre Duo -->'''

content = pattern.sub(single_essentials_card, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
