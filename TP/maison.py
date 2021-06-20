# Programme Python pour dessiner une maison avec le module turtle*

# Import du module dessinMSDA
import dessinMSDA as D
# Import du module turtle
from turtle import *
# Import du module math
import math
bgcolor("white")
shape("turtle")
# Dessiner le devant de la maison
# Dessiner un  rectangle longuer L et de largeur l et de couleur a
fillcolor("white")
begin_fill()
D.rectangle(200, 150, "white")
end_fill
#  Dessiner la porte de la maison 
# dessiner un rectangle
penup()
D.t.goto(60, 0)
pendown()
fillcolor("white")
begin_fill()
D.rectangle(40, 80, "white")
end_fill
D.t.goto(0, 0)


# Dessiner le toit de la maison
# Dessiner un triangle 
penup() 
D.t.goto(0, 150)
D.t.goto(-20, 150)
pendown()
begin_fill()
D.triangle(240)
end_fill()
goto(0, 0)


# Dessiner lle cheminée de la maison 
# Dessiner un triangle 
penup()
D.t.goto(220, 150)
D.t.goto(170, 200)
D.t.goto(140, 200)
fillcolor("white")
begin_fill()
D.rectangle(30, 60, "white")
end_fill

# Dessiner les fenetres de la maison
D.t.penup()
D.t.goto(150, 40)
D.t.pendown()
begin_fill()
D.carre(40)
end_fill

D.t.penup()
D.t.goto(170, 40)
D.t.pendown()
D.t.lt(90)
D.t.fd(40)

D.t.penup()
D.t.goto(150, 60)
D.t.pendown()
D.t.rt(90)
D.t.fd(40)

# Bordure de la maison
D.t.penup()
D.t.goto(0, -8)
D.t.pendown()
D.rectangle(40, 8, "black")

D.t.penup()
D.t.goto(40, -8)
D.t.pendown()
D.rectangle(80, 8, "white")

D.t.penup()
D.t.goto(120, -8)
D.t.pendown()
D.rectangle(80, 8, "black")













D.turtle.done()


