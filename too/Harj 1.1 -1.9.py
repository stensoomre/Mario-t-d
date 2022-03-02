# Tõõ
# Sten Soomre
# 02.03.2022

# Tervitus
def tere():
    print("Tere, maailm!")

tere()

# Aastaliblikas
def liblikas():
    aasta = 2020
    liblikas = "teelehe-mosaiikliblikas"
    lause_keskosa = ". aasta liblikas on "
    lause = str(aasta)+lause_keskosa+liblikas
    print(lause)

liblikas()

# Pilved
def pilved():
    korgus = float(input("Sisesta pilvede kõrgus (näide 5.4): "))
    if korgus > 6.0:
        print("Need on ülemised pilved")
    else:
        print("Need ei ole ülemised pilved")
        
pilved()

# Bussid
def bussid():
    inimesed = int(input("Sisesta inimeste arv: "))
    istekohad = int(input("Sisesta bussi kohtade arv: "))
    viimane = inimesed%istekohad
    if viimane == 0:
        bussid = inimesed//istekohad
        viimane = istekohad
    else:
        bussid = inimesed//istekohad+1
    print(f"Busse vaja: {bussid}\nViimases bussis inimesi: {viimane}")

bussid()
