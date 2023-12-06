// Ülesanne 12
// Sten Soomre
// 2023-12-6

//var pealkiri1 = document.querySelector("h1"); //otsib esimest h1 elementi dokumentis ja lisab all olevad tegurid juurde :)
//let html = "<h2>Uus pealkiri</h2>";
//pealkiri1.insertAdjacentHTML("afterend", html);


//yoinkitud yl 10 kood

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
            var pealkiri = document.querySelector("ul");
            let html = (`${toode.nimi} - ${toode.hind} EUR - Kogus: ${toode.kogus}<br>`); //et kuvada tooteid ul-s
            pealkiri.insertAdjacentHTML("afterend", html); // Maagiliselt töötab, ma ei küsi kuidas aga see töötab
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
        summa = parseFloat(summa.toFixed(2));
        var pealkiri = document.querySelector("p");
        let html = (`Kogusumma: ${summa} EUR`); //et kuvada tooteid ul-s
        pealkiri.insertAdjacentHTML("afterend", html); // Maagiliselt töötab, ma ei küsi kuidas aga see töötab
        return summa;
    },
};

//ostukorv.lisaToode("Kohv", 5.80, 2);
ostukorv.kuvaSisu();
ostukorv.koguSumma();

