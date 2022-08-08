let body = document.querySelector('html');
body.addEventListener('click', function () {
    body.style.background = "#" + ((1 << 24) * Math.random() | 0).toString(16);
});
