// Sten Soomre
// 2023-12-13
// Ülesanne  7


// Tooted
const products = ["Õunad", "Piim", "Leib", "Juust", "Tomatid", "Kanafilee", "Muna", "Sibul", "Apelsinid", "Riis", "Jogurt", "Kartul", "Kalafilee", "Pasta", "Jogurtijook", "Porgandid", "Virsikud", "Pähklid", "Rosinad", "Kapsas", "Kreeka jogurt", "Veiseliha", "Banaanid", "Oliivid", "Mandlid", "Magus kartul", "Greibid"];

//for (let i = 0; i < products.length; i++) { // käib iga toote eraldi läbi ja hoiab meelde selle asukoha
//   console.log((i+1)+". "+products[i]); // lisab meelde jäätud asukoha teksti ja väljastab selle
//}

// see on täiendus
let arv = 0;
for (let i = 0; arv < 10; i++) {
    arv += 1; // liidame juurde, sest uus ring tuli peale
    if (products[i] == "Muna" || products[i] == "Sibul" || products[i] == "Riis") { // Kas produkt on muna v sibul v riis, kui on siis lahutab arvu maha ja jätkab, ei prindi
        arv -= 1; // lahutab sest algul liidame ja me ei taha neid produkte lugeda valiideseks
        continue; // Et ta jätkaks, mitte ei prindiks
    }
    console.log(arv + ". " + products[i] + "  (i: " + i + ")"); // Väljastamine
}


//Temperatuurid

const temperatures = [
    [5, 8, 12, 10, 7, 9, 11, 14, 16, 13, 10, 6, 4, 3, 2, 4, 6, 8, 10, 12, 15, 17, 18, 16, 13, 10],
    [1, 4, 6, 7, 9, 11, 13, 15, 12, 9, 7, 5, 3, 2, 3, 6, 8, 10, 12, 15, 17, 19, 18, 16, 13, 11],
    [8, 10, 13, 15, 16, 18, 19, 20, 17, 15, 13, 11, 10, 9, 8, 10, 12, 14, 16, 18, 20, 22, 21, 18, 16, 14],
    [2, 5, 7, 9, 12, 15, 17, 18, 15, 13, 11, 8, 6, 5, 4, 7, 9, 12, 14, 16, 19, 21, 20, 18, 16, 13],
    [6, 8, 11, 14, 16, 18, 20, 21, 18, 15, 12, 10, 8, 6, 5, 8, 10, 13, 15, 18, 20, 22, 21, 19, 16, 13],
    [11, 14, 17, 19, 21, 23, 24, 22, 19, 16, 13, 11, 10, 9, 9, 12, 15, 18, 20, 23, 25, 27, 26, 24, 21, 18],
    [9, 11, 14, 16, 18, 20, 22, 21, 18, 16, 13, 11, 9, 8, 7, 10, 13, 16, 18, 21, 23, 24, 23, 21, 18, 15],
    [7, 10, 13, 15, 17, 20, 22, 23, 20, 17, 14, 12, 10, 9, 8, 11, 14, 17, 19, 22, 24, 26, 25, 23, 20, 17],
    [3, 6, 9, 11, 13, 15, 17, 18, 16, 14, 11, 9, 7, 6, 5, 8, 10, 13, 15, 17, 19, 21, 20, 18, 15, 12],
    [1, 3, 5, 7, 9, 11, 13, 15, 12, 9, 7, 5, 3, 2, 3, 6, 8, 10, 12, 15, 17, 19, 18, 16, 13, 11],
    [6, 8, 11, 14, 16, 18, 20, 21, 18, 15, 12, 10, 8, 6, 5, 8, 10, 13, 15, 18, 20, 22, 21, 19, 16, 13],
    [10, 13, 16, 18, 20, 22, 23, 24, 21, 18, 15, 13, 11, 10, 9, 12, 15, 18, 20, 23, 25, 27, 26, 24, 21, 18] // Neid on 12
];
const months = "Jaanuar, Veebruar, Märts, Aprill, Mai, Juuni, Juuli, August, September, Oktoober, November, Detsember";

// Leian iga kuu keskmise temperatuuri
const kuud = months.split(",");
for (let i = 0; i < temperatures.length; i++) {
    const keskmine = temperatures[i].reduce((acc, temp) => acc + temp, 0) / temperatures[i].length; //keskmine
    console.log(kuud[i] + ": " + keskmine.toFixed(2) + "°C"); // paneme siia ümartatud, kuni decimal koha 2 ja lisame ägeda sümboli ka juurde, et välja tuua, et too on ikkagi celsius, sest ferenhait või kuidas kurat sa seda kirjutad on praak ja halb
}
let korgeimKuu = "";
let madalaimKuu = "";
let korgeimTemp = Number.MIN_VALUE; // määrab suurema arvu kui sinu suurus :)
let madalaimTemp = Number.MAX_VALUE; // määrab sellise suuruse, mida sa kunagi ei saavuta :)

for (let i = 0; i < temperatures.length; i++) {
    const maxTemp = Math.max(...temperatures[i]); // otsime nii kõige kõrgemat tempi, võttes kõige kõrgema
    const minTemp = Math.min(...temperatures[i]); // nii otsib madalat
    if (maxTemp > korgeimTemp) {
        korgeimTemp = maxTemp;
        korgeimKuu = kuud[i];// salvestamine
    }
    if (minTemp < madalaimTemp) {
        madalaimTemp = minTemp;
        madalaimKuu = kuud[i]; // salvestamine x2
    }
}
console.log("Kõige kõrgem temperatuur oli kuus" + korgeimKuu + " ja see oli "+korgeimTemp+"°C.\nKõige madalam temperatuur oli kuus" + madalaimKuu + " ja see oli " + madalaimTemp + "°C.");