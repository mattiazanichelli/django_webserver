(function () {

    const download_container = document.getElementById('download_container');
    const download = document.getElementById('download');

    download.addEventListener('click', function () {
        const p = document.createElement('p');
        p.innerText = "Your download should start in a moment";
        download_container.appendChild(p);
        download.style.display = 'none';
    });
})();

