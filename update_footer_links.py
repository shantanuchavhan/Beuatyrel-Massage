import os
import re

directory = '/Users/shantanu/Desktop/infotechproject/'

new_quick_links = """                <div class="footer-quick-links">
                    <a href="about.html"><i class="fas fa-angle-right"></i>About Us</a>
                    <a href="products.html"><i class="fas fa-angle-right"></i>Shop Products</a>
                    <a href="gallery.html"><i class="fas fa-angle-right"></i>Gallery</a>
                    <a href="contact.html"><i class="fas fa-angle-right"></i>Contact Us</a>
                    <a href="#"><i class="fas fa-angle-right"></i>Terms & Conditions</a>
                    <a href="#"><i class="fas fa-angle-right"></i>Privacy Policy</a>
                    <a href="#"><i class="fas fa-angle-right"></i>Refund & Return Policy</a>
                </div>"""

# Regex pattern to find the .footer-quick-links block
pattern = re.compile(r'<div class="footer-quick-links">.*?</div>', re.DOTALL)

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Replace the quick links section
        updated_content = pattern.sub(new_quick_links, content)
        
        # Write back to file if changed
        if updated_content != content:
            with open(filepath, 'w') as file:
                file.write(updated_content)
            print(f"Updated footer links in {filename}")
