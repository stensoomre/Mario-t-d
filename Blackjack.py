# Lihtne blackjacki mäng vaatame kui hästi tuleb


import random
import time

def main():
    cls
    print("""
    ###############################
            Tere tulemast
             Blackjacki!
    ###############################
    Alustamiseks kirjuta:      PLAY
    Sättete vahetamiseks:  SETTINGS
    Kes selle koodi tegid:  CREDITS
    ###############################
    Versioon: 1
    """)
    
def settings():
    cls
    print("""
    ##############################
            Sätted mängul
    ##############################
    """)
    print("(R) Raskustase:" + difficulty) 
    print("")
    print("(Back) Tagasi?")
    soov2 = input()
    if soov2 == "R":
        raskus()
    if soov2 == "Back":
        main()
    else:
        main()
        
def rasksus():
    cls
    print("""
    ##############################
            Raskustase
    ##############################
    """)
    print("Kerge") 
    print("Kesmine")
    print("Raske")
    soov3 = input()
    if soov3 == "Kerge":
        difficulty = "Kerge"
        settings()
    elif soov3 == "Keskmine":
        difficulty = "Keskmine"
        settings()
    elif soov3 == "Raske":
        difficulty = "Raske"
        settings()
    else:
        raskus()
        
def credits():
    cls
    print("""
    ###############################
               Arendajad
    ###############################
    Kirjutas:           Sten Soomre
    Tegi:               Sten Soomre
    Proovitestis:       Sten Soomre
    ###############################
    (Back)Tagasi?
    """)
    soov4 = input()
    if soov4 == "Back":
        main()
    else:
        main()
            
main()
soov = input()

if soov == "PLAY":
    play()
if soov == "SETTINGS":
    settings()
if soov == "CREDITS":
    credits()