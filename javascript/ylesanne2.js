// Sten Soomre
// 2023-12-13
// Ülesanne  2

// Kellaaeg
let tunnid = 12;    // See on
let minutid = 14;   // Hetkene
let sekundid = 59;  // Aeg

let kokku = tunnid + ":" + minutid + ":" + sekundid +"PM"; // Liidab
console.log(kokku); // Väljastab

// Tsitaat
let tsitaat = "Magamine on nõrkadele"                         // faktid ofc ofc
let paremversioon = "Tark Inimene - " + "\"" + tsitaat + "\"" // Kui sa sellest osast aru ei saa, on sinuga midagi tõsist viga
console.log(paremversioon)                                    // Väljastab  naq ikka :)

// Mallide kasutamine
let esinimi = "Sten"
let perenimi = "Soomre"

let initals = esinimi.charAt(0) + "." + perenimi.charAt(0) + "."
console.log(`${esinimi} ${perenimi} nimetähed on ${initals}`) // Template literals on tüütu kasutada, sest see char mis selle aktiveerib on halvas kohas :c


// Perenime pikkus
const muutuja = "Perenimi, Esinimi"                  // Peale vaadates saad aru :)
let koma = muutuja.charAt(muutuja.indexOf(","))      // otsib muutujast , asukoha ja siis selle asukohaga annab endale , väärtuse
let erastus = muutuja.split(koma)[0]                 // Splitib teksti kuni , ja annab endale väärtuse, esimese spliti järgi
console.log(erastus.length)                          // Vaata loogiliselt peale ja mõtle, kas actully sa sellest aru ei saa?

// E-posti aadressi muutmine
let email = "sten.soomre1@gmail.com"
let muutus = email.split("@")[0] + "@metshein.com"; // Otsib @ muutujas ja sealt tekitab kaks varianti, millest valib esimese ja lisab selle lõppu @metshein.com
console.log(muutus)                                 // Väljastus 

// Andmerida analüüs
let andmerida = "1,Marshal,Martinovic,mmartinovic0@dedecms.com,Male,40.19.226.175"
console.log("\"" + andmerida.split(",")[5] + "\" ja \"" + (andmerida.split(",")[3]).split("@")[0] + "\"") // Andmereast võtab 6 sõna mis tuleb pärast , siis lisab "ja", ning siis võtab selle emaili, splittib seda @-st ja võtab split-i ja väljastab selle, ofc jutumärgid on mõlemale lisatud ette, kui ka taha. Muidu selle loogika on lihtne aga seda on natukene eh.. kirjutada, sest oleme ausad, kui oleks veel tingimusi olnud, vb oleks keerulisemaks minna aga oleme ausad ka natukene, et mario pühakiri on parim asi mis on siia maailmasse tekkinud ja tänu sellele ma saan 5-e eksju mario :)
