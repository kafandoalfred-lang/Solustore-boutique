import re

with open('produit-landkaidi.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add ViewContent event to Pixel script in head
if "fbq('track', 'PageView');" in html and "fbq('track', 'ViewContent'" not in html:
    view_content_code = "fbq('track', 'PageView');\\n    fbq('track', 'ViewContent', {\\n        content_ids: ['sac-landkaidi'],\\n        content_type: 'product',\\n        value: 10000,\\n        currency: 'XOF'\\n    });"
    html = html.replace("fbq('track', 'PageView');", view_content_code)

# Add data-product-id to the form (if it exists)
form_pattern = r'(<form.*?id="orderForm".*?>)'
match = re.search(form_pattern, html)
if match and 'data-product-id' not in match.group(1):
    new_form_tag = match.group(1).replace('id="orderForm"', 'id="orderForm" data-product-id="sac-landkaidi"')
    html = html.replace(match.group(1), new_form_tag)

with open('produit-landkaidi.html', 'w', encoding='utf-8') as f:
    f.write(html)
