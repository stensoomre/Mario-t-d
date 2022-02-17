# Sten Soomre
# Harjutus 8
# 16.02.22
from random import *

def rand(): #Random gen lmaoo
    global varv2
    global aasta2
    global kiirus2
    global hind2
    global nimi2
    varv2 = choice("Sinine Kollane Punane Oranž Lilla Pruun Valge Must Hall Hele-hall Tume-Sinine Tume-Kollane Roosa Beež Neon-Roheline ".split())
    aasta2 = str(randint(1000,2022))+".a"
    kiirus2 = str(randint(10,350))+"km/h"
    hind2 = str(randint(10,50000))+"RUB"
    nimi2 = choice("Volksaagen-Kolf Nissan-Eesti Jalgrattas-venemaalt Nissian-Volks Parim-Auto-2022".split())
    
class auto:
    mark= 'Volksaagen Kolt' #Placeholder
    aasta= 0
    hind= 0
    varv=0
    kiir=0
    
    def lisaaasta(self,x):
        self.aasta = x
    
    def lisahind(self,x):
        self.hind = x
        
    def lisamark(self,x):
        self.mark = x
    
    def lisavarv(self,x):
        self.varv = x
        
    def lisakiir(self,x):
        self.kiir = x
        
    def kuva(self):
        print("{0:<24}{1:<9}{2:<12}{3:<15}{4:<30}".format(self.mark, self.aasta, self.hind, self.varv, self.kiir))

uusobjekt = auto()
rand()
uusobjekt.lisamark(nimi2)
uusobjekt.lisahind(hind2)
uusobjekt.lisaaasta(aasta2)
uusobjekt.lisavarv(varv2)
uusobjekt.lisakiir(kiirus2)
uusobjekt.kuva()

uus = auto()
rand()
uus.lisamark(nimi2)
uus.lisahind(hind2)
uus.lisaaasta(aasta2)
uus.lisavarv(varv2)
uus.lisakiir(kiirus2)
uus.kuva()
