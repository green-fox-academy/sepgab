'use strict'

var paragraphs = document.querySelectorAll('body p');

paragraphs[1].innerHTML = paragraphs[0].innerText;
paragraphs[2].innerHTML = paragraphs[0].innerHTML;
