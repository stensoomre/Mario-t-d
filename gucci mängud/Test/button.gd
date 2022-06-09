extends Node

var point = 0
var PPC = 1# fix this
var arv = 0
var arv2 = 0
var PPS = 0
var reborn = 0
var arv3

func _process(delta):
	$"Point Score".text = str(point)
	$"PPC".text = str(PPC)
	$"PPS".text = str(PPS)
	$"Reborn2".text = str(reborn)
	$"Shop_1".text = str("PAY ", arv, " POINTS FOR 1 PPC")
	$"Shop_2".text = str("PAY ", arv2, " POINTS FOR 1 PPS")
	$"Reborn".text = str("PAY ", arv3, " POINTS FOR A REBORN")
		
# Called when the node enters the scene tree for the first time.
func _ready():
	arv = 100
	arv2 = 150
	arv3 = 10000
	pass # Replace with function body.




func _on_TextureButton_pressed():
	point += PPC
	pass # Replace with function body.


func _on_Shop_1_button_down():
	if point >= arv:
		point -= arv
		PPC += 1
		arv = round(arv*1.2)
		
		pass


func _on_Shop_2_button_down():
	if point >= arv2:
		point -= arv2
		PPS += 1
		arv2 = round(arv2*1.2)
	pass # Replace with function body.


func _on_Timer_timeout():
	point += PPS
	pass # Replace with function body.


func _on_Reborn_pressed():
	if point >= arv3:
		point = 0
		PPC = 2
		PPS = 0
		arv = 100
		arv2 = 150
		reborn +=1
		arv3 = round(arv3*1.5)
	pass # Replace with function body.

