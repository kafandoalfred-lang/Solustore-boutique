import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Restore the 3 Essentials cards
pattern = re.compile(r'<!-- Modèle Essentials Unique -->.*?</div>\s*</div>', re.DOTALL)

restored_cards = '''<!-- Modèle 1 : Vert Kaki -->
                <div class="feature-card">
                    <div class="feature-image-wrapper">
                        <img src="essentials-vert-nouveau.jpg" alt="Sac à dos Essentials Vert Kaki">
                    </div>
                    <span class="badge-tag-minimal" style="background: rgba(5, 150, 105, 0.1); color: var(--success-color);">+ Mini Pochette Offerte</span>
                    <h3>ESSENTIALS : Vert Olive</h3>
                    <p>Finition naturelle matte avec petite pochette zippée assortie pour vos accessoires.</p>
                    <div class="price-row">
                        <strong>12 500 FCFA</strong>
                        <a href="produit-sac.html" class="btn-outline" style="padding: 0.5rem 1.2rem; font-size: 0.85rem;">Commander</a>
                    </div>
                </div>

                <!-- Modèle 2 : Bicolore Noir/Cyan -->
                <div class="feature-card">
                    <div class="feature-image-wrapper">
                        <img src="essentials-poster-cyan.jpg" alt="Sac à dos Essentials Cyan">
                    </div>
                    <span class="badge-tag-minimal">Best-Seller</span>
                    <h3>ESSENTIALS : Noir & Bleu</h3>
                    <p>Contraste dynamique et audacieux. Parfait pour les étudiants et les esprits créatifs.</p>
                    <div class="price-row">
                        <strong>12 500 FCFA</strong>
                        <a href="produit-sac.html" class="btn-outline" style="padding: 0.5rem 1.2rem; font-size: 0.85rem;">Commander</a>
                    </div>
                </div>

                <!-- Modèle 3 : Gris Podium -->
                <div class="feature-card">
                    <div class="feature-image-wrapper">
                        <img src="essentials-gris-podium.jpg" alt="Sac à dos Essentials Gris">
                    </div>
                    <span class="badge-tag-minimal">Édition Classique</span>
                    <h3>ESSENTIALS : Noir & Gris</h3>
                    <p>L'élégance discrète pour le bureau. S'accorde parfaitement avec une tenue professionnelle.</p>
                    <div class="price-row">
                        <strong>12 500 FCFA</strong>
                        <a href="produit-sac.html" class="btn-outline" style="padding: 0.5rem 1.2rem; font-size: 0.85rem;">Commander</a>
                    </div>
                </div>'''

content = pattern.sub(restored_cards, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
