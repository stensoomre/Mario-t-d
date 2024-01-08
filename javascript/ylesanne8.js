// Sten Soomre
// 2023-12-13
// Ülesanne  8

const munt = [200, 0.2, 10, 0.01, 2, 1, 0.1, 0.02, 0.05, 100, 5, 0.5, 50, 20];

const sorteeritudmunt = [];
let kokku = 0;
let countmunt = 0;

while (munt.length > 0) {
  const muntid = munt.pop();

  if (muntid >= 1) {
    sorteeritudmunt.push(muntid);
    kokku += muntid;
    countmunt++;
  } else {
    const mundidecial = munt.filter((c) => c + kokku <= 1);
    if (mundidecial.length > 0) {
      const sum = mundidecial.reduce((acc, c) => acc + c, 0);
      if (sum + kokku <= 1) {
        sorteeritudmunt.push(...mundidecial);
        kokku += sum;
        countmunt += mundidecial.length;
        munt.splice(munt.indexOf(mundidecial[0]), mundidecial.length);
      }
    }
  }
}

console.log("Sorteeritud mündid:", sorteeritudmunt);
console.log(`Kokku sai ${countmunt} münti ja nende summa on ${kokku.toFixed(2)}`);

