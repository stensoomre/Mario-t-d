from random import *
import time
global check
check = 0

def moot():
    global check
    global temperatuurid
    global mintemp
    global maxtemp
    global temp
    temperatuurid = []
    mintemp = 0
    maxtemp = 0
    for i in range(100):
        temp = randint(-10,40)
        temperatuurid.append(temp)
        if temp < mintemp:
            mintemp = temp;
        if temp > maxtemp:
            maxtemp = temp;
    check = 1
    main()

def naita():
    global check
    global temperatuurid
    global mintemp
    global maxtemp
    global temp
    if check == 1:
       check = 1
    else:
        temp = "Pole mõõdetud"
    print("Viimase mõõtmise tulemus on:", temp)
    time.sleep(2)
    main()
def minjamax():
    global check
    global temperatuurid
    global mintemp
    global maxtemp
    global temp
    if check == 1:
        check = 1
    else:
        mintemp = "Pole mõõdetud"
        maxtemp = "Pole mõõdetud"
    print("Suurim temperatuur mõõdetud:", maxtemp)
    print("Väikseim temperatuur mõõdetud:", mintemp)

    time.sleep(2)
    main()

def crash():
    try:
        crash()
    except:
        crash()
        
def main():
    global check
    print("""
    Tere!
    See kontrolltöö ajas, mind vägagi kettasse :)
    ───────────────────────
    1.│ Tee 100 uut mõõtmist. st genereeri vastav kogus arve ja määra selle käigus min ja maks temperatuurid. Lisaks jäta meelde viimase mõõtmise tulemus.
    ───────────────────────
    2.│ Näita viimase mõõtmise tulemust.
    ────────────────────────    
    3.│ Näita seni mõõdetutest maksimum- ja miinimumtemperatuuri.'
    ────────────────────────
    4.│ Nulli maks- ja min temperatuurid (selleks algväärtusta nad viimati "mõõdetud" temperatuuriga).
    ────────────────────────
    5.│ Välju programmist.
    """)
    soov = str(input("Kirjuta siia, koha number, mida soovid teha: "))

    if soov == "1":
        check = 1
        moot()
    if soov == "2":
        naita()
    if soov == "3":
        minjamax()
    if soov == "4":
        check = 0
        main()
    
    if soov == "5":
        crash()
main()
    
