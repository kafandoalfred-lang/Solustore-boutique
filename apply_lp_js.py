with open('app.js', 'a', encoding='utf-8') as f:
    f.write('''
// -------------------------------------------------------------
// 11. FAQ ACCORDION
// -------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const item = question.parentElement;
            const isActive = item.classList.contains('active');
            
            // Close all
            document.querySelectorAll('.faq-item').forEach(faq => {
                faq.classList.remove('active');
            });
            
            // Open if wasn't active
            if (!isActive) {
                item.classList.add('active');
            }
        });
    });
});
''')
