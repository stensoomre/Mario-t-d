// Ülesanne 14
// Sten Soomre
// 2024-01-08

//console.log("test");

const elements = document.querySelectorAll("li"); /// osting
elements.forEach(element => {
   // console.log(element)
    let test = element.innerHTML;
    if (test.includes("Tehtud")) { // kui classname on string ja täpselt niimoodi kirjutatud siis teeb alam olevat käsku
        element.style.fontWeight = "700";// weight.. on 700?
        element.classList.replace("list-group-item", "list-group-item-success");

    }
    else if (test.includes("Ootel")) { // kui classname on string ja täpselt niimoodi kirjutatud siis teeb alam olevat käsku
        element.classList.replace("list-group-item", "list-group-item-warning");

    }
    else if (test.includes("Viga")) { // kui classname on string ja täpselt niimoodi kirjutatud siis teeb alam olevat käsku
        element.classList.replace("list-group-item", "list-group-item-danger");

    }
});
//console.log(elements)

//addClass("Ootel", "list-group-item-warning");
//addClass("Tehtud", "list-group-item-success");
//addClass("Viga", "list-group-item-danger");

