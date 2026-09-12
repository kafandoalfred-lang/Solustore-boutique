with open('style.css', 'a', encoding='utf-8') as f:
    f.write('''
/* ==========================================================================
   ORDER MODAL STYLES
   ========================================================================== */
.modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(4px);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 1rem;
}

.modal-content {
    background: #ffffff;
    width: 100%;
    max-width: 500px;
    border-radius: var(--radius-lg);
    position: relative;
    max-height: 90vh;
    overflow-y: auto;
    box-shadow: var(--shadow-xl);
    padding: 1rem;
    animation: slideUp 0.3s ease-out;
}

.modal-close {
    position: absolute;
    top: 10px;
    right: 15px;
    font-size: 2rem;
    line-height: 1;
    color: var(--text-muted);
    cursor: pointer;
    z-index: 10;
    transition: color 0.2s;
}

.modal-close:hover {
    color: var(--primary-accent);
}

@keyframes slideUp {
    from { transform: translateY(50px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}
''')
