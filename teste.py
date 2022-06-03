import math
import os
from math import *
os.system('cls')

texto = "3**(2)+5*6"
cont = texto.count("**(")
if(cont>0):
    taux = texto[:texto.find("**(")]
    texto = texto[texto.find("**("):]
    for i in range(0,cont):
        if(texto[texto.find("**(")+3]==")"):
            texto = texto[:texto.find("**(")+3]+"1"+texto[texto.find("**(")+3:]
            taux = taux + texto[:texto.find(")")+1]
            texto = texto[texto.find(")")+1:]
        else:
            taux = taux + texto[:texto.find(")")+1]
            texto = texto[texto.find(")")+1:]
        texto = taux + texto
print(eval(texto))