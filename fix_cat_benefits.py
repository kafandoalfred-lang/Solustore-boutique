import re

with open('produit-cat.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Rewrite benefits section
benefits_pattern = r'<section class="lp-benefits">.*?</section>'
new_benefits = '''<section class="lp-benefits">
              <h2 class="lp-section-title">Pourquoi choisir CAT ?</h2>
              
              <div class="lp-benefit-row">
                  <div class="lp-img-wrapper"><img src="cat-sac-profil.jpg" alt="Cadenas antivol"></div>
                  <div class="lp-benefit-text">
                      <h3>SÉCURITÉ MAXIMALE : CADENAS ANTIVOL</h3>
                      <p>Voyagez l'esprit tranquille. Le sac intègre un cadenas à code ultra-robuste sur le côté pour verrouiller les fermetures et protéger vos objets de valeur.</p>
                  </div>
              </div>
  
              <div class="lp-benefit-row reverse">
                  <div class="lp-img-wrapper"><img src="cat-sac-details.jpg" alt="Tissu en Jean"></div>
                  <div class="lp-benefit-text">
                      <h3>TISSU EN JEAN ULTRA-RÉSISTANT</h3>
                      <p>Fini les sacs qui se déchirent. Fabriqué à partir d'un tissu jean épais et de haute qualité, ce sac est conçu pour endurer les pires conditions tout en gardant un style unique.</p>
                  </div>
              </div>
              
              <div class="lp-benefit-row">
                  <div class="lp-img-wrapper"><img src="cat-sac-face.jpg" alt="Grande capacité"></div>
                  <div class="lp-benefit-text">
                      <h3>ASSEZ GROS POUR VOYAGER</h3>
                      <p>Ne laissez rien derrière vous. Son format XL et ses multiples poches intelligentes vous permettent d'emporter vos vêtements, votre ordinateur et tous vos documents pour de longs voyages.</p>
                  </div>
              </div>
          </section>'''
html = re.sub(benefits_pattern, new_benefits, html, flags=re.DOTALL)

# Rewrite specs section
specs_pattern = r'<table class="lp-spec-table">.*?</tbody>'
new_specs = '''<table class="lp-spec-table">
                      <tbody>
                          <tr><td>Matière</td><td>Tissu Jean haute résistance</td></tr>
                          <tr><td>Utilisation</td><td>Voyage, Études, Professionnel</td></tr>
                          <tr><td>Sécurité</td><td>Cadenas à code intégré</td></tr>
                          <tr><td>Capacité</td><td>Format XL avec poches multiples</td></tr>
                      </tbody>'''
html = re.sub(specs_pattern, new_specs, html, flags=re.DOTALL)

# Rewrite FAQ regarding laptop and rain
html = html.replace("Oui, le sac CAT possède un grand compartiment matelassé spécialement conçu pour accueillir un ordinateur portable allant jusqu'à 15,6 pouces en toute sécurité.", "Oui, le sac offre une grande capacité idéale pour voyager, et permet de transporter votre ordinateur et toutes vos affaires.")
html = html.replace("Oui, le tissu extérieur est hautement résistant à l'eau, ce qui permet de protéger vos affaires lors d'une pluie pendant vos trajets.", "Oui, son tissu en jean est particulièrement épais et résistant pour faire face à vos déplacements quotidiens.")

with open('produit-cat.html', 'w', encoding='utf-8') as f:
    f.write(html)
