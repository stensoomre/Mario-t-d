# Harjutus 4
# Sten Soomre
# 08.02.22

from time import sleep

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



