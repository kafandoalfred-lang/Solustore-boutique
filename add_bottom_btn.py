import re

files = ['produit-sac.html', 'produit-landkaidi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the end of reassurance-box
    pattern = re.compile(r'(<div class="reassurance-item">\s*<i class="fa-solid fa-check-circle"></i>\s*<span>Qualit[é\ufffd] Premium garantie SoluStore</span>\s*</div>\s*</div>)', re.DOTALL)
    
    match = pattern.search(content)
    if match:
        new_btn = '''
                    <a href="#order-section" class="btn-submit" style="display: flex; justify-content: center; align-items: center; gap: 0.5rem; margin-top: 1.5rem; text-decoration: none;">
                        Commander maintenant
                        <i class="fa-solid fa-arrow-up"></i>
                    </a>'''
        content = content[:match.end()] + new_btn + content[match.end():]
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
