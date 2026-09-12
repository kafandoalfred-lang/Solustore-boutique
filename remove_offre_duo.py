import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change button class from btn-primary to btn-confirm
content = content.replace('class="btn-primary" style="padding: 0.8rem 1.5rem; font-size: 1rem; width: 100%; text-align: center; margin-top: 1rem;"', 'class="btn-confirm" style="padding: 0.8rem 1.5rem; font-size: 1rem; width: 100%; text-align: center; margin-top: 1rem;"')

# 2. Remove the "Offre Duo" section completely
# It starts with <!-- Offre Duo --> and ends before <!-- Testimonials -->
pattern = re.compile(r'<!-- Offre Duo -->.*?<!-- Testimonials -->', re.DOTALL)
content = pattern.sub('<!-- Testimonials -->', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
