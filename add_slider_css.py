with open('style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* --- Catalog Slider Styles --- */
.slider-container {
    position: relative;
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    overflow: hidden;
    padding: 1rem 0;
}

.slider-track {
    display: flex;
    transition: transform 0.5s ease-in-out;
    gap: 2rem;
}

/* On override le CSS de la grille existante si elle est dans un slider */
.slider-track > .feature-card {
    flex: 0 0 calc(100% - 2rem);
    min-width: calc(100% - 2rem);
    margin: 0 1rem;
}

@media(min-width: 768px) {
    .slider-track > .feature-card {
        flex: 0 0 calc(50% - 2rem);
        min-width: calc(50% - 2rem);
    }
}

@media(min-width: 1024px) {
    .slider-track > .feature-card {
        flex: 0 0 calc(33.333% - 2rem);
        min-width: calc(33.333% - 2rem);
    }
}

.slider-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: var(--primary-accent);
    color: white;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
    box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    transition: all 0.3s ease;
}

.slider-btn:hover {
    background: var(--primary-color);
    transform: translateY(-50%) scale(1.1);
}

.slider-btn-prev {
    left: 10px;
}

.slider-btn-next {
    right: 10px;
}
''')
