# Sten Soomre
# Harjutus 9
# 17.02.22

import datetime
soov = input("Kas soovite INGLIS või EESTI keeles aega?\n").upper()
if soov == "EESTI":
    kuud = ["Jaanuar","Veeburar","Märts"]
    kuup = datetime.date.today()
    kuu = int(kuup.month)
    kuup2 = datetime.date(kuup.year, kuu , kuup.day)
    print(kuup2.strftime("%d")+". "+str(kuud[kuu-1])+" "+kuup2.strftime("%Y"))
elif soov == "INGLIS":
    kuud = ["January","Veburary","March"]
    kuup = datetime.date.today()
    kuu = int(kuup.month)
    kuup2 = datetime.date(kuup.year, kuu , kuup.day)
    print(kuup2.strftime("%d")+". "+str(kuud[kuu-1])+" "+kuup2.strftime("%Y"))

ik = "50416121910"
ik = input("Sisesta isikukood: ")
aasta = int("20"+ik[1]+ik[2])
kuu = int(ik[3]+ik[4])
paev = int(ik[5]+ik[6])
sp = datetime.date(aasta, kuu, paev)


now = datetime.date.today().year
vanus = now - aasta
print("Su vanus: ",vanus)
print("Sa sündisid:",datetime.date(aasta,kuu,paev))