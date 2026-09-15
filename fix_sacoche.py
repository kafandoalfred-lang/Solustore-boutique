import re

with open('produit-sacoche.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Meta and Title
html = html.replace('Sac À Dos CAT', 'Sacoche pour Homme')
html = html.replace('SAC À DOS CAT', 'SACOCHE POUR HOMME')
html = html.replace('Sac à dos CAT très résistant en tissu Jean', 'Sacoche élégante pour homme en Cuir PU de haute qualité')
html = html.replace('cat-sac-face.jpg', 'sacoche-1.jpg')
html = html.replace('cat-sac-profil.jpg', 'sacoche-2.jpg')
html = html.replace('cat-sac-details.jpg', 'sacoche-3.jpg')
html = html.replace('cat-sac-interieur.jpg', 'sacoche-3.jpg')
html = html.replace('sac-cat', 'sacoche-homme')
html = html.replace('10 000 FCFA', '7 000 FCFA')
html = html.replace('10.000 FCFA', '7.000 FCFA')
html = html.replace('15 000 FCFA', '10 000 FCFA')

# Rewrite benefits section completely
benefits_pattern = r'<section class="lp-benefits">.*?</section>'
new_benefits = '''<section class="lp-benefits">
              <h2 class="lp-section-title">Pourquoi choisir cette Sacoche ?</h2>
              
              <div class="lp-benefit-row">
                  <div class="lp-img-wrapper"><img src="sacoche-2.jpg" alt="Sacoche Style"></div>
                  <div class="lp-benefit-text">
                      <h3>AFFIRMEZ VOTRE STYLE AU QUOTIDIEN</h3>
                      <p>Une sacoche chic et minimaliste qui s'adapte parfaitement à toutes vos tenues. Idéale pour vos rendez-vous d'affaires, le bureau ou vos sorties entre amis.</p>
                  </div>
              </div>
  
              <div class="lp-benefit-row reverse">
                  <div class="lp-img-wrapper"><img src="sacoche-1.jpg" alt="Qualité Cuir PU"></div>
                  <div class="lp-benefit-text">
                      <h3>QUALITÉ PREMIUM EN CUIR PU</h3>
                      <p>Fabriquée avec un revêtement en Cuir PU haut de gamme (texture GG en relief), elle offre une résistance exceptionnelle et des finitions soignées pour durer dans le temps.</p>
                  </div>
              </div>
              
              <div class="lp-benefit-row">
                  <div class="lp-img-wrapper"><img src="sacoche-3.jpg" alt="Intérieur organisé"></div>
                  <div class="lp-benefit-text">
                      <h3>VOS AFFAIRES TOUJOURS BIEN RANGÉES</h3>
                      <p>Découvrez un intérieur intelligent avec de multiples poches. Rangez facilement votre téléphone, votre portefeuille, vos clés et documents sans jamais les chercher.</p>
                  </div>
              </div>
          </section>'''
html = re.sub(benefits_pattern, new_benefits, html, flags=re.DOTALL)

# Rewrite specs section
specs_pattern = r'<table class="lp-spec-table">.*?</tbody>'
new_specs = '''<table class="lp-spec-table">
                      <tbody>
                          <tr><td>Matière</td><td>Cuir PU Premium (motif en relief)</td></tr>
                          <tr><td>Utilisation</td><td>Quotidien, Affaires, Sorties</td></tr>
                          <tr><td>Compartiments</td><td>Plusieurs poches de rangement internes</td></tr>
                          <tr><td>Fermeture</td><td>Zip métallique robuste</td></tr>
                      </tbody>'''
html = re.sub(specs_pattern, new_specs, html, flags=re.DOTALL)

# Fix FAQ
html = html.replace("le sac offre une grande capacité idéale pour voyager, et permet de transporter votre ordinateur et toutes vos affaires", "la sacoche est assez spacieuse pour contenir tous vos essentiels : téléphone, portefeuille, parfum, et documents de petite taille")
html = html.replace("son tissu en jean est particulièrement épais et résistant pour faire face à vos déplacements quotidiens", "son revêtement en Cuir PU protège parfaitement vos affaires contre les éclaboussures et les intempéries")

with open('produit-sacoche.html', 'w', encoding='utf-8') as f:
    f.write(html)
