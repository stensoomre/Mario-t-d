# Lihtne blackjacki mäng vaatame kui hästi tuleb
from random import *

from time import sleep
import os
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def main():
    global raha
    screen_clear()
    print("""
    ###############################
    
            Tere tulemast
             Blackjacki!""")
    print("    ") 
    print("            " ,difficulty , "tase")
    print("    ") 
    print("    ###############################")
    print("            Sul on ",raha,"€")
    if raha == 0:
        print("  Tahad raha juurde saada?: PALUN")
    print("""    ###############################

    Alustamiseks kirjuta:      PLAY
    Sättete vahetamiseks:  SETTINGS
    Kes selle koodi tegid:  CREDITS
    
    ###############################
    Versioon: 1.16
    """)
    global arv
    global arv2
    global tyhiarv
    global tyhiarv1
    global kaartarv
    global kaartarv2
    global botil
    global stand
    global stand1
    global panus
    arv = 0
    arv2 = 0
    tyhiarv = 2
    tyhiarv1 = 0
    kaartarv = 2
    kaartarv2 = 2
    botil = 0
    stand = 0
    stand1 = 0
    panus = 0
    soov = input().upper()

    if soov == "PLAY":
        print("Palju panustad €? Sul on ",raha,"€ : ")
        panus = int(input())
        if panus > raha:
            print("Sa ei saa panustada raha mida sul pole!!!")
            sleep(2)
            main()            
        if panus < raha:
            randomnimi()
        if panus == raha:
            screen_clear()
            print("Kas oled kindel, et soovid kõik oma raha panustada?")
            pariselt = input().upper()
            if pariselt == "JAH" or "JA":
                randomnimi()
            if pariselt == "EI":
                print("Ma arvasin ka nii.")
                sleep(2)
                main()
    if soov == "SETTINGS":
        settings()
    if soov == "CREDITS":
        credits()
    if soov == "PALUN":
        if raha == 0:
            print("Palun need on mu ülejäänud taara tšekkid.")
            print("               +100 €                    ")
            raha = raha + 100
            sleep(2)
            main()
        if raha != 0:
            print("Mida sa siin teed ah?")
            sleep(1)
            main()
        
    else:
        print("Vigane käsk: ", soov)
        print("Kas ikka kirjutasid õieti?")
        sleep(2)
        main()
    
def settings():
    screen_clear()
    print("""
    ##############################
            Sätted mängul
    ##############################
    """)
    print("Siin pole veel midagi ):") 
    print("")
    print("(BACK) Tagasi?")
    soov2 = input().upper()
    if soov2 == "BACK":
        main()
    else:
        main()
        
def credits():
    screen_clear()
    print("""
    ###############################
               Arendajad
    ###############################
    
    Kirjutas:           Sten Soomre
    Tegi:               Sten Soomre
    Proovitestis:       Sten Soomre
    
    ###############################
    
    (BACK) Tagasi?
    """)
    soov4 = input().upper()
    if soov4 == "BACK":
        main()
    else:
        main()
        
def info():
    screen_clear()
    global arv2
    global arv
    arv2 = arv;
    print("""
    ###############################
    #           Info              #
    #####################################################################
    
     Mäng on tegelikult väga lihtne.
     Sul on vaja ainult saada nii palju kaarte, et nende numbri kogus
     oleks vähemalt 21, üle ei tohi minna.
     
     
     Need kaartid siin on väärtusega 10 alati:
     
             ┌───────┐         ┌───────┐         ┌───────┐                                            
             │ J     │         │ Q     │         │ K     │                               
             │       │         │       │         │       │     
             │       │         │       │         │       │
             │     J │         │     Q │         │     K │                                   
             └───────┘         └───────┘         └───────┘
              (Poiss)           (Emand)           (Kunn)
             
     Aga see kaart on väärtusega 1 ja 11. Ta on 1 siis, kui sul läks
     kogemata üle 21 aga ta on 11 siis kui veel ole läinud!!!
     
                               ┌───────┐
                               │ A     │
                               │       │ 
                               │       │
                               │     A │
                               └───────┘
                                 (Äss)
     
    #####################################################################
    
    (BACK) Tagasi?
    """)
    soov5 = input().upper()
    if soov5 == "BACK":
        play()
    else:
        info()


