# Harjutus 2
# Sten Soomre
# 02.02.22

from math import *

# Kütuse maania
kyts = int(input("Siseta kulutatud kütus (Liitrides): "))
maa = int(input("Siseta selle kütusega sõidetud maa (km): "))
kulund1 = (maa/kyts)/100
print("Kulutate 100 km kohta",kulund1,"L kütust")
# Arvusüsteemid
numba = int(input("Siseta number : "))
numba2 = bin(numba)
print(numba2)
numba3 = hex(numba)
print(numba3)
    

# Ajateisendus
minutid = int(input("Siseta minutite arv: "))
aeg = minutid//60
aeg2 = minutid-(aeg*60)
print("Aeg oleks siis:",aeg,":",aeg2)

# Hüpotenuus
a = 16
b = 9
c2 = a*a+b*b
c = round(sqrt(c2),2)
print("Hüpetnuus on",c)

# Rulluisutajad
kiirus = 29.9 #km/h
aeg = 24 # minut
kuluaeg = round(((kiirus/60)*aeg),2)
print("Rulluikudega kiirusega" ,str(kiirus), "km/h jõuaks" ,aeg, "minutiga," ,kuluaeg, "km kaugusele")

# Pitsa
soberad = 3
Hind = 12.90
Joot = 0.1
summa1 = round(soberad/(Hind*Joot),2)
print("Iga üks peab jätma ",summa1,"€")

# Toote hind
Toode = 36.75
Soodus = 0.4
Kogus = 3
summa = round(Kogus*(Toode-(Toode*Soodus)), 2)
print(Kogus, "Toote hind on",summa, "€")

# Kolmnurga ümbermõõt
a,b,c = 15,16,18

Kolmnurk = 15+16+18

print("Kolmnurga ümbermõõt: ",Kolmnurk)

