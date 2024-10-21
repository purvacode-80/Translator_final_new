document.getElementById('translateForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const textInput = document.getElementById('textInput').value;
    const destLang = document.getElementById('languageSelect').value;

    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'text': textInput,
            'dest_lang': destLang,
            'source_lang': 'en' // Source language set to English by default
        })
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('outputText').value = data;
    });
});
