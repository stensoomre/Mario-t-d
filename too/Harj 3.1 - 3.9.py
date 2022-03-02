# Töö 3
# Sten Soomre
# 02.03.2022


# Ülikooli vastuvõetud 3.1
def vastuvoetud():
    fail1 = open("rebased.txt", encoding="UTF-8")
    vastuvoetud = []
    for w in fail1:
        vastuvoetud.append(int(w))
    fail1.close()
    aasta = int(input("millise aasta andmeid vaja läheb (2011-2019): "))
    aastad = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
    koht = aastad.index(aasta)
    andmed = vastuvoetud[koht]
    print(f"{aasta}. aastal oli vastuvõetuid {andmed}")
vastuvoetud()

# Vanemate mure 3.2
def mure():
    ringid = int(input("Sisestage ringide arv:"))
    porgandid = 0
    for q in range(ringid-1):
        if ringid%2 == 0:
            porgandid += ringid
        ringid += -1
    print(f"porgandite koguarv on {porgandid}")
mure()

# Sissetulekud 3.3
def sissetulekud():
    fail2 = open("konto.txt", encoding = "UTF-8")
    for e in fail2:
        arv = float(e)
        if arv > 0.0:
            print(arv)
sissetulekud()

# Jukebox 3.4
def jukebox():
    failinimi = input("sisestage failinimi koos laiendiga (näiteks 'jukebox.txt'): ")
    fail3 = open(failinimi, encoding = "UTF-8")
    laulud = []
    jarjekord = 1
    for t in fail3:
        print(f"{jarjekord}. {t}")
        laulud.append(t)
        jarjekord += 1
    valik = int(input("vali laulu järjekorra number: "))-1
    laul = laulud[valik]
    print(f"Mängitav muusikapala on {laul}")
jukebox() 