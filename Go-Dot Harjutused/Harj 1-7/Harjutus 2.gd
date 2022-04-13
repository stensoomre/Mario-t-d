# Sten Soomre
# HKHK
# 4/4/2022 23:02
extends Node

func _ready(): # siia tekitab oma skripti, et pärast käivitamist teeks, midagi ka 
	var raha = 106
	var hind = 100
	var summa = raha - hind
	var puudu = hind-summa
	print("Sul on: ", raha," raha")
	print("Kulutan ", hind ," raha")
	raha -= hind
	print("Sul on: ", raha," raha")
	print("Kulutan ", hind ," raha")
	if summa >= hind:
		raha -= hind
		print("Sul oli piisvalt")
	else:
		print("Sul jäi puudu ", puudu, " raha")
	
	
	var a = 206
	var b = 200
	var pindala = a*b
	if a*4 == b*4:
		print("Küljed ", a , " ja ", b, " | Moodustavad ruudu")
	else:
		print("Küljed ", a , " ja ", b, " | Moodustavad ristküliku")
	print("Selle pindala oleks ", pindala)
