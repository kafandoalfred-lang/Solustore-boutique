import re

with open('produit-sac.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add ViewContent event to Pixel script in head
if "fbq('track', 'PageView');" in html and "fbq('track', 'ViewContent'" not in html:
    view_content_code = "fbq('track', 'PageView');\\n    fbq('track', 'ViewContent', {\\n        content_ids: ['sac-essentials'],\\n        content_type: 'product',\\n        value: 12500,\\n        currency: 'XOF'\\n    });"
    html = html.replace("fbq('track', 'PageView');", view_content_code)

# Add data-product-id to the form
if 'data-product-id="sac-essentials"' not in html:
    form_tag = '<form name="commande-solustore" method="POST" netlify id="orderForm" data-price1="12500" data-price2="20000" data-price3="28000" class="order-form">'
    new_form_tag = '<form name="commande-solustore" method="POST" netlify id="orderForm" data-product-id="sac-essentials" data-price1="12500" data-price2="20000" data-price3="28000" class="order-form">'
    html = html.replace(form_tag, new_form_tag)

with open('produit-sac.html', 'w', encoding='utf-8') as f:
    f.write(html)
