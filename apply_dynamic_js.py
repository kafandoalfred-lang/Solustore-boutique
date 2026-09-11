import re

with open('app.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the old catalog slider logic
content = re.sub(r'// 10\. CATALOG SLIDER.*', '', content, flags=re.DOTALL)

# Add the new dynamic card logic
content += '''
// -------------------------------------------------------------
// 10. DYNAMIC CATALOG CARDS
// -------------------------------------------------------------
const essentialsSlides = [
    {
        img: "essentials-vert-nouveau.jpg",
        badge: "+ Mini Pochette Offerte",
        badgeColor: "var(--success-color)",
        badgeBg: "rgba(5, 150, 105, 0.1)",
        title: "ESSENTIALS : Vert Olive",
        desc: "Finition naturelle matte avec petite pochette zippée assortie pour vos accessoires."
    },
    {
        img: "essentials-poster-cyan.jpg",
        badge: "Best-Seller",
        badgeColor: "var(--text-color)",
        badgeBg: "rgba(0,0,0,0.05)",
        title: "ESSENTIALS : Noir & Bleu",
        desc: "Contraste dynamique et audacieux. Parfait pour les étudiants et les esprits créatifs."
    },
    {
        img: "essentials-gris-podium.jpg",
        badge: "Édition Classique",
        badgeColor: "var(--text-color)",
        badgeBg: "rgba(0,0,0,0.05)",
        title: "ESSENTIALS : Noir & Gris",
        desc: "L'élégance discrète pour le bureau. S'accorde parfaitement avec une tenue professionnelle."
    }
];

const landkaidiSlides = [
    {
        img: "landkaidi-vert.jpg",
        badge: "Vert Olive",
        badgeColor: "var(--success-color)",
        badgeBg: "rgba(5, 150, 105, 0.1)",
        title: "LANDKAIDI : Vert Olive",
        desc: "Tissu Jean très résistant et dos renforcé ultra confortable. Idéal pour voyager."
    },
    {
        img: "landkaidi-rose.jpg",
        badge: "Kaki Tendance",
        badgeColor: "var(--primary-accent)",
        badgeBg: "rgba(30, 58, 138, 0.1)",
        title: "LANDKAIDI : Kaki",
        desc: "L'alliage parfait entre robustesse et style décontracté pour vos sorties quotidiennes."
    }
];

function initDynamicCard(cardId, slides, interval) {
    const card = document.getElementById(cardId);
    if (!card) return;
    
    let currentIndex = 0;
    const imgEl = card.querySelector('.dyn-img');
    const badgeEl = card.querySelector('.dyn-badge');
    const titleEl = card.querySelector('.dyn-title');
    const descEl = card.querySelector('.dyn-desc');
    
    setInterval(() => {
        currentIndex = (currentIndex + 1) % slides.length;
        const slide = slides[currentIndex];
        
        // Remove fade class to reset animation
        imgEl.classList.remove('fade-in');
        titleEl.classList.remove('fade-in');
        descEl.classList.remove('fade-in');
        badgeEl.classList.remove('fade-in');
        
        // Timeout to allow DOM to register removal, then apply new content and re-add class
        setTimeout(() => {
            imgEl.src = slide.img;
            badgeEl.textContent = slide.badge;
            badgeEl.style.color = slide.badgeColor;
            badgeEl.style.background = slide.badgeBg;
            titleEl.textContent = slide.title;
            descEl.textContent = slide.desc;
            
            imgEl.classList.add('fade-in');
            titleEl.classList.add('fade-in');
            descEl.classList.add('fade-in');
            badgeEl.classList.add('fade-in');
        }, 50);
        
    }, interval);
}

// Initialize dynamic cards
initDynamicCard('card-essentials', essentialsSlides, 3500);
initDynamicCard('card-landkaidi', landkaidiSlides, 3800); // Différent délai pour éviter une synchro visuelle
'''

with open('app.js', 'w', encoding='utf-8') as f:
    f.write(content)
