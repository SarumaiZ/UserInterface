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
        self.tradicional_ui.pushButton_21.clicked.connect(self.inverte_sinal)  # +/-
        self.tradicional_ui.pushButton_18.clicked.connect(self.virgula)  # ,

        # Botões parênteses calculadora tradicional
        self.tradicional_ui.pushButton_23.clicked.connect(self.abre)  # (
        self.tradicional_ui.pushButton_22.clicked.connect(self.fecha)  # )

        # Botão resultado calculadora tradicional
        self.tradicional_ui.pushButton_17.clicked.connect(self.resultado)  # =

        # Botão voltar calculadora tradicional
        self.tradicional_ui.pushButton_20.clicked.connect(self.voltar)  # Voltar

        # Botões delete calculadora tradicional
        self.tradicional_ui.pushButton_4.clicked.connect(self.apagaDEL)
        self.tradicional_ui.pushButton_5.clicked.connect(self.apaga)

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
        self.cientifica_ui.pushButton_27.clicked.connect(self.exp)  # exp
        self.cientifica_ui.pushButton.clicked.connect(self.angulo)  # SEN
        self.cientifica_ui.pushButton_9.clicked.connect(self.angulo)  # COS
        self.cientifica_ui.pushButton_22.clicked.connect(self.angulo)  # TAN
        self.cientifica_ui.pushButton_26.clicked.connect(self.arco)  # arco
        self.cientifica_ui.pushButton_18.clicked.connect(self.virgula)  # ,

        # Botões parênteses calculadora científica
        self.cientifica_ui.pushButton_25.clicked.connect(self.abre)  # (
        self.cientifica_ui.pushButton_29.clicked.connect(self.fecha)  # )

        # Botão resultado calculadora científica
        self.cientifica_ui.pushButton_21.clicked.connect(self.resultado)  # =

        # Botão voltar calculadora tradicional
        self.cientifica_ui.pushButton_28.clicked.connect(self.voltar)  # Voltar

        # Botões delete calculadora científica
        self.cientifica_ui.pushButton_4.clicked.connect(self.apagaDEL)
        self.cientifica_ui.pushButton_5.clicked.connect(self.apaga)
    
    # Métodos
    # Todos os métodos garantem que a inserção do que está sendo digitado seja feito de maneira correta para que posteriormente a função eval consiga compilar e calcular o resultado

    def inverte_sinal(self):
        "Irá inverter o sinal do último número no visor da calculadora utilizando '(-'"
        texto = self.tradicional_ui.label.text()
        if(texto.endswith(("*","/","+","-","("," "))):
            if(texto[len(texto)-2]=="(" and texto.endswith("-")):
                envia = texto[:len(texto)-2]
            else:
                envia = texto+"(-"
        elif(texto.endswith(")")):
            envia = texto+"*(-"
        elif(texto.endswith(("0","1","2","3","4","5","6","7","8","9",","))):
            if((texto.rfind("-")>(texto.rfind("+"))) and (texto.rfind("-") > texto.rfind("/")) and (texto.rfind("-") > texto.rfind("*")) and (texto.rfind("-") >texto.rfind("sqrt"))):
                if(texto[texto.rfind("-")-1]=="("):
                    envia = texto[:texto.rfind("-")-1]+texto[texto.rfind("-")+1:]
                else:
                    envia = texto[:texto.rfind("-")+1]+"(-"+texto[texto.rfind("-")+1:]
            else:
                find = max(texto.rfind("+"), texto.rfind("-"), texto.rfind("/"), texto.rfind("*"), texto.rfind("sqrt"), texto.rfind("("))
                if(find==-1):
                    envia=("(-"+texto).replace(" ","")
                else:
                    envia = texto[:find+1]+"(-"+texto[find+1:]
        else:
            envia = texto
        self.tradicional_ui.label.setText(envia)

    def exp(self):
        "Insere a função exponencial no visor da calculadora científica"
        texto = self.cientifica_ui.label.text()
        if(texto.endswith(("+", "-", "*", "√", "÷", "(", " "))):
            envia = texto+"exp("
        elif(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π",")"))):
            envia = texto+"*exp("
        elif(texto.endswith(",")):
            envia = texto+"0*exp("
        elif(texto.endswith("a")):
            envia = texto
        else:
            envia = texto
        self.cientifica_ui.label.setText(envia)

    def operadores(self):
        "Quando algum botão de operador for clicado, este método garante que a inserção seja feita de maneira correta"
        
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
            sender = self.tradicional_Window.sender().text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()
            sender = self.cientifica_Window.sender().text()
        # Verifica qual janela está aberta para que o texto no visor e o texto do botão clicado sejam adquiridos corretamente
        
        if(sender=="√"):
            if(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π",")"))):
                envia = texto + "*√("
            elif(texto.endswith(("+", "-", "*", "÷", " ","("))):
                envia = texto + "√("
            elif(texto.endswith(",")):
                envia = texto + "0*√("
            elif(texto.endswith("a")):
                envia = texto
            else:
                envia = texto
        elif(sender=="x^"):
            if(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9","π",")"))):
                envia = texto + "^("
            elif(texto.endswith(("+", "-", "*", "÷", " ","("))):
                envia = texto
            elif(texto.endswith(",")):
                envia = texto + "0^("
            elif(texto.endswith("a")):
                envia = texto
            else:
                envia = texto
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
        elif(texto == " " or texto.endswith("a")):
            envia = texto
        else:
            envia = texto + sender
        
        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def virgula(self):
        "Garante o uso correto da vírgula na calculadora"
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
        elif(texto.endswith("a")):
            envia = texto
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def abre(self):
        "Abertura de parênteses, sendo formatada conforme o final do texto"
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
        elif(texto.endswith("a")):
            envia = texto
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def fecha(self):
        "Fecha os parênteses, limitando pelo final do texto e pela quantidade de parênteses abertos"
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
        elif(texto.endswith("a")):
            envia = texto
        else:
            envia = texto

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def angulo(self):
        "Exibirá a função trigonométrica que for clicada formatada"
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
        "Insere a letra 'a' no visor da calculadora, indicando que será feito o cálculo de um arco, seja ele seno, cosseno ou tangente"
        texto = self.cientifica_ui.label.text()
        if(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")","π"))):
            envia=texto+"*a"
        elif(texto.endswith(("+", "-", "*", "÷", "(", " "))):
            envia=texto+"a"
        elif(texto.endswith(",")):
            envia=texto+"0*a"
        elif(texto.endswith("a")):
            envia=texto
        else:
            envia=texto
        self.cientifica_ui.label.setText(envia)

    def escreve(self):
        "Método que irá escrever no visor o número que foi clicado, utilizado para os números"
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
            sender = self.tradicional_Window.sender().text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()
            sender = self.cientifica_Window.sender().text()

        if(sender=="π"):
            if(texto.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ")","π"))):
                envia = texto+"*"+sender
            elif(texto.endswith(("+", "-", "*", "÷", "(", " "))):
                envia = texto+sender
            elif(texto.endswith(",")):
                envia = texto + "0*"+ sender
            elif(texto.endswith("a")):
                envia = texto
        else:
            if(texto.endswith(")")):
                envia = texto + "*" + sender
            elif(texto.endswith("a")):
                envia=texto
            elif(texto.endswith("π")):
                envia = texto+"*"+sender
            else:
                envia = texto+sender

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def resultado(self):
        "Irá finalizar a formatação do texto no visor da calculadora para que a função eval calcule o resultado e exiba no visor"
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()

        contab = texto.count("(")
        contfe = texto.count(")")
        if(contab-contfe >= 1):
            texto = texto+")"*(contab-contfe)
        # Caso o usuário não feche todos os parêteses, é feita uma última verificação para que todos os parênteses estejam fechados corretamente, para que a função eval não emita erro
        
        texto = texto.replace(",",".").replace("se","si").replace("√","sqrt").replace("^","**").replace("÷","/").replace("π","pi")
        if(texto.count("**(")>0):
            taux = texto[:texto.find("**(")]
            texto = texto[texto.find("**("):]
            for i in range(0,texto.count("**(")):
                if(texto[texto.find("**(")+3]==")"):
                    texto = texto[:texto.find("**(")+3]+"1"+texto[texto.find("**(")+3:]
                    taux = taux + texto[:texto.find(")")+1]
                    texto = texto[texto.find(")")+1:]
                else:
                    taux = taux + texto[:texto.find(")")+1]
                    texto = texto[texto.find(")")+1:]
                texto = taux + texto
        elif(texto.count("sqrt(")>0):
            taux = texto[:texto.find("sqrt(")]
            texto = texto[texto.find("sqrt("):]
            for i in range(0,texto.count("sqrt(")):
                if(texto[texto.find("sqrt(")+5]==")"):
                    texto = texto[:texto.find("sqrt(")+5]+"1"+texto[texto.find("sqrt(")+5:]
                    taux = taux + texto[:texto.find(")")+1]
                    texto = texto[texto.find(")")+1:]
                else:
                    taux = taux + texto[:texto.find(")")+1]
                    texto = texto[texto.find(")")+1:]
                texto = taux + texto
        if(texto == " "):
            envia = texto
        else:
            try:
                aux = eval(texto)
                if(self.tradicional_Window.isActiveWindow()):
                    envia = str(float(f'{aux:.4f}')).replace(".",",")
                elif(self.cientifica_Window.isActiveWindow()):
                    envia = str(aux).replace(".",",")
            except (NameError, ValueError):
                envia = texto.replace(".",",").replace("pi","π").replace("si","se").replace("sqrt","√").replace("**","^").replace("/","÷")
                QtWidgets.QMessageBox.about(self.cientifica_Window, "Math Error", "Raízes negativas não são permitidas\nArcos (seno e cosseno) são calculados para valores entre -1 e +1\nCorrija a equação")
            except SyntaxError:
                envia = texto.replace(".",",").replace("pi","π").replace("si","se").replace("sqrt","√").replace("/","÷").replace("**","^")
                QtWidgets.QMessageBox.about(self.cientifica_Window, "Erro de Sintaxe", "Sintaxe inválida - corrija a equação")

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def apagaDEL(self):
        "Relacioando ao botão 'C' da calculadora, apagará tudo que estiver no visor"
        # Calculadora tradicional
        self.tradicional_ui.label.setText(" ")

        # Calculadora científica
        self.cientifica_ui.label.setText(" ")

    def apaga(self):
        "Relacionado ao botão 'CE' da calculadora, apagrá o último digito"
        if(self.tradicional_Window.isActiveWindow()):
            texto = self.tradicional_ui.label.text()
        elif(self.cientifica_Window.isActiveWindow()):
            texto = self.cientifica_ui.label.text()
        
        envia = texto[0:len(texto)-1]
        if(texto == " "):
            envia = " "
        elif(texto.endswith("(") and texto[:len(texto)-1].endswith(("√", "^"))):
            envia = texto[0:len(texto)-2]
        elif(texto.endswith("(") and texto[:len(texto)-1].endswith(("n", "s","p"))):
            envia = texto[0:len(texto)-4]

        # Calculadora tradicional
        self.tradicional_ui.label.setText(envia)

        # Calculadora científica
        self.cientifica_ui.label.setText(envia)

    def voltar(self):
        "Fecha a calculadora atual e volta à tela inicial"
        self.tradicional_Window.close()
        self.cientifica_Window.close()
        self.tela_inicial_Window.show()

    def show_tela_inicial(self):
        "Abre a tela inicial"
        self.tela_inicial_Window.show()

    def show_calc(self):
        "Método para abrir a calculadora"
        self.tradicional_ui.label.setText(" ") # Garante que as duas calculadoras iniciem com um espaço vazio
        self.cientifica_ui.label.setText(" ")
        if self.tela_inicial_ui.radioButton.isChecked(): # Verifica se o RadioButton da Calculadora Tradicional está selecionado
            self.tradicional_Window.show() # Abre a calculadora tradicional
            self.tela_inicial_Window.close() # Fecha a tela inicial

        if self.tela_inicial_ui.radioButton_2.isChecked(): # Verifica se o RadioButton da Calculadora Científica está selecionado
            self.cientifica_Window.show() # Abre a calculadora científica
            self.tela_inicial_Window.close() # Fecha a tela inicial
            QtWidgets.QMessageBox.about(self.cientifica_Window, "Aviso", "Os ângulos são calculados em radianos")
            # Ao abrir a calculadora científica, avisa ao usuário que os ângulos são em radianos através de um MessageBox

        if not(self.tela_inicial_ui.radioButton.isChecked()) and not(self.tela_inicial_ui.radioButton_2.isChecked()):
            QtWidgets.QMessageBox.about(self.tela_inicial_Window, "Erro", "Escolha uma opção!")
            # Caso nenhum dos dois Radio Buttons estiverem selecionados, uma mensagem de erro é emitida

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = controller()
    controller.show_tela_inicial()
    sys.exit(app.exec_())