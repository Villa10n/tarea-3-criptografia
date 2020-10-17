// ==UserScript==
// @name         tarea3
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://htmlpreview.github.io/?https://github.com/Villa10n/tarea-3-criptografia/blob/main/index.html
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.0.0/crypto-js.min.js
// ==/UserScript==

(function() {
    'use strict';
    const mensaje_cifrado = document.getElementsByClassName('AES-ECB')[0].id;
    console.log(mensaje_cifrado);
})();