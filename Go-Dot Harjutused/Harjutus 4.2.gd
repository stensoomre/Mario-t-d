# Sten Soomre
# HKHK
# 4/4/2022 23:02
extends Node

func _ready(): # siia tekitab oma skripti, et pärast käivitamist teeks, midagi ka 
	var player = {"name":"john", "str":38, "def":16, "gold":0, "items":["sword","stuff", "bow"]}
	print(player.gold)
	for i in range(5):
		player.gold += 5
		print("+5 Kulda")
	print(player.gold)
