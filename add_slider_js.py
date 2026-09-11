with open('app.js', 'a', encoding='utf-8') as f:
    f.write('''
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
    
    const offset = -(currentSlide * (100 / visibleCards));
    sliderTrack.style.transform = 	ranslateX(%);
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
''')
