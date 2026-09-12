import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace btn-primary with btn-header
content = content.replace('class="btn-primary" style="padding: 0.6rem 1rem; font-size: 0.8rem; line-height: 1.2; width: 100%; text-align: center; margin-top: 1rem;"', 'class="btn-header" style="padding: 0.6rem 1rem; font-size: 0.8rem; line-height: 1.2; width: 100%; text-align: center; margin-top: 1rem;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
