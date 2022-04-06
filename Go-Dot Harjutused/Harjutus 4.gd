# Sten Soomre
# HKHK
# 4/4/2022 23:02
extends Node
var playerskorrastatud = []
var players = ["Feake","Bradwell","Dreger","Bloggett","Lambole","Daish","Lippiett","Blackie","Stollenbeck","Houseago","Dugall","Sprowson","Kitley","Mcenamin","Allchin","Doghartie","Brierly","Pirrone","Fairnie","Seal","Scoffins","Galer","Matevosian","DeBlase","Cubbin","Izzett","Ebi","Clohisey","Prater","Probart","Samwaye","Concannon","MacLure","Eliet","Kundt","Reyes"]
var arv1 = 0
var arv = 0 
var arv2 = 0
func korrastamine():
	while 1==1:
		break # mai ei oska
	return players		

func _ready(): # siia tekitab oma skripti, et pärast käivitamist teeks, midagi ka 
	print("Mängijad kokku: ", len(players))
	print("Esimene mängija: ", players[0])
	playerskorrastatud = korrastamine()
	print(playerskorrastatud)
	players.append("Sten")
	players.erase("Reyes")
	print(players.max())
	print(players)
