m = float(input("entrez la valeur de la masse du mercure en kg"))
mvolumique = 13.6
v = m*10**3/mvolumique
print("le volume versé de la masse de mercure est : ", v,"cm3")
print("le volume versé de la masse de mercure est : ", v*10**-6 ,"m3")
l = float(input(" entrez la largeur du parrallepipede "))
L = float(input(" entrez la longueur du parrallepipede "))
H = float(input(" entrez la hauteur du parrallepipede "))
Vm = l*L*H
T = int(input("entrez le nombre des tubes cylindriques :"))
vt = (v-Vm)/T
print(" le volume de mercure versé dans chaque tube est: ",vt,"m*3")
s = 0.02
H = vt/s
print("la hauteur de mercure dans chaque tube est : " ,H,"m")
g = 10
h1 = 0.4
h2 = 0.5
delta  = h1+h2
print("la valeur de delta h est : ",delta ,"m")
S = l*L
print("la section du parallipipede est :",S,"m*2")
F = mvolumique*g*delta*S*10**-3/10**-6
print("l'intensité de force qui s'exerce sur le fond horizentale du récipient est :",F,"N")











