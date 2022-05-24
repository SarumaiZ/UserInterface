import sys
from math import *

from PyQt5 import QtCore, QtGui, QtWidgets

# arquivos das telas
import tela_inicial
import calc_tradicional
import calc_cientifica

def operadores(texto, sender):
    if(sender=="√"):
        if(texto[len(texto)-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",")","π"]):
            envia = texto + "*√("
        elif(texto[len(texto)-1] in ["+", "-", "*", "÷", " ","("]):
            envia = texto + "√("
        elif(texto[len(texto)-1]==","):
            envia = texto + "0*√("
    elif(sender=="x^"):
        if(texto[len(texto)-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",")","π"]):
            envia = texto + "^("
        elif(texto[len(texto)-1] in ["+", "-", "*", "÷", " ","("]):
            envia = texto
        elif(texto[len(texto)-1]==","):
            envia = texto + "0^("
    elif(texto[len(texto)-1] in ["+", "-", "*", "÷"]):
        if(texto[len(texto)-2]=="(" and sender in ["+","-"]):
            envia = texto[0:len(texto)-1]+sender
        elif(texto[len(texto)-2] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",")","π"]):
            envia = texto[0:len(texto)-1]+sender
        else:
            envia = texto
    elif(texto[len(texto)-1] == ","):
        envia = texto + "0" + sender
    elif(texto[len(texto)-1] == "("):
        if(sender in ["+", "-"]):
            envia = texto + sender
        else:
            envia = texto
    elif(texto == " "):
        envia = texto
    else:
        envia = texto + sender
    return envia

def virgula(texto):
    if(texto == " " or texto[len(texto)-1] in ["+", "-", "*", "√", "÷", "("]):
        envia = texto+"0,"
    elif(texto[len(texto)-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π"]):
        numeros = [""]
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
                envia = texto+","
    elif(texto[len(texto)-1] == ","):
        envia = texto
    else:
        envia = texto
    return envia

def abrep(texto):
    for dig in texto:
        if(dig in ["+", "-", "*", "÷", "√", "(", " "]):
            envia = texto+"("
        elif(dig in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")","π"]):
            envia = texto+"*("
    if(texto == ""):
        envia = texto
    elif(texto[len(texto)-1] == ","):
        envia = texto+"0*("
    return envia

def fechap(texto):
    contab = 0
    contfe = 0
    for dig in texto:
        if(dig == "("):
            contab += 1
        if(dig == ")"):
            contfe += 1
    if(contab-contfe == 0 or texto[len(texto)-1] in ["+", "-", "*", "÷", "(", " "]):
        envia = texto
    elif(texto[len(texto)-1]==","):
        envia = texto + "0)"
    elif(contab-contfe >= 1):
        envia = texto+")"
    else:
        envia = texto
    return envia

def porcentagem(texto):
    # texto=str(float(texto)/100)
    if(texto == " " or texto[len(texto)-1] in ["+", "-", "*", "√", "÷", "(", " ", ")", "%"]):
        envia = texto
    elif(texto[len(texto)-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π"]):
        envia = texto+"%"
    else:
        envia = texto
    return envia

def angulos(texto, sender):
    if(texto[len(texto)-1] in ["+", "-", "*", "÷", "(", " ", "o"]):
        envia = texto+sender+"("
    elif(texto[len(texto)-1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")","π"]):
        envia = texto+"*"+sender+"("
    else:
        envia = texto+sender+"("
    return envia

def apaga(texto):
    envia = texto[0:len(texto)-1]
    if(texto == " "):
        envia = " "
    elif(texto[len(texto)-1]=="(" and texto[len(texto)-2] in ["√", "^"]):
        envia = texto[0:len(texto)-2]
    elif(texto[len(texto)-1]=="(" and texto[len(texto)-2] in ["n", "s"]):
        envia = texto[0:len(texto)-4]
    return envia

def escrever(texto, sender):
    if(texto[len(texto)-1]==")"):
        envia = texto + "*" + sender
    else:
        envia = texto+sender
    return envia

def igual(texto):
    i=0
    j=0
    for dig in texto:
        if(dig==","):
            texto = texto[:i]+"."+texto[i+1:]
        if(dig=="e"):
            texto = texto[:i]+"i"+texto[i+1:]
        if(dig=="√"):
            texto = texto[:i]+"sqrt"+texto[i+1:]
            i+=3
        if(dig=="^"):
            texto = texto[:i]+"**"+texto[i+1:]
            i+=1
        if(dig=="÷"):
            texto = texto[:i]+"/"+texto[i+1:]
        if(dig=="π"):
            texto = texto[:i]+"pi"+texto[i+1:]
            i+=1
        i+=1
    envia = str(eval(texto))
    for dig in envia:
        if(dig=="."):
            envia = envia[:j]+","+envia[j+1:]
        j+=1
    return envia

class controller:
    def __init__(self):
        self.tela_inicial_Window = QtWidgets.QMainWindow()
        self.tela_inicial_ui = tela_inicial.Ui_Dialog()
        self.tela_inicial_ui.setupUi(self.tela_inicial_Window)

        self.tradicional_Window = QtWidgets.QMainWindow()
        self.tradicional_ui = calc_tradicional.Ui_Dialog()
        self.tradicional_ui.setupUi(self.tradicional_Window)

        self.cientifica_Window = QtWidgets.QMainWindow()
        self.cientifica_ui = calc_cientifica.Ui_Dialog()
        self.cientifica_ui.setupUi(self.cientifica_Window)

        self.tela_inicial_ui.pushButton.clicked.connect(self.show_calc)

        # Botões algarismos calculadora tradicional
        self.tradicional_ui.pushButton_19.clicked.connect(self.escreve)  # 0
        self.tradicional_ui.pushButton_13.clicked.connect(self.escreve)  # 1
        self.tradicional_ui.pushButton_14.clicked.connect(self.escreve)  # 2
        self.tradicional_ui.pushButton_16.clicked.connect(self.escreve)  # 3
        self.tradicional_ui.pushButton_8.clicked.connect(self.escreve)  # 4
        self.tradicional_ui.pushButton_12.clicked.connect(self.escreve)  # 5
        self.tradicional_ui.pushButton_3.clicked.connect(self.escreve)  # 6
        self.tradicional_ui.pushButton_7.clicked.connect(self.escreve)  # 7
        self.tradicional_ui.pushButton_6.clicked.connect(self.escreve)  # 8
        self.tradicional_ui.pushButton_2.clicked.connect(self.escreve)  # 9

        # Botões operadores calculadora tradicional
        self.tradicional_ui.pushButton_15.clicked.connect(self.operadores)  # +
        self.tradicional_ui.pushButton_11.clicked.connect(self.operadores)  # -
        self.tradicional_ui.pushButton_10.clicked.connect(self.operadores)  # *
        self.tradicional_ui.pushButton_9.clicked.connect(self.operadores)  # ÷
        self.tradicional_ui.pushButton.clicked.connect(self.operadores)  # √
        self.tradicional_ui.pushButton_21.clicked.connect(self.porco)  # %
        self.tradicional_ui.pushButton_18.clicked.connect(self.virgula)  # ,

        # Botões parênteses calculadora tradicional
        self.tradicional_ui.pushButton_23.clicked.connect(self.abre)  # (
        self.tradicional_ui.pushButton_22.clicked.connect(self.fecha)  # )

        # Botão resultado calculadora tradicional
        self.tradicional_ui.pushButton_17.clicked.connect(self.resultado)  # =

        # Botão voltar calculadora tradicional
        self.tradicional_ui.pushButton_20.clicked.connect(self.voltar)  # Voltar

        # Botões delete calculadora tradicional
        self.tradicional_ui.pushButton_4.clicked.connect(self.apaga)
        self.tradicional_ui.pushButton_5.clicked.connect(self.apagaDEL)

        # Botões algarismos calculadora científica
        self.cientifica_ui.pushButton_17.clicked.connect(self.escreve)  # π
        self.cientifica_ui.pushButton_19.clicked.connect(self.escreve)  # 0
        self.cientifica_ui.pushButton_13.clicked.connect(self.escreve)  # 1
        self.cientifica_ui.pushButton_14.clicked.connect(self.escreve)  # 2
        self.cientifica_ui.pushButton_16.clicked.connect(self.escreve)  # 3
        self.cientifica_ui.pushButton_8.clicked.connect(self.escreve)  # 4
        self.cientifica_ui.pushButton_12.clicked.connect(self.escreve)  # 5
        self.cientifica_ui.pushButton_3.clicked.connect(self.escreve)  # 6
        self.cientifica_ui.pushButton_7.clicked.connect(self.escreve)  # 7
        self.cientifica_ui.pushButton_6.clicked.connect(self.escreve)  # 8
        self.cientifica_ui.pushButton_2.clicked.connect(self.escreve)  # 9

        # Botões operadores calculadora científica
        self.cientifica_ui.pushButton_24.clicked.connect(self.operadores)  # +
        self.cientifica_ui.pushButton_15.clicked.connect(self.operadores)  # -
        self.cientifica_ui.pushButton_11.clicked.connect(self.operadores)  # *
        self.cientifica_ui.pushButton_23.clicked.connect(self.operadores)  # ÷
        self.cientifica_ui.pushButton_10.clicked.connect(self.operadores)  # √
        self.cientifica_ui.pushButton_20.clicked.connect(self.operadores)  # x^
        self.cientifica_ui.pushButton_27.clicked.connect(self.porco)  # %
        self.cientifica_ui.pushButton.clicked.connect(self.angulo)  # SEN
        self.cientifica_ui.pushButton_9.clicked.connect(self.angulo)  # COS
        self.cientifica_ui.pushButton_22.clicked.connect(self.angulo)  # TAN
        self.cientifica_ui.pushButton_26.clicked.connect(self.arco)  # arco (em desenvolvimento)
        self.cientifica_ui.pushButton_18.clicked.connect(self.virgula)  # ,

        # Botões parênteses calculadora científica
        self.cientifica_ui.pushButton_25.clicked.connect(self.abre)  # (
        self.cientifica_ui.pushButton_29.clicked.connect(self.fecha)  # )

        # Botão resultado calculadora científica
        self.cientifica_ui.pushButton_21.clicked.connect(self.resultado)  # =

        # Botão voltar calculadora tradicional
        self.cientifica_ui.pushButton_28.clicked.connect(self.voltar)  # Voltar

        # Botões delete calculadora científica
        self.cientifica_ui.pushButton_4.clicked.connect(self.apaga)
        self.cientifica_ui.pushButton_5.clicked.connect(self.apagaDEL)
    
    # Métodos
    def textos(self):
        # Calculadora tradicional
        self.texto = self.tradicional_ui.label.text()
        self.sender = self.tradicional_Window.sender().text()

        # Calculadora científica
        self.textoc = self.cientifica_ui.label.text()
        self.senderc = self.cientifica_Window.sender().text()

    def porco(self):
        self.textos()

        # Calculadora tradicional
        self.tradicional_ui.label.setText(porcentagem(self.texto))

        # Calculadora científica
        self.cientifica_ui.label.setText(porcentagem(self.textoc))

    def operadores(self):
        self.textos()
        
        # Calculadora tradicional
        self.tradicional_ui.label.setText(operadores(self.texto, self.sender))

        # Calculadora científica
        self.cientifica_ui.label.setText(operadores(self.textoc, self.senderc))

    def virgula(self):
        self.textos()

        # Calculadora tradicional
        self.tradicional_ui.label.setText(virgula(self.texto))

        # Calculadora científica
        self.cientifica_ui.label.setText(virgula(self.textoc))

    def abre(self):
        self.textos()

        # Calculadora tradicional
        self.tradicional_ui.label.setText(abrep(self.texto))

        # Calculadora científica
        self.cientifica_ui.label.setText(abrep(self.textoc))

    def fecha(self):
        self.textos()

        # Calculadora tradicional
        self.tradicional_ui.label.setText(fechap(self.texto))

        # Calculadora científica
        self.cientifica_ui.label.setText(fechap(self.textoc))

    def angulo(self):
        self.textos()

        self.cientifica_ui.label.setText( angulos(self.textoc, self.senderc) )

    def arco(self):
        self.textos()

        self.cientifica_ui.label.setText( self.textoc + self.senderc )

    def escreve(self):
        self.textos()

        # Calculadora tradicional
        self.tradicional_ui.label.setText(escrever(self.texto, self.sender))

        # Calculadora científica
        self.cientifica_ui.label.setText(escrever(self.textoc, self.senderc))

    def resultado(self):
        self.textos()

        # Calculadora tradicional
        self.tradicional_ui.label.setText(igual(self.texto))

        # Calculadora científica
        self.cientifica_ui.label.setText(igual(self.textoc))

    def apagaDEL(self):
        # Calculadora tradicional
        self.tradicional_ui.label.setText(" ")

        # Calculadora científica
        self.cientifica_ui.label.setText(" ")

    def apaga(self):
        self.textos()

        # Calculadora tradicional
        self.tradicional_ui.label.setText(apaga(self.texto))

        # Calculadora científica
        self.cientifica_ui.label.setText(apaga(self.textoc))

    def voltar(self):
        self.tradicional_Window.close()
        self.cientifica_Window.close()
        self.tela_inicial_Window.show()

    def show_tela_inicial(self):
        self.tela_inicial_Window.show()

    def show_calc(self):
        self.tradicional_ui.label.setText(" ")
        self.cientifica_ui.label.setText(" ")
        if self.tela_inicial_ui.radioButton.isChecked():
            self.tradicional_Window.show()
            self.tela_inicial_Window.close()

        if self.tela_inicial_ui.radioButton_2.isChecked():
            self.cientifica_Window.show()
            self.tela_inicial_Window.close()

        if not(self.tela_inicial_ui.radioButton.isChecked()) and not(self.tela_inicial_ui.radioButton_2.isChecked()):
            QtWidgets.QMessageBox.about(self.tela_inicial_Window, "Erro", "Escolha uma opção!")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = controller()
    controller.show_tela_inicial()
    sys.exit(app.exec_())