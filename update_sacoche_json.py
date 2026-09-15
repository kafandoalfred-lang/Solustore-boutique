import json

with open('products.json', 'r', encoding='utf-8-sig') as f:
    products = json.load(f)

if not any(p['id'] == 'sacoche-homme' for p in products):
    products.append({
        "id": "sacoche-homme",
        "title": "Sacoche pour Homme",
        "description": "Sacoche élégante pour homme en Cuir PU de haute qualité. Parfaite pour le quotidien et les affaires. Livraison GRATUITE.",
        "availability": "in stock",
        "condition": "new",
        "price": "7000 XOF",
        "link": "https://solustore.netlify.app/produit-sacoche.html",
        "image_link": "https://solustore.netlify.app/sacoche-1.jpg",
        "brand": "SoluStore"
    })

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)
