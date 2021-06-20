#Programme Python pour dessiner des figures avec turtle
# import du module turtle  
import turtle

# initialisation de turtle 
t = turtle.Turtle()

# dessiner un cercle 
def cercle(r):
#on trace un cercle de rayon (r) pour permettre a l'utilisateur de choisir son rayon(r)
    t.circle(r)

# dessiner un demicercle de rayon r
def demicercle(r):
#on trace un demi cercle de rayon (r) pour permettre a l'utilisateur de choisir son rayon(r)
    t.circle(r, 180)

# dessiner un carre de coté egal à a unites 
def carre(a):
# utilisation d'une boucle pour dessiner un carre 
    for i in range(4): # la boucle va tourner 4 fois
        t.fd(a)   # Avancer le dessinateur de 100 pas en avant 
        t.left(90) # rotation du dessinateur de 90 degres 

# dessiner un triangle
import math
def triangle(L):
        t.fd(L)
        t.lt(135)
        t.fd(L/math.sqrt(2))
        t.lt(90)
        t.fd(L/math.sqrt(2))
        t.lt(135)



# dessiner un rectangle de longuer L et de largeur l
def rectangle(L, l, couleur):
# utilisation de la boucle pour dessiner un rectangle
    t.fillcolor(couleur)
    t.begin_fill()
    for i in range(2): # la boucle va tourner 2 fois
        t.fd(L) # deplace la tortue de L unites vers l'avant
        t.lt(90) # rotation de la tortue de 90 degres vers la gauche 
        t.fd(l)  # deplace la tortue de l unites vers l'avant
        t.lt(90) # rotation de la tortue de 90 degres vers la gauche 
    t.end_fill()


# dessiner un polygone parametrable de L cotés qui mesurent l unités 
def polygone(L, l):
# utilisation de la boucle pour dessiner un polygone 
    for i in range(L-1):  # la boucle va tourner (L-1) fois
        t.fd(l)           # deplace la tortue de l unites vers l'avant
        t.left(360/L)     # rotation de la tortue de (360/L) degres 
    t.goto(0, 0)          # retour de la tortue au point d'origine 


# dessiner un trapeze de grande base B, petite base b et de hauteur H
def trapeze(B, b, H):
    t.backward(B)  # deplace la tortue de B unites vers l'arrière 
    t.right(90)    # rotation de la tortue de 90 degres vers la droite 
    t.backward(H)  # deplace la tortue de H unites vers l'arrière 
    t.right(90)    # rotation de la tortue de 90 degres vers la droite
    t.backward(b)  # deplace la tortue de H unites vers l'arrière
    t.goto(0,0)    # retour de la tortue au point d'origine

# dessiner un losange
def losange(L, A):
    for i in range(2): # La boucle va tourner de deux fois
        t.forward(L)   # deplace la tortue de L unites vers l'avant 
        t.lt(A)        # rotation de la tortue de A degres vers la gauche   
        t.forward(L)   # deplace la tortue de L unites vers l'avant
        t.lt(180-A)    # rotation de la tortue de (180-A) degres vers la gauche 
    t.seth(-60)
    

# dessiner une ellipse de dimension r 
def ellipse(r):
    for i in range(2):    # La boucle va tourner de deux fois
        t.circle(r,90)    # tracer un arc de cercle de rayon r et d'angle egal a 90 degres
        t.circle(r//2,90) # tracer un arc de cercle de rayon r//2 et d'angle egal a 90 degres
    t.seth(90)   

