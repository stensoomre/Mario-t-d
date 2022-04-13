extends Node


# Declare member variables here. Examples:
# var a = 2
# var b = "text"

onready var dmg = $"Harjutused".dmg

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

func _process(delta):
	var kuul = $"Harjutused".kuul
	var kuulmax = $"Harjutused".kuulmax
	var dmg = $"Harjutused".dmg
	var kas = $"Harjutused".kas
	var vastasehp = $"Harjutused".vastasehp
	$"Bg/Elud".text = "Elud: " +str(vastasehp)
	if kas == 4:
		$"Bg/END".text = "GAME OVER!!!"
		var punkt = $"Harjutused".punkt
		var tulemus = $"Harjutused".tulemus
		var pihtas = $"Harjutused".pihtas
		var mooda = $"Harjutused".mooda
		tulemus = round(tulemus)
		var lasku = pihtas + mooda
		$"Bg/STATS".text = "Effektiivsus: %s%%\nLaske kokku: %s\nLasid pihta %s lasku\nLasid mõõda %s lasku\nSaavutasid %s punkti" % [tulemus, lasku, pihtas, mooda, punkt]
		get_tree().paused = true
	else:
		if dmg == 0:
			$"Bg/Damage".text = "Pole veel lasknud"
		else:
			if kas == 3:
				$"Bg/Damage".text = "Su relv on laetud"
			elif kas == 2:
				$"Bg/Damage".text = "Relv on tühi"
			elif kas == 0:
				$"Bg/Damage".text = "Pihtas: -"+str(dmg)+" elu"
			else:
				$"Bg/Damage".text = "Lasid mööda"
		$"Bg/Kuul".text = "Kuule: "+str(kuul)+"/"+str(kuulmax)
		if kuul <= kuulmax:
			$"Bg/Kuul".text = "Kuule: "+str(kuul)+"/"+str(kuulmax)+" | Lae relva (R)"
		

