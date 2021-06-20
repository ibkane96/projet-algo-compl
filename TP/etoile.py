# Programme python pour dessiner une etoile avec le module turtle
# Import du module dessinMSDA
import dessinMSDA as D
# Import du module turtle
from turtle import *
fillcolor("yellow")
penup()
goto(0, 0)
pendown()
for i in range(5) :
    forward(200)
    right(144)
D.turtle.done()