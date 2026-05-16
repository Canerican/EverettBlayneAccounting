import os
import glob
import re

footer_html = """    <footer>
        <div class="container">
            <div class="footer-logo">Everett<span>Blayne</span></div>
            <div class="footer-links">
                <a href="index.html">Home</a>
                <a href="monthly-accounting.html">Accounting</a>
                <a href="payroll.html">Payroll</a>
                <a href="consultations.html">Consultations</a>
                <a href="about.html">About</a>
            </div>
            <div class="footer-copyright">
                &copy; 2026 EverettBlayne CPAs & Business Advisors. All rights reserved.
            </div>
        </div>
    </footer>"""

css_to_add = """
        /* --- Footer --- */
        footer { background: white; padding: 4rem 0 2rem 0; text-align: center; border-top: 1px solid var(--border-light); }
        .footer-logo { font-family: var(--font-logo); font-size: 1.8rem; font-weight: 800; font-style: italic; color: var(--brand-navy); margin-bottom: 1rem; }
        .footer-links { display: flex; justify-content: center; gap: 2rem; margin-bottom: 2rem; }
        .footer-links a { color: var(--text-body); transition: color 0.3s; }
        .footer-links a:hover { color: var(--brand-ruby); }
        .footer-copyright { color: var(--text-muted); font-size: 0.9rem; }
"""

for filepath in glob.glob('*.html'):
    if filepath == 'index.html':
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace simple footer
    content = re.sub(r'<footer>.*?</footer>', footer_html, content, flags=re.DOTALL)

    # replace simple footer css
    content = re.sub(r'/\* --- Footer --- \*/.*?}', css_to_add, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated footers successfully.")
