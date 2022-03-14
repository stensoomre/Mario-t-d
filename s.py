import turtle
import random

#akna seaded
aken = turtle.Screen()
aken.setup(600,800)
aken.title("Harjutus 1")

colors = ("red", "blue", "orange", "green")
turn = 0
spikes = 8
size = 10 

kk = turtle.Turtle()

for i in range(spikes):
    
    kk.forward(50)
    kk.left(45)
    
    kk.forward(50)
    kk.left(-90)

turtle.exitonclick()