def kaart(erikaart):
    global arv
 
    if erikaart == 1:  
        arv = arv + 1
        return ["┌───────┐",
                "│ 1     │",
                "│       │",
                "│       │",
                "│     1 │",
                "└───────┘",]
        

    elif erikaart == 2:
        arv = arv + 2
        return ["┌───────┐",
                "│ 2     │",
                "│       │",
                "│       │",
                "│     2 │", # katiki
                "└───────┘",]
        
        
    elif erikaart == 3:
        arv = arv + 3
        return ["┌───────┐",
                "│ 3     │", # katki
                "│       │",
                "│       │",
                "│     3 │",
                "└───────┘",]
        
        
    elif erikaart == 4:
        arv = arv + 4
        return ["┌───────┐",
                "│ 4     │",
                "│       │",
                "│       │", # katki
                "│     4 │",
                "└───────┘",]
        
        
    elif erikaart == 5:
        arv = arv + 5
        return ["┌───────┐",
                "│ 5     │",
                "│       │",
                "│       │",
                "│     5 │",
                "└───────┘",]
        
        
    elif erikaart == 6:
        arv = arv + 6
        return ["┌───────┐",
                "│ 6     │",
                "│       │",
                "│       │",
                "│     6 │",
                "└───────┘",]
        
        
    elif erikaart == 7:
        arv = arv + 7
        return ["┌───────┐",
                "│ 7     │",
                "│       │",
                "│       │",
                "│     7 │",
                "└───────┘",]
        
        
    elif erikaart == 8:
        arv = arv + 8
        return ["┌───────┐",
                "│ 8     │",
                "│       │",
                "│       │",
                "│     8 │",
                "└───────┘",]
        
        
    elif erikaart == 9:
        arv = arv + 9
        return ["┌───────┐",
                "│ 9     │",
                "│       │",
                "│       │",
                "│     9 │",
                "└───────┘",]
        
        
    elif erikaart == 10:
        arv = arv + 10
        return ["┌───────┐",
                "│ 10    │",
                "│       │",
                "│       │",
                "│    10 │",
                "└───────┘",]
        
        
    elif erikaart == 11:
        arv = arv + 10
        return ["┌───────┐",
                "│ J     │",
                "│       │",
                "│       │",
                "│     J │",
                "└───────┘",]
        
        
    elif erikaart == 12:
        arv = arv + 10
        return ["┌───────┐",
                "│ Q     │",
                "│       │",
                "│       │",
                "│     Q │",
                "└───────┘",]
        
        
    elif erikaart == 13:
        arv = arv + 10
        return ["┌───────┐",
                "│ K     │",
                "│       │",
                "│       │",
                "│     K │",
                "└───────┘",]
        
        
    else:
        arv = arv + 11 #Hetkel ainult
        return ["┌───────┐",
                "│ A     │",
                "│       │",
                "│       │",
                "│     A │",
                "└───────┘",]

        
# print(                                                  # print the whole
#       '\n'.join(                                        # join the lines
#                 map('   '.join,                         # join the swapped chunks
#                     zip(*[                              # swap the chunks
#                           kaart(random.randint(1,14))   # valib suvalise erikaarti / number kaarte + 1(else)
#                                  for i in range(2)      # kordab 2 korda
#                          ]
#                         )
#                     )
#                )
#      )
  
def tyhikaart():
        return ["┌───────┐",
                "│ ?     │",
                "│       │",
                "│       │",
                "│     ? │",
                "└───────┘",]
    
def randomnimi():
    global nimevalik
    nimevalik = choice("Timmu Adolf Peeter Margus Urod Dima Kolya".split())
    randomgen()
    play()

def randomgen():
    global aaa
    global bbb
    global ccc
    global ddd
    global eee
    global fff
    global ggg
    global hhh
    
    aaa = randint(1,14)
    bbb = randint(1,14)
    ccc = randint(1,14)
    ddd = randint(1,14)
    eee = randint(1,14)
    fff = randint(1,14)
    ggg = randint(1,14)
    hhh = randint(1,14)


