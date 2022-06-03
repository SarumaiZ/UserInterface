import math
import os
from math import *
os.system('cls')

texto = "3*sqrt()+5*6"
cont = texto.count("sqrt(")
if(cont>0):
    taux = texto[:texto.find("sqrt(")]
    texto = texto[texto.find("sqrt("):]
    for i in range(0,cont):
        if(texto[texto.find("sqrt(")+5]==")"):
            texto = texto[:texto.find("sqrt(")+5]+"1"+texto[texto.find("sqrt(")+5:]
            taux = taux + texto[:texto.find(")")+1]
            texto = texto[texto.find(")")+1:]
        else:
            taux = taux + texto[:texto.find(")")+1]
            texto = texto[texto.find(")")+1:]
        texto = taux + texto
print(eval(texto))