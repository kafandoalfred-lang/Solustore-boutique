import re

# 1. Add CSS class
with open('style.css', 'a', encoding='utf-8') as f:
    f.write('''
.btn-confirm {
    background: var(--success-color) !important;
}
.btn-confirm:hover {
    background: #047857 !important;
}
''')

# 2. Update HTML files
files = ['produit-sac.html', 'produit-landkaidi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the submit button
    pattern = re.compile(r'(<button type="submit" class="btn-submit".*?>\s*Valider la commande\s*<i class="fa-solid fa-arrow-right"></i>\s*</button>)', re.DOTALL)
    
    # We replace 'class="btn-submit"' with 'class="btn-submit btn-confirm"' in that specific matched block
    def replace_class(match):
        return match.group(1).replace('class="btn-submit"', 'class="btn-submit btn-confirm"')
        
    content = pattern.sub(replace_class, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
