import math
from PIL import Image
img = Image.open('canale convergente.jpeg')
img.show()
x = float(input(" entrez la valeur de l'angle de convergence en radian "))
D1 = float(input("entrez la valeur de la langeur D en nanomètre "))
V1 = float(input("entrez la valeur de la vitesse en mètre/seconde "))
V2 = float(input("entrez la valeur de la vitessse en mètre/seconde" ))
MV = 10
try:
    L = (-D1/2 * math.tan(x)) * (math.sqrt(V1/V2) -1)
    print("la langeur du convergent est :",L)
    P = 1/2 * MV * 2*(V1**2 - V2**2)
    print("la valeur de la pression entre l'entré et la sortie du convergent est :",P)
except:
    print("erreur")



