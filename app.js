/**
 * SMARTSTAND 360° - LANDING PAGE LOGIC
 * Optimized for Mobile performance & West African COD conversion
 */

// CONFIGURATION : Configurez votre numéro WhatsApp ici (sans le signe + ni les espaces)
const WHATSAPP_PHONE = "22658909806"; // Modifiez avec votre vrai numéro WhatsApp burkinabè ou guinéen

// CONFIGURATION DU CODE DE TEST META (Optionnel - Pour voir vos tests CAPI en direct, ex: "TEST12345")
// Mettez le code fourni dans l'onglet "Événements de test" de Meta Business Suite. Laissez vide "" en production.
const META_TEST_EVENT_CODE = ""; 

// -------------------------------------------------------------
// 1. GALERIE PHOTO INTERACTIVE
// -------------------------------------------------------------
function changeImage(imageSrc, thumbnailElement) {
    const mainImage = document.getElementById('mainProductImage');
    if (mainImage) {
        mainImage.src = imageSrc;
    }
    
    // Mettre à jour la classe active sur les miniatures
    const thumbnails = document.querySelectorAll('.thumbnail');
    thumbnails.forEach(thumb => {
        thumb.classList.remove('active');
    });
    
    if (thumbnailElement) {
        thumbnailElement.classList.add('active');
    }
}

// -------------------------------------------------------------
// 2. SYSTEME D'ONGLETS INTERACTIFS (TABS)
// -------------------------------------------------------------
const tabButtons = document.querySelectorAll('.tab-btn');
const tabPanes = document.querySelectorAll('.tab-pane');

tabButtons.forEach(button => {
    button.addEventListener('click', () => {
        const targetTab = button.getAttribute('data-tab');
        
        // Retirer la classe active de tous les boutons
        tabButtons.forEach(btn => btn.classList.remove('active'));
        // Masquer tous les volets
        tabPanes.forEach(pane => pane.classList.remove('active'));
        
        // Activer le bouton actuel
        button.classList.add('active');
        
        // Afficher le volet correspondant
        const activePane = document.getElementById(`tab-${targetTab}`);
        if (activePane) {
            activePane.classList.add('active');
        }
    });
});

// -------------------------------------------------------------
// 3. BARRE D'ACHAT COLLANTE MOBILE (STICKY BUY BAR)
// -------------------------------------------------------------
const stickyBar = document.getElementById('stickyBuyBar');
const heroSection = document.getElementById('heroSection');

if (stickyBar && heroSection) {
    window.addEventListener('scroll', () => {
        // Obtenir la position du bas de la section hero
        const heroBottom = heroSection.offsetTop + heroSection.offsetHeight;
        
        // Afficher la barre collante si on défile au-delà du hero
        if (window.scrollY > heroBottom - 100) {
            stickyBar.classList.add('show');
        } else {
            stickyBar.classList.remove('show');
        }
    });
}

// -------------------------------------------------------------
// 4. CALCULATEUR DYNAMIQUE DE PRIX
// -------------------------------------------------------------
const orderForm = document.getElementById('orderForm');
const quantitySelect = document.getElementById('quantity');
const totalPriceDisplay = document.getElementById('totalPrice');

let pricing = {
    "1": "15 000 FCFA",
    "2": "27 000 FCFA",
    "3": "38 000 FCFA"
};

let pricingText = {
    "1": "1 Trépied (15 000 FCFA)",
    "2": "2 Trépieds (27 000 FCFA)",
    "3": "3 Trépieds (38 000 FCFA)"
};

let productName = "Trépied Intelligent 360° (+ Trépied 1m70)";

// Charger dynamiquement les configurations du produit depuis les attributs data du formulaire
if (orderForm) {
    if (orderForm.dataset.price1) {
        pricing["1"] = `${Number(orderForm.dataset.price1).toLocaleString('fr-FR')} FCFA`;
        pricing["2"] = `${Number(orderForm.dataset.price2).toLocaleString('fr-FR')} FCFA`;
        pricing["3"] = `${Number(orderForm.dataset.price3).toLocaleString('fr-FR')} FCFA`;
    }
    if (orderForm.dataset.priceText1) {
        pricingText["1"] = orderForm.dataset.priceText1;
        pricingText["2"] = orderForm.dataset.priceText2;
        pricingText["3"] = orderForm.dataset.priceText3;
    }
    if (orderForm.dataset.productName) {
        productName = orderForm.dataset.productName;
    }
}

if (quantitySelect && totalPriceDisplay) {
    // Mettre à jour le prix affiché initialement
    const initialQty = quantitySelect.value;
    if (pricing[initialQty]) {
        totalPriceDisplay.textContent = pricing[initialQty];
    }

    quantitySelect.addEventListener('change', (e) => {
        const qty = e.target.value;
        if (pricing[qty]) {
            totalPriceDisplay.textContent = pricing[qty];
        }
    });
}

