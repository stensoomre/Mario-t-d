# Sten Soomre
# Harj. 15
# Sest ma mängisin tunnis :(
import re
kraadid = open('kraadid.txt', encoding="UTF-8")

print("{0:<13}{1:<9}{2:<12}".format("Kuu", "Päev", "Kui soe oli",))
print("---------------------------------")
for line in kraadid:
    mitmes, mitmes2, paev, soe, soe1 = 0,0,0,0,0
    kuuinfo = line.split()
    kuu = kuuinfo[0]   
    
#######################
#  Allolev osa töötab #
#######################
    for paev in kuuinfo:
         if re.search('[0-9]', paev):
            mitmes += 1
            if soe1 > 0:               # Lihtne vaade kas kraade on enne salvestatud
                if paev > soe:         # Kui päev on soejem, kui kõige soeem siis salvestab.
                    soe = paev
                    mitmes3 = mitmes;
                    continue 
                else:
                    continue            # Kui see päev pole kõige soejem siis skipib
            else:
                soe = paev             # Kui ei ole annab sellele esimese väärtuse
                soe1 += 1              # Ja teeb nii et rohkem ei kordaks
                continue
    soe = str(soe) + "°C"
    print("{0:<13}{1:<9}{2:<12}".format(kuu, mitmes3, soe,))
    mitmes2 += 1

