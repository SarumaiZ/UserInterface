import os
from math import *
os.system('cls')

texto="4+50%"
cont = texto.count("%")
for i in range(0,cont):
    index = max(texto.find("+"), texto.find("-"),texto.find("*"),texto.find("/"),texto.find("sqrt"),texto.find("**"))
    if(index==-1):
        if(texto.find("(")==-1):
            texto = str(eval(texto[:len(texto)-1])/100)
            taux=""
        else:
            texto = str(eval(texto[1:len(texto)-2])/100)
            taux=""
    else:
        taux = texto[:texto.find("%")]
        index1 = max(taux.find("+"), taux.find("-"),taux.find("*"),taux.find("/"),taux.find("sqrt"),taux.find("**"))
        if(index1==-1):
            taux = str(eval(taux[:len(texto)-1])/100)
        else:
            if(taux.endswith(")")):
                if(taux.count("(")==1):
                    perc = str(eval(taux[taux.find("("):])/100)
                else:
                    if(taux.count(")")>1):
                        if(taux.count("(") == taux.count(")")):
                            perc = str(eval(taux)/100)
                        else:
                            if(taux.count("(")>taux.count(")")):
                                #print(taux)
                                if(taux.find(")")<taux.rfind("(")):
                                    perc = str(eval(taux[taux.rfind("("):])/100)
                                    taux = taux[:taux.rfind("(")]
                                    #print(taux[:taux.rfind("(")]+perc+")")
                                    #perc = str(eval(taux+")"*(taux.count("(")-taux.count(")")))/100)
                            elif(taux.count("(")<taux.count(")")):
                                perc = str(eval("("*(taux.count(")")-taux.count("("))+taux)/100)
                    else:
                        perc = str(eval(taux[taux.rfind("("):])/100)
                if(taux[taux.find("(")-1] in ["+","-"]):
                    print("aqui")
                    taux = str(eval(taux[:taux.find("(")]+"("+taux[:taux.find("(")-1]+")"+"*"+perc))
                elif(taux[taux.find("(")-1] in ["*","/"]):
                    taux = str(eval(taux[:taux.find("(")]+perc))
                elif(taux[taux.find("(")-1] in ["t"]):
                    taux = str(eval(taux[taux.find("(")-4:])/100)
                else:
                    taux = perc
            else:
                if(taux.find("sqrt")+1):
                    index2 = max(taux.find("+"), taux.find("-"),taux.find("*"),taux.find("/"), taux.find("**"))
                    if(index2==-1):
                        perc = str(eval(taux[taux.find("sqrt")+5:])/100)
                        taux = "("+str(eval("sqrt("+perc+")"))
                    else:
                        perc = str(eval(taux[index2+1:])/100)
                        if(taux[index2] in ["+","-"]):
                            taux = "("+str(eval("sqrt("+str(eval(taux[taux.find("(")+1:index2+1]+"("+taux[taux.find("(")+1:index2]+")"+"*"+perc))+")"))
                        elif(taux[index2] in ["*","/"]):
                            taux = "("+str(eval("sqrt("+str(eval(taux[taux.find("(")+1:index2+1]+perc))+")"))
                else:
                    find = max(taux.rfind("+"), taux.rfind("-"), taux.rfind("/"), taux.rfind("*"))
                    perc = taux[find+1:]
                    if(taux.find("(")==-1):
                        if(taux[find] in ["+","-"]):
                            taux = str(eval(taux[:find+1]+taux[:find]+"*"+taux[find+1:]+"/100"))
                        elif(taux[find] in ["*","/"]):
                            taux = str(eval(taux[:find+1]+"("+perc+"/100)"))
                    else:
                        if(taux[find] in ["+","-"]):
                            taux = "("+str(eval(taux[taux.find("(")+1:find+1]+taux[taux.find("(")+1:find]+"*"+perc+"/100"))
                        elif(taux[find] in ["*","/"]):
                            taux = "("+str(eval(taux[taux.find("(")+1:find]+taux[find]+"("+perc+"/100)"))
    texto = taux+texto[texto.find("%")+1:]
print(eval(texto))