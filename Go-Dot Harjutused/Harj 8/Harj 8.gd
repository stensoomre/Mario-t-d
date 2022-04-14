extends Node
 
var summa = 0
 
func _process(delta):
	$"Bg/Kast/Tekst".text = str(summa)
	$"Bg/nupp".text = "Vajuta mind"

func _on_nupp_pressed():
	summa += 1
