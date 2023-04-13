import string
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QComboBox,QSpinBox
from PyQt5.QtGui import QIcon

class Rotor:
    def __init__(self, tab): #Constructeur de la classe Rotor
        self.tab = tab
    def decaler(self,GD): # Decaler les deux lignes du rotor d'un cran, soit à gauche ou à droite 
        if (GD=='D'):
            self.tab[0]=np.roll(self.tab[0],1)
            self.tab[1]=np.roll(self.tab[1],1)
        elif (GD=='G'):
            self.tab[0]=np.roll(self.tab[0],-1)
            self.tab[1]=np.roll(self.tab[1],-1)
    def decalage_initial(self,n):# Decaler les deux lignes du rotor de n cases    
        self.tab[0]=np.roll(self.tab[0],n)
        self.tab[1]=np.roll(self.tab[1],n)
    # Construir une chaine de caractère contenant un tableau rangeant le rotor en séparant ses cases avec des bordures pour un affichage beau  
    def rotorInterface(self):
        #construir les bordures externes 
        interface = chr(0x2554)
        for i in range(25):
            interface = interface + 3*chr(0x2550)+chr(0x2566)
        interface = interface + 3*chr(0x2550)+ chr(0x2557) + "\n" +chr(0x2551) 
        ## la première ligne du tableau
        for i in range(26):
            interface = interface + str(self.tab[0][i]) + chr(0x2551)
        interface = interface + "\n" + chr(0x2560)
        #séparer la première ligne de la deuxième
        for i in range(25):
            interface = interface + 3*chr(0x2550)+ chr(0x256C)
        interface = interface + 3*chr(0x2550) + chr(0x2563)+"\n" + chr(0x2551)
        #la deuxième ligne du tableau
        for i in range(26):
            interface = interface + str(self.tab[1][i]) + chr(0x2551)
        interface = interface + "\n" + chr(0x255A)
        #les bordures externes
        for i in range(25):
            interface = interface + 3*chr(0x2550)+ chr(0x2569)
        interface = interface + 3*chr(0x2550) + chr(0x255D)+"\n" 
        return(interface)

class Reflecteur:
    def __init__(self):#Constructeur de la classe Reflecteur
        self.tab = ["+25", "+23", "+21", "+19", "+17", "+15", "+13", "+11", " +9", " +7", " +5", " +3", " +1", " -1", " -3", " -5", " -7", " -9", "-11", "-13", "-15", "-17", "-19", "-21", "-23", "-25"]  
    # Construir une chaine de caractère contenant un tableau rangeant le reflecteur en séparant ses cases avec des bordures pour un affichage beau  
    def reflecteurInterface(self):
         #construir les bordures externes 
        interface = chr(0x2554)
        for i in range(25):
            interface = interface + 3*chr(0x2550)+chr(0x2566)
        interface = interface + chr(0x2550)+ chr(0x2550)+chr(0x2550)+ chr(0x2557) + "\n" +chr(0x2551) 
        ## la première ligne du tableau
        for i in range(26):
            interface = interface + str(self.tab[i]) + chr(0x2551)
        interface = interface + "\n" + chr(0x255A)
         #les bordures externes
        for i in range(25):
            interface = interface + 3*chr(0x2550)+ chr(0x2569)
        interface = interface + 3*chr(0x2550) + chr(0x255D)
        return(interface)

class Alphabet:
    def __init__(self, tab):#Constructeur de la classe Alphabet
        self.tab = tab 
    # Construir une chaine de caractère contenant un tableau rangeant le tableau d'alphabets en séparant ses cases avec des bordures pour un affichage beau  
    def alphaInterface(self):
        #construir les bordures externes 
        interface = chr(0x2554)
        for i in range(25):
            interface = interface + chr(0x2550)+ chr(0x2550)+chr(0x2550)+chr(0x2566)
        interface = interface + chr(0x2550)+ chr(0x2550)+chr(0x2550)+ chr(0x2557) + "\n" +chr(0x2551) 
          ## la première ligne du tableau
        for i in range(26):
            interface = interface +" " + str(self.tab[i]) + " " + chr(0x2551)
        interface = interface + "\n" + chr(0x255A)
         #les bordures externes
        for i in range(25):
            interface = interface + chr(0x2550)+ chr(0x2550)+chr(0x2550)+ chr(0x2569)
        interface = interface + chr(0x2550)+ chr(0x2550)+chr(0x2550) + chr(0x255D)
        return(interface)

