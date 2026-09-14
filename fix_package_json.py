import json

data = {
  "name": "solustore",
  "version": "1.0.0",
  "description": "Boutique Solustore",
  "scripts": {
    "build": "node generate_catalog.js"
  },
  "author": "Antigravity",
  "license": "ISC"
}

with open('package.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)
