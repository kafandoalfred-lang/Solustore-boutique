import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the whole section from <section class="features-section" id="catalogue"> to <!-- Offre Duo -->
pattern = re.compile(r'<section class="features-section" id="catalogue">.*?<!-- Offre Duo -->', re.DOTALL)

new_section = '''<section class="features-section" id="catalogue">
            <div class="section-title">
                <h2>Notre Catalogue</h2>
                <p>Découvrez tous nos modèles disponibles. Chaque produit bénéficie de la livraison gratuite sous 2h à Ouagadougou.</p>
            </div>

            <div class="features-grid">
                <!-- Modèle Landkaidi Dynamique -->
                <div class="feature-card dynamic-card" id="card-landkaidi">
                    <div class="feature-image-wrapper">
                        <img src="landkaidi-vert.jpg" alt="Sac à dos Landkaidi" class="dyn-img fade-in">
                    </div>
                    <span class="badge-tag-minimal dyn-badge" style="background: rgba(5, 150, 105, 0.1); color: var(--success-color);">Tissu Jean Très Résistant</span>
                    <h3 class="dyn-title fade-in">LANDKAIDI : Vert Olive</h3>
                    <p class="dyn-desc fade-in">Dos renforcé ultra confortable. Idéal pour voyager avec vos habits et votre ordinateur 15.6".</p>
                    <div class="price-row">
                        <strong>10 000 FCFA</strong>
                        <a href="produit-landkaidi.html" class="btn-outline" style="padding: 0.5rem 1.2rem; font-size: 0.85rem;">Découvrir la collection</a>
                    </div>
                </div>

                <!-- Modèle Essentials Dynamique -->
                <div class="feature-card dynamic-card" id="card-essentials">
                    <div class="feature-image-wrapper">
                        <img src="essentials-vert-nouveau.jpg" alt="Sac à dos Essentials" class="dyn-img fade-in">
                    </div>
                    <span class="badge-tag-minimal dyn-badge" style="background: rgba(5, 150, 105, 0.1); color: var(--success-color);">+ Mini Pochette Offerte</span>
                    <h3 class="dyn-title fade-in">ESSENTIALS : Vert Olive</h3>
                    <p class="dyn-desc fade-in">Finition naturelle matte avec petite pochette zippée assortie pour vos accessoires.</p>
                    <div class="price-row">
                        <strong>12 500 FCFA</strong>
                        <a href="produit-sac.html" class="btn-outline" style="padding: 0.5rem 1.2rem; font-size: 0.85rem;">Découvrir la collection</a>
                    </div>
                </div>
            </div>
        </section>

        <!-- Offre Duo -->'''

content = pattern.sub(new_section, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