def play():
    global aaa
    global bbb
    global ccc
    global ddd
    global eee
    global fff
    global ggg
    global hhh
    global arv2
    global arv
    arv2 = arv;
    global kaartarv
    global kaartarv1
    kaartarv2 = kaartarv;
    global tyhiarv
    global tyhiarv1
    tyhiarv1 = tyhiarv;
    global botil
    global stand
    global stand1
    global raha
    
    stand1 = 0

    
    screen_clear()
    print("    #######################")
    print("       AI." + nimevalik)    # mai viitsinud mingit random geni teha nimedega
    print("    ")
    if difficulty == "Kerge":
        if botil == 0:
            botil = randint(1,10) + randint(1,10)
            print('    \n'.join(map('   '.join, zip(*[tyhikaart() for i in range(tyhiarv)]))))
        else:
            if botil < 12: # Hittib kui on alla
                botil = botil + randint(1,10)
                tyhiarv = tyhiarv + 1
                if botil > 21: # Kaotab kui on 21
                    print("########################################################")
                    print(" AI. ",nimevalik," oli ",botil,"              SA VÕITSID")
                    print("########################################################")
                    print("                    +",panus,"€")
                    raha = raha + panus
                    sleep(5)

                else:
                    print('    \n'.join(map('   '.join, zip(*[tyhikaart() for i in range(tyhiarv)]))))    
            else: # Standib kui üle
                stand1 = 1
                if botil > 21: # Kaotab kui on 21
                    print("########################################################")
                    print(" AI. ",nimevalik," oli ",botil,"              SA VÕITSID")
                    print("########################################################")
                    print("                    +",panus,"€")
                    raha = raha + panus
                    sleep(5)

                else:
                    stand1 = 1
                    print('    \n'.join(map('   '.join, zip(*[tyhikaart() for i in range(tyhiarv)]))))
                    if stand > 0:
                        if botil > arv:
                            print("########################################################")
                            print(" AI. ",nimevalik," oli ",botil,"     SA KAOTASID!!!! :( ")
                            print("########################################################")
                            print("                    -",panus,"€")
                            raha = raha - panus
                            sleep(5)
                            main()
                        elif botil < arv:
                            print("########################################################")
                            print(" AI. ",nimevalik," oli ",botil,"              SA VÕITSID")
                            print("########################################################")
                            print("                    +",panus,"€")
                            raha = raha + panus
                            sleep(5)
                            main()
                        elif botil == arv:
                            print("########################################################")
                            print("                         VIIK")
                            print("########################################################")
                            sleep(5)
                            main()
        
    if difficulty == "Keskmine":
        if botil == 0:
            botil = randint(1,10) + randint(1,10)
            print('    \n'.join(map('   '.join, zip(*[tyhikaart() for i in range(tyhiarv)]))))
        else:
            if botil < 15: # Hittib kui on alla
                botil = botil + randint(3,10)
                tyhiarv = tyhiarv + 1
                if botil > 21: # Kaotab kui on 21
                    print("########################################################")
                    print(" AI. ",nimevalik," oli ",botil,"              SA VÕITSID")
                    print("########################################################")
                    print("                    +",panus,"€")
                    raha = raha + panus
                    sleep(5)

                else:
                    print('    \n'.join(map('   '.join, zip(*[tyhikaart() for i in range(tyhiarv)]))))    
            else: # Standib kui üle
                stand1 = 1
                if botil > 21: # Kaotab kui on 21
                    print("########################################################")
                    print(" AI. ",nimevalik," oli ",botil,"              SA VÕITSID")
                    print("########################################################")
                    print("                    +",panus,"€")
                    raha = raha + panus
                    sleep(5)

                else:
                    stand1 = 1
                    print('    \n'.join(map('   '.join, zip(*[tyhikaart() for i in range(tyhiarv)]))))
                    if stand > 0:
                        if botil > arv:
                            print("########################################################")
                            print(" AI. ",nimevalik," oli ",botil,"     SA KAOTASID!!!! :( ")
                            print("########################################################")
                            print("                    -",panus,"€")
                            raha = raha - panus
                            sleep(5)
                            main()
                        elif botil < arv:
                            print("########################################################")
                            print(" AI. ",nimevalik," oli ",botil,"              SA VÕITSID")
                            print("########################################################")
                            print("                    +",panus,"€")
                            raha = raha + panus
                            sleep(5)
                            main()
                        elif botil == arv:
                            print("########################################################")
                            print("                         VIIK")
                            print("########################################################")
                            sleep(5)
                            main()

                    
    if difficulty == "Raske":
        if botil == 0:
            botil = randint(1,10) + randint(1,10)
            print('    \n'.join(map('   '.join, zip(*[tyhikaart() for i in range(tyhiarv)]))))
        else:
            if botil < 17: # Hittib kui on alla
                botil = botil + randint(3,10)
                tyhiarv = tyhiarv + 1
                if botil > 21: # Kaotab kui on 21
                    print("########################################################")
                    print(" AI. ",nimevalik," oli ",botil,"              SA VÕITSID")
                    print("########################################################")
                    print("                    +",panus,"€")
                    raha = raha + panus
                    sleep(5)

                else:
                    print('    \n'.join(map('   '.join, zip(*[tyhikaart() for i in range(tyhiarv)]))))    
            else: # Standib kui üle
                stand1 = 1
                if botil > 21: # Kaotab kui on 21
                    print("########################################################")
                    print(" AI. ",nimevalik," oli ",botil,"              SA VÕITSID")
                    print("########################################################")
                    print("                    +",panus,"€")
                    raha = raha + panus
                    sleep(5)
                else:
                    stand1 = 1
                    print('    \n'.join(map('   '.join, zip(*[tyhikaart() for i in range(tyhiarv)]))))
                    if stand > 0:
                        if botil > arv:
                            print("########################################################")
                            print(" AI. ",nimevalik," oli ",botil,"     SA KAOTASID!!!! :( ")
                            print("########################################################")
                            print("                    -",panus,"€")
                            raha = raha - panus
                            sleep(5)
                            main()
                        elif botil < arv:
                            print("########################################################")
                            print(" AI. ",nimevalik," oli ",botil,"              SA VÕITSID")
                            print("########################################################")
                            print("                    +",panus,"€")
                            raha = raha + panus
                            sleep(5)
                            main()
                        elif botil == arv:
                            print("########################################################")
                            print("                         VIIK")
                            print("########################################################")
                            sleep(5)
                            main()
    stand = 0
    print("    ")
    print("    ")
    print("    ")
    print("    ")
    print("    ")
    if kaartarv == 8:
        print('    \n'.join(map('   '.join, zip(*[kaart(aaa), kaart(bbb), kaart(ccc), kaart(ddd), kaart(eee), kaart(fff), kaart(ggg), kaart(hhh)]))))
        arv = arv2+ccc+ddd+eee+fff+ggg+hhh
                
        if arv > 21: # Kaotab kui on 21
            print("########################################################")
            print(" AI. ",nimevalik," oli ",botil,"     SA KAOTASID!!!! :( ")
            print("########################################################")
            print("                    -",panus,"€")
            raha = raha - panus
            sleep(5)
            main()
    if kaartarv == 7:
        print('    \n'.join(map('   '.join, zip(*[kaart(aaa), kaart(bbb), kaart(ccc), kaart(ddd), kaart(eee), kaart(fff), kaart(ggg)]))))
        arv = arv2+ccc+ddd+eee+fff+ggg
        if arv > 21: # Kaotab kui on 21
            print("########################################################")
            print(" AI. ",nimevalik," oli ",botil,"     SA KAOTASID!!!! :( ")
            print("########################################################")
            print("                    -",panus,"€")
            raha = raha - panus
            sleep(5)
            main()
    if kaartarv == 6:
        print('    \n'.join(map('   '.join, zip(*[kaart(aaa), kaart(bbb), kaart(ccc), kaart(ddd), kaart(eee), kaart(fff)]))))
        arv = arv2+ccc+ddd+eee+fff
        if arv > 21: # Kaotab kui on 21
            print("########################################################")
            print(" AI. ",nimevalik," oli ",botil,"     SA KAOTASID!!!! :( ")
            print("########################################################")
            print("                    -",panus,"€")
            raha = raha - panus
            sleep(5)
            main()
    if kaartarv == 5:
        print('    \n'.join(map('   '.join, zip(*[kaart(aaa), kaart(bbb), kaart(ccc), kaart(ddd), kaart(eee)]))))
        arv = arv2+ccc+ddd+eee
        if arv > 21: # Kaotab kui on 21
            print("########################################################")
            print(" AI. ",nimevalik," oli ",botil,"     SA KAOTASID!!!! :( ")
            print("########################################################")
            print("                    -",panus,"€")
            raha = raha - panus
            sleep(5)
            main()
    if kaartarv == 4:
        print('    \n'.join(map('   '.join, zip(*[kaart(aaa), kaart(bbb), kaart(ccc), kaart(ddd)]))))
        arv = arv2+ccc+ddd
        if arv > 21: # Kaotab kui on 21
            print("########################################################")
            print(" AI. ",nimevalik," oli ",botil,"     SA KAOTASID!!!! :( ")
            print("########################################################")
            print("                    -",panus,"€")
            raha = raha - panus
            sleep(5)
            main()
    if kaartarv == 3:
        print('    \n'.join(map('   '.join, zip(*[kaart(aaa), kaart(bbb), kaart(ccc)]))))
        arv = arv2+ccc
        if arv > 21: # Kaotab kui on 21
            print("########################################################")
            print(" AI. ",nimevalik," oli ",botil,"     SA KAOTASID!!!! :( ")
            print("########################################################")
            print("                    -",panus,"€")
            raha = raha - panus
            sleep(5)
            main()
    if kaartarv == 2:
        print('    \n'.join(map('   '.join, zip(*[kaart(aaa), kaart(bbb)]))))
        if arv2 != 0:
            if arv/2 == arv2:
                arv = arv2
        
    
        
    print("    ")
    if arv2 != 0:
        if arv/2 == arv2:
            arv = arv2
    print("    ")     
    print("      Sina, sul on: ", arv ,"/21")
    print("  ##############################")
    print("    ") 
    print("    Mida soovid teha?         ")
    print("    ")
    print("    ") 
    print("    Veel üks kaart?    - HIT  ")
    print("    ") 
    print("    Oled rahul mis on? - STAND")
    print("    ") 
    print("    Mida teha?         - INFO ")
    print("    ") 
    print("  ##############################")
    soov10 = input("    ").upper()
    if soov10 == "INFO":
        info()
    if soov10 == "STAND":
        stand = 1
        if stand1 > 0:
            if botil > arv:
                print("########################################################")
                print(" AI. ",nimevalik," oli ",botil,"     SA KAOTASID!!!! :( ")
                print("########################################################")
                print("                    -",panus,"€")
                raha = raha - panus
                sleep(5)
                main()
            elif botil < arv:
                print("########################################################")
                print(" AI. ",nimevalik," oli ",botil,"              SA VÕITSID")
                print("########################################################")
                print("                    +",panus,"€")
                raha = raha + panus
                sleep(5)
                main()
            elif botil == arv:
                print("########################################################")
                print("                         VIIK")
                print("########################################################")
                sleep(5)
                main()
        play()
    if soov10 == "HIT":
        kaartarv = kaartarv + 1
        play()
    sleep(5)

while True:
    print("""

(Palun avada see programeerimis skript mängimise ajal täisekraanile)
        
        
                   Sisesta raskustase
                 
    ###################################################
    
          Kerge         Keskmine         Raske
          
    ###################################################

         """)
    difficulty = input().capitalize()
    
    global raha
    if difficulty == "Kerge":
        raha = 2500
        main()
    elif difficulty == "Keskmine":
        raha = 1000
        main()  
    elif difficulty == "Raske":
        raha = 250
        main()