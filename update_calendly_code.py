import glob

old_str = "onclick=\"gtag('event', 'schedule_meeting', {'event_category': 'engagement'});\""
new_str = "onclick=\"gtag('event', 'conversion', {'send_to': 'AW-18085429312/Qm-SCJnksa4cEMCA569D'});\""

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(old_str, new_str)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated Calendly tracking codes successfully.')
