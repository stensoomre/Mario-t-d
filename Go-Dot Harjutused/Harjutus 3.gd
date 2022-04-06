# Sten Soomre
# HKHK
# 4/4/2022 23:02
extends Node
func random(a,b): # funktioon oleks lihtsam
	var rand = RandomNumberGenerator.new()#lühend
	rand.randomize() # randomizib
	var rand2 = rand.randi_range(a,b) #genib
	return rand2 # returnib
func _ready(): # siia tekitab oma skripti, et pärast käivitamist teeks, midagi ka 
	var enemyhp = 100
	var playerhp = 100 #Sättib algus elud paika 
	
	while playerhp or enemyhp >= 1:	
		var rand2 = random(1,12) # küsib
		playerhp -= rand2 # pärib
		print("P2 Hit: ",rand2," | P1 Life: ",playerhp)
		if playerhp >= 1:
			pass
		else:
			break
		var rand3 = random(1,12) # küsib
		enemyhp -= rand3 # pärib
		print("P1 Hit: ",rand3," | P2 Life: ",enemyhp)
		if enemyhp >= 1:
			pass
		else:
			break
	print("Game Over!")
	if playerhp > enemyhp:
		print("Võitis P1")
	else:
		print("Võitis P2")
