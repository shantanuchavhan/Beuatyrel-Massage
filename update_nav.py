import os
import re

nav_html = """<nav class="navbar" id="navbar">
    <div class="nav-container">
        <div class="logo"><a href="./index.html"><img src="./images/logo.png" alt="Rose Embroidery"></a></a><div></div>
        <div class="nav-links">
            <a class="nav-attribute" href="index.html">Home</a>
            <a class="nav-attribute" href="about.html">About</a>
            <a class="nav-attribute" href="products.html">Shop</a>
            <a class="nav-attribute" href="gallery.html">Gallery</a>
            <a class="nav-attribute" href="contact.html">Contact</a>
            <a class="nav-attribute" href="login.html"><i class="fas fa-user"></i> Login</a>
            <a class="nav-attribute cart-icon" href="cart.html">
                <i class="fas fa-shopping-cart"></i> 
                <span class="cart-count" id="cartCount">0</span>
            </a>
        </div>
        <div class="hamburger" onclick="toggleMenu()"><span></span><span></span><span></span></div>
    </div>
</nav>
<div class="sidebar" id="sidebar">
    <div class="close-btn" onclick="toggleMenu()">✕</div>
    <a href="index.html"><i class="fas fa-home"></i> Home</a>
    <a href="about.html"><i class="fas fa-info-circle"></i> About</a>
    <a href="products.html"><i class="fas fa-box"></i> Shop</a>
    <a href="gallery.html"><i class="fas fa-images"></i> Gallery</a>
    <a href="contact.html"><i class="fas fa-envelope"></i> Contact</a>
    <a href="login.html"><i class="fas fa-user"></i> Login</a>
    <a href="cart.html"><i class="fas fa-shopping-cart"></i> Cart <span id="mobileCartCount">0</span></a>
</div>
<div class="overlay" id="overlay" onclick="toggleMenu()"></div>"""

js_addition = """
    // Update cart count from localStorage
    function updateCartCount() {
        let cart = JSON.parse(localStorage.getItem('cart')) || [];
        let totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
        const cartCountSpan = document.getElementById('cartCount');
        const mobileCartSpan = document.getElementById('mobileCartCount');
        if (cartCountSpan) cartCountSpan.innerText = totalItems;
        if (mobileCartSpan) mobileCartSpan.innerText = totalItems;
    }
    
    // Initialize cart count
    updateCartCount();
    
    // Listen for storage changes (when cart updates from other pages)
    window.addEventListener('storage', function(e) {
        if (e.key === 'cart') {
            updateCartCount();
        }
    });
"""

css_addition = """
        .cart-icon { position: relative; }
        .cart-count {
            position: absolute;
            top: -8px;
            right: -12px;
            background: #ff6b9d;
            color: white;
            font-size: 10px;
            font-weight: bold;
            padding: 2px 6px;
            border-radius: 50%;
            animation: pulse 1.5s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }"""

def update_file(filepath):
    if filepath.endswith('index.html') or not filepath.endswith('.html'):
        return

    with open(filepath, 'r') as f:
        content = f.read()

    print(f"Processing {filepath}...")
    
    # 1. Replace nav
    # The current <nav> to <div class="overlay"...></div>
    # Using regex search to replace
    pattern = re.compile(r'<nav class="navbar".*?<div class="overlay".*?</div>', re.DOTALL)
    
    # Check if the exact pattern exists
    if not pattern.search(content):
        # Fallback 1: Maybe overlay doesn't have same quote style or spacing
        pattern2 = re.compile(r'<nav class="navbar".*?</nav>\s*<div class="sidebar[a-zA-Z0-9\s="-]*>.*?</div>\s*<div class="overlay[a-zA-Z0-9\s="-]*></div>', re.DOTALL)
        if pattern2.search(content):
            content = pattern2.sub(nav_html, content)
        else:
            # Fallback 2: Just replace <nav class="navbar"...</nav> and append sidebar and overlay if missing?
            pattern3 = re.compile(r'<nav class="navbar".*?</nav>', re.DOTALL)
            if pattern3.search(content):
                print(f"  Fallback 2 engaged for {filepath}")
                content = pattern3.sub(nav_html, content)
                # Next we need to remove old sidebar and overlay if they exist randomly
                content = re.sub(r'<div class="sidebar".*?</div>', '', content, flags=re.DOTALL)
                content = re.sub(r'<div class="overlay".*?</div>', '', content, flags=re.DOTALL)
            else:
                print(f"  Failed: Could not find nav in {filepath}")
                return
    else:
        content = pattern.sub(nav_html, content)

    # 2. Add active class
    filename = os.path.basename(filepath)
    content = content.replace(f'<a class="nav-attribute" href="{filename}">', f'<a class="nav-attribute active" href="{filename}">')

    # 3. Add CSS
    if '.cart-icon {' not in content:
        content = content.replace('</style>', css_addition + '\n    </style>')

    # 4. Add JavaScript
    if 'updateCartCount()' not in content:
        if '</script>' in content:
            # We'll inject just before the last </script>
            # Or better, just append it before </body> inside its own <script>
            content = content.replace('</body>', '<script>' + js_addition + '\n</script>\n</body>')
        else:
            content = content.replace('</body>', '<script>' + js_addition + '\n</script>\n</body>')
            
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"  Success: Updated {filepath}")

if __name__ == '__main__':
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    print(f"Found HTML files: {html_files}")
    for filename in html_files:
        update_file(filename)
