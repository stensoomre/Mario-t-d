# Sten Soomre
# Töö 4
# 08.03.2022

# Kuupäev

def kuu_nimi(a):
    kuud = ["","Jaan", "Veeb", "Mär", "Apr"]
    return kuud[a]
print(kuu_nimi(1))

def kuupaev_sonena(b):
    dd,mm,yyyy=b.split(".")
    print(dd,kuu_nimi(int(mm)),yyyy)

kuupaev_sonena("24.02.1918")


# Mündid
fail = input("Sisestqa failinimi: ")
mundid = open(fail, encoding="UTF-8")
mundid2 = 0
for line in mundid:
    line = int(line)
    if line <= 5:
        mundid2 += line
print("Hoiupõrasse läheb",mundid2,"senti.")


# Tervitus

def tervitus():
    arv = int(input("Mitu külalist külastab? "))
    number = 0
    for i in range(arv):
        number += 1 
        print("Võõrustaja: \"Tere\"")
        print(f"Täna {number}. kord tervitada, mõtiskleb võõrustaja.")
        print("Külaline: \"Tere, suur tänu kutse eest!\"")
    
tervitus()
# Peo eelarve

def eelarve2():
    inim = int(input("Mitu külalist tuleb? "))
    inim2 = int(input("Mitu nendest on teatanud, et tuleb? "))
    inim1 = inim - inim2
    eelarve(inim, inim2)
    
def eelarve(inim, inim2):
    raha = (10*inim+55)
    raha2 = (10*inim2+55)
    print("Minimaalne eelarve:",raha2,"eurot")
    print("Maksimaalne eelarve:",raha,"eurot")
    
    
eelarve2()

# Õunamahla tegemine
ounkogu = int(input("Sisestage mitu kilogrammi õunu on: "))
mahlapakkarv = round((ounkogu*0.4/3),0)
print(mahlapakkarv)

# Banner

def banner(vaide):
    vaide = vaide.upper()
    print(vaide)

def banner2():
    vaar1 = int(input("Mitu korda soovite reklaamlauset kuvada? "))
    vaide = input("Sisestage reklaamlause: ")
    
    for i in range(vaar1):
        banner(vaide)
        
banner2()
 