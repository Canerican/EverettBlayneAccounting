import glob

replacements = [
    (
        "onclick=\"gtag('event', 'click_to_call', {'event_category': 'contact'});\"",
        "onclick=\"gtag('event', 'conversion', {'send_to': 'AW-18085429312/18qRCMXBma4cEMCA569D'});\""
    ),
    (
        "onclick=\"gtag('event', 'click_to_text', {'event_category': 'contact'});\"",
        "onclick=\"gtag('event', 'conversion', {'send_to': 'AW-18085429312/qwwOCMjBma4cEMCA569D'});\""
    ),
    (
        "onclick=\"gtag('event', 'click_email', {'event_category': 'contact'});\"",
        "onclick=\"gtag('event', 'conversion', {'send_to': 'AW-18085429312/GG8mCKHHma4cEMCA569D'});\""
    )
]

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_str, new_str in replacements:
        content = content.replace(old_str, new_str)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated all remaining tracking codes successfully.')