// -------------------------------------------------------------
// 5. ACCORDÉONS FOIRE AUX QUESTIONS (FAQ)
// -------------------------------------------------------------
const faqItems = document.querySelectorAll('.faq-item');

faqItems.forEach(item => {
    const questionButton = item.querySelector('.faq-question');
    const answerDiv = item.querySelector('.faq-answer');

    if (questionButton && answerDiv) {
        questionButton.addEventListener('click', () => {
            const isActive = item.classList.contains('active');
            
            // Fermer tous les autres accordéons
            faqItems.forEach(otherItem => {
                otherItem.classList.remove('active');
                otherItem.querySelector('.faq-answer').style.maxHeight = null;
            });

            // Ouvrir ou fermer l'accordéon actuel
            if (!isActive) {
                item.classList.add('active');
                answerDiv.style.maxHeight = answerDiv.scrollHeight + "px";
            } else {
                item.classList.remove('active');
                answerDiv.style.maxHeight = null;
            }
        });
    }
});

// -------------------------------------------------------------
// 6. COMPTE À REBOURS DYNAMIQUE (URGENCE)
// -------------------------------------------------------------
const timerDisplay = document.getElementById('countdownTimer');

function startCountdown(durationSeconds) {
    let timer = durationSeconds;
    setInterval(() => {
        let hours = Math.floor(timer / 3600);
        let minutes = Math.floor((timer % 3600) / 60);
        let seconds = timer % 60;

        hours = hours < 10 ? "0" + hours : hours;
        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        if (timerDisplay) {
            timerDisplay.textContent = `${hours}h : ${minutes}m : ${seconds}s`;
        }

        if (--timer < 0) {
            timer = durationSeconds; // Reset le timer pour garder l'effet d'urgence
        }
    }, 1000);
}

// Lancer le compte à rebours pour 2 heures, 14 minutes, 5 secondes (8045 secondes)
startCountdown(8045);

// -------------------------------------------------------------
// 7. FORMULAIRE : DOUBLE ENREGISTREMENT (EMAIL VIA NETLIFY + LOCAL)
// -------------------------------------------------------------
const submitButton = document.getElementById('btnSubmitOrder');

