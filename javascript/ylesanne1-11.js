// Kohe ütlen ette ära, et kõik tööd mis siin on, on suure armastusega tehtud ja austusega Mario Metsheina vastu :) (nohomo)




// Ülesanne 3
// Sten Soomre
// 2023-10-11

// Sõidu aeg ja kaugus
var kaugus = 150; // Kaugus kilomeetrites
var kiirus = 60; // Kiirus kilomeetrites tunnis
var sõiduAeg = kaugus / kiirus; // Sõidu aeg tundides
console.log(`Sõidu aeg: ${sõiduAeg} tundi`);

// Postituste kuvamine
var postitusteArv = 137;
var postitusteLehtedeArv = Math.ceil(postitusteArv / 10); // Arvutame lehekülgede arvu
var viimaselLehelPostitusi = postitusteArv % 10; // Arvutame viimasel lehel olevate postituste arvu
console.log(`Lehekülgi vaja: ${postitusteLehtedeArv}`);
console.log(`Viimasel lehel postitusi: ${viimaselLehelPostitusi}`);

// Serveri töökulu
var võimsus = 400; // Võimsus vattides (W)
var elektriHind = 0.0969; // Elektri hind eurodes kilovatt-tunni kohta (eurod/kWh)
var voolutarbimine = võimsus / 1000; // Voolutarbimine kilovatt-tundides (kWh)
var töökulu = voolutarbimine * elektriHind; // Serveri töökulu eurodes ühe tunni jooksul
console.log(`Serveri töökulu ühe tunni jooksul: ${töökulu.toFixed(2)} eurot`);

// Ülesanne 4
// Sten Soomre
// 2023-10-11


// Leet nädalapäevad
let leetNadalapaevad = ["Esmaspäev", "Teisipäev", "Kolmapäev", "Neljapäev", "Reede"];

// Paranda massiiv ja kuva selle elemendid
leetNadalapaevad[2] = "Kolmapäev"; // Parandame massiivi elementi
console.log(leetNadalapaevad);

// Kuva massiivi suurus
console.log(`Massiivi suurus: ${leetNadalapaevad.length}`);

// Lisa lõppu koodi abiga Laupäev ja Pühapäev
leetNadalapaevad.push("Laupäev", "Pühapäev");
console.log(leetNadalapaevad);

// Sorteeri elemendid kahanevalt
leetNadalapaevad.sort().reverse();
console.log(leetNadalapaevad);

// Kuva viimane element
console.log(`Viimane element: ${leetNadalapaevad[leetNadalapaevad.length - 1]}`);

// Andmerida ja operatsioonid
let koodid = "444689936146563731 2452966188592191874 52634311978613959924676311 4874232339 491973615889195397613151 64491375479568464397 2799868298847212752434 9464245911 84529438455334236247245 8131257451645317232949247 26471594451453281675411332 6631592725297745964837 616698332453173937881461 3311783543427862468268 385418321228899775431 4659867 73395213225525916984356 833792195426925124155181841 123388893 6941777837193213644325351 11353488912476869536954 61173937137292328237388335 5344692 452956158 31937616696951768494 584842118999165552436 8832121577139589884 15282516522883423742885 14713349724 6919979438697694 2252585676244745856486 5617683424485959291 547443594 2678324174797795449925 43753791352187862731151912 6875665565836721939262 35482977 84421878934473534291995 798457553821668942312 11114498238219156246883553 3599955 8831995953696776 8138759916933117676486 2388776737768787 37232647683297835458183 11318659392964788174775 683293746169875551252354 741545327395636643318531 38447974824822841161273 88768222547689886222 6345677462396774359 4942661761 1354569165 2553653936124138282 851786784517417366411515 42279319649497959785 5523951771 45941761289678527316294 37776454913244819275691 436669892715419465494342 682264111527 734681268219555989841131 882641896825571288724 382545666 12133138432672285179566156291 83644842221351483476411355532 9589336353993598224 184537669759184472427331 41851326945453796784 525783591 173773335961894524914465 47516715963756294236321 7296569497726217615 79487235 4931878519724923131437 31214731844284735237658435 1378458823933518466122 1241955123792435126557994 347427652476673662454 55596877477154112241923 9789414554758712319821 86228624276917113671233411 89659521 1352796469161477381192 69483824148396716861472 4766533634762298963245 5155973593459278561 1784478259974148659431 29583142566714785218623 244371427148584159487652 871836193187759591363 247956";

