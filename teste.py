import os
from math import *
os.system('cls')

'''texto="50"
aux=""
for dig in texto:
    if(dig not in ["+", "-", "X", "√", "÷"]):
        carac=str(float(texto)/100)
print(carac)
print(type(carac))
print(texto[0])'''

'''x=texto.find("u")
#print(degrees(atan(sqrt(3)/3))+0.1)
if(x):
    print(x)
    print(texto)
else:
    print(x)
    print(texto)'''
texto="2,0+0,1"
index = max(texto.rfind("+"), texto.rfind("-"), texto.rfind("*"), texto.rfind("÷"), texto.rfind("√"), texto.rfind("^"))+1
if(texto[index:].find(",")==-1):
    envia=texto+","
else:
    envia=texto

'''numeros = [""]
i = 0
for dig in texto:
    if(dig in ["+", "-", "*", "÷", "√"]):
        numeros.append("")
    numeros[i] = numeros[i]+dig
    if(dig in ["+", "-", "*", "÷", "√"]):
        numeros[i] = numeros[i][:len(numeros[i])-1]
        i += 1
for alg in numeros[i]:
    if(alg == ','):
        envia = texto
        break
    else:
        envia = texto+","'''