if (orderForm) {
    orderForm.addEventListener('submit', function(e) {
        e.preventDefault(); // Bloquer l'envoi classique pour traiter en JS

        // Désactiver le bouton pour éviter les doubles clics
        const currentSubmitBtn = document.getElementById('submitOrderBtn') || submitButton;
        if (currentSubmitBtn) {
            currentSubmitBtn.disabled = true;
            currentSubmitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Enregistrement...';
        }

        // Récupérer les données du formulaire en toute sécurité
        const fullNameEl = document.getElementById('fullName');
        const phoneNumberEl = document.getElementById('phoneNumber');
        const cityEl = document.getElementById('city');
        const landmarkEl = document.getElementById('landmark');
        
        const fullName = fullNameEl ? fullNameEl.value.trim() : "";
        const phoneNumber = phoneNumberEl ? phoneNumberEl.value.trim() : "";
        const city = cityEl ? cityEl.value.trim() : "";
        const landmark = landmarkEl ? landmarkEl.value.trim() : "";
        const quantityVal = quantitySelect ? quantitySelect.value : "1";
        const qtyText = quantitySelect ? pricingText[quantityVal] : pricingText["1"];
        const finalPrice = quantitySelect ? pricing[quantityVal] : pricing["1"];
        const orderId = 'order_' + Date.now() + '_' + Math.floor(Math.random() * 1000);

        // Préparer le message WhatsApp
        const whatsappMessage = `Bonjour Alfred ! Je souhaite commander le ${productName}.

Voici mes coordonnées de livraison :
👤 Nom Complet : ${fullName}
📞 Téléphone : ${phoneNumber}
📍 Ville & Quartier : ${city}
🏠 Point de repère : ${landmark ? landmark : 'Non renseigné'}
📦 Commande : ${qtyText}
💵 Total à payer : ${finalPrice}

Merci de confirmer ma commande pour la livraison !`;

        const encodedMessage = encodeURIComponent(whatsappMessage);
        const whatsappUrl = `https://wa.me/${WHATSAPP_PHONE}?text=${encodedMessage}`;

        // Mettre à jour aussi le widget WhatsApp au cas où
        const whatsappWidget = document.getElementById('whatsappWidget');
        if (whatsappWidget) {
            whatsappWidget.href = whatsappUrl;
        }

        // 1. Sauvegarde locale dans le navigateur (LocalStorage) pour historique local
        try {
            const orders = JSON.parse(localStorage.getItem('promomarket_orders') || '[]');
            orders.push({
                date: new Date().toLocaleString('fr-FR'),
                fullName: fullName,
                phoneNumber: phoneNumber,
                city: city,
                landmark: landmark,
                quantity: qtyText,
                price: finalPrice
            });
            localStorage.setItem('promomarket_orders', JSON.stringify(orders));
            console.log("Commande sauvegardée localement dans commandes.html !");
        } catch (err) {
            console.error("Erreur lors de la sauvegarde locale :", err);
        }

        // 1b. Déclencher le tracking Facebook Pixel si configuré (avec Dédoublonnement)
        let numericPrice = 15000; // Valeur par défaut
        if (quantityVal === "2") numericPrice = 27000;
        if (quantityVal === "3") numericPrice = 38000;
        if (orderForm.dataset.price1) {
            const prices = {
                "1": Number(orderForm.dataset.price1),
                "2": Number(orderForm.dataset.price2),
                "3": Number(orderForm.dataset.price3)
            };
            numericPrice = prices[quantityVal] || numericPrice;
        }

        if (typeof fbq === 'function') {
            fbq('track', 'Purchase', {
                value: numericPrice,
                currency: 'XOF',
                content_name: productName,
                content_type: 'product'
            }, { eventID: orderId });
            console.log("Événement Purchase envoyé au Pixel Facebook ! Valeur : " + numericPrice + " XOF (EventID: " + orderId + ")");
        }

        // Fonction sécurisée pour rediriger vers WhatsApp sans doublons
        let redirected = false;
        function redirectUser() {
            if (!redirected) {
                redirected = true;
                window.location.href = whatsappUrl;
            }
        }

        // Sécurité : Forcer la redirection après 4 secondes au cas où le réseau est très lent
        const fallbackTimeout = setTimeout(() => {
            console.log("Timeout de sécurité déclenché, redirection forcée.");
            redirectUser();
        }, 4000);

        // 1c. Préparer le tracking Facebook Conversions API & Envoi Supabase (Server-side via Netlify Functions)
        const capiPromise = fetch("/.netlify/functions/track-purchase", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                fullName: fullName,
                phoneNumber: phoneNumber,
                productName: productName,
                value: numericPrice,
                currency: 'XOF',
                orderId: orderId,
                quantity: Number(quantityVal),
                price: finalPrice,
                city: city,
                landmark: landmark,
                testEventCode: META_TEST_EVENT_CODE
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log("CAPI Meta Success :", data);
            return data;
        })
        .catch(error => {
            console.error("CAPI Meta Error :", error);
            return null;
        });

        // 2. Préparer l'envoi silencieux à Netlify Forms en arrière-plan
        const formData = new FormData(orderForm);
        const searchParams = new URLSearchParams();
        for (const pair of formData.entries()) {
            searchParams.append(pair[0], pair[1]);
        }
        
        const netlifyPromise = fetch("/", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: searchParams.toString()
        })
        .then(() => {
            console.log("Commande envoyée avec succès à Netlify !");
        })
        .catch(error => {
            console.error("Erreur lors de l'envoi Netlify :", error);
        });

        // Attendre que les deux requêtes soient complétées avant de rediriger
        Promise.all([netlifyPromise, capiPromise]).then(() => {
            clearTimeout(fallbackTimeout); // Annuler le timeout de sécurité
            console.log("Toutes les requêtes de tracking et formulaire terminées, redirection...");
            redirectUser();
        });
    });
}


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

// -------------------------------------------------------------
// 10. CATALOG SLIDER
// -------------------------------------------------------------
const sliderTrack = document.getElementById('sliderTrack');
let currentSlide = 0;
let slideInterval;

function getVisibleCardsCount() {
    if (window.innerWidth >= 1024) return 3;
    if (window.innerWidth >= 768) return 2;
    return 1;
}

function moveSlider(direction) {
    if (!sliderTrack) return;
    const cards = sliderTrack.querySelectorAll('.feature-card');
    const totalCards = cards.length;
    const visibleCards = getVisibleCardsCount();
    
    currentSlide += direction;
    
    if (currentSlide > totalCards - visibleCards) {
        currentSlide = 0; // loop back to start
    } else if (currentSlide < 0) {
        currentSlide = totalCards - visibleCards; // loop to end
    }
    
    const cardWidth = cards[0].offsetWidth;
    const gap = 32; // 2rem
    const shift = (cardWidth + gap) * currentSlide;
    sliderTrack.style.transform = 	ranslateX(-px);
}

function startSliderAutoPlay() {
    if (sliderTrack) {
        slideInterval = setInterval(() => {
            moveSlider(1);
        }, 4000);
    }
}

function stopSliderAutoPlay() {
    clearInterval(slideInterval);
}

if (sliderTrack) {
    startSliderAutoPlay();
    
    sliderTrack.addEventListener('mouseenter', stopSliderAutoPlay);
    sliderTrack.addEventListener('mouseleave', startSliderAutoPlay);
    
    // Pour le tactile
    sliderTrack.addEventListener('touchstart', stopSliderAutoPlay);
    sliderTrack.addEventListener('touchend', startSliderAutoPlay);
    
    // Recalculate on resize
    window.addEventListener('resize', () => {
        currentSlide = 0;
        sliderTrack.style.transform = 	ranslateX(0%);
    });
}