// Tükelda sõne ja kuva mitu koodi saad
let koodiArray = koodid.split(" ");
console.log(`Sõne jagamisel saadud koodide arv: ${koodiArray.length}`);

// Mitmes index on koodil 35482977
let indeks = koodiArray.indexOf("35482977");
console.log(`Koodi "35482977" indeks: ${indeks}`);

// Kuva saadud massiivist täpselt pooled elemendid
let poolMassiivist = koodiArray.slice(0, koodiArray.length / 2);
console.log("Saadud massiivist täpselt pooled elemendid:");
console.log(poolMassiivist);

// Sportlaste tulemused
let sportlased = [
  ["Alice", 25, [10.2, 9.8, 10.5]],
  ["Bob", 22, [9.5, 9.6, 9.7]],
  ["Charlie", 28, [11.1, 11.2, 11.5]]
];

// Kuva õpilase nimi ja parim tulemus
for (let i = 0; i < sportlased.length; i++) {
  let sportlane = sportlased[i];
  let nimi = sportlane[0];
  let tulemused = sportlane[2];
  let parimTulemus = Math.max(...tulemused);
  console.log(`${nimi} - Parim tulemus: ${parimTulemus}`);
}

// Ülesanne 5
// Sten Soomre
// 2023-10-11

// Temperatuur
let temperatuur = 18; // Muuda siin temperatuuri vastavalt vajadusele

if (temperatuur > 25) {
  console.log("Väga kuum ilm!");
} else if (temperatuur >= 15 && temperatuur <= 25) {
  console.log("Mõnus temperatuur");
} else {
  console.log("Jahe ilm");
}

// Kasutajanime kontroll
let kasutajanimi = "admin"; // Muuda siin kasutajanimi vastavalt vajadusele

if (kasutajanimi === "admin") {
  console.log("Tere, administraator!");
} else {
  console.log("Tere, külaline!");
}

// Ürituse piletite hind
let piletitüüp = "taispilet"; // Muuda siin piletitüüp vastavalt vajadusele
let vanus = 25; // Muuda siin vanus vastavalt vajadusele

let piletiHind;

if (piletitüüp === "taispilet") {
  if (vanus < 18) {
    piletiHind = 10;
  } else if (vanus >= 18 && vanus <= 64) {
    piletiHind = 20;
  } else {
    piletiHind = 15;
  }
} else if (piletitüüp === "sooduspilet") {
  if (vanus < 18 || vanus >= 65) {
    piletiHind = 8;
  } else if (vanus >= 18 && vanus <= 64) {
    piletiHind = 15;
  }
}

console.log(`Pileti hind: ${piletiHind} eurot`);

// Ülesanne 6
// Sten Soomre
// 2023-10-11

// Positiivne või negatiivne
let numbers = -5; // Muuda siin sisestatud number vastavalt vajadusele

switch (true) {
  case numbers > 0:
    console.log("Number on positiivne.");
    break;
  case numbers < 0:
    console.log("Number on negatiivne.");
    break;
  default:
    console.log("Number on null.");
}

// Restoran
let broneeringuArv = 4; // Muuda siin broneeringu arv vastavalt vajadusele

