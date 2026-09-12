with open('style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* ==========================================================================
   LANDING PAGE SPECIFIC STYLES (produit-sac.html Conversion Optimization)
   ========================================================================== */

/* Typography & General */
.landing-main {
    background: #f8fafc;
    padding-bottom: 2rem;
}

.lp-section-title {
    text-align: center;
    font-size: 2rem;
    color: var(--primary-accent);
    margin-bottom: 2.5rem;
    font-family: var(--font-heading);
}

/* 1. HERO */
.lp-hero {
    background: #ffffff;
    padding: 0;
    display: flex;
    flex-direction: column;
    border-bottom: 1px solid var(--border-soft);
}

.lp-hero-image img {
    width: 100%;
    height: auto;
    display: block;
}

.lp-hero-content {
    padding: 2rem 1.5rem;
    text-align: center;
}

.lp-badge {
    display: inline-block;
    background: rgba(30, 58, 138, 0.1);
    color: var(--primary-accent);
    font-size: 0.8rem;
    font-weight: 700;
    padding: 0.4rem 1rem;
    border-radius: 50px;
    margin-bottom: 1rem;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.lp-title {
    font-size: 2.2rem;
    color: var(--text-main);
    margin-bottom: 1rem;
    font-family: var(--font-heading);
    line-height: 1.2;
}

.lp-price-box {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.price-old {
    font-size: 1.2rem;
    color: var(--text-muted);
    text-decoration: line-through;
    font-weight: 500;
}

.price-new {
    font-size: 2.5rem;
    color: var(--success-color);
    font-weight: 800;
    font-family: var(--font-heading);
}

.lp-btn-primary {
    display: block;
    background: var(--success-color);
    color: #ffffff;
    font-size: 1.2rem;
    font-weight: 700;
    text-align: center;
    padding: 1rem 1.5rem;
    border-radius: var(--radius-md);
    text-decoration: none;
    box-shadow: 0 4px 15px rgba(5, 150, 105, 0.4);
    transition: transform 0.3s ease, background 0.3s ease;
    margin-bottom: 1.5rem;
}

.lp-btn-primary:hover {
    background: #047857;
    transform: translateY(-2px);
}

.lp-reassurance-mini {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    font-size: 0.9rem;
    color: var(--text-muted);
}
.lp-reassurance-mini span i {
    color: var(--success-color);
    margin-right: 0.5rem;
    width: 20px;
}

/* 2. VALUE PROPS (4 blocks) */
.lp-value-props {
    padding: 3rem 1.5rem;
    background: #ffffff;
    display: grid;
    grid-template-columns: 1fr;
    gap: 2rem;
}

.lp-prop {
    text-align: center;
}

.lp-prop-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.lp-prop h3 {
    font-size: 1.2rem;
    color: var(--primary-accent);
    margin-bottom: 0.5rem;
}

.lp-prop p {
    color: var(--text-muted);
    font-size: 0.95rem;
}

.lp-btn-secondary {
    display: inline-block;
    background: var(--primary-accent);
    color: #ffffff;
    font-size: 1.1rem;
    font-weight: 600;
    padding: 0.8rem 2rem;
    border-radius: var(--radius-md);
    text-decoration: none;
    transition: transform 0.2s ease;
}

/* 3. BENEFITS */
.lp-benefits {
    padding: 4rem 1.5rem;
}

.lp-benefit-row {
    display: flex;
    flex-direction: column;
    background: #ffffff;
    border-radius: var(--radius-lg);
    overflow: hidden;
    margin-bottom: 2rem;
    box-shadow: var(--shadow-sm);
}

.lp-img-wrapper img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    display: block;
}

.lp-benefit-text {
    padding: 1.5rem;
}

.lp-benefit-text h3 {
    font-size: 1.3rem;
    color: var(--text-main);
    margin-bottom: 0.5rem;
}

.lp-benefit-text p {
    color: var(--text-muted);
    font-size: 1rem;
}

/* 4. DEMO & GALLERY PLACEHOLDERS */
.lp-demo {
    background: #ffffff;
    padding: 4rem 1.5rem;
}

.lp-placeholders {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1rem;
    margin: 2rem auto 0;
    max-width: 600px;
}

.lp-ph-item {
    background: #f1f5f9;
    border: 2px dashed #cbd5e1;
    border-radius: var(--radius-md);
    height: 150px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #94a3b8;
    font-size: 0.85rem;
    text-align: center;
    padding: 1rem;
}

/* 5. CAPACITY */
.lp-capacity {
    padding: 4rem 1.5rem;
}
.lp-capacity-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    max-width: 500px;
    margin: 0 auto;
}
.capacity-item {
    background: #ffffff;
    padding: 1rem;
    border-radius: var(--radius-md);
    text-align: center;
    box-shadow: var(--shadow-sm);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
}
.capacity-item i {
    font-size: 1.5rem;
    color: var(--primary-accent);
}
.lp-placeholder-img {
    background: #e2e8f0;
    border-radius: var(--radius-lg);
    height: 250px;
    max-width: 600px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #64748b;
}

/* 6. SPECS TABLE */
.lp-specs {
    background: #ffffff;
    padding: 4rem 1.5rem;
}
.table-responsive {
    max-width: 600px;
    margin: 0 auto;
    overflow-x: auto;
}
.lp-spec-table {
    width: 100%;
    border-collapse: collapse;
}
.lp-spec-table td {
    padding: 1rem;
    border-bottom: 1px solid var(--border-soft);
}
.lp-spec-table tr td:first-child {
    font-weight: 600;
    color: var(--text-main);
    width: 40%;
}
.lp-spec-table tr td:last-child {
    color: var(--text-muted);
}

/* 7. REASSURANCE LARGE */
.lp-reassurance-large {
    padding: 4rem 1.5rem;
}
.lp-reassure-block {
    text-align: center;
    margin-bottom: 2rem;
}
.re-icon {
    width: 60px;
    height: 60px;
    background: rgba(5, 150, 105, 0.1);
    color: var(--success-color);
    font-size: 1.5rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1rem;
}
.lp-reassure-block h3 {
    margin-bottom: 0.5rem;
}

/* 8. REVIEWS */
.lp-reviews {
    background: #ffffff;
    padding: 4rem 1.5rem;
}
.lp-reviews-empty {
    text-align: center;
    color: var(--text-muted);
    font-style: italic;
}

/* 9 & 10. OFFER & ORDER */
.lp-offer-order {
    padding: 4rem 1.5rem;
    background: #eff6ff; /* slight blue tint */
}
.lp-offer-box {
    background: var(--primary-accent);
    color: #ffffff;
    padding: 2rem;
    border-radius: var(--radius-lg);
    text-align: center;
    margin-bottom: -2rem; /* Overlap with form */
    position: relative;
    z-index: 2;
    box-shadow: var(--shadow-lg);
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}
.lp-offer-box h2 {
    color: #93c5fd;
    font-size: 1rem;
    letter-spacing: 2px;
    margin-bottom: 0.5rem;
}
.lp-offer-box h3 {
    font-size: 2rem;
    margin-bottom: 1rem;
}
.lp-offer-box .price-old {
    color: #94a3b8;
}
.lp-offer-perks {
    list-style: none;
    padding: 0;
    margin-top: 1.5rem;
    text-align: left;
    display: inline-block;
}
.lp-offer-perks li {
    margin-bottom: 0.5rem;
}
.lp-offer-perks li i {
    color: var(--success-color);
    margin-right: 0.5rem;
}

.lp-form-box {
    background: #ffffff;
    padding: 4rem 1.5rem 2rem; /* Extra top padding for overlap */
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    max-width: 600px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

/* 11. FAQ */
.lp-faq {
    padding: 4rem 1.5rem;
    max-width: 700px;
    margin: 0 auto;
}
.faq-item {
    border-bottom: 1px solid var(--border-soft);
    margin-bottom: 1rem;
}
.faq-question {
    width: 100%;
    background: none;
    border: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 0;
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--text-main);
    cursor: pointer;
    text-align: left;
}
.faq-answer {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
}
.faq-answer p {
    padding-bottom: 1rem;
    color: var(--text-muted);
}
.faq-item.active .faq-answer {
    max-height: 200px;
}
.faq-item.active .faq-question i {
    transform: rotate(180deg);
}
.faq-question i {
    transition: transform 0.3s ease;
    color: var(--primary-accent);
}


/* Desktop Enhancements */
@media(min-width: 768px) {
    .lp-hero {
        flex-direction: row;
        align-items: center;
        padding: 4rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    .lp-hero-image {
        flex: 1;
    }
    .lp-hero-content {
        flex: 1;
        text-align: left;
        padding: 2rem 4rem;
    }
    .lp-price-box {
        justify-content: flex-start;
    }
    .lp-btn-primary {
        display: inline-block;
        padding: 1rem 3rem;
    }
    .lp-value-props {
        grid-template-columns: repeat(4, 1fr);
        max-width: 1200px;
        margin: 0 auto;
    }
    .lp-benefits {
        max-width: 900px;
        margin: 0 auto;
    }
    .lp-benefit-row {
        flex-direction: row;
        align-items: center;
    }
    .lp-benefit-row.reverse {
        flex-direction: row-reverse;
    }
    .lp-img-wrapper {
        flex: 1;
    }
    .lp-img-wrapper img {
        height: 100%;
    }
    .lp-benefit-text {
        flex: 1;
        padding: 3rem;
    }
    .lp-reassurance-large {
        display: flex;
        justify-content: space-around;
        max-width: 1000px;
        margin: 0 auto;
        flex-wrap: wrap;
    }
    .lp-reassure-block {
        flex: 1;
        min-width: 250px;
    }
}
''')
