# Sten Soomre
# HKHK
# 4/4/2022 23:02
extends Node
var tasu = 0
var tunnid = 30
var tunnitasu = 10
var tootunnid = 10 #mdea mis see peab olema, las olgu 10 ss
var eksamitulemused = []
var arv = 0
func random(a,b): # funktioon oleks lihtsam
	var rand = RandomNumberGenerator.new()#lühend
	rand.randomize() # randomizib
	var rand2 = rand.randi_range(a,b) #genib
	return rand2 # returnib

func palk(tunnid, tunnitasu):
	if tunnid >= 40:
		tasu = tunnid*tunnitasu
	else: 
		tasu = 40*tunnitasu+(tunnid-40)*1.5*tootunnid
	tasu = round(tasu)
	print("Tasu: ",tasu, " | Tunde: ", tunnid)
	eksam(tunnid, tasu)
func eksam(tunnid, tasu):
	var punktid = 0
	if tunnid >= 40: # Kui väga tubli saad 20
		punktid += 20
	elif tunnid >= 30: # Vähem tublimad saavad vähem
		punktid += 15
	else:
		punktid += 10 # lollkad saavad vähim
	
	if tasu >= 500:
		punktid += 40
	elif tasu >= 400:
		punktid += 30
	else:
		punktid += 10
	var rand2 = random(1,40)
	punktid += rand2
	eksamitulemused.append(punktid)
	
	
func suvakad():
	for i in range(2):
		var rand2 = random(1,100)
		if arv == 0:
			tunnid = rand2
			arv += 1
		else:
			tunnitasu = rand2
	arv = 0
func keskmine():
	var keskmine = 0
	for i in eksamitulemused:
		keskmine += i
	keskmine = keskmine/len(eksamitulemused)
	return keskmine

func hinded():
	var hinded = []
	for i in eksamitulemused:
		if i >= 90:
			hinded.append(str(i)+" - 5")
		elif i >= 75:
			hinded.append(str(i)+" - 4")
		elif i >= 50:
			hinded.append(str(i)+" - 3")
		else:
			hinded.append(str(i)+" - 2")
	return hinded
	
func _ready(): # siia tekitab oma skripti, et pärast käivitamist teeks, midagi ka

	for i in range(5): # Töölised lähevad testile :)
		suvakad()
		palk(tunnid, tunnitasu)
	var keskmine = keskmine()
	print(keskmine)
	print(eksamitulemused)
	var hinded = hinded()
	print(hinded)
