import re

# 1. Update index.html for the button color
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace btn-outline with btn-primary for the catalogue buttons
html = html.replace('class="btn-outline" style="padding: 0.5rem 1.2rem; font-size: 0.85rem;"', 'class="btn-primary" style="padding: 0.8rem 1.5rem; font-size: 1rem; width: 100%; text-align: center; margin-top: 1rem;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css to fix mobile hero font size
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add media query at the end if not exists
mobile_fix = '''
/* Fix mobile hero size */
@media (max-width: 768px) {
    .poster-content h2 {
        font-size: 2.2rem !important;
    }
    .poster-content .desc {
        font-size: 1rem !important;
    }
    .poster-banner-section {
        margin: 1.5rem auto 3rem !important;
    }
    .poster-content {
        padding: 2.5rem 1.5rem !important;
    }
}
'''

css += mobile_fix

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
