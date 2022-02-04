# Lihtne blackjacki mäng vaatame kui hästi tuleb

from random import *


from os import system, name
from time import sleep
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


        

def main():
    clear()
    print("""
    ###############################
            Tere tulemast
             Blackjacki!""")
    print("            " ,difficulty , "tase")
    print("""
    ###############################
    Alustamiseks kirjuta:      PLAY
    Sättete vahetamiseks:  SETTINGS
    Kes selle koodi tegid:  CREDITS
    ###############################
    Versioon: 1
    """)
    soov = input()

    if soov == "PLAY":
        play()
    if soov == "SETTINGS":
        settings()
    if soov == "CREDITS":
        credits()
    else:
        print("Vigane käsk: ", soov)
        main()
    
def settings():
    clear()
    print("""
    ##############################
            Sätted mängul
    ##############################
    """)
    print("Siin pole veel midagi ):") 
    print("")
    print("(Back) Tagasi?")
    soov2 = input()
    if soov2 == "Back":
        main()
    else:
        main()
        
def credits():
    clear()
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

while True:
    print("Sisesta raskustase: Kerge , Keskmine, Raske.")
    difficulty = input().capitalize()
    if difficulty is "Kerge" or "Keskmine" or "Raske":
        main()
        break
