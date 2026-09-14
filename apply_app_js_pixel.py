import re

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Update the Modal Trigger to fire InitiateCheckout
modal_trigger_pattern = r"(btn\.addEventListener\('click', \(e\) => {.*?)(modal\.style\.display = 'flex';)"
if 'InitiateCheckout' not in js:
    replacement = r"\1" + "\\n            // FB Pixel InitiateCheckout\\n            const prodId = formElement ? formElement.dataset.productId : 'unknown';\\n            if (typeof fbq === 'function' && prodId !== 'unknown') {\\n                fbq('track', 'InitiateCheckout', {\\n                    content_ids: [prodId],\\n                    content_type: 'product'\\n                });\\n            }\\n            " + r"\2"
    js = re.sub(modal_trigger_pattern, replacement, js, flags=re.DOTALL)

# 2. Update Purchase event to include content_ids
purchase_pattern = r"(fbq\('track', 'Purchase', {.*?)(content_name: productName,)"
if 'content_ids' not in js.split("fbq('track', 'Purchase'")[1]:
    replacement = r"\1" + "content_ids: [orderForm.dataset.productId || 'unknown'],\\n                " + r"\2"
    js = re.sub(purchase_pattern, replacement, js, flags=re.DOTALL)

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(js)
