// Sten Soomre
// 2023-12-13
// Ülesanne  3


// Sõiduaeg ja kaugus
let km = 100000 // Kogu maa
let kmh = 2000  // Hüpoteetiline kiirus

console.log(km + "km sõitmiseks, kiirusel "+ kmh + "km/h kuluks " + km/kmh + " tundi.") // väljastab km, kmh ja nende vahel jagtud summa. Ning väljastab kogu komplekti, loetaval kujul.

// Postituste kuvamine

let arv = 137 // Kujutame ette, et meil on array, kus on 137 sisendit aga hetkel paneme selle var-ina siia
let max = 10  // Kuna me teame, et leheküljel saab olla maksimaaselt 10 postitust siis lisame selle muutujaks
let muutuja1 = parseInt(arv/max) // Kiire arvutamine saavutab 13.7 aga ma tahan 13, et siis võtan aint int, milleks on 13
let muutuja2 = arv - muutuja1*10 // kuna 13*10 on 130 täisarv ja jagatab ilusti 10-ga siis ma saan selle maha lahutada orginaal arvust et saada teada ülejääki
if (muutuja2 == 0){ // vaatab kas viimane arv oli 0, kui oli siis see ei lisa midag
    console.log("Et kuvada kõike " + arv + " postitust. Oleks sul vaja " + muutuja1 + " lehekülge") 
}
else{ // Kui polnud siis lisab +1, et näidata korrekset lehekülgede arvu
    console.log("Et kuvada kõike " + arv + " postitust. Oleks sul vaja " + (muutuja1+1) + " lehekülge")
}

// Serveri töökulu

let watt = 400
let ehind = 9.69
let tund = 1

let tookulu = ((((watt/1000) * ehind)/100) * tund).toFixed(2) // kasutab seda valemit, mis ette anti ülesandes ja siis veel roundib 2 decimali kohani.
console.log(watt + "W psu-ga serveri käimas hoidmine elektri hinnaga " + ehind + " senti/kWh, " + tund +" tund(i), maksab " + tookulu + "EURi") // Ilmselgelt saad aru mis see teeb