switch (true) {
  case broneeringuArv >= 1 && broneeringuArv <= 2:
    console.log("Valige laud kahele inimesele.");
    break;
  case broneeringuArv >= 3 && broneeringuArv <= 4:
    console.log("Valige laud neljale inimesele.");
    break;
  case broneeringuArv >= 5 && broneeringuArv <= 6:
    console.log("Valige laud kuuele inimesele.");
    break;
  default:
    console.log("Valige suur laud.");
}
// Ülesanne 7
// Sten Soomre
// 2023-10-11
// Tooted
const products = [
    "Õunad", "Piim", "Leib", "Juust", "Tomatid", "Kanafilee", "Muna", "Sibul", "Apelsinid", "Riis", 
    "Jogurt", "Kartul", "Kalafilee", "Pasta", "Jogurtijook", "Porgandid", "Virsikud", "Pähklid", 
    "Rosinad", "Kapsas", "Kreeka jogurt", "Veiseliha", "Banaanid", "Oliivid", "Mandlid", "Magus kartul", 
    "Greibid"
  ];
  
  const months = "Jaanuar, Veebruar, Märts, Aprill, Mai, Juuni, Juuli, August, September, Oktoober, November, Detsember";
  console.log("Tooted koos järjekorranumbritega:");
  for (let i = 0; i < products.length; i++) {
    console.log(`${i + 1}. ${products[i]}`);
  }
  
  // Temperatuurid
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
    [10, 13, 16, 18, 20, 22, 23, 24, 21, 18, 15, 13, 11, 10, 9, 12, 15, 18, 20, 23, 25, 27, 26, 24, 21, 18]
  ];
  
  // Leian iga kuu keskmise temperatuuri
  const kuud = months.split(", ");
  for (let i = 0; i < temperatures.length; i++) {
    const keskmine = temperatures[i].reduce((acc, temp) => acc + temp, 0) / temperatures[i].length;
    console.log(`${kuud[i]}: ${keskmine.toFixed(2)}°C`);
  }
  
  // Leian kõrgeimad ja madalaimad temperatuurid
  let korgeimKuu = "";
  let madalaimKuu = "";
  let korgeimTemp = Number.MIN_VALUE;
  let madalaimTemp = Number.MAX_VALUE;
  
  for (let i = 0; i < temperatures.length; i++) {
    const maxTemp = Math.max(...temperatures[i]);
    const minTemp = Math.min(...temperatures[i]);
    if (maxTemp > korgeimTemp) {
      korgeimTemp = maxTemp;
      korgeimKuu = kuud[i];
    }
    if (minTemp < madalaimTemp) {
      madalaimTemp = minTemp;
      madalaimKuu = kuud[i];
    }
  }
  
  console.log(`Kõige kõrgem temperatuur oli kuus "${korgeimKuu}" ja see oli ${korgeimTemp}°C.`);
  console.log(`Kõige madalam temperatuur oli kuus "${madalaimKuu}" ja see oli ${madalaimTemp}°C.`);
  

// Ülesanne 8
// Sten Soomre
// 2023-10-11

const coins = [200, 0.2, 10, 0.01, 2, 1, 0.1, 0.02, 0.05, 100, 5, 0.5, 50, 20];

const sortedCoins = [];
let totalCoins = 0;
let coinCount = 0;

while (coins.length > 0) {
  const coin = coins.pop();

  if (coin >= 1) {
    sortedCoins.push(coin);
    totalCoins += coin;
    coinCount++;
  } else {
    const fractionalCoins = coins.filter((c) => c + totalCoins <= 1);
    if (fractionalCoins.length > 0) {
      const sum = fractionalCoins.reduce((acc, c) => acc + c, 0);
      if (sum + totalCoins <= 1) {
        sortedCoins.push(...fractionalCoins);
        totalCoins += sum;
        coinCount += fractionalCoins.length;
        coins.splice(coins.indexOf(fractionalCoins[0]), fractionalCoins.length);
      }
    }
  }
}

console.log("Sorteeritud mündid:", sortedCoins);
console.log(`Kokku sai ${coinCount} münti ja nende summa on ${totalCoins.toFixed(2)}`);


// Ülesanne 9
// Sten Soomre
// 2023-10-11

