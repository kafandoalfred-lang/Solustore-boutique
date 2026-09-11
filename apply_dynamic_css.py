import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove slider styles
content = re.sub(r'/\* --- Catalog Slider Styles --- \*/.*', '', content, flags=re.DOTALL)

# Add dynamic card styles
content += '''/* --- Dynamic Cards Styles --- */
.dynamic-card {
    transition: all 0.3s ease;
}

.fade-in {
    animation: fadeContent 0.5s ease-in-out forwards;
}

@keyframes fadeContent {
    0% {
        opacity: 0.3;
        transform: translateY(2px);
    }
    100% {
        opacity: 1;
        transform: translateY(0);
    }
}
'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
