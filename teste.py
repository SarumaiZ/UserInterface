import os
os.system('cls')

"""lista=[]
texto = "8+6-5*7"
i=0
for  dig in texto:
    lista.append(dig)
    i+=1
numeros=[""]
operadores=[]
i=0
for dig in texto:
    if(dig in ["+", "-", "*", "÷", "√"]):
        operadores.append(dig)
        numeros.append("")
    numeros[i]=numeros[i]+dig
    if(dig in ["+", "-", "*", "÷", "√"]):
        numeros[i]=numeros[i][:len(numeros[i])-1]
        i+=1

print(numeros)
print(operadores)
print(lista)"""

texto="50"
aux=""
for dig in texto:
    if(dig not in ["+", "-", "X", "√", "÷"]):
        carac=str(float(texto)/100)
print(carac)
print(type(carac))
print(texto[0])