// Funktsioon klassikalises stiilis, mis väljastab nime
function minuNimi() {
    console.log("Sten Soomre");
  }
  
  // Noolefunktsioon, mis väljastab nime
  const minuNimiNool = () => {
    console.log("Sten Soomre");
  };
  
  // Funktsioon kuupäeva ja kuu kuvamiseks eesti keeles
  function kuupaevEesti(kuupaev) {
    const kuud = [
      "jaanuar",
      "veebruar",
      "märts",
      "aprill",
      "mai",
      "juuni",
      "juuli",
      "august",
      "september",
      "oktoober",
      "november",
      "detsember"
    ];
  
    const parts = kuupaev.split(".");
    if (parts.length === 3) {
      const paev = parseInt(parts[0]);
      const kuu = parseInt(parts[1]);
      const aasta = parts[2];
      if (paev >= 1 && paev <= 31 && kuu >= 1 && kuu <= 12) {
        console.log(`${paev}. ${kuud[kuu - 1]} ${aasta}`);
      } else {
        console.log("Vigane kuupäev");
      }
    } else {
      console.log("Vigane kuupäev");
    }
  }
  
  // Funktsioon teadmata hulga arvude koguarvu ja keskmise leidmiseks
  function koguKeskmine(...arvud) {
    const summa = arvud.reduce((acc, arv) => acc + arv, 0);
    const keskmine = summa / arvud.length;
    console.log(`Kokku: ${summa}, Keskmine: ${keskmine}`);
  }
  
  // Noolefunktsioon salajase sõnumi loomiseks
  const salajaneSonum = (sisend) => {
    const taishaalikud = "aeiouAEIOU";
    let tarnaSone = "";
    for (let i = 0; i < sisend.length; i++) {
      if (taishaalikud.indexOf(sisend[i]) !== -1) {
        tarnaSone += "*";
      } else {
        tarnaSone += sisend[i];
      }
    }
    return tarnaSone;
  };
  
  // Noolefunktsioon unikaalsete nimede leidmiseks
  const leiaUnikaalsedNimed = (nimed) => {
    const unikaalsed = [];
    for (let i = 0; i < nimed.length; i++) {
      if (unikaalsed.indexOf(nimed[i]) === -1) {
        unikaalsed.push(nimed[i]);
      }
    }
    return unikaalsed;
  };
  
  const nimed = ["Kati", "Mati", "Kati", "Mari", "Mati", "Jüri"];
  const unikaalsedNimed = leiaUnikaalsedNimed(nimed);
  
  console.log("Klassikaline funktsioon: Minu nimi");
  minuNimi();
  console.log("Noolefunktsioon: Minu nimi");
  minuNimiNool();
  console.log("Kuupäev eesti keeles");
  kuupaevEesti("19.07.23");
  console.log("Kogu ja keskmine");
  koguKeskmine(10, 20, 30, 40, 50);
  console.log("Salajane sõnum");
  console.log(salajaneSonum("Tere, ma olen salajane!"));
  console.log("Unikaalsed nimed");
  console.log(unikaalsedNimed);

// Ülesanne 10
// Sten Soomre
// 2023-10-31
  // Toote objekt
const toode = {
  nimetus: "Piim",
  hind: 3.60,
  kogus: 2,
  koguhind: function () {
    return this.hind * this.kogus;
  },
  muudaKogus: function (uusKogus) {
    this.kogus = uusKogus;
  },
  kuvaSisu: function () {
    return `${this.nimetus} - ${this.hind} EUR - Kogus: ${this.kogus}`;
  },
};

console.log("Toote omadused:");
console.log("Nimetus:", toode.nimetus);
console.log("Hind:", toode.hind + " EUR");
console.log("Kogus:", toode.kogus);

console.log("Koguhind:", toode.koguhind() + " EUR");

// Ostukorv objekt
const ostukorv = {
  tooted: [
    { nimi: "Piim", hind: 3.60, kogus: 2 },
    { nimi: "Leib", hind: 2.00, kogus: 1 },
    { nimi: "Munad", hind: 1.50, kogus: 6 },
    { nimi: "Juust", hind: 4.20, kogus: 1 },
    { nimi: "Tomatid", hind: 2.30, kogus: 3 },
  ],
  kuvaSisu: function () {
    for (let toode of this.tooted) {
      console.log(`${toode.nimi} - ${toode.hind} EUR - Kogus: ${toode.kogus}`);
    }
  },
  lisaToode: function (nimi, hind, kogus) {
    this.tooted.push({ nimi, hind, kogus });
  },
  koguSumma: function () {
    let summa = 0;
    for (let toode of this.tooted) {
      summa += toode.hind * toode.kogus;
    }
    return summa;
  },
};

console.log("Ostukorvi sisu:");
ostukorv.kuvaSisu();

console.log("Lisa toode 'Kohv' ostukorvi:");
ostukorv.lisaToode("Kohv", 5.80, 2);
console.log("Uus ostukorvi sisu:");
ostukorv.kuvaSisu();

console.log("Ostukorvi kogu summa:", ostukorv.koguSumma() + " EUR");

// Ülesanne 11
// Sten Soomre
// 2023-11-8

const nimed1 = ["mari maasikas", "jaan jõesaar", "kristiina kukk", "margus mustikas", "jaak järve", "kadi kask", "Toomas Tamm", "Kadi Meri", "Leena Laas", "Madis Mets", "Hannes Hõbe", "Anu Allikas", "Kristjan Käär", "Eva Esimene", "Jüri Jõgi", "Liis Lepik", "Kalle Kask", "Tiina Teder", "Kaidi Koppel", "tiina Toom", "Sten Soomre"];

