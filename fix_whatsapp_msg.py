import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

pattern = re.compile(r'(const whatsappMessage = Bonjour Alfred.*?Prix total à payer à la livraison : \$\{finalPrice\};)', re.DOTALL)

new_whatsapp = '''let whatsappMessage = Bonjour Alfred ! Je souhaite commander le .

Voici mes coordonnées :
👤 Nom Complet : 
📞 Téléphone : ;

        if (city) whatsappMessage += \n🏙️ Ville & Quartier : ;
        if (landmark) whatsappMessage += \n📍 Point de repère : ;

        whatsappMessage += \n\n🛍️ Commande : \n💰 Prix total à payer à la livraison : ;'''

content = pattern.sub(new_whatsapp, content)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
