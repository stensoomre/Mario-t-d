# Lihtne blackjacki mäng vaatame kui hästi tuleb


# import only system from os
from os import system, name
  
# import sleep to show output for some time period
from time import sleep
import random
  
# define our clear function
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
             Blackjacki!
    ###############################
    Alustamiseks kirjuta:      PLAY
    Sättete vahetamiseks:  SETTINGS
    Kes selle koodi tegid:  CREDITS
    ###############################
    Versioon: 1
    """)
    
def settings():
    clear()
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
    clear()
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

import random


def main():
    clear()
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
    clear()
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
    clear()
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
            
main()
soov = input()

if soov == "PLAY":
    play()
if soov == "SETTINGS":
    settings()
if soov == "CREDITS":
    credits()
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
            
main()
soov = input()

if soov == "PLAY":
    play()
if soov == "SETTINGS":
    settings()
if soov == "CREDITS":
    credits()