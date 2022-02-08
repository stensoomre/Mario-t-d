from random import *
from time import *

def randomgen():
    global kaart
    global a
    global b
    kaart = '''\
    ______    ______
   /     /   /     /
     {a}        {b}  
 /_____/   /_____/
                     '''.format(a=randint(1,10), b=randint(1,10)) # a on siin kui varieable mille väärtus on = järgi juurde saab panna , https://stackoverflow.com/questions/10112614/how-do-i-create-a-multiline-python-string-with-inline-variables
    
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
print(kaart)
