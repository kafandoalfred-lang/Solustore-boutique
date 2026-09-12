import re

with open('extracted_form.txt', 'r', encoding='utf-8') as f:
    form_content = f.read()

# Make sure form has the CTA button if it was missing or if we need to style it. The existing form already has a button.

with open('produit-sac.html', 'r', encoding='utf-8') as f:
    original_html = f.read()

# Extract head and footer
head_match = re.search(r'(<!DOCTYPE html>.*?</header>)', original_html, re.DOTALL)
footer_match = re.search(r'(<footer.*)', original_html, re.DOTALL)

if not head_match or not footer_match:
    print("Error extracting head or footer.")
    exit(1)

head_content = head_match.group(1)
footer_content = footer_match.group(1)

new_main = f'''
    <main class="landing-main">
        <!-- 1. HERO -->
        <section class="lp-hero">
            <div class="lp-hero-image">
                <img src="essentials-etudiant.jpg" alt="Sac à dos Essentials porté">
            </div>
            <div class="lp-hero-content">
                <span class="lp-badge">Premium • Résistant • Imperméable</span>
                <h1 class="lp-title">SAC À DOS ESSENTIALS</h1>
                <div class="lp-price-box">
                    <span class="price-old">20 000 FCFA</span>
                    <span class="price-new">12 500 FCFA</span>
                </div>
                <a href="#commande" class="lp-btn-primary">COMMANDER MAINTENANT</a>
                <div class="lp-reassurance-mini">
                    <span><i class="fa-solid fa-truck"></i> Livraison Gratuite Ouaga</span>
                    <span><i class="fa-solid fa-bolt"></i> Livraison Rapide</span>
                    <span><i class="fa-solid fa-hand-holding-dollar"></i> Paiement à la réception</span>
                </div>
            </div>
        </section>

        <!-- 2. VALUE PROP -->
        <section class="lp-value-props">
            <div class="lp-prop">
                <div class="lp-prop-icon">☔</div>
                <h3>RÉSISTE À LA PLUIE</h3>
                <p>Protège mieux vos affaires lors de vos déplacements.</p>
            </div>
            <div class="lp-prop">
                <div class="lp-prop-icon">💻</div>
                <h3>PROTECTION ORDINATEUR</h3>
                <p>Compartiment adapté aux ordinateurs jusqu'à 15,6 pouces.</p>
            </div>
            <div class="lp-prop">
                <div class="lp-prop-icon">📚</div>
                <h3>GRANDE CAPACITÉ</h3>
                <p>Permet de transporter ordinateur, cahiers, livres et accessoires.</p>
            </div>
            <div class="lp-prop">
                <div class="lp-prop-icon">🎒</div>
                <h3>CONFORT AU QUOTIDIEN</h3>
                <p>Dos et bretelles conçus pour un port confortable.</p>
            </div>
            <div style="text-align: center; margin-top: 2rem; width: 100%;">
                <a href="#commande" class="lp-btn-secondary">JE VEUX MON SAC ESSENTIALS</a>
            </div>
        </section>

        <!-- 3. POURQUOI CHOISIR -->
        <section class="lp-benefits">
            <h2 class="lp-section-title">Pourquoi choisir Essentials ?</h2>
            
            <div class="lp-benefit-row">
                <div class="lp-img-wrapper"><img src="sac_dos_details_1788628077455.jpg" alt="Tissu Imperméable"></div>
                <div class="lp-benefit-text">
                    <h3>PROTÉGEZ VOS AFFAIRES DE LA PLUIE</h3>
                    <p>Son tissu Oxford imperméable très résistant aide à protéger vos documents et appareils électroniques lors de vos déplacements sous la pluie.</p>
                </div>
            </div>

            <div class="lp-benefit-row reverse">
                <div class="lp-img-wrapper"><img src="sac_dos_interieur_1788628042441.jpg" alt="Compartiment PC"></div>
                <div class="lp-benefit-text">
                    <h3>PROTÉGEZ VOTRE ORDINATEUR</h3>
                    <p>Un compartiment dédié et matelassé permet de transporter en toute sécurité votre ordinateur (jusqu'à 15,6 pouces) contre les chocs du quotidien.</p>
                </div>
            </div>
            
            <div class="lp-benefit-row">
                <div class="lp-img-wrapper"><img src="sac_dos_portant_1788628057960.jpg" alt="Confort"></div>
                <div class="lp-benefit-text">
                    <h3>CONFORT MAXIMAL SANS TRANSPIRER</h3>
                    <p>Le dos rembourré et respirant réduit la fatigue et la transpiration, même lorsque votre sac est lourdement chargé.</p>
                </div>
            </div>
        </section>

        <!-- 4. DÉMONSTRATION -->
        <section class="lp-demo">
            <h2 class="lp-section-title">Le sac en détail</h2>
            <div class="hero-gallery" style="max-width: 600px; margin: 0 auto; background: var(--bg-surface); padding: 1rem; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);">
                <div class="main-image-container">
                    <img src="essentials-vert-nouveau.jpg" alt="Détail Essentials" id="mainProductImage">
                </div>
                <div class="gallery-thumbnails">
                    <img src="essentials-vert-nouveau.jpg" class="thumbnail active" onclick="changeImage('essentials-vert-nouveau.jpg', this)">
                    <img src="essentials-gris-podium.jpg" class="thumbnail" onclick="changeImage('essentials-gris-podium.jpg', this)">
                    <img src="essentials-poster-cyan.jpg" class="thumbnail" onclick="changeImage('essentials-poster-cyan.jpg', this)">
                    <img src="sac_dos_main_1788628026108.jpg" class="thumbnail" onclick="changeImage('sac_dos_main_1788628026108.jpg', this)">
                </div>
            </div>
            
            <!-- Placeholders demandés par le client pour photos futures -->
            <div class="lp-placeholders">
                <div class="lp-ph-item"><span>[Vue de profil - À venir]</span></div>
                <div class="lp-ph-item"><span>[Détails zip - À venir]</span></div>
            </div>

            <div style="text-align: center; margin-top: 2rem;">
                <a href="#commande" class="lp-btn-secondary">COMMANDER — 12 500 FCFA</a>
            </div>
        </section>

        <!-- 5. CAPACITÉ -->
        <section class="lp-capacity">
            <h2 class="lp-section-title">Voyez ce qu'il peut contenir</h2>
            <div class="lp-capacity-grid">
                <div class="capacity-item"><i class="fa-solid fa-laptop"></i><span>PC 15.6"</span></div>
                <div class="capacity-item"><i class="fa-solid fa-book"></i><span>Cahiers / Livres</span></div>
                <div class="capacity-item"><i class="fa-solid fa-plug"></i><span>Chargeur</span></div>
                <div class="capacity-item"><i class="fa-solid fa-headphones"></i><span>Accessoires</span></div>
                <div class="capacity-item"><i class="fa-solid fa-bottle-water"></i><span>Bouteille d'eau</span></div>
            </div>
            <div class="lp-placeholder-img" style="margin-top: 1.5rem;">
                <span>[Photo du sac rempli - À venir]</span>
            </div>
        </section>

        <!-- 6. SPECS -->
        <section class="lp-specs">
            <h2 class="lp-section-title">Caractéristiques Techniques</h2>
            <div class="table-responsive">
                <table class="lp-spec-table">
                    <tbody>
                        <tr><td>Matière</td><td>Tissu Oxford haute densité</td></tr>
                        <tr><td>Ordinateur</td><td>Jusqu'à 15,6 pouces</td></tr>
                        <tr><td>Imperméabilité</td><td>Oui</td></tr>
                        <tr><td>Compartiments</td><td>Plusieurs poches intérieures/extérieures</td></tr>
                        <tr><td>Utilisation</td><td>Études / Travail / Quotidien</td></tr>
                        <tr><td>Prix</td><td><strong>12 500 FCFA</strong></td></tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- 7. RÉASSURANCE -->
        <section class="lp-reassurance-large">
            <div class="lp-reassure-block">
                <div class="re-icon"><i class="fa-solid fa-truck-fast"></i></div>
                <h3>LIVRAISON RAPIDE</h3>
                <p>Livraison à Ouagadougou en un temps record selon nos disponibilités.</p>
            </div>
            <div class="lp-reassure-block">
                <div class="re-icon"><i class="fa-solid fa-money-bill-wave"></i></div>
                <h3>PAIEMENT À LA LIVRAISON</h3>
                <p>Vous ne payez que lorsque le livreur vous remet le colis, aucun risque.</p>
            </div>
            <div class="lp-reassure-block">
                <div class="re-icon"><i class="fa-solid fa-box-open"></i></div>
                <h3>VÉRIFICATION DU PRODUIT</h3>
                <p>Vérifiez la qualité de votre sac avec le livreur avant de payer.</p>
            </div>
            <div style="text-align: center; margin-top: 2rem; width: 100%;">
                <a href="#commande" class="lp-btn-secondary">PASSER MA COMMANDE</a>
            </div>
        </section>

        <!-- 8. AVIS -->
        <section class="lp-reviews">
            <h2 class="lp-section-title">Ils ont choisi Essentials</h2>
            <div class="lp-reviews-empty">
                <p>Les premiers avis clients arrivent bientôt.</p>
            </div>
        </section>

        <!-- 9 & 10. OFFRE & FORMULAIRE -->
        <section class="lp-offer-order" id="commande">
            <div class="lp-offer-box">
                <h2>OFFRE SPÉCIALE</h2>
                <h3>SAC À DOS ESSENTIALS</h3>
                <div class="lp-price-box" style="justify-content: center; margin: 1rem 0;">
                    <span class="price-old">20 000 FCFA</span>
                    <span class="price-new">12 500 FCFA</span>
                </div>
                <ul class="lp-offer-perks">
                    <li><i class="fa-solid fa-check"></i> Livraison gratuite à Ouaga</li>
                    <li><i class="fa-solid fa-check"></i> Paiement à la réception</li>
                    <li><i class="fa-solid fa-check"></i> Stock très limité</li>
                </ul>
            </div>

            <div class="lp-form-box">
                <h3 style="text-align: center; margin-bottom: 0.5rem; font-size: 1.2rem; color: var(--text-main);">Je remplis ce formulaire pour commander mon sac</h3>
                <p style="text-align: center; font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.5rem;">Simple, rapide et 100% sécurisé (Paiement à la livraison).</p>
                
                {form_content}
                
            </div>
        </section>

        <!-- 11. FAQ -->
        <section class="lp-faq">
            <h2 class="lp-section-title">Questions Fréquentes (FAQ)</h2>
            
            <div class="faq-item">
                <button class="faq-question">Est-ce qu'un ordinateur 15,6 pouces peut entrer dans le sac ? <i class="fa-solid fa-chevron-down"></i></button>
                <div class="faq-answer"><p>Oui, le sac Essentials possède un grand compartiment matelassé spécialement conçu pour accueillir un ordinateur portable allant jusqu'à 15,6 pouces en toute sécurité.</p></div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Le sac résiste-t-il à la pluie ? <i class="fa-solid fa-chevron-down"></i></button>
                <div class="faq-answer"><p>Oui, le tissu extérieur est hautement résistant à l'eau, ce qui permet de protéger vos affaires lors d'une pluie pendant vos trajets.</p></div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Quels sont les moyens de paiement ? <i class="fa-solid fa-chevron-down"></i></button>
                <div class="faq-answer"><p>Pour votre sécurité, le paiement s'effectue uniquement en espèces (cash) directement auprès du livreur lors de la réception de votre sac à Ouagadougou.</p></div>
            </div>

            <div class="faq-item">
                <button class="faq-question">Comment fonctionne la livraison ? <i class="fa-solid fa-chevron-down"></i></button>
                <div class="faq-answer"><p>Une fois le formulaire rempli, notre équipe vous contacte sur WhatsApp pour confirmer. Un livreur vous l'apporte ensuite gratuitement à Ouagadougou.</p></div>
            </div>
            
            <div class="faq-item">
                <button class="faq-question">Puis-je choisir une couleur ? <i class="fa-solid fa-chevron-down"></i></button>
                <div class="faq-answer"><p>Oui, le modèle Essentials est disponible en 3 coloris. Notre agent vous demandera votre couleur préférée sur WhatsApp lors de la confirmation de votre commande.</p></div>
            </div>
        </section>
        
        <div style="text-align: center; margin: 4rem 0 2rem;">
            <a href="#commande" class="lp-btn-primary" style="display: inline-block; width: 90%; max-width: 400px; animation: pulse 2s infinite;">COMMANDER MAINTENANT</a>
        </div>

    </main>
'''

final_html = head_content + new_main + footer_content

with open('produit-sac.html', 'w', encoding='utf-8') as f:
    f.write(final_html)
print("Updated produit-sac.html successfully.")
