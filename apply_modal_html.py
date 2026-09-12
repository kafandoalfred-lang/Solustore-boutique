import re

with open('produit-sac.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all <a href="#commande" class="lp-btn-primary"> with <a href="#commande" class="lp-btn-primary trigger-order">
# Same for secondary
html = html.replace('href="#commande"', 'href="javascript:void(0)" class="trigger-order"')

# Wrap the form
form_pattern = r'(<form name="commande-solustore".*?</form>)'
match = re.search(form_pattern, html, re.DOTALL)
if match:
    wrapped_form = '<div id="form-container-bottom">\n' + match.group(1) + '\n</div>'
    html = html.replace(match.group(1), wrapped_form)

# Add Modal HTML before </body>
modal_html = '''
<!-- ORDER MODAL -->
<div id="orderModal" class="modal-overlay" style="display: none;">
    <div class="modal-content">
        <span class="modal-close" id="closeModal">&times;</span>
        <div id="form-container-modal"></div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('orderModal');
    const closeBtn = document.getElementById('closeModal');
    const containerBottom = document.getElementById('form-container-bottom');
    const containerModal = document.getElementById('form-container-modal');
    const formElement = document.getElementById('orderForm');
    
    // Open modal when any trigger is clicked (except if we just want to scroll to bottom, but user requested popup)
    document.querySelectorAll('.trigger-order').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            // Move form to modal
            if(formElement) {
                containerModal.appendChild(formElement);
            }
            modal.style.display = 'flex';
        });
    });

    // Close modal
    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
        // Move form back to bottom
        if(formElement) {
            containerBottom.appendChild(formElement);
        }
    });

    // Close on outside click
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
            if(formElement) {
                containerBottom.appendChild(formElement);
            }
        }
    });
});
</script>
'''

html = html.replace('</body>', modal_html + '\n</body>')

with open('produit-sac.html', 'w', encoding='utf-8') as f:
    f.write(html)
