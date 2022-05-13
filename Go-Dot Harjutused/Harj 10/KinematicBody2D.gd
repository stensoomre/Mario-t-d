extends KinematicBody2D
 
#seaded
const SPEED = 200
const ACCEL = 50
const UP = Vector2(0,-1)
const GRAV = 100
const JUMPHIGH = -1500
 
var motion = Vector2()
 
func _physics_process(_delta):
 motion.y += GRAV
 run()
 jump()
 motion = move_and_slide(motion, UP)
 
#funktsioonid
func run():
 if Input.is_action_pressed("ui_right") and not Input.is_action_pressed("ui_left"):
	 motion.x += ACCEL
	 motion.x = min(SPEED, motion.x)
	 $AnimatedSprite.flip_h = false
	 $AnimatedSprite.play("run")
 elif Input.is_action_pressed("ui_left") and not Input.is_action_pressed("ui_right"):
	 motion.x -= ACCEL
	 motion.x = max(-SPEED, motion.x)
	 $AnimatedSprite.flip_h = true
	 $AnimatedSprite.play("run")
 else:
	 $AnimatedSprite.play("idle")
 
func jump():
	if is_on_floor():
		if Input.is_action_pressed("ui_up"):
			motion.y = JUMPHIGH
 else:
		$AnimatedSprite.play("jump")
