import os
from math import *
os.system('cls')

"""texto="50"
aux=""
for dig in texto:
    if(dig not in ["+", "-", "X", "√", "÷"]):
        carac=str(float(texto)/100)
print(carac)
print(type(carac))
print(texto[0])"""

texto = "3*√(9*√(4))"
#texto=""
i=0
for dig in texto:
    if(dig=="√"):
        texto = texto[:i]+"sqrt"+texto[i+1:]
        i+=3
    i+=1
print((texto))