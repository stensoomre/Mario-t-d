// Ülesanne 15
// Sten Soomre
// 2024-01-08

const item = document.querySelector("button"); // võtab esimese nuppu (mitte soovitadav üldse)
    item.addEventListener("click", () => {
        console.log("pihtas");
        if(item.classList.contains("btn-light")){
            item.classList.replace("btn-light", "btn-dark") //dark theme siia
            item.innerText = "White Theme";
            const tiitel = document.querySelector("body");
            tiitel.style.color = "white";
            tiitel.style.backgroundColor = "black";
 //           const tekst = document.querySelectorAll("p");
 //           tekst.style.color = "white";
 //           tekst.style.backgroundColor = "black";

        }
        else if (item.classList.contains("btn-dark")){
            item.classList.replace("btn-dark", "btn-light") // imeliku režiim siia
            item.innerText = "Dark Theme";
            const tiitel = document.querySelector("body");
            tiitel.style.color = "black";
            tiitel.style.backgroundColor = "white";
        }
        
    });