# Sten Soomre
# Harjutus 6
# 15.02.22

# facebooki poliitikud

re, ke, sde, irl = 0, 0, 0, 0
erakonnad = 0

with open('s6pru_l6ustaraamatus.txt','r') as sobrad:
    for rida in sobrad:
        enimi, pnimi, er, likes = rida.split()
        print ("{0:<11}{1:<12}{2:<7}{3:<30}".format(enimi, pnimi, er, likes))
        if er=="RE":
            re+=1
        elif er=="SDE":
            sde+=1
        elif er=="IRL":
            irl+=1
        elif er=="KE":
            ke+=1

if re >= 0:
    erakonnad+=1
if ke >= 0:
    erakonnad+=1
if sde >= 0:
    erakonnad+=1
if irl >= 0:
    erakonnad+=1

print()
print(f"IRL: {irl}\nRE: {re}\nSDE: {sde}\nKE: {ke}\n")
print(f"erakondikokku: {erakonnad}")