// Funktsioon nimede korrastamiseks
function korrastaNimed(nimed1) {
    const korrastatudNimed = nimed1.map(nimi => {
        const nimeOsad = nimi.split(" ");
        const eesnimi = nimeOsad[0].charAt(0).toUpperCase() + nimeOsad[0].slice(1);
        const perenimi = nimeOsad[1].charAt(0).toUpperCase() + nimeOsad[1].slice(1);
        const email = perenimi.toLowerCase() + "@metshein.com";
        return `${eesnimi} ${perenimi} (${email})`;
    });
    return korrastatudNimed;
}

console.log("Korras nimed ja e-mailid:");
console.log(korrastaNimed(nimed1));

// Funktsioon nime otsimiseks massiivist
function otsiNime(nimi, nimedeMassiiv) {
    const leitudNimi = nimedeMassiiv.find(n => n.toLowerCase() === nimi.toLowerCase());
    if (leitudNimi) {
        console.log("Leitud nimi:", leitudNimi);
    } else {
        console.log("Nime ei leitud.");
    }
}

otsiNime("Jaak Järve", nimed1);
otsiNime("Sten Soomre", nimed1);

/// Sünniaeg ja vanus
const inimesteAndmed = [
  { nimi: "Mari Maasikas", isikukood: "38705123568" },
  { nimi: "Jaan Jõesaar", isikukood: "49811234567" },
  { nimi: "Kristiina Kukk", isikukood: "39203029876" },
  { nimi: "Margus Mustikas", isikukood: "49807010346" },
  { nimi: "Jaak Järve", isikukood: "39504234985" },
  { nimi: "Kadi Kask", isikukood: "39811136789" },
  // Lisa kontrollimiseks oma nimi ja isikukood
  { nimi: "Sten Soomre", isikukood: "50502144226"}
];

// Funktsioon sünniaja ja vanuse leidmiseks
function leiaSynniAegJaVanus(isikukood) {
  const sünniaasta = parseInt(isikukood.slice(1, 3)); // Võta aastaosa isikukoodist
  const sugu = parseInt(isikukood.slice(0, 1)) % 2 === 0 ? "naine" : "mees"; // Kontrolli soo järgi
  const sünnikuupäev = (sünniaasta < 22 ? "20" : "19") + isikukood.slice(1, 3) + "-" + isikukood.slice(3, 5) + "-" + isikukood.slice(5, 7);
  const täna = new Date();
  const sünniaeg = new Date(sünnikuupäev);
  const vanus = täna.getFullYear() - sünniaeg.getFullYear();
  return { sünniaeg: sünnikuupäev, vanus: vanus, sugu: sugu };
}

console.log("Sünniaeg, vanus ja sugu:");
inimesteAndmed.forEach(isik => {
  const synniAndmed = leiaSynniAegJaVanus(isik.isikukood);
  console.log(`${isik.nimi}: Sünniaeg - ${synniAndmed.sünniaeg}, Vanus - ${synniAndmed.vanus} aastat, Sugu - ${synniAndmed.sugu}`);
});

// Kaugushüpped
const opilased = [
    { nimi: "Anna", tulemused: [4.5, 4.8, 4.6] },
    { nimi: "Mart", tulemused: [5.2, 5.1, 5.4] },
    { nimi: "Kati", tulemused: [4.9, 5.0, 4.7] },
    { nimi: "Jaan", tulemused: [4.3, 4.6, 4.4] },
    { nimi: "Liis", tulemused: [5.0, 5.2, 5.1] },
    { nimi: "Peeter", tulemused: [5.5, 5.3, 5.4] },
    { nimi: "Eva", tulemused: [4.8, 4.9, 4.7] },
    { nimi: "Marten", tulemused: [4.7, 4.6, 4.8] },
    { nimi: "Kairi", tulemused: [5.1, 5.3, 5.0] },
    { nimi: "Rasmus", tulemused: [4.4, 4.5, 4.3] },
];

console.log("Kaugushüppe tulemused:");
opilased.forEach(õpilane => {
    const parimTulemus = Math.max(...õpilane.tulemused);
    const keskmineTulemus = (õpilane.tulemused.reduce((a, b) => a + b, 0) / õpilane.tulemused.length).toFixed(2);
    console.log(`${õpilane.nimi}: Parim tulemus - ${parimTulemus}, Keskmine tulemus - ${keskmineTulemus}`);
});


// Ülesanne 12
// Sten Soomre
// 2023-12-6