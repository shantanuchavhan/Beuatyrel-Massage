import os
import re

directory = '/Users/shantanu/Desktop/infotechproject/'

# Regex pattern to find the .tetro-footer background and replace it
pattern = re.compile(r'\.tetro-footer\s*\{([^\}]*)background:\s*#142435;', re.DOTALL)
replacement = r'.tetro-footer {\1background: linear-gradient(135deg, #d45a7a, #b34262);'

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()
            
        updated_content = pattern.sub(replacement, content)
        
        # also check for hardcoded old inline backgrounds if any, but the user specifically asked for footer
        
        if updated_content != content:
            with open(filepath, 'w') as file:
                file.write(updated_content)
            print(f"Updated footer color in {filename}")
