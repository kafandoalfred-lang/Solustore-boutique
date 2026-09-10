import re

files = ['produit-sac.html', 'produit-landkaidi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract the form container at the bottom
    form_pattern = re.compile(r'\s*<div class="mini-checkout-wrapper" id="order-section">.*?</form>\s*</div>', re.DOTALL)
    match = form_pattern.search(content)
    
    if match:
        form_html = match.group(0)
        # Remove it from the bottom
        content = content[:match.start()] + content[match.end():]
        
        # Style form for dropdown
        form_html = form_html.replace('class="mini-checkout-wrapper" id="order-section"', 'class="mini-checkout-wrapper" id="order-section" style="display: none; margin-top: 1rem; padding: 1.5rem; background: var(--bg-secondary); border-radius: var(--radius-lg); box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);"')
        
        # Now replace the anchor button with a real button + form
        btn_pattern = re.compile(r'\s*<a href="#orderForm" class="btn-submit" style="margin-bottom: 1.5rem; display: flex; justify-content: center; align-items: center; gap: 0.5rem; background: var\(--primary-accent\); animation: pulse 2s infinite;">\s*Cliquez ici pour commander votre sac\s*<i class="fa-solid fa-arrow-down"></i>\s*</a>', re.DOTALL)
        
        new_btn = '''
                    <button type="button" class="btn-submit" style="margin-bottom: 1.5rem; display: flex; justify-content: center; align-items: center; gap: 0.5rem; background: var(--primary-accent); animation: pulse 2s infinite; width: 100%; cursor: pointer; border: none; font-size: 1.1rem; padding: 1rem;" onclick="document.getElementById('order-section').style.display='block'; this.style.display='none';">
                        Cliquez ici pour commander votre sac
                        <i class="fa-solid fa-arrow-down"></i>
                    </button>'''
        
        content = btn_pattern.sub(new_btn + form_html, content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
