import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add green pulse keyframes if not exists
if '@keyframes pulseGreen' not in css:
    green_pulse = '''
@keyframes pulseGreen {
    0% {
        box-shadow: 0 0 0 0 rgba(5, 150, 105, 0.7);
    }
    70% {
        box-shadow: 0 0 0 15px rgba(5, 150, 105, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(5, 150, 105, 0);
    }
}
'''
    css += green_pulse

# Add animation to lp-btn-primary
css = css.replace('transition: transform 0.3s ease, background 0.3s ease;', 'transition: transform 0.3s ease, background 0.3s ease;\\n    animation: pulseGreen 2s infinite;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added green pulse to lp-btn-primary.")
