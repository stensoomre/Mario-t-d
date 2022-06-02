from random import *

divine = 100000 # 0,00001%
mythical = 1000 # 0,001%
legendary = 100 # 0,01%
epic = 50 # 0,5%
rare = 6 # 16,6%
uncommon = 3 # 33,3%
common = 1

print("""
        Card Pack Simulator
        
open(x,y)

x = how many
y = [1] - Text based
    [2] - Picture based
    [0] - Nothing

""")

def open(arv, text):
    div = 0
    myth = 0
    legen = 0
    ep = 0
    rar = 0
    un = 0
    comm = 0
    for i in range(arv):
        if randint(1,divine) == divine:
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
    print("You unpacked")
    print(div ," - Divine cards")
    print(myth ," - Mythical cards")
    print(legen ," - Legendary cards")
    print(ep ," - Epic cards")
    print(rar, " - Rare cards")
    print(un ," - Uncommon cards")
    print(comm ," - Common cards")