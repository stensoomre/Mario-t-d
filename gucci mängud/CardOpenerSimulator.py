from random import *
from time import *

divine = 100000 # 0,00001%
mythical = 1000 # 0,001%
legendary = 100 # 0,01%
epic = 50 # 0,5%
rare = 6 # 16,6%
uncommon = 3 # 33,3%
common = 1
debug = 0
global money
money = 0.01

def main():
    global money
    money = round(money,2)
    print("""
            Card Pack Simulator
            
    Each pack is 1$!!
    Pack = 4 cards!!!
            
    TYPE  1  to open a pack!!!
    TYPE  2  to make money!!!
    TYPE  3  to see the chances!
""")
    print("Money:",money,"$")
    e = input("")
    if e == "1":
        arv2 = input("How many packs you want to open? (number or 'all')  ")
        try:
            arv = int(arv2)
            text = int(input("""
        Type the corresponding number for a option.
        [1] - Open packs with text based only
        [2] - Open packs with a picture
        [0] - Open packs quick
            """))
            open(arv, text)
        except:
            if arv2 == "all":
                arv = int(money //1)
                text = int(input("""
        Type the corresponding number for a option.
        [1] - Open packs with text based only
        [2] - Open packs with a picture
        [0] - Open packs quick
            """))
                open(arv, text)
            else:
                print("Vale number!!!")
                sleep(2)
                main()
    elif e == "2":
        math()
    elif e == "3":
        print("""
0,00001%   Divine
0,001%     Mythical
0,01%      Legendary
0,5%       Epic
16,6%      Rare
33,3%      Uncommon
49,58899%  Common""")
        input("")
        main()
    else:
        print("Vale vaste")
        sleep(2)
        main()

def open(arv, text):
    global money
    if money >= arv*1:
        money -= arv*1
        moneygot = 0
        div = 0
        myth = 0
        legen = 0
        ep = 0
        rar = 0
        un = 0
        comm = 0
        for i in range(arv*4):
            if randint(1,divine) == divine:
                moneygot += 10000
                if text == 1:
                    print("You got a divine card")
                div += 1
                if text == 2:
                    print ("""
    ┌───────┐
    │ Divine│
    │       │
    │       │
    │   card│
    └───────┘""")
            else:
                if randint(1,mythical) == mythical:
                    moneygot += 70
                    if text == 1:
                        print("You got a mythical card")
                    myth += 1    
                    if text == 2:
                        print ("""
    ┌───────┐
    │Myth   │
    │   ical│
    │       │
    │   card│
    └───────┘""")
                else:
                    if randint(1,legendary) == legendary:
                        moneygot += 5.00
                        if text == 1:
                            print("You got a legendary card")
                        legen += 1
                        if text == 2:
                            print ("""
    ┌───────┐
    │Legen  │
    │  Dary │
    │       │
    │   card│
    └───────┘""")
                    else:
                        if randint(1,epic) == epic:
                            moneygot += 1
                            if text == 1:
                                print("You got a epic card")
                            ep += 1    
                            if text == 2:
                                print ("""
    ┌───────┐
    │   Epic│
    │       │
    │       │
    │   card│
    └───────┘""")
                        else:
                            if randint(1,rare) == rare:
                                moneygot += 0.20
                                if text == 1:
                                    print("You got a epic card")
                                rar += 1
                                if text == 2:
                                    print ("""
    ┌───────┐
    │  Rare │
    │       │
    │       │
    │   card│
    └───────┘""")
                            else:
                                if randint(1,uncommon) == uncommon:
                                    moneygot += 0.10
                                    if text == 1:
                                        print("You got a uncommon card")
                                    un += 1
                                    if text == 2:
                                        print ("""
    ┌───────┐
    │Not so │
    │ Common│
    │       │
    │   card│
    └───────┘""")
                                else:
                                    if randint(1,common) == common:
                                        moneygot += 0.01
                                        if text == 1:
                                            print("You got a common card")
                                        comm += 1
                                        if text == 2:
                                            print ("""
    ┌───────┐
    │ Common│
    │       │
    │       │
    │   card│
    └───────┘""")
        moneygot = round(moneygot, 2)
        money +=moneygot
        money = round(money, 2)
        print("You unpacked")
        print(div ," - Divine cards          | 10000$ per 1")
        print(myth ," - Mythical cards       | 70$ per 1")
        print(legen ," - Legendary cards     | 5$ per 1")
        print(ep ," - Epic cards             | 1$ per 1")
        print(rar, " - Rare cards            | 0.20$ per 1")
        print(un ," - Uncommon cards         | 0.10$ per 1")
        print(comm ," - Common cards         | 0.01$ per 1")
        print("You have earned ", moneygot,"$")
        if arv >= moneygot:
            print("Man you lost",round(moneygot-arv,2),"$")
        else:
            print("Man you profitted",round(moneygot-arv,2),"$")
        print("")
        print(money,"$ - Money you have")
        sleep(2)
        main()
    else:
        print("You dont have enough funds")
        print("You need", round(money-arv,2),"$ more to buy", arv,"packs!")
        sleep(2)
        main()
        
def math():

    global money
    try:
        print("")
        print("")
        print("")
        print("")
        a = randint(1,100)
        b = randint(1,100)
        valik = randint(1,2)
        if valik == 1:
            c= a-b
            print("What is the answer?")
            print(a,"-",b,"= ???")
            if debug == 1:
                print(c)
            d = int(input(""))
            if d == c:
                print("Correct!!!")
                e = randint(1,100)
                money += e
                print("You earned",e,"$!!")
                sleep(2)
                main()
            else:
                print("Incorrect!!! :C")
                sleep(2)
                main()
        
        else:
            c = a+b
            print(a,"+",b,"= ???")
            if debug == 1:
                print(c)
            d = int(input(""))
            if d == c:
                print("Correct!!!")
                e = randint(1,100)
                money += e
                print("You earned",e,"$!!")
                sleep(2)
                main()
            else:
                print("Incorrect!!! :C")
                sleep(2)
                main()
    except:
        print("Viga 404")
        sleep(2)
        main()
main()
