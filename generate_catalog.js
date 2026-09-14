const fs = require('fs');

try {
    let rawdata = fs.readFileSync('products.json', 'utf8');
    if (rawdata.charCodeAt(0) === 0xFEFF) {
        rawdata = rawdata.slice(1);
    }
    const products = JSON.parse(rawdata);
    const headers = ['id', 'title', 'description', 'availability', 'condition', 'price', 'link', 'image_link', 'brand'];
    
    const rows = products.map(p => {
        return headers.map(header => {
            let val = p[header] || '';
            val = val.replace(/"/g, '""');
            return `"${val}"`;
        }).join(',');
    });

    const csvContent = headers.join(',') + '\n' + rows.join('\n');
    fs.writeFileSync('catalog.csv', csvContent, 'utf8');
    console.log('✅ catalog.csv généré avec succès !');
} catch (error) {
    console.error('❌ Erreur lors de la génération:', error);
    process.exit(1);
}
