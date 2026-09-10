import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

if "window.addEventListener('hashchange'" not in content:
    content += '''

// Gestion globale de l'affichage du formulaire pour le bouton 'Commander'
document.addEventListener('DOMContentLoaded', () => {
    const orderSection = document.getElementById('order-section');
    if(orderSection) {
        // Rendre visible si on accède directement avec #orderForm
        if(window.location.hash === '#orderForm') {
            orderSection.style.display = 'block';
        }
        
        // Intercepter tous les clics sur les boutons qui pointent vers le formulaire
        document.querySelectorAll('a[href$="#orderForm"], a[href$="#order-section"]').forEach(btn => {
            btn.addEventListener('click', () => {
                orderSection.style.display = 'block';
            });
        });
    }
});
'''
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(content)
