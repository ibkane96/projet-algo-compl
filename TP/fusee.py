# Programme Python pour dessiner un avion avec le module turtle
# Import du module dessinMSDA
import dessinMSDA as D
# Import du module turtle
from turtle import *
# Import du module math
import math
# Dessiner le centre de la fusee
begin_fill()
D.rectangle(150, 20, "white")
end_fill

D.t.penup()
D.t.goto(-20, 0)
D.t.pendown()
begin_fill()
D.carre(20)
end_fill

D.t.penup()
D.t.goto(150, 0)
D.t.pendown()
begin_fill()
D.carre(20)
end_fill

D.t.penup()
D.t.goto(0, 20)
D.t.pendown()
begin_fill()
D.rectangle(150, 20, "white")
end_fill

D.t.penup()
D.t.goto(-20, 20)
D.t.pendown()
goto(-20, 0)
goto(-20, 20)
goto(0, 40)
goto(0, 0)
goto(170, 0)
goto(170, 20)
goto(150, 40)

D.t.penup()
D.t.goto(30, 40)
D.t.pendown()
begin_fill()
D.rectangle(90, 60, "white")
end_fill
goto(120, 100)
goto(30, 100)
goto(0, 40)
D.t.penup()
D.t.goto(20, 100)
D.t.pendown()
begin_fill()
D.triangle(110)
end_fill()

D.t.penup()
D.t.goto(50, 100)
D.t.pendown()
begin_fill()
D.rectangle(50, 30, "white")
end_fill
goto(0, 0)
goto(-10, -60)
goto(-20, 0)
D.t.penup()
D.t.goto(10, -40)
D.t.pendown()
begin_fill()
D.cercle(15)
end_fill
goto(150, 0)
goto(160, -60)
goto(170, 0)
D.t.penup()
D.t.goto(140, -40)
D.t.pendown()
begin_fill()
D.cercle(15)
end_fill
D.t.penup()
D.t.goto(40, -45)
D.t.pendown()
begin_fill()
D.rectangle(70, 45, "white")
end_fill
D.t.penup()
D.t.goto(11, -65)
D.t.pendown()
begin_fill()
D.rectangle(130, 20, "white")
end_fill
D.t.penup()
D.t.goto(50, -95)
D.t.pendown()
begin_fill()
D.rectangle(50, 30, "white")
end_fill
D.t.penup()
D.t.goto(50, -185)
D.t.pendown()
begin_fill()
D.rectangle(50, 90, "white")
end_fill
D.t.penup()
D.t.goto(30, -90)
D.t.pendown()
begin_fill()
D.cercle(6)
end_fill
D.t.penup()
D.t.goto(120, -90)
D.t.pendown()
begin_fill()
D.cercle(6)
end_fill
D.t.penup()
D.t.goto(50, -95)
D.t.pendown()
begin_fill
D.t.lt(-115)
D.t.fd(100)
end_fill
D.t.penup()
D.t.goto(100, -95)
D.t.pendown()
begin_fill
D.t.lt(50)
D.t.fd(100)
end_fill
D.t.goto(100, -95)



D.turtle.done()