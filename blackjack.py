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
    #screen_clear()
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
        randomnimi()
    if soov == "SETTINGS":
        settings()
    if soov == "CREDITS":
        credits()
    else:
        print("Vigane käsk: ", soov)
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
    print("(Back) Tagasi?")
    soov2 = input()
    if soov2 == "Back":
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
    (Back)Tagasi?
    """)
    soov4 = input()
    if soov4 == "Back":
        main()
    else:
        main()

def randomgen():
    global kaart
    global a1
    global a2
    global arv
    a1 = randint(1,10)
    b1 = randint(1,10)
    arv = a1 + b2
kaart = '''\
    ______    ______
   /     /   /     /
     {a}        {b}  
 /_____/   /_____/
                     '''.format(a=a1, b=b1) # a on siin kui varieable mille väärtus on = järgi juurde saab panna , https://stackoverflow.com/questions/10112614/how-do-i-create-a-multiline-python-string-with-inline-variables
   
global tyhikaart
tyhikaart = '''\
    ______
   /     /   
  /  ?  /    
 /_____/     
                     '''.format(length='multi-line', ordinal='second')    
    
def randomnimi():
    global nimevalik
    nimevalik = choice("Timmu Adolf Peeter Margus Urod Dima Kolya".split())
    randomgen()
    play()
    
def play():
    screen_clear()
    print("#######################")
    print("   AI." + nimevalik)    # mai viitsinud mingit random geni teha nimedega
    print("")
    print(tyhikaart + "\n" + tyhikaart)
    print("")
    print("")
    print("")
    print("")
    print("")
    print(kaart)
    print("")
    print("")     
    print("     Sina, sul on: ", arv ,"/21")
    print("#######################")
    sleep(5)



while True:
    print("Sisesta raskustase: Kerge , Keskmine, Raske.")
    difficulty = input().capitalize()
    if difficulty is "Kerge" or "Keskmine" or "Raske":
        main()
        break
