extends Node
var option
var punkt = 0
var valik
func random(a,b): # funktioon oleks lihtsam
	var rand = RandomNumberGenerator.new()#lühend
	rand.randomize() # randomizib
	var rand2 = rand.randi_range(a,b) #genib
	return rand2 # returnib

func _process(delta):
	$"Bg/kivi".text = "Kivi"
	$"Bg/paber".text = "Paber"
	$"Bg/kaarid".text = "Käärid"
	$"Kast/Punkte".text = "Punkte: "+str(punkt)	
	
func _on_kivi_pressed():
	print("Kivi")
	option = "Kivi"
	pt2(option)

func _on_paber_pressed():
	print("Paber")
	option = "Kivi"
	pt2(option)

func _on_kaarid_pressed():
	print("Käärid")
	option = "Kivi"
	pt2(option)
	
func pt2(option):  # 3 = Kivi # 2 = Käärid # 1 = Paber
	valik = random(1,3)
	print(valik)
	if option == "Kivi":
		if valik == 2:
			punkt += 1
			$"Vastane/Tegi".text = "Vastane valis: Käärid"
		elif valik == 3:
			$"Vastane/Tegi".text = "Vastane valis: Kivi"
		else:
			punkt -= 1
			$"Vastane/Tegi".text = "Vastane valis: Paber"
	elif option == "Paber":
		if valik == 3:
			punkt += 1
			$"Vastane/Tegi".text = "Vastane valis: Kivi"
		elif valik == 1:
			$"Vastane/Tegi".text = "Vastane valis: Paber"
		else:
			punkt -= 1
			$"Vastane/Tegi".text = "Vastane valis: Käärid"
	elif option == "Käärid":
		if valik == 1:
			punkt += 1
			$"Vastane/Tegi".text = "Vastane valis: Paber"
		elif valik == 2:
			$"Vastane/Tegi".text = "Vastane valis: Käärid"
		else:
			punkt -= 1
			$"Vastane/Tegi".text = "Vastane valis: Kivi"
			
		
		
