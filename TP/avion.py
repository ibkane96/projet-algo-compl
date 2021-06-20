# Programme Python pour dessiner un avion avec le module turtle
# Import du module dessinMSDA
import dessinMSDA as D
# Import du module turtle
from turtle import *
# Import du module math
import math
pencolor("skyblue")
begin_fill()
D.t.rt(-45)
D.t.fd(100)
D.demicercle(30)
D.t.fd(100)
D.t.rt(60)
D.t.fd(95)
D.t.rt(-65)
D.t.fd(20)
D.t.rt(-100)
D.t.fd(80)
D.t.rt(110)
D.t.fd(80)
D.t.rt(65)
D.t.fd(50)
D.t.rt(-65)
D.t.fd(35)
D.t.rt(-120)
D.t.fd(60)
D.t.rt(45)
D.t.fd(60)
D.t.rt(-90)
D.t.fd(30)
D.t.rt(-90)
D.t.fd(40)
D.t.rt(85)
D.t.fd(80)
D.t.rt(90)
D.t.fd(80)
D.t.rt(-75)
D.t.fd(21)
D.t.rt(-87)
D.t.goto(0, 0)
end_fill()

D.turtle.done()