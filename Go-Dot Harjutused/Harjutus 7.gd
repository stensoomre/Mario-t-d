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
	
	var vastasehp = $"Harjutused".vastasehp
	$"Bg/Elud".text = "Elud: " +str(vastasehp)
