import re
iplist = []
plist = []
valjad = open('valjad.txt')
for line in valjad:
    ipaddress = "None"
    parool = "None"
    if line.find(".") > 0:
        ipaddress = line[:len(line) - 1]
        iplist.append(ipaddress)
    else:
        parool = line[:len(line) - 1]
        plist.append(parool)
        for a in range(0,10):
            if parool.find(str(a)) > 0:
                print(parool)

# print(iplist)
# print(plist)

            
     