m = float(input("entrez la valeur de la masse de mercure en Kg"))
mvolumique = 13.6
v = m*10**3/mvolumique
print("le volume versé de la masse de mercure est : ", v,"cm3")
print("le volume versé de la masse de mercure est : ", v*10**-6 ,"m3")
v = v*10**-6
l = float(input(" entrez la largeur du parrallepipede "))
L = float(input(" entrez la longueur du parrallepipede "))
H = float(input(" entrez la hauteur du parrallepipede "))
Vm = l*L*H
T = int(input("entrez le nombre des tubes cylindriques :"))
vt = (v-Vm)/T
print(" la volume de mercure versé dans chaque tube est: ",vt)




