// EverettBlayne site script: mobile menu + lead forms. Used by every page.
//
// FORMS: Web3Forms access key (web3forms.com). This one key covers every form on the
// site; leads are emailed to the address the key was created with.
var WEB3FORMS_ACCESS_KEY = '23de7105-8719-45aa-aa1f-7d4beb0d8aba';
var LEAD_EMAIL = 'everettbirving@gmail.com';

(function () {
    function track() { if (typeof gtag === 'function') gtag.apply(null, arguments); }

    // Mobile menu (only on pages that have one)
    var btn = document.getElementById('hamburgerBtn');
    var menu = document.getElementById('mobileMenu');
    var close = document.getElementById('mobileClose');
    if (btn && menu && close) {
        var setOpen = function (open) {
            menu.classList.toggle('open', open);
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
            document.body.style.overflow = open ? 'hidden' : '';
            if (open) close.focus();
        };
        btn.addEventListener('click', function () { setOpen(true); });
        close.addEventListener('click', function () { setOpen(false); btn.focus(); });
        menu.querySelectorAll('a[href^="#"], .js-close-menu').forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
        document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu.classList.contains('open')) { setOpen(false); btn.focus(); } });
    }

    // Lead forms: send through Web3Forms, then go to thank-you.html (where the Google Ads conversion counts).
    document.querySelectorAll('.lead-form').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            var status = form.querySelector('.form-status');
            var button = form.querySelector('.form-submit');
            var label = button.textContent;
            status.className = 'form-status';
            status.textContent = '';

            if (!form.checkValidity()) {
                var firstBad = form.querySelector(':invalid');
                status.className = 'form-status error';
                status.textContent = firstBad && firstBad.type === 'email' ? 'Enter a valid email address so I can reply.' : 'Fill in the fields marked with *.';
                if (firstBad) firstBad.focus();
                return;
            }

            var data = new FormData(form);
            var name = ((data.get('first_name') || '') + ' ' + (data.get('last_name') || '')).trim();
            var page = form.getAttribute('data-page') || document.title;
            var service = data.get('service') || 'General';
            var detail = data.get('months_behind') || data.get('stage') || data.get('employees') || '';
            var subject = 'New lead: ' + service + (detail ? ' (' + detail + ')' : '') + ' - ' + name;

            if (WEB3FORMS_ACCESS_KEY.indexOf('PASTE_') === 0) {
                var lines = [];
                data.forEach(function (v, k) { if (k !== 'botcheck' && v) lines.push(k.replace(/_/g, ' ') + ': ' + v); });
                window.location.href = 'mailto:' + LEAD_EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(lines.join('\n'));
                status.textContent = 'Your email app should open with your message. Press send there to finish.';
                return;
            }

            data.append('access_key', WEB3FORMS_ACCESS_KEY);
            data.append('subject', subject);
            data.append('from_name', 'EverettBlayne website');
            data.append('page', page);
            button.disabled = true;
            button.textContent = 'Sending...';

            fetch('https://api.web3forms.com/submit', { method: 'POST', body: data, headers: { 'Accept': 'application/json' } })
                .then(function (r) { return r.json(); })
                .then(function (res) {
                    if (!res.success) throw new Error(res.message || 'Send failed');
                    track('event', 'generate_lead', { 'event_category': 'engagement', 'event_label': page });
                    window.location.href = 'thank-you.html';
                })
                .catch(function () {
                    button.disabled = false;
                    button.textContent = label;
                    status.className = 'form-status error';
                    status.innerHTML = 'Your message didn\'t go through. Please call or text <a href="tel:+13852364087">(385) 236-4087</a> or email <a href="mailto:' + LEAD_EMAIL + '">' + LEAD_EMAIL + '</a>.';
                });
        });
    });
})();
