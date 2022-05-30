import os
from math import *
os.system('cls')

texto="30+50%-5"
cont = texto.count("%")
for i in range(0,cont):
    find = texto.find("%")
    textoaux = texto[:find]
    textoaux.rfind("+")
    print(textoaux)


'''texto=texto[::-1]
for dig in texto:
    if(dig not in ["+", "-", "X", "√", "÷"]):
        carac=str(float(texto)/100)
print(texto)'''