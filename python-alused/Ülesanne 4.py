# Harjutus 4
# Sten Soomre
# 08.02.22

from time import sleep
from random import *

#ruut
a = int(input("1. Külg: "))
b = int(input("2. Külg: "))

if a==b:
    print("See on ruut")
else:
    print("See on ristkülik")

# Lihtne matemaatika
arv1 = int(input("Esimene arv: "))
arv2 = int(input("Teine arv: "))
tehe = input("Valige tehe:\n +\n -\n *\n /\n")

if tehe == "+": # liidab
    tehe2 = arv1 + arv2
elif tehe == "-": # lahutab
    tehe2 = arv1 - arv2
elif tehe == "*": # korrutab
    tehe2 = arv1 * arv2
elif tehe == "/": # jägab
    tehe2 = arv1 / arv2
print (f"{arv1}{tehe}{arv2}={tehe2}")

# Juubeli arvutamine

aasta = input("Sisesta sünniaeg kujul dd.mm.yyyy: ")
d,m,y = aasta.split(".")
aasta1 = 2022
aasta2 = aasta1 - int(y)
if aasta2%5==0:
    print("Sul on juubel")
else:
    print("Sul pole juubel")
    

# Müük

hind = int(input("Siseta toote hind: "))
if hind <= 10:
    ale = 0.90 # 90% hinnast, seega 10% soodus
else:
    ale = 0.80 # 80% hinnast, seega 20% soodus
hind = hind*ale
print(hind)

# Jalgpalli meeskond

def meeskond():
    sugu  = input("Siseta kandidaadi liikme sugu: ").upper()
    if sugu == "NAINE":
        print("Ei ole lubatud meeskonda")
    elif sugu == "MEES":
        vanus = int(input("Sisesta kandidaadi liikme vanus: "))
        if vanus >= 16 or vanus <= 18:
            print("Kandidaadi vanus:", vanus)
            print("Lubatud meeskonda")
        else:
            print("Kandidaadi vanus:", vanus)
            print("Ei ole lubatud meeskonda")    
    else:
        print("Vigane sugu")
        sleep(2)
        meeskond()
meeskond()

# Tärnid
a = int(input("Mitu rida tahad? "))
for i in range(1,a+1):
    print(i * "*")
    sleep(0.1)
print()

a = int(input("Mitu rida tahad? "))
for i in range(1,a+1):
    print("*" * a)
    a-=1
    sleep(0.1)
print()

# Loto
Loto = randint(10000,99999)
print(Loto)

#paaris paaritu
arvv = 1
for i in range (1,101):
    if arvv%2:
        print(arvv, " ei ole paaris arv")
    else:
        print(arvv, " on paaris arv")
    arvv = arvv + 1
    
# Pisike korrutus tabel
arvv = 1
for i in range(1,11):
    arvv2 = 5 * arvv
    print("5 x",arvv," =", arvv2)
    arvv = arvv + 1

# Viisikud
arvv = 1
for i in range (1,101):
    if arvv%5:
        pass
    else:
        print(arvv)
    arvv = arvv + 1

# Numbrimäng aga 3 pakumise järgi küsib kas annad alla

nr = randint(1,50)
loop = 1
kordade_arv = 0
jatka = 0
 
print('Arva ära number 1-50')
 
while loop == 1:
    arva = int(input('Sisesta täisarv: '))
    
    if arva == nr:
        kordade_arv += 1
        print('Tubli, pakkumisi kokku: ',kordade_arv)
        loop = 0
        
    elif arva < nr:
        kordade_arv += 1
        if jatka == 1:
            print('Sinu pakutud arv on liiga väike')
            pass
        else:
            print('Sinu pakutud arv on liiga väike')
            if kordade_arv == 3:
                soov = input("Kas sa soovid veel arvata? jah või ei: ").upper()
                if soov == "JAH":
                    jatka = 1
                    print('Sinu pakutud arv on liiga väike')
                elif soov == "EI":
                    print("Mäng on läbi ): õige arv oli:",nr)
                    loop = 0
    else:
        kordade_arv += 1
        if jatka == 1:
            print('Sinu pakutud arv on liiga suur')
            pass
        else:
            print('Sinu pakutud arv on liiga suur')
            if kordade_arv == 3:
                soov = input("Kas sa soovid veel arvata? jah või ei: ").upper()
                if soov == "JAH":
                    jatka = 1
                    print('Sinu pakutud arv on liiga suur')
                elif soov == "EI":
                    print("Mäng on läbi ): õige arv oli:",nr)
                    loop = 0
                    
# Monei is kewl
raha = int(input("Palju soovite panka panna? "))
aastaid = int(input("Mitmeks aastaks? "))
aastaid = aastaid + 1
aasta = 1
kasum = 0
print("Aasta   Algsumma    Intress     Aasta lõpuks")
for i in range (1,aastaid):
    intress = round((raha/100*5), 2)
    loppuks = round((raha + intress), 2)
    print ("{0:<8}{1:<12}{2:<12}{3:<30}".format(aasta, raha, intress, loppuks))
    raha = loppuks
    aasta = aasta + 1
    kasum = round((kasum + intress), 2)
print("Summa kokku:",loppuks,"€")
print("Kasum:",kasum,"€")

# Arv ruut kuup

arv = 1
print("Arv   Ruut   Kuup")
for i in range (1,11):
    ruut = arv * arv
    kuup = arv * arv * arv
    print ("{0:<6}{1:<7}{2:<1}".format(arv, ruut, kuup))
    arv = arv + 1
