var xhr = new XMLHttpRequest();

xhr

xhr.onreadystatechange = function() { console.log( xhr ) }

xhr.open( 'GET', 'https://otthonterkep.hu/assets/48424837/settings.json?param=', true )

xhr.send()

error: nem fogad el kérést tőlünk, nem férünk hozzá!
Ha hozzáférést akarunk, akkor meg kell keresni a doksiban az adott szerver 'get' metódusának endpoint request url-jét - ehhez lesz hozzáférésünk.

xhr.open( 'GET', 'request url', true )

xhr.send()

5 db ready state change után logol a képernyőre...

'POST' metódussal küldünk adatot

'DELETE' metódussal lehet törölni adatot

setRequestHeader: metaadatokat tartalmaz, mi a content type?

xhr.open( 'GET', 'request url', true )

xhr.setRequestHeader('Content-type', 'text/html') vagy lehet pl 'Application/json'

xhr.send()

xhr.response

lista a szerver válaszával

xhr.response[0].text - semmi nem történik, mert nem igazi lista - parse-olni kell!

console.log(JSON.parse(xhr.response));

ekkor lesz használható a lista, objektumokkal

var resp = JSON.parse(xhr.response)

resp[0].text - OK, kaptunk egy textet
resp[1].id - OK, pl. 2

'PUT' metódus: a szerveren kicserélünk egy adatot

fetch API - egyszerűbb, de kötötebb, keress rá MDN-en 'fetch API'...
fetch(myRequest).then(function(response) {
  ...
}).then(function(blob))