class Ui_Form(object):
    #declarer les rotors, le reflecteur et le tableau d'alphabet
    reflecteur = Reflecteur()
    rotor3 = Rotor([["+12", " -1", "+23", "+10", " +2", "+14", " +5", " -5", " +9", " -2", "-13", "+10", " -2", " -8", "+10", " -6", " +6", "-16", " +2", " -1", "-17", " -5", "-14", " -9", "-20", "-10"],[" +1", "+16", " +5", "+17", "+20", " +8", " -2", " +2", "+14", " +6", " +2", " -5", "-12", "-10", " +9", "+10", " +5", " -9", " +1", "-14", " -2", "-10", " -6", "+13", "-10", "-23"]])
    rotor2 = Rotor([["+25", " +7", "+17", " -3", "+13", "+19", "+12", " +3", " -1", "+11", " +5", " -5", " -7", "+10", " -2", " +1", " -2", " +4", "-17", " -8", "-16", "-18", " -9", " -1", "-22", "-16"],[" +3", "+17", "+22", "+18", "+16", " +7", " +5", " +1", " -7", "+16", " -3", " +8", " +2", " +9", " +2", " -5", " -1", "-13", "-12","-17", "-11", " -4", " +1", "-10", "-19", "-25"]])
    rotor1 = Rotor([["+17", " +4", "+19", "+21", " +7", "+11", " +3", " -5", " +7", " +9", "-10", " +9", "+17", " +6", " -6", " -2", " -4", " -7", "-12", " -5", " +3", " +4", "-21", "-16", " -2", "-21"],["+10", "+21", " +5" , "-17", "+21", " -4", "+12", "+16", " +6", " -3", " +7", " -7", " +4", " +2", " +5", " -7", "-11", "-17", " -9", " -6", " -9", "-19", " +2", " -3", "-21", " -4"]])
    alphabet = Alphabet(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    valeur = ''
    var=''
    nb=0
    le = [-1,-1,-1,-1,-1,-1,-1,-1,-1]  
    # l'interface graphique
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 1000)
        self.label = QtWidgets.QLabel(Form)
        # les labels du reflecteur, rotors et alphabet
        self.label.setGeometry(QtCore.QRect(40, 40, 71, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 220, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 310, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 430, 67, 17))
        self.label_5.setObjectName("label_5")
        #******************Reflecteur*******************
        self.reflect = QtWidgets.QLabel(Form)
        self.reflect.setGeometry(QtCore.QRect(130,30, 760, 50))
        self.reflect.setStyleSheet("color: #0F131F; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
        #******************Rotor3***********************
        self.rtr3 = QtWidgets.QLabel(Form)
        self.rtr3.setGeometry(QtCore.QRect(130, 110, 760, 100))
        self.rtr3.setStyleSheet("color: #0F131F; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
        #******************Rotor2***********************
        self.rtr2 = QtWidgets.QLabel(Form)
        self.rtr2.setGeometry(QtCore.QRect(130, 200, 760, 100))
        self.rtr2.setStyleSheet("color: #0F131F; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
        #******************Rotor1***********************
        self.rtr1 = QtWidgets.QLabel(Form)
        self.rtr1.setGeometry(QtCore.QRect(130, 300, 760, 78))
        self.rtr1.setStyleSheet("color: #0F131F; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
        #******************Alphabet*********************
        self.alpha = QtWidgets.QLabel(Form)
        self.alpha.setGeometry(QtCore.QRect(130, 410, 760, 50))
        self.alpha.setStyleSheet("color: #0F131F; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
        #*****************les labels pour suivre les étapes de l'encryption et le décryptage****************
        self.caseSA1 = QtWidgets.QLabel(Form)
        self.caseSA1.setGeometry(QtCore.QRect(133 + 29*self.le[0], 423, 28, 25)) 
        self.caseSR10 = QtWidgets.QLabel(Form)
        self.caseSR10.setGeometry(QtCore.QRect(133 + 29*self.le[7], 316, 28, 25))
        self.caseSR11 = QtWidgets.QLabel(Form)
        self.caseSR11.setGeometry(QtCore.QRect(133 + 29*self.le[1], 344, 28, 25))
        self.caseSR20 = QtWidgets.QLabel(Form)
        self.caseSR20.setGeometry(QtCore.QRect(133 + 29*self.le[6], 227, 28, 25))
        self.caseSR21 = QtWidgets.QLabel(Form)
        self.caseSR21.setGeometry(QtCore.QRect(133 + 29*self.le[2], 255, 28, 25))
        self.caseSR30 = QtWidgets.QLabel(Form)
        self.caseSR30.setGeometry(QtCore.QRect(133 + 29*self.le[5], 127, 28, 25))
        self.caseSR31 = QtWidgets.QLabel(Form)
        self.caseSR31.setGeometry(QtCore.QRect(133 + 29*self.le[3], 155, 28, 25))
        self.caseSRef1 = QtWidgets.QLabel(Form)
        self.caseSRef1.setGeometry(QtCore.QRect(133 + 29*self.le[4], 43, 28, 25))
        self.caseSRef2 = QtWidgets.QLabel(Form)
        self.caseSRef2.setGeometry(QtCore.QRect(133 + 29*self.le[5], 43, 28, 25))
        self.caseSA2 = QtWidgets.QLabel(Form)
        self.caseSA2.setGeometry(QtCore.QRect(133 + 29*self.le[8], 423, 28, 25))
        #******************les bouttons*****************************************
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 620, 831, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_9.setIcon(QIcon("Assets/1.png"))
        self.pushButton_9.setIconSize(QtCore.QSize(27,27))
        self.pushButton_9.clicked.connect(lambda:self.encrypter_a_la_volee(self.valeur))
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_4.setIcon(QIcon("Assets/1.png"))
        self.pushButton_4.setIconSize(QtCore.QSize(27,27))
        self.pushButton_4.clicked.connect(lambda:self.encrypter(self.valeur))
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_2.setIcon(QIcon("Assets/2.png"))
        self.pushButton_2.setIconSize(QtCore.QSize(27,27))
        self.pushButton_2.clicked.connect(self.etape_suivante)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(lambda:self.decrypter(self.valeur))
        self.pushButton.setIcon(QIcon("Assets/3.png"))
        self.pushButton.setIconSize(QtCore.QSize(27,27))
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_7 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_7.clicked.connect(lambda:self.decrypter_a_la_volee(self.valeur))
        self.pushButton_7.setIcon(QIcon("Assets/3.png"))
        self.pushButton_7.setIconSize(QtCore.QSize(27,27))
        #*********************************Clé***********************************       
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(180, 480, 270, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        rotors = [" ","R1", "R2", "R3"]
        self.case = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.case.setObjectName("case")
        self.gridLayout.addWidget(self.case, 1, 2)
        self.case1 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.case1.setObjectName("case1")
        self.gridLayout.addWidget(self.case1, 2, 2)
        self.case2 = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.case2.setObjectName("case2")
        self.gridLayout.addWidget(self.case2, 3, 2)
        G_D=["G","D"]
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(rotors)
        self.gridLayout.addWidget(self.comboBox, 1, 0)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(rotors)
        self.gridLayout.addWidget(self.comboBox_2, 2, 0)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItems(rotors)
        self.gridLayout.addWidget(self.comboBox_3, 3, 0)
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItems(G_D)
        self.gridLayout.addWidget(self.comboBox_4, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItems(G_D)
        self.gridLayout.addWidget(self.comboBox_5, 2, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItems(G_D)
        self.gridLayout.addWidget(self.comboBox_6, 3, 1)
        self.label_6=QtWidgets.QLabel("Clé")
        self.gridLayout.addWidget(self.label_6, 0, 1)        
        self.case.setRange(-25,25)
        self.case1.setRange(-25,25)
        self.case2.setRange(-25,25)
        #*****************************Zones de texte**************************
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(550, 510, 300, 25))
        self.label_6.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(550, 535, 350, 25))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit.returnPressed.connect(self.action)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.action)
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(550, 570, 300, 25))
        self.label_7.setObjectName("label_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(550, 595, 350, 25))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.action1)
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        #***********************configurer&reinistialiser************************
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 535, 120, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_3.setIcon(QIcon("Assets/cle.png"))
        self.pushButton_3.setIconSize(QtCore.QSize(27,27))
        self.pushButton_3.clicked.connect(self.configurer)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_8)
        self.pushButton_8.setIcon(QIcon("Assets/5.png"))
        self.pushButton_8.setIconSize(QtCore.QSize(27,27))
        self.pushButton_8.clicked.connect(self.reinistialiser)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.comboBox.currentTextChanged.connect(self.index)
        self.comboBox_2.currentTextChanged.connect(self.index1)
 
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Enigma"))
        labelReflacteur = self.reflecteur.reflecteurInterface()
        lblRotor3 = self.rotor3.rotorInterface()
        lblRotor2 = self.rotor2.rotorInterface()
        lblRotor1 = self.rotor1.rotorInterface()
        lblAlpha = self.alphabet.alphaInterface()
        self.label.setText(_translate("Form", "Reflecteur"))
        self.label_2.setText(_translate("Form", "Rotor3"))
        self.label_3.setText(_translate("Form", "Rotor2"))
        self.label_4.setText(_translate("Form", "Rotor1"))
        self.label_5.setText(_translate("Form", "Alphabet"))
        self.reflect.setText(_translate("Form", labelReflacteur))
        self.rtr3.setText(_translate("Form", lblRotor3))
        self.rtr2.setText(_translate("Form", lblRotor2))
        self.rtr1.setText(_translate("Form", lblRotor1))
        self.alpha.setText(_translate("Form", lblAlpha))
        self.pushButton_4.setText(_translate("Form", "Encrypter"))
        self.pushButton_2.setText(_translate("Form", "Etape suivante"))
        self.pushButton.setText(_translate("Form", "Décrypter"))
        self.label_6.setText(_translate("Form", "Message à encrypter"))
        self.pushButton_5.setText(_translate("Form", "OK"))
        self.label_7.setText(_translate("Form", "Message à décrypter"))
        self.pushButton_6.setText(_translate("Form", "OK"))
        self.pushButton_9.setText(_translate("Form", "Encryter à la volée"))
        self.pushButton_7.setText(_translate("Form", "Décrypter à la volée"))
        self.pushButton_8.setText(_translate("Form", "Réinitialiser"))
        self.pushButton_3.setText(_translate("Form", "Configurer"))

    def action(self):#pour recuperer le texte ecrit dans la premiere zone de texte pour encrypter
        self.valeur=self.lineEdit.text().upper()
        return self.valeur
    def action1(self):#pour recuperer le texte ecrit dans la deuxieme zone de texte pour decrypter
        self.valeur=self.lineEdit_2.text().upper()
        return self.valeur

    def encrypter(self, valeur):             
        if not valeur[0].isalpha():  
            self.var=self.var+valeur[0]
        else:
            i = self.alphabet.tab.index(valeur[0])
            self.caseSA1.setGeometry(QtCore.QRect(133 + 29*i, 423, 28, 25))# déplacer le labels à la case selectionnée dans le tableau d'alphabets
            self.caseSA1.setStyleSheet("color: #434172;background: #A6D0E9; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSA1.setText(" " + self.alphabet.tab[i])
            v = int(self.rotor1.tab[1][i])
            self.caseSR11.setGeometry(QtCore.QRect(133 + 29*i, 334, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR11.setStyleSheet("color: #434172;background: #A6D0E9; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR11.setText("" + self.rotor1.tab[1][i])
            i = (i + v)%26
            v = int(self.rotor2.tab[1][i])
            self.caseSR21.setGeometry(QtCore.QRect(133 + 29*i, 245, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR21.setStyleSheet("color: #434172;background: #A6D0E9; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR21.setText("" + self.rotor2.tab[1][i])
            i = (i + v)%26
            v = int(self.rotor3.tab[1][i])
            self.caseSR31.setGeometry(QtCore.QRect(133 + 29*i, 155, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR31.setStyleSheet("color: #434172;background: #A6D0E9; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR31.setText("" + self.rotor3.tab[1][i])
            i = (i + v)%26
            v = int(self.reflecteur.tab[i])
            self.caseSRef1.setGeometry(QtCore.QRect(133 + 29*i, 43, 28, 25))# déplacer le labels à la case selectionnée dans le reflecteur
            self.caseSRef1.setStyleSheet("color: #434172;background: #A6D0E9; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSRef1.setText("" + self.reflecteur.tab[i])# déplacer le labels à la case selectionnée dans le tableau d'alphabets
            i = (i + v)%26
            v = int(self.rotor3.tab[0][i])
            self.caseSRef2.setGeometry(QtCore.QRect(133 + 29*i, 43, 28, 25))# déplacer le labels à la case selectionnée dans le reflecteur)
            self.caseSRef2.setStyleSheet("color: #434172;background: #F0A6CA; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSRef2.setText("" + self.reflecteur.tab[i])
            self.caseSR30.setGeometry(QtCore.QRect(133 + 29*i, 127, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR30.setStyleSheet("color: #434172;background: #F0A6CA; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR30.setText("" + self.rotor3.tab[0][i])
            i = (i + v)%26
            v = int(self.rotor2.tab[0][i])
            self.caseSR20.setGeometry(QtCore.QRect(133 + 29*i, 217, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR20.setStyleSheet("color: #434172;background: #F0A6CA; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR20.setText("" + self.rotor2.tab[0][i])
            i = (i + v)%26
            v = int(self.rotor1.tab[0][i])
            self.caseSR10.setGeometry(QtCore.QRect(133 + 29*i, 306, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR10.setStyleSheet("color: #434172;background: #F0A6CA; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR10.setText("" + self.rotor1.tab[0][i])
            i = (i + v)%26
            l = self.alphabet.tab[i]
            self.caseSA2.setGeometry(QtCore.QRect(133 + 29*i, 423, 28, 25))# déplacer le labels à la case selectionnée dans le tableau d'alphabets
            self.caseSA2.setStyleSheet("color: #434172;background: #F0A6CA; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSA2.setText(" " + self.alphabet.tab[i])
            self.var=self.var+l
        self.lineEdit_2.setText(self.var)
        return valeur

    def decrypter(self, valeur):
        if not valeur[0].isalpha():  
            self.var=self.var+valeur[0]
        else:
            i = self.alphabet.tab.index(valeur[0])
            self.caseSA1.setGeometry(QtCore.QRect(133 + 29*i, 423, 28, 25)) # déplacer le labels à la case selectionnée dans le tableau d'alphabets
            self.caseSA1.setStyleSheet("color: #434172;background: #A6D0E9; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSA1.setText(" " + self.alphabet.tab[i])
            v = int(self.rotor1.tab[1][i])
            self.caseSR11.setGeometry(QtCore.QRect(133 + 29*i, 334, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR11.setStyleSheet("color: #434172;background: #A6D0E9; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR11.setText("" + self.rotor1.tab[1][i])
            i = (i + v)%26
            v = int(self.rotor2.tab[1][i])
            self.caseSR21.setGeometry(QtCore.QRect(133 + 29*i, 245, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR21.setStyleSheet("color: #434172;background: #A6D0E9; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR21.setText("" + self.rotor2.tab[1][i])
            i = (i + v)%26
            v = int(self.rotor3.tab[1][i])
            self.caseSR31.setGeometry(QtCore.QRect(133 + 29*i, 155, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR31.setStyleSheet("color: #434172;background: #A6D0E9; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR31.setText("" + self.rotor3.tab[1][i])
            i = (i + v)%26
            v = int(self.reflecteur.tab[i])
            self.caseSRef1.setGeometry(QtCore.QRect(133 + 29*i, 43, 28, 25))# déplacer le labels à la case selectionnée dans le reflecteur
            self.caseSRef1.setStyleSheet("color: #434172;background: #A6D0E9; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSRef1.setText("" + self.reflecteur.tab[i])
            i = (i + v)%26
            v = int(self.rotor3.tab[0][i])
            self.caseSRef2.setGeometry(QtCore.QRect(133 + 29*i, 43, 28, 25))# déplacer le labels à la case selectionnée dans le reflecteur
            self.caseSRef2.setStyleSheet("color: #434172;background: #F0A6CA; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSRef2.setText("" + self.reflecteur.tab[i])
            self.caseSR30.setGeometry(QtCore.QRect(133 + 29*i, 127, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR30.setStyleSheet("color: #434172;background: #F0A6CA; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR30.setText("" + self.rotor3.tab[0][i])
            i = (i + v)%26
            v = int(self.rotor2.tab[0][i])
            self.caseSR20.setGeometry(QtCore.QRect(133 + 29*i, 217, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR20.setStyleSheet("color: #434172;background: #F0A6CA; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR20.setText("" + self.rotor2.tab[0][i])
            i = (i + v)%26
            v = int(self.rotor1.tab[0][i])
            self.caseSR10.setGeometry(QtCore.QRect(133 + 29*i, 306, 28, 25))# déplacer le labels à la case selectionnée dans le rotor
            self.caseSR10.setStyleSheet("color: #434172;background: #F0A6CA; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSR10.setText("" + self.rotor1.tab[0][i])
            i = (i + v)%26
            l = self.alphabet.tab[i]
            self.caseSA2.setGeometry(QtCore.QRect(133 + 29*i, 423, 28, 25))# déplacer le labels à la case selectionnée dans le tableau d'alphabet
            self.caseSA2.setStyleSheet("color: #434172;background: #F0A6CA; font-weight: 1000 ; font: 9pt\"DejaVu Sans Mono\"")
            self.caseSA2.setText(" " + self.alphabet.tab[i])
            self.var=self.var+l
        self.lineEdit.setText(self.var)
        return valeur

    def etape_suivante(self):
        if self.nb<26:#tourner le 1er rotor selectionné 
            contenu = self.comboBox.currentText()#recuperer le 1er rotor selectionné
            sens = self.comboBox_4.currentText()#recuperer le sens de rotation du 1er rotor
            if contenu == 'R1':
                self.rotor1.decaler(sens)#faire appel a la fonction decaler pour tourner le rotor 1 d'un cran
            elif contenu == 'R2':
                self.rotor2.decaler(sens)#faire appel a la fonction decaler pour tourner le rotor 2 d'un cran
            elif contenu == 'R3':
                self.rotor3.decaler(sens)#faire appel a la fonction decaler pour tourner le rotor 3 d'un cran
        elif self.nb>=26 and self.nb<52:#tourner le 2eme rotor selectionné 
            contenu1 = self.comboBox_2.currentText()#recuperer le 2eme rotor selectionné
            sens1 = self.comboBox_5.currentText()#recuperer le sens de rotation du 2eme rotor
            if contenu1 == 'R1':
                self.rotor1.decaler(sens1)#faire appel a la fonction decaler pour tourner le rotor 1 d'un cran
            elif contenu1 == 'R2':
                self.rotor2.decaler(sens1)#faire appel a la fonction decaler pour tourner le rotor 2 d'un cran
            elif contenu1 == 'R3':
                self.rotor3.decaler(sens1)#faire appel a la fonction decaler pour tourner le rotor 3 d'un cran
        elif self.nb>=52:#tourner le 3eme rotor selectionné 
            contenu2 = self.comboBox_3.currentText()#recuperer le 3eme rotor selectionné
            sens2 = self.comboBox_6.currentText()#recuperer le sens de rotation du 3eme rotor
            if contenu2 == 'R1':
                self.rotor1.decaler(sens2)#faire appel a la fonction decaler pour tourner le rotor 1 d'un cran
            elif contenu2 == 'R2':
                self.rotor2.decaler(sens2)#faire appel a la fonction decaler pour tourner le rotor 2 d'un cran
            elif contenu2 == 'R3':
                self.rotor3.decaler(sens2)#faire appel a la fonction decaler pour tourner le rotor 3 d'un cran
        #affichage des 3 rotors aprés modification
        lblRotor1 = self.rotor1.rotorInterface()    
        self.rtr1.setText(lblRotor1)
        lblRotor2 = self.rotor2.rotorInterface()
        self.rtr2.setText(lblRotor2)
        lblRotor3 = self.rotor3.rotorInterface()
        self.rtr3.setText(lblRotor3)
        self.valeur=self.valeur[1:]
        self.nb=self.nb+1
        ensemble=[self.caseSA1,self.caseSR10,self.caseSR11,self.caseSR20,self.caseSR21,self.caseSR30,self.caseSR31,self.caseSRef1,self.caseSRef2,self.caseSA2]
        for k in ensemble:
             k.setStyleSheet("background: none; ")
             k.setText("") 

    def configurer(self):#faire appel a la fonction decalage_initial pour la configuration initiale des 3 rotors 
        contenu = self.comboBox.currentText()
        valeur = self.case.value()
        if contenu == 'R1':
             self.rotor1.decalage_initial(valeur)
        elif contenu == 'R2':
             self.rotor2.decalage_initial(valeur)
        elif contenu == 'R3':
             self.rotor3.decalage_initial(valeur)
        contenu1 = self.comboBox_2.currentText()
        valeur1 = self.case1.value()
        if contenu1 == 'R1':
             self.rotor1.decalage_initial(valeur1)
        elif contenu1 == 'R2':
             self.rotor2.decalage_initial(valeur1)
        elif contenu1 == 'R3':
             self.rotor3.decalage_initial(valeur1)
        contenu2 = self.comboBox_3.currentText()
        valeur2 = self.case2.value()
        if contenu2 == 'R1':
             self.rotor1.decalage_initial(valeur2)
        elif contenu2 == 'R2':
             self.rotor2.decalage_initial(valeur2)
        elif contenu2 == 'R3':
             self.rotor3.decalage_initial(valeur2) 
	#affichage des 3 rotors aprés modification  
        lblRotor1 = self.rotor1.rotorInterface()
        self.rtr1.setText(lblRotor1)
        lblRotor2 = self.rotor2.rotorInterface()
        self.rtr2.setText(lblRotor2)
        lblRotor3 = self.rotor3.rotorInterface()
        self.rtr3.setText(lblRotor3)

    def configurerABC(self):
        #pour rendre les trois rotors à leurs configuration initiale apres l'encryption ou le décryptage
        a = Rotor([["+17", " +4", "+19", "+21", " +7", "+11", " +3", " -5", " +7", " +9", "-10", " +9", "+17", " +6", " -6", " -2", " -4", " -7", "-12", " -5", " +3", " +4", "-21", "-16", " -2", "-21"],["+10", "+21", " +5" , "-17", "+21", " -4", "+12", "+16", " +6", " -3", " +7", " -7", " +4", " +2", " +5", " -7", "-11", "-17", " -9", " -6", " -9", "-19", " +2", " -3", "-21", " -4"]])
        b = Rotor([["+25", " +7", "+17", " -3", "+13", "+19", "+12", " +3", " -1", "+11", " +5", " -5", " -7", "+10", " -2", " +1", " -2", " +4", "-17", " -8", "-16", "-18", " -9", " -1", "-22", "-16"],[" +3", "+17", "+22", "+18", "+16", " +7", " +5", " +1", " -7", "+16", " -3", " +8", " +2", " +9", " +2", " -5", " -1", "-13", "-12","-17", "-11", " -4", " +1", "-10", "-19", "-25"]])
        c = Rotor([["+12", " -1", "+23", "+10", " +2", "+14", " +5", " -5", " +9", " -2", "-13", "+10", " -2", " -8", "+10", " -6", " +6", "-16", " +2", " -1", "-17", " -5", "-14", " -9", "-20", "-10"],[" +1", "+16", " +5", "+17", "+20", " +8", " -2", " +2", "+14", " +6", " +2", " -5", "-12", "-10", " +9", "+10", " +5", " -9", " +1", "-14", " -2", "-10", " -6", "+13", "-10", "-23"]])
  
        contenu = self.comboBox.currentText()
        valeur = self.case.value()
        if contenu == 'R1':   
             a.decalage_initial(valeur)
        elif contenu == 'R2':
             b.decalage_initial(valeur)
        elif contenu == 'R3':
             c.decalage_initial(valeur)
        contenu1 = self.comboBox_2.currentText()
        valeur1 = self.case1.value()
        if contenu1 == 'R1':
             a.decalage_initial(valeur1)
        elif contenu1 == 'R2':
             b.decalage_initial(valeur1)
        elif contenu1 == 'R3':
             c.decalage_initial(valeur1)
        contenu2 = self.comboBox_3.currentText()
        valeur2 = self.case2.value()
        if contenu2 == 'R1':
             a.decalage_initial(valeur2)
        elif contenu2 == 'R2':
             b.decalage_initial(valeur2)
        elif contenu2 == 'R3':
             c.decalage_initial(valeur2)  
        T = [a, b, c]
        return(T)
    #2 fonctions pour pouvoir supprimer l'element selectionné de la liste déroulante 
    def index(self,text):
        index = self.comboBox_2.findText(text)
        self.comboBox_2.removeItem(index)  
        index = self.comboBox_3.findText(text) 
        self.comboBox_3.removeItem(index)
    def index1(self,text):
        index = self.comboBox_3.findText(text) 
        self.comboBox_3.removeItem(index)

    def encrypter_a_la_volee(self,valeur):
        for j in range (0,len(valeur)):#parcourir le texte à encrypter
            if not valeur[j].isalpha(): #dans le cas d'un caractere non alphabetique on renvoi le meme caractere sans passer par l'encryption  
                self.var=self.var+valeur[j]
            else:
                i = self.alphabet.tab.index(valeur[j])#recuperer l'indice de la lettre alphabetique
                v = int(self.rotor1.tab[1][i])#recuper le contenu de la case correspondante dans rotor1
                i = (i + v)%26
                v = int(self.rotor2.tab[1][i])#recuper le contenu de la case correspondante dans rotor2
                i = (i + v)%26
                v = int(self.rotor3.tab[1][i])#recuper le contenu de la case correspondante dans rotor3
                i = (i + v)%26
                v = int(self.reflecteur.tab[i])#recuper le contenu de la case correspondante dans reflecteur
                i = (i + v)%26
                v = int(self.rotor3.tab[0][i])#recuper le contenu de la case correspondante dans rotor3
                i = (i + v)%26
                v = int(self.rotor2.tab[0][i])#recuper le contenu de la case correspondante dans rotor2
                i = (i + v)%26
                v = int(self.rotor1.tab[0][i])#recuper le contenu de la case correspondante dans rotor1
                i = (i + v)%26
                l = self.alphabet.tab[i]#recuper la lettre correspondante à l'encryption
                self.var=self.var+l
            self.etape_suivante()#faire appel a la fonction etape_suivante 
        self.lineEdit_2.setText(self.var)#afficher le resultat de l'encryption
        return valeur 

    def decrypter_a_la_volee(self,valeur):
        for j in range (0,len(valeur)):#parcourir le texte à décrypter
            if not valeur[j].isalpha(): #dans le cas d'un caractere non alphabetique on renvoi le meme caractere sans passer par le decryptage  
                self.var=self.var+valeur[j]
            else:
                i = self.alphabet.tab.index(valeur[j])#recuperer l'indice de la lettre alphabetique
                v = int(self.rotor1.tab[1][i])#recuper le contenu de la case correspondante dans rotor1
                i = (i + v)%26
                v = int(self.rotor2.tab[1][i])#recuper le contenu de la case correspondante dans rotor2
                i = (i + v)%26
                v = int(self.rotor3.tab[1][i])#recuper le contenu de la case correspondante dans rotor3
                i = (i + v)%26
                v = int(self.reflecteur.tab[i])#recuper le contenu de la case correspondante dans reflecteur
                i = (i + v)%26
                v = int(self.rotor3.tab[0][i])#recuper le contenu de la case correspondante dans rotor3
                i = (i + v)%26
                v = int(self.rotor2.tab[0][i])#recuper le contenu de la case correspondante dans rotor2
                i = (i + v)%26
                v = int(self.rotor1.tab[0][i])#recuper le contenu de la case correspondante dans rotor1
                i = (i + v)%26
                l = self.alphabet.tab[i]#recuper la lettre correspondante au décryptage
                self.var=self.var+l
            self.etape_suivante()#faire appel a la fonction etape_suivante 
        self.lineEdit.setText(self.var)#afficher le resultat du décryptage
        return valeur
    # remettre les rotors à leurs positions initiales   
    def reinistialiser(self):        
        T = []
        T = self.configurerABC()#faire appel à la fonction configurerABC
        self.rotor3 = T[2]
        self.rotor2 = T[1]
        self.rotor1 = T[0]
        #afficher les 3 rotors aprés modification
        lblRotor1 = self.rotor1.rotorInterface()
        self.rtr1.setText(lblRotor1)
        lblRotor2 = self.rotor2.rotorInterface()
        self.rtr2.setText(lblRotor2)
        lblRotor3 = self.rotor3.rotorInterface()
        self.rtr3.setText(lblRotor3) 
        self.valeur=""
        self.var=""
        self.lineEdit.setText(self.var)
        self.lineEdit_2.setText(self.valeur)
        self.nb = 0
        ensemble=[self.caseSA1,self.caseSR10,self.caseSR11,self.caseSR20,self.caseSR21,self.caseSR30,self.caseSR31,self.caseSRef1,self.caseSRef2,self.caseSA2]
        for k in ensemble:
             k.setStyleSheet("background: none; ")
             k.setText("") 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
