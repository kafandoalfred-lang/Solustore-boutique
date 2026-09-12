import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The current button looks like this:
# <a href="produit-landkaidi.html" class="btn-confirm" style="padding: 0.8rem 1.5rem; font-size: 1rem; width: 100%; text-align: center; margin-top: 1rem;">Découvrir la collection</a>
# <a href="produit-sac.html" class="btn-confirm" style="padding: 0.8rem 1.5rem; font-size: 1rem; width: 100%; text-align: center; margin-top: 1rem;">Découvrir la collection</a>

new_landkaidi_btn = '<a href="produit-landkaidi.html" class="btn-primary" style="padding: 0.6rem 1rem; font-size: 0.8rem; line-height: 1.2; width: 100%; text-align: center; margin-top: 1rem;">Cliquer pour<br>découvrir la collection</a>'
new_essentials_btn = '<a href="produit-sac.html" class="btn-primary" style="padding: 0.6rem 1rem; font-size: 0.8rem; line-height: 1.2; width: 100%; text-align: center; margin-top: 1rem;">Cliquer pour<br>découvrir la collection</a>'

content = re.sub(r'<a href="produit-landkaidi\.html" class="btn-confirm" [^>]+>.*?</a>', new_landkaidi_btn, content)
content = re.sub(r'<a href="produit-sac\.html" class="btn-confirm" [^>]+>.*?</a>', new_essentials_btn, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
