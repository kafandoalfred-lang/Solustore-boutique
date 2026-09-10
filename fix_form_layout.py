import re

files = ['produit-sac.html', 'produit-landkaidi.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Extract and remove the info-message block
    info_pattern = re.compile(r'\s*<div class="info-message".*?</div>', re.DOTALL)
    match = info_pattern.search(content)
    if match:
        info_block = match.group(0)
        content = content[:match.start()] + content[match.end():]
        # modify margin
        info_block = info_block.replace('margin-bottom: 1.5rem;', 'margin-top: 1rem; margin-bottom: 0.5rem;')
    else:
        info_block = ''
        
    # 2. Remove the red warning note
    warning_pattern = re.compile(r'\s*<p class="security-note" style="color: var\(--warning-color\);.*?</p>', re.DOTALL)
    content = warning_pattern.sub('', content)
    
    # 3. Insert the info-message after the submit button
    btn_pattern = re.compile(r'(<button type="submit" class="btn-submit" id="submitOrderBtn">.*?</button>)', re.DOTALL)
    content = btn_pattern.sub(r'\1' + info_block, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
