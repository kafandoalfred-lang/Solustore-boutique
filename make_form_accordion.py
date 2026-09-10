import re

files = ['produit-sac.html', 'produit-landkaidi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Extract the form-container
    form_pattern = re.compile(r'(<div class="form-container" id="order-section">.*?</form>\s*</div>)', re.DOTALL)
    match = form_pattern.search(content)
    if not match:
        continue
    
    form_html = match.group(1)
    
    # 2. Remove it from its original place (at the bottom)
    content = content[:match.start()] + content[match.end():]
    
    # 3. Modify the quick order button to be a toggle, and place the form right after it
    # We will hide the form by default adding style="display: none;" to the form_html, or we wrap it in a div that toggles.
    form_html = form_html.replace('<div class="form-container" id="order-section">', '<div class="form-container" id="order-section" style="display: none; margin-top: 1rem; animation: fadeIn 0.5s;">')
    
    btn_pattern = re.compile(r'<a href="#orderForm" class="btn-submit" style="margin-bottom: 1.5rem; display: flex; justify-content: center; align-items: center; gap: 0.5rem; background: var\(--primary-accent\); animation: pulse 2s infinite;">\s*Cliquez ici pour commander votre sac\s*<i class="fa-solid fa-arrow-down"></i>\s*</a>', re.DOTALL)
    
    new_btn_and_form = '''
                    <button onclick="document.getElementById('order-section').style.display = document.getElementById('order-section').style.display === 'none' ? 'block' : 'none'; this.style.display='none';" class="btn-submit" style="margin-bottom: 1.5rem; display: flex; justify-content: center; align-items: center; gap: 0.5rem; background: var(--primary-accent); animation: pulse 2s infinite; width: 100%; cursor: pointer;">
                        Cliquez ici pour commander votre sac
                        <i class="fa-solid fa-arrow-down"></i>
                    </button>
''' + form_html

    content = btn_pattern.sub(new_btn_and_form, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
