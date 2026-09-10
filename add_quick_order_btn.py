import re

files = ['produit-sac.html', 'produit-landkaidi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if we already inserted it
    if "Cliquez ici pour commander votre sac" not in content:
        insert_text = '''
                    <a href="#orderForm" class="btn-submit" style="margin-bottom: 1.5rem; display: flex; justify-content: center; align-items: center; gap: 0.5rem; background: var(--primary-accent); animation: pulse 2s infinite;">
                        Cliquez ici pour commander votre sac
                        <i class="fa-solid fa-arrow-down"></i>
                    </a>
'''
        content = content.replace('<div class="hero-buy-box">', '<div class="hero-buy-box">' + insert_text)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
