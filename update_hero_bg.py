with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("url('essentials-poster-cyan.jpg')", "url('solustore-vitrine-banner.jpg')")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
