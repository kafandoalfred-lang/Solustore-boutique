import re

with open('produit-sac.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the form block
match = re.search(r'<form name="commande-solustore".*?</form>', content, re.DOTALL)
if match:
    with open('extracted_form.txt', 'w', encoding='utf-8') as out:
        out.write(match.group(0))
    print("Form extracted successfully.")
else:
    print("Could not find the form!")
