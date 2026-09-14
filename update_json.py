import json

with open('products.json', 'r', encoding='utf-8-sig') as f:
    products = json.load(f)

# Ensure it's not already added
if not any(p['id'] == 'sac-cat' for p in products):
    products.append({
        "id": "sac-cat",
        "title": "Sac à Dos CAT",
        "description": "Sac à dos CAT très résistant en tissu Jean. Idéal pour voyager, avec cadenas antivol intégré. Livraison GRATUITE.",
        "availability": "in stock",
        "condition": "new",
        "price": "10000 XOF",
        "link": "https://solustore.netlify.app/produit-cat.html",
        "image_link": "https://solustore.netlify.app/cat-sac-face.jpg",
        "brand": "Caterpillar"
    })

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)
