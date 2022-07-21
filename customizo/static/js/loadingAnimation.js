(function () {

    for (let elem of document.querySelectorAll('*')) {
        elem.addEventListener('click', e => {
            if (e.target.id == "register_submit") {
                createDownloadableContent();
            }
        }, true);
        break;
    }

    function createDownloadableContent() {
        const submit = document.getElementById("register_submit");
        const loading = document.getElementById("loading");
        loading.style.display = 'none';
        submit.addEventListener('click', () => {
            submit.style.display = 'none';
            loading.style.display = '';
        });
    }

    window.onunload = function () {
        document.body.removeEventListener('click', () => {
            loading.style.display = 'none';
        });
    }

})();