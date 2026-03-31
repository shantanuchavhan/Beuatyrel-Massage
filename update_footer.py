import os
import re

footer_html = """<footer class="footer-footer">
    <div class="footer-footer-container">
        <div class="footer-footer-row">
            <div class="footer-footer-col col-brand">
                <a href="index.html" class="footer-brand">
                    <h2>Rose Embroidery</h2>
                </a>
                <p>Trusted provider of high-performance embroidery machinery, dedicated to elevating craftsmanship with precision and quality.</p>
                <div class="footer-social-links">
                    <a href="#"><i class="fab fa-instagram"></i></a>
                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-linkedin-in"></i></a>
                </div>
            </div>
            
            <div class="footer-footer-col col-links">
                <h3>Quick Links</h3>
                <div class="footer-quick-links">
                    <a href="about.html"><i class="fas fa-angle-right"></i>About Us</a>
                    <a href="products.html"><i class="fas fa-angle-right"></i>Shop Products</a>
                    <a href="gallery.html"><i class="fas fa-angle-right"></i>Gallery</a>
                    <a href="contact.html"><i class="fas fa-angle-right"></i>Contact Us</a>
                    <a href="#"><i class="fas fa-angle-right"></i>Privacy Policy</a>
                </div>
            </div>
            
            <div class="footer-footer-col col-contact">
                <h3>Contact Info</h3>
                <div class="footer-contact-info">
                    <a href="#"><i class="fas fa-map-marker-alt"></i>76 first avenue millenium town adayalampattu madhuravoyal chennai 600095</a>
                    <a href="tel:+91902555206"><i class="fas fa-phone-alt"></i>+91 902555206</a>
                    <a href="mailto:Drroslineg@gmail.com"><i class="fas fa-envelope"></i>Drroslineg@gmail.com</a>
                    <p><i class="fas fa-clock"></i>Mon-Sat: 9AM - 7PM</p>
                </div>
            </div>
        </div>
        <hr class="footer-footer-divider">
        <div class="footer-footer-bottom">
            <div class="footer-copyright">
                <i class="fas fa-copyright"></i> <span id="copyright-year">2026</span> <a href="index.html">Rose Embroidery</a>. All rights reserved.
            </div>
            <div class="footer-tagline">
                Quality Precision Trust
            </div>
        </div>
    </div>
</footer>"""

css_addition = """
        /* footer-style Footer */
        .footer-footer {
            background: #212529;
            color: #fff;
            padding: 70px 0 30px;
            font-family: 'Montserrat', sans-serif;
            text-align: left;
        }
        .footer-footer-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 30px;
        }
        .footer-footer-row {
            display: flex;
            flex-wrap: wrap;
            gap: 40px;
            margin-bottom: 40px;
        }
        .footer-footer-col {
            flex: 1;
            min-width: 280px;
        }
        .footer-footer-col.col-brand p {
            color: #f8f9fa;
            line-height: 1.8;
            margin-bottom: 25px;
            font-size: 15px;
            opacity: 0.9;
        }
        .footer-brand {
            text-decoration: none;
            display: inline-block;
            margin-bottom: 20px;
        }
        .footer-brand h2 {
            color: #fff;
            font-weight: 700;
            font-size: 32px;
            font-family: 'Montserrat', sans-serif;
            margin: 0;
        }
        .footer-brand span {
            color: #d45a7a;
        }
        .footer-social-links {
            display: flex;
            gap: 12px;
        }
        .footer-social-links a {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: #fff;
            color: #d45a7a;
            border-radius: 8px;
            text-decoration: none;
            transition: all 0.3s ease;
            font-size: 18px;
        }
        .footer-social-links a:hover {
            background: #d45a7a;
            color: #fff;
            transform: translateY(-3px);
        }
        .footer-footer-col h3 {
            color: #d45a7a;
            font-size: 24px;
            margin-bottom: 25px;
            font-weight: 600;
            font-family: 'Montserrat', sans-serif;
        }
        .footer-quick-links {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        .footer-quick-links a {
            color: #fff;
            text-decoration: none;
            font-size: 15px;
            transition: 0.3s;
            display: flex;
            align-items: center;
            opacity: 0.9;
        }
        .footer-quick-links a i {
            color: #d45a7a;
            margin-right: 12px;
            font-size: 12px;
        }
        .footer-quick-links a:hover {
            color: #d45a7a;
            padding-left: 8px;
            opacity: 1;
        }
        .footer-contact-info {
            display: flex;
            flex-direction: column;
            gap: 0;
        }
        .footer-contact-info a, .footer-contact-info p {
            color: #fff;
            text-decoration: none;
            font-size: 15px;
            display: flex;
            align-items: flex-start;
            border-bottom: 1px solid rgba(255,255,255,0.1);
            padding: 16px 0;
            margin: 0;
            line-height: 1.5;
            opacity: 0.9;
        }
        .footer-contact-info a:first-child {
            padding-top: 0;
        }
        .footer-contact-info a:last-child, .footer-contact-info p:last-child {
            border-bottom: none;
            padding-bottom: 0;
        }
        .footer-contact-info i {
            color: #d45a7a;
            margin-right: 15px;
            margin-top: 4px;
            width: 16px;
            text-align: center;
        }
        .footer-contact-info a:hover {
            color: #d45a7a;
            opacity: 1;
        }
        .footer-footer-divider {
            border: none;
            height: 1px;
            background: rgba(255,255,255,0.1);
            margin: 0 0 25px 0;
        }
        .footer-footer-bottom {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }
        .footer-copyright {
            color: #fff;
            font-size: 14px;
            opacity: 0.8;
        }
        .footer-copyright a {
            color: #d45a7a;
            text-decoration: none;
            font-weight: 500;
        }
        .footer-copyright a:hover {
            text-decoration: underline;
        }
        .footer-tagline {
            color: #fff;
            font-size: 14px;
            opacity: 0.8;
            font-weight: 500;
        }
        @media (max-width: 768px) {
            .footer-footer-row {
                flex-direction: column;
                gap: 30px;
            }
            .footer-footer-bottom {
                flex-direction: column;
                text-align: center;
                gap: 10px;
            }
        }
"""

def update_file(filepath):
    if not filepath.endswith('.html') or filepath.endswith('footer.html'):
        return

    with open(filepath, 'r') as f:
        content = f.read()
    
    # 1. Replace <footer> tag completely
    # Sometimes it has class, sometimes it's just <footer>...</footer>, and could be multiline.
    # regex to find from <footer to </footer>
    pattern = re.compile(r'<footer.*?</footer>', re.DOTALL)
    if not pattern.search(content):
        print(f"Failed to find footer in {filepath}")
        return
    else:
        content = pattern.sub(footer_html, content)
        
    # 2. Add CSS
    if '.footer-footer {' not in content:
        content = content.replace('</style>', css_addition + '\n    </style>')
        
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"Success: Updated {filepath}")

if __name__ == '__main__':
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'footer.html']
    for filename in html_files:
        update_file(filename)
