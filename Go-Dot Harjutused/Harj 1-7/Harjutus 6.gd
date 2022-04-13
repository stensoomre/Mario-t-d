extends Node
# Sten Soomre
# HKHK
# 07.04.2022

func random(a,b): # funktioon oleks lihtsam
	var rand = RandomNumberGenerator.new()#lühend
	rand.randomize() # randomizib
	var rand2 = rand.randi_range(a,b) #genib
	return rand2 # returnib

var vastasehp = 100
var dmg = 0
var protsent = 0
var pihtas = 0
var mooda = 0
var tulemus = 0
var kuulmax = 30
var kuul = kuulmax
var kas
var punkt = 0
var lasku
func _ready():
	pass

func _process(delta):
	if Input.is_action_just_pressed("lask"):
		protsent = random(0,100)
		dmg = random(8,12)
		if kuul == 0:
			print("Relv on tühi | ",kuul,"/",kuulmax) #
			kas = 2
		else:
			kuul -= 1
			if protsent >= 80:
				print("Möödas | ",kuul,"/",kuulmax) # 
				kas = 1
				mooda += 1
			else:
				vastasehp -= dmg
				print("Pihtas: -",dmg," elu | ",kuul,"/",kuulmax," | Elusi järgi: ", vastasehp) #
				pihtas += 1
				kas = 0
				if vastasehp <= 0:
					var lasku = pihtas+mooda
					tulemus = 100-((float(mooda)/float(lasku))*100)
					if mooda == 0:
						tulemus = 100
						punkt = 10
					if lasku <= 10:
						punkt += 10
					elif lasku <= 15:
						punkt += 5
					else:
						punkt += 1
					if vastasehp < 0:
						vastasehp = 0
					kas = 4
					print("""
					------------------------------------------------
					-------------------MÄNG LÄBI--------------------
					------------------------------------------------
					""")
					print("\nEffektiivsus %0.2f%%" % tulemus)
					print("Said ", punkt, " punkti")
					print("Lasid kokku: ", lasku)
					
					print(mooda, " Lasid mööda")
					print(pihtas, " Lasid pihta")
					

					
	if Input.is_action_just_pressed("reload"):
		if kuul == kuulmax:
			print("Su relv on juba laetud")
			kas = 3
		else:
			kuul += 1
			print("Laadisid relva | ",kuul,"/",kuulmax)
