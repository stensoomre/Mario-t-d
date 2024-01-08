// Sten Soomre
// 2023-12-13
// Ülesanne  5

// Temperatuur

let temp = 20 // anname alg väärtuse muutujale

if (temp > 25){ // kui rohkem, kui 25 kraadi
    console.log("Väga kuum ilm!") // Väljastuse
}
else{ // Kui pole
    if (temp > 15){ // Vaatab kas on üle 15 kraadi vähemalt
        console.log("Mõnus temperatuur")
    }
    else{ // Kui seda ka pole või on lausa negatiivne või NaN ss annab selle vaste
        console.log("Jahe ilm")
    }
}

// Kasutajanime kontroll
// Programmi sa küll ei saa

let kasutajanimi = "markuspuult"
if (kasutajanimi = "admin"){
    console.log("Tere, administratoor!")
}
else{
    console.log("Tere, külaline!")
}

// Ürituse piletite hind

let soov = "sooduspilet"
let vanus = "1"

if (soov == "taispilet"){
    if(vanus < 18){
        console.log("10 EUR)")
    }
    else if(vanus >= 18 && vanus <= 64){ // Kontrollib kas inimene on 18 või sellest vanem või 64 noorem või lausa 65
        console.log("20 EUR")
    }
    else if(vanus >= 65){
        console.log("15 EUR")
    }
}
else if (soov == "sooduspilet"){
    if(vanus < 18 || vanus >= 65){ // Vaatab kas inimese vanus on noorem kui 18 või vanem või võrdne kui 65
        console.log("8 EUR");
    }
    else if(vanus >= 18 && vanus <= 64){
        console.log("15 EUR")
    }
}
else{
    console.log("Õpi kirjutama") // Kui valesti kirjutad soovi
}
