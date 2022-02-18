# Harjutus 10
# Sten Soomre
# 18.02.2022
import re
import socket
iplist = []
plist = []
valjad = open('valjad.txt')
for line in valjad:
    ipaddress = "None"
    parool = "None"
    if line.find(".") > 2: # Kui listis on . siis on IP
        ipaddress = line[:len(line) - 1]
        try: # Siis kui on ip
            socket.inet_aton(ipaddress) 
            iplist.append(ipaddress)
        except socket.error: # Siis kui see ei ole ip
            continue
    else:
        if line.find(".") > 0:
            continue
        else:
            parool = line[:len(line) - 1]
            if re.search('[a-z]', line): # otsib kas on tähti, väikseid
                if re.search('[A-Z]', line): # otsib kas on tähti suuri
                    if re.search('[0-9]', line): #otsib kas on numbreid
                       plist.append(parool)
            else: #juhul kui pole väikseid äkki on suuri
                if re.search('[A-Z]', line): # otsib kas on tähti suuri
                    if re.search('[0-9]', line): #otsib kas on numbreid
                       plist.append(parool)
            
             
print("IP-adressid")
print(iplist)
print()
print("Paroolid")
print(plist)

