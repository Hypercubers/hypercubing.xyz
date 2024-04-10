function replaceSymbols(event){
    document.querySelectorAll('span[data-replace]')
        .forEach(span => {
            span.innerHTML = span.dataset.replace;
        });
}

// do it twice, once when the script loads and once when the document loads
// so it always replaces the symbols properly
replaceSymbols();
document.addEventListener('load', replaceSymbols);