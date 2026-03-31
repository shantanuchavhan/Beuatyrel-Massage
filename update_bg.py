import os
import re

directory = '/Users/shantanu/Desktop/infotechproject/'

pattern = re.compile(r'\.footer-footer\s*\{\s*background:\s*#142435;')
replacement = r'.footer-footer {\n      background: linear-gradient(135deg, #d45a7a, #b34262);'

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()
            
        updated_content = pattern.sub(replacement, content)
        
        # also make sure text color is white explicitly inside footer-footer
        # but the CSS already has `color: #fff;` under .footer-footer
        
        if updated_content != content:
            with open(filepath, 'w') as file:
                file.write(updated_content)
            print(f"Updated footer color in {filename}")
