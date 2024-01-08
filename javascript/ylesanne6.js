// Sten Soomre
// 2023-12-13
// Ülesanne  6


// Postiivne või negatiivne
let number = 3;

switch (true) {
    case number === 0: // Kas on null?
        console.log("Number on null");
        break;
    case number > 0: // Kas on postiivne?
        console.log("Number on suurem, kui null");
        break;
    case number < 0: // Kas on negatiivne, nagu keskmine IT vend
        console.log("Number on negatiivne");
        break;
    default: // Kas see üldse on number?
        console.log("See pole number");
}

//Restoran
let inimestearv = 10 // ilmselgelt see on see arv mida võrreltakse

switch (true) {
    case (inimestearv === 1 || inimestearv === 2): // kas on 1 või 2 inimesest
        console.log("Valige laud kahele inimesele")
        break;
    case (inimestearv === 3 || inimestearv === 4): // 3 või 4
        console.log("Valige laud neljale inimesele")
        break;
    case (inimestearv === 5 || inimestearv === 6): // 5 või 6
        console.log("Valige laud kuuele inimesele")
        break;
    case (inimestearv>6): // rohkem kui 6
        console.log("Valige suur laud")
        break;
    default: // vähem, kui 1 või NaN või undefined
        console.log("Minge palun ära")
}
