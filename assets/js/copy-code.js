(function () {
    function createButton() {
        var button = document.createElement('button');
        button.className = 'copy-code-btn';
        button.type = 'button';
        button.setAttribute('aria-label', 'Copy code');
        button.textContent = 'Copy';
        return button;
    }

    function wrapPre(pre) {
        var wrapper = document.createElement('div');
        wrapper.className = 'code-block';
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.appendChild(pre);
        return wrapper;
    }

    function getCodeText(pre) {
        var code = pre.querySelector('code');
        return (code ? code.innerText : pre.innerText).trim();
    }

    function attachCopy(pre) {
        var wrapper = wrapPre(pre);
        var btn = createButton();
        wrapper.insertBefore(btn, wrapper.firstChild);
        btn.addEventListener('click', function () {
            var text = getCodeText(pre);
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(text).then(function () {
                    btn.textContent = 'Copied!';
                    setTimeout(function () { btn.textContent = 'Copy'; }, 1200);
                }, function () {
                    fallbackCopy(text, btn);
                });
            } else {
                fallbackCopy(text, btn);
            }
        });
    }

    function fallbackCopy(text, btn) {
        var textarea = document.createElement('textarea');
        textarea.value = text;
        textarea.style.position = 'fixed';
        textarea.style.top = '-1000px';
        document.body.appendChild(textarea);
        textarea.focus();
        textarea.select();
        try {
            document.execCommand('copy');
            btn.textContent = 'Copied!';
        } catch (e) {
            btn.textContent = 'Error';
        }
        setTimeout(function () { btn.textContent = 'Copy'; }, 1200);
        document.body.removeChild(textarea);
    }

    function init() {
        var pres = document.querySelectorAll('pre');
        for (var i = 0; i < pres.length; i++) {
            attachCopy(pres[i]);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();


