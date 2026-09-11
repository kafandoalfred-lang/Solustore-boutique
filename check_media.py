import re
with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Find media queries
matches = re.finditer(r'@media\s*\(max-width:\s*768px\)\s*\{([^}]|\}[^{])*\}', content, re.DOTALL)
for match in matches:
    print(match.group(0))
