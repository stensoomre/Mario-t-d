# Sten Soomre
# Harjutus 5
# 15.02.22

import math

# LooB funktsiooni

def tervita(nimi, keel="de"):
    if keel=="et":
        print(f"Tere {nimi}!")
    elif keel=="en":
        print(f"Hi {nimi}!")
    else:
        print(f"Hail {nimi}!")
     
n = input("Sisestage nimi: ")
k = input("Vali keel et/en/de: ")
tervita(n,k)


# Ruumala
def kuup(a):
    v = a ** 3
    return v

def kera(r):
    v = round(4/3 ** math.pi * r ** 3,2)
    return v

def koonus(r, h):
    v = round(1/3*math.pi*r**2*h,2)
    return v

def silinder(r, h):
    v = round(math.pi*r**2*h,2)
    return v

print("Vali kujund: \n1 (kuup)\n2 (kera)\n3 (koonus)\n4 (silinder)\n5 (EXIT)")
valik = int(input("Vali soovitud kujundi number: "))
if valik == 1:
    a = int(input("Sisestage kuubi üks külg pikkus a = "))
    print(kuup(a))

if valik == 2:
    r = int(input("Sisestage kera raadius r = "))
    print(kera(r))

if valik == 3:
    r = int(input("Sisestage koonuse põhja pindala Sp = "))
    h = int(input("Sisestage koonuse korgus h = ")) 
    print(koonus(r,h))
    

if valik == 4:
    r = int(input("Sisestage silindri pohjapindala Sp = "))
    h = int(input("Sisestage koonuse kõrgus H = "))
    print(silinder(r,h))


