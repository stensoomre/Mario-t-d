extends Node

var point = 0
var PPC = 1
var arv = 0


func _process(delta):
	$"Point Score".text = str(point)
	$"PPC".text = str(PPC)
	$"Shop_1".text = str("PAY ", arv, " POINTS FOR 1 PPC")
# Called when the node enters the scene tree for the first time.
func _ready():
	arv = 100
	pass # Replace with function body.




func _on_TextureButton_pressed():
	point += PPC
	print(point)
	pass # Replace with function body.


func _on_Shop_1_pressed():
	
	if point >= arv:
		point -= 100
		PPC += 1
		arv = arv*1.2
	pass # Replace with function body.
