// Ülesanne 13
// Sten Soomre
// 2023-12-6

const id = document.querySelector("p");
id.innerText = "See töötas";
id.setAttribute("attr", "sten soomre"); // oi kui raske
id.removeAttribute("id");
console.log(id.getAttribute("attr"))

