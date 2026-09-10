import os

with open('produit-sac.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('ESSENTIALS', 'LANDKAIDI')
content = content.replace('Essentials', 'Landkaidi')
content = content.replace('essentials', 'landkaidi')
content = content.replace('12 500 FCFA', '10 000 FCFA')
content = content.replace('12500', '10000')
content = content.replace('25 000 FCFA', '20 000 FCFA')
content = content.replace('25000', '20000')
content = content.replace('sac-landkaidi-bleu.jpg', 'landkaidi-vert.jpg')
content = content.replace('landkaidi-etudiant.jpg', 'landkaidi-vert.jpg')
content = content.replace('landkaidi-vert-nouveau.jpg', 'landkaidi-rose.jpg')
content = content.replace('landkaidi-gris-podium.jpg', 'landkaidi-dos.jpg')
content = content.replace('landkaidi-poster-cyan.jpg', 'landkaidi-vert.jpg')
content = content.replace('sac_dos_main_1788628026108.jpg', 'landkaidi-vert.jpg')
content = content.replace('sac_dos_portant_1788628057960.jpg', 'landkaidi-rose.jpg')
content = content.replace('sac_dos_details_1788628077455.jpg', 'landkaidi-dos.jpg')
content = content.replace('sac_dos_interieur_1788628042441.jpg', 'landkaidi-vert.jpg')
content = content.replace('Vert Olive Premium', 'Beige & Vert Kaki')
content = content.replace('Noir & Bleu Océan (Best-Seller)', 'Beige & Rose Saumon')
content = content.replace('Noir & Gris Anthracite', 'Beige & Rose Saumon')
content = content.replace('Textile Imperméable', 'Tissu Jean Ultra-Résistant')
content = content.replace('L\'eau glisse sur la surface. Protégez efficacement vos affaires pendant la saison des pluies.', 'Un matériau réputé pour son extrême durabilité, résistant aux déchirures.')
content = content.replace('Compartiment Matelassé', 'Dos Renforcé & Respirant')
content = content.replace('Protection anti-chocs spécialement conçue pour ordinateurs portables jusqu\'à 15.6 pouces.', 'Support en mousse épaisse et respirante pour un confort maximal, idéal pour les longues distances.')
content = content.replace('Espace intérieur optimisé pour transporter facilement tous vos cahiers, livres et documents de travail.', 'Idéal pour le voyage. Parfait pour ranger ses habits et son ordinateur en toute sécurité.')

with open('produit-landkaidi.html', 'w', encoding='utf-8') as f:
    f.write(content)
