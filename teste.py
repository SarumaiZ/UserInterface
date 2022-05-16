import os
os.system('cls')

#Código que permite o uso de vírgulas corretamente na calculadora
ver=False
carac = ""
numeros=[""]
i=0
cont=0
texto="236,05+36,09-6"
for dig in texto:
    if(dig in ["+", "-", "X", "/", "r"]):
        numeros.append("")
    numeros[i]=numeros[i]+dig
    if(dig in ["+", "-", "X", "/", "r"]):
        numeros[i]=numeros[i][:len(numeros[i])-1]
        i+=1
for alg in numeros[i]:
    if(alg == ','):
        ver=True
if(ver):
    carac=""
else:
    carac=","
#print(numeros)
#print(texto+carac)

#Código para abertura dos parênteses na calculadora
texto="25+((268"
carac=""
for dig in texto:
    if(dig in ["+", "-", "X", "/", "r", "("]):
        carac="("
    elif(dig in ["0","1","2","3","4","5","6","7","8","9"]):
        carac="X("
#print(texto+carac)

#Código para fechar os parênteses na calculadora
texto="25+((268+7)-80"
carac=""
contab=0
contfe=0
for dig in texto:
    if(dig=="("):
        contab+=1
    if(dig==")"):
        contfe+=1
if(contab-contfe==0):
    carac=""
elif(contab-contfe>=1):
    carac=")"
#print(contab)
#print(contfe)
print(texto+carac)