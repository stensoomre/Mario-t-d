# Töö 2
# Sten Soomre
# 02.03.2022

import random

# Äratus 2.1
def aratus():
    korrad = int(input("Mitu korda on vaja äratada: "))
    while korrad >= 1:
        print("Tõuse ja sära!")
        korrad += -1
aratus()

# Murelikud Lapsevanemad 2.2
def mure():
    ringid = int(input("Mitu ringi läbiti: "))
    porgandid = 0
    while ringid >= 1:
        if ringid%2 == 0:
            porgandid += ringid
        ringid += -1
    print(f"porgandite koguarv on {porgandid}")
mure()

# Täringud 2.3
def taringud():
    kogus = int(input("Mitut täringut lähed vaja: "))
    for q in range(kogus):
        vastus = random.randint(1,6)
        print(vastus)
taringud()

# Male 2.4
def male():
    taisarv = int(input("Mitmes ruut: "))
    i = 1
    terad = 1
    while i <= taisarv-1:
        terad *= 2
        i += 1
    print(f"nisu teri {taisarv}. ruudu eest: {terad}")
male()

# Õunad 2.6
def ounad():
    ulejaanud = 14
    poisid = int(input("Mitu pöialpoissi õunu tahavad (0-7): "))
    while poisid > 0:
        ounad = random.randint(1,2)
        print(ounad)
        ulejaanud -= ounad
        poisid -= 1
    print(f"Lumivalgekese jäi {ulejaanud} õuna")
ounad()