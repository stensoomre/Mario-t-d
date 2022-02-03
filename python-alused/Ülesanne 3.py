# Harjutus 3
# Sten Soomre
# 03.02.22


# Nimi
# Sten Soomre
# 03.02.22

nimi = input("Siseta oma nimi: ")
nimi2 = nimi.capitalize()
print(nimi2.strip(" ")) # Täiega töötab

# Email
# Sten Soomre
# 03.02.22

email= input("Sisesta oma email: ")
print("@" in email) # Väga sitt kood, ausalt saab exploitida pannes lih @

# Vandumine
# Sten Soomre
# 03.02.22

S = input("Ära vannu(kurat ütle): ")
S = S.lower()
V = S.replace("kurat","!£%€#") # Semi ei tööta aga moh \_(.-.)_/
print(V)

# Tundide ajad
# Sten Soomre
# 03.02.22

aeg1 = input("Algusaeg:")
aeg2 = input("Lõpuaeg:")
hh1, mm1 = aeg1.split(":")
hh2, mm2 = aeg2.split(":")
vastus = (int(hh2)*60+int(mm2)) - (int(hh1)*60+int(mm1)) # Overcomplicated
h = vastus//60
m = vastus%60
print(f"{h}:{m}")

# Palindroom
# Sten Soomre
# 03.02.22

sisestus = input("Sisesta Palindroom:")
print(sisestus == sisestus[::-1]) # See on seaalne wat moment