import os
import glob
import re

def add_tracking(html_content):
    # Match <a href="..." ...> and inject onclick
    
    # Remove existing onclick attributes to prevent duplicates if script is run multiple times
    html_content = re.sub(r'\s*onclick="gtag\([^"]+"\)', '', html_content)

    # 1. Calendly
    html_content = re.sub(
        r'(<a\s+[^>]*href=["\']https://calendly\.com[^>]*)(>)',
        r'\1 onclick="gtag(\'event\', \'schedule_meeting\', {\'event_category\': \'engagement\'});"\2',
        html_content
    )
    
    # 2. tel:
    html_content = re.sub(
        r'(<a\s+[^>]*href=["\']tel:[^>]*)(>)',
        r'\1 onclick="gtag(\'event\', \'click_to_call\', {\'event_category\': \'contact\'});"\2',
        html_content
    )
    
    # 3. sms:
    html_content = re.sub(
        r'(<a\s+[^>]*href=["\']sms:[^>]*)(>)',
        r'\1 onclick="gtag(\'event\', \'click_to_text\', {\'event_category\': \'contact\'});"\2',
        html_content
    )
    
    # 4. mailto:
    html_content = re.sub(
        r'(<a\s+[^>]*href=["\']mailto:[^>]*)(>)',
        r'\1 onclick="gtag(\'event\', \'click_email\', {\'event_category\': \'contact\'});"\2',
        html_content
    )
    
    return html_content

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = add_tracking(content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Tracking injected successfully.")
