import sys
from math import *

from PyQt5 import QtCore, QtGui, QtWidgets

# arquivos das telas
import tela_inicial
import calc_tradicional
import calc_cientifica

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

        # Calculadora tradicional
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
        self.tradicional_ui.pushButton_21.clicked.connect(self.porcentagem)  # %
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

        # Calculadora científica
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
        self.cientifica_ui.pushButton_27.clicked.connect(self.porcentagem)  # %
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
    def porcentagem(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()

        # texto=str(float(texto)/100)
        if(texto == " " or texto.endswith(("+", "-", "*", "√", "÷", "(", " ", ")", "%"))):
            envia = texto
        elif(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π"))):
            envia = texto+"%"
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def operadores(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
            sender = self.tradicional_Window.sender().text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()
            sender = self.cientifica_Window.sender().text()
        
        if(sender=="√"):
            if(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π",")"))):
                envia = texto + "*√("
            elif(texto.endswith(("+", "-", "*", "÷", " ","("))):
                envia = texto + "√("
            elif(texto.endswith(",")):
                envia = texto + "0*√("
        elif(sender=="x^"):
            if(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π",")"))):
                envia = texto + "^("
            elif(texto.endswith(("+", "-", "*", "÷", " ","("))):
                envia = texto
            elif(texto.endswith(",")):
                envia = texto + "0^("
        elif(texto.endswith(("+", "-", "*", "÷"))):
            if(texto[len(texto)-2]=="(" and sender in ["+","-"]):
                envia = texto[0:len(texto)-1]+sender
            elif(texto[:len(texto)-1].endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9",")","π"))):
                envia = texto[0:len(texto)-1]+sender
            else:
                envia = texto
        elif(texto.endswith(",")):
            envia = texto + "0" + sender
        elif(texto.endswith("(")):
            if(sender in ["+", "-"]):
                envia = texto + sender
            else:
                envia = texto
        elif(texto == " "):
            envia = texto
        else:
            envia = texto + sender
        
        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def virgula(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()

        if(texto == " " or texto.endswith(("+", "-", "*", "√", "÷", "("))):
            envia = texto+"0,"
        elif(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π"))):
            index = max(texto.rfind("+"), texto.rfind("-"), texto.rfind("*"), texto.rfind("÷"), texto.rfind("√"), texto.rfind("^"))+1
            if(texto[index:].find(",")==-1):
                envia=texto+","
            else:
                envia=texto
        elif(texto.endswith(",")):
            envia = texto
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def abre(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()

        if(texto.endswith(("+", "-", "*", "÷", "√", "(", " "))):
            envia = texto+"("
        elif(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")","π"))):
            envia = texto+"*("
        elif(texto.endswith(",")):
            envia = texto+"0*("
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def fecha(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()

        contab = texto.count("(")
        contfe = texto.count(")")
        if(contab-contfe == 0 or texto.endswith(("+", "-", "*", "÷", "(", " "))):
            envia = texto
        elif(texto.endswith(",")):
            envia = texto + "0)"
        elif(contab-contfe >= 1):
            envia = texto+")"
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def angulo(self):
        texto = self.cientifica_ui.label.text()
        sender = self.cientifica_Window.sender().text()

        if(texto.endswith(("+", "-", "*", "÷", "(", " ", "a"))):
            envia = texto+sender+"("
        elif(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")","π"))):
            envia = texto+"*"+sender+"("
        else:
            envia = texto+sender+"("

        self.cientifica_ui.label.setText(envia)

    def arco(self):
        texto = self.cientifica_ui.label.text()

        self.cientifica_ui.label.setText(texto+"a")

    def escreve(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
            sender = self.tradicional_Window.sender().text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()
            sender = self.cientifica_Window.sender().text()

        if(texto.endswith(")")):
            envia = texto + "*" + sender
        else:
            envia = texto+sender

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def resultado(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()

        contab = texto.count("(")
        contfe = texto.count(")")
        if(contab-contfe >= 1):
            texto = texto+")"*(contab-contfe)

        texto = texto.replace(",",".").replace("e","i").replace("√","sqrt").replace("^","**").replace("÷","/").replace("π","pi")
        try:
            envia = str(eval(texto)).replace(".",",")
        except (NameError, ValueError, SyntaxError):
            envia = texto.replace(".",",").replace("pi","π").replace("i","e").replace("sqrt","√").replace("**","^").replace("/","÷")
            QtWidgets.QMessageBox.about(self.cientifica_Window, "Math domain error", "Raízes negativas não são permitidas\nArcos (seno e cosseno) são calculados para valores entre -1 e +1")

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def apagaDEL(self):
        # Calculadora tradicional
        self.tradicional_ui.label.setText(" ")

        # Calculadora científica
        self.cientifica_ui.label.setText(" ")

    def apaga(self):
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()
        
        envia = texto[0:len(texto)-1]
        if(texto == " "):
            envia = " "
        elif(texto.endswith("(") and texto[:len(texto)-1].endswith(("√", "^"))):
            envia = texto[0:len(texto)-2]
        elif(texto.endswith("(") and texto[:len(texto)-1].endswith(("n", "s"))):
            envia = texto[0:len(texto)-4]

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

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
            QtWidgets.QMessageBox.about(self.cientifica_Window, "Aviso", "Os ângulos são calculados em radianos")

        if not(self.tela_inicial_ui.radioButton.isChecked()) and not(self.tela_inicial_ui.radioButton_2.isChecked()):
            QtWidgets.QMessageBox.about(self.tela_inicial_Window, "Erro", "Escolha uma opção!")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = controller()
    controller.show_tela_inicial()
    sys.exit(app.exec_())