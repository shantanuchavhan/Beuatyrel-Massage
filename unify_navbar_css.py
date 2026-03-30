import os
import re

navbar_css = """
/* UNIVERSAL NAVBAR STYLES */
.navbar { position: fixed; top: 0; left: 0; width: 100%; padding: 12px 0; z-index: 1000; transition: all 0.4s ease; background: rgba(255, 255, 255, 0.98); box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
.navbar.scrolled { backdrop-filter: blur(10px); padding: 8px 0; box-shadow: 0 5px 20px rgba(212, 90, 122, 0.15); background: rgba(255,255,255,0.95); }
.nav-container { max-width: 1200px; margin: 0 auto; padding: 0 30px; display: flex; justify-content: space-between; align-items: center; }
.logo img { height: 60px; transition: all 0.3s ease; }
.nav-links { display: flex; align-items: center; gap: 28px; }
.nav-attribute { color: #3e2a2f; text-decoration: none; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; transition: all 0.3s; position: relative; }
.nav-attribute::after { content: ''; position: absolute; bottom: -6px; left: 0; width: 0; height: 2px; background: #d45a7a; transition: width 0.3s ease; }
.nav-attribute:hover::after, .nav-attribute.active::after { width: 100%; }
.nav-attribute:hover, .nav-attribute.active { color: #d45a7a; }
.cart-icon { position: relative; display: flex; align-items: center; }
.cart-icon i { font-size: 16px; }
.cart-count { position: absolute; top: -10px; right: -14px; background: linear-gradient(135deg, #d45a7a, #b34262); color: white; font-size: 10px; font-weight: bold; padding: 2px 6px; border-radius: 50%; animation: pulse 1.5s infinite; border: 2px solid white; }
@keyframes pulse { 0% { transform: scale(1); } 50% { transform: scale(1.15); } 100% { transform: scale(1); } }
.hamburger, .sidebar, .overlay { display: none; }
@media (max-width: 768px) {
    .hamburger { display: block; cursor: pointer; z-index: 1001; }
    .hamburger span { display: block; width: 26px; height: 2px; background: #b34262; margin: 6px 0; transition: 0.3s; border-radius: 2px; }
    .navbar.scrolled .hamburger span { background: #d45a7a; }
    .sidebar { position: fixed; top: 0; left: -300px; width: 280px; height: 100%; background: linear-gradient(145deg, #fff9fb, #fff0f4); padding: 90px 28px 30px; display: flex; flex-direction: column; gap: 18px; transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1); z-index: 10000; box-shadow: 4px 0 20px rgba(0,0,0,0.1); }
    .sidebar.active { left: 0; }
    .sidebar a { color: #3e2a2f; text-decoration: none; font-size: 16px; font-weight: 600; padding: 12px 0; border-bottom: 1px solid rgba(212, 90, 122, 0.1); display: flex; align-items: center; gap: 12px; transition: 0.3s; }
    .sidebar a:hover, .sidebar a.active { color: #d45a7a; padding-left: 5px; }
    .sidebar .close-btn { position: absolute; top: 20px; right: 24px; font-size: 28px; cursor: pointer; color: #b34262; transition: 0.3s; }
    .sidebar .close-btn:hover { transform: rotate(90deg); color: #d45a7a; }
    .overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); opacity: 0; visibility: hidden; transition: 0.3s; z-index: 9999; backdrop-filter: blur(3px); }
    .overlay.active { opacity: 1; visibility: visible; }
    .nav-links { display: none !important; }
}
@media (min-width: 769px) { .hamburger, .sidebar, .overlay { display: none !important; } .nav-links { display: flex !important; } }
"""

def update_file(filepath):
    if not filepath.endswith('.html') or filepath.endswith('tetro.html'):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    # We want to insert the completely unified CSS just before </style> to override previous properties.
    # But wait, maybe inline styles have higher specificity? We can just append !important to standard properties?
    # No, since we append to the deeply bottom of <style>, it cleanly overrides if same specificity.
    
    # Actually, the safest is to strip out blocks related to ".navbar", ".logo", ".nav-links", ".sidebar" etc using naive removal
    # 1. Remove blocks starting with .navbar { ... } iteratively.
    
    patterns_to_remove = [
        r'\.navbar\s*\{[^}]*\}',
        r'\.navbar\.scrolled\s*\{[^}]*\}',
        r'\.nav-container\s*\{[^}]*\}',
        r'\.nav-links\s*a?\s*\{[^}]*\}',
        r'\.nav-attribute\s*\{[^}]*\}',
        r'\.nav-attribute::after\s*\{[^}]*\}',
        r'\.nav-attribute:hover::after,\s*\.nav-attribute\.active::after\s*\{[^}]*\}',
        r'\.nav-attribute:hover,\s*\.nav-attribute\.active\s*\{[^}]*\}',
        r'\.navbar\.scrolled\s*\.nav-attribute\s*\{[^}]*\}',
        r'\.logo\s*img\s*\{[^}]*\}',
        r'\.hamburger,\s*\.sidebar,\s*\.overlay\s*\{[^}]*\}',
        r'@media\s*\([^)]+\)\s*\{\s*\.hamburger\s*\{[^}]*\}\s*\.hamburger\s*span\s*\{[^}]*\}\s*\.navbar\.scrolled\s*\.hamburger\s*span\s*\{[^}]*\}\s*\.sidebar\s*\{[^}]*\}\s*\.sidebar\.active\s*\{[^}]*\}\s*\.sidebar\s*a\s*\{[^}]*\}\s*\.sidebar\s*\.close-btn\s*\{[^}]*\}\s*\.overlay\s*\{[^}]*\}\s*\.overlay\.active\s*\{[^}]*\}\s*\.nav-links\s*\{[^}]*\}\s*\}',
        r'@media\s*\([^)]+\)\s*\{\s*\.hamburger,\s*\.sidebar,\s*\.overlay\s*\{[^}]*\}\s*\.nav-links\s*\{[^}]*\}\s*\}'
    ]
    
    for pattern in patterns_to_remove:
        content = re.sub(pattern, '', content, flags=re.MULTILINE)

    # Clean up random leftover CSS rules if we missed any, specifically for sidebar matching like:
    content = re.sub(r'\.sidebar\s*[^{]*\{[^}]*\}', '', content)
    content = re.sub(r'\.hamburger\s*[^{]*\{[^}]*\}', '', content)
    content = re.sub(r'\.overlay\s*[^{]*\{[^}]*\}', '', content)

    # Insert the master CSS block right before </style>
    if 'UNIVERSAL NAVBAR STYLES' not in content:
        content = content.replace('</style>', navbar_css + '\n</style>')
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Updated CSS in {filepath}")

if __name__ == '__main__':
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'tetro.html']
    for filename in html_files:
        update_file(filename)
