import sys
from math import sqrt,pow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 700)
        MainWindow.setStyleSheet("QMainWindow{\n"
"        background-color:rgb(86,86,86)\n"
"}")
        
        self.centralwidget = QtWidgets.QWidget()
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 40, 475, 100))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("""QLineEdit {
        color: #f0f0f0;
        background-color: rgb(86, 86, 86);  
        border-radius: 5px;
        border: 2px solid #f0f0f0;                             }
""")
      
        self.lineEdit.setObjectName("lineEdit")
        self.PrecenntButton = QtWidgets.QPushButton(self.centralwidget)
        self.PrecenntButton.setGeometry(QtCore.QRect(5, 150, 115, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.PrecenntButton.setFont(font)
        self.PrecenntButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.PrecenntButton.setObjectName("PrecenntButton")
        self.CEButton = QtWidgets.QPushButton(self.centralwidget)
        self.CEButton.setGeometry(QtCore.QRect(120, 150, 115, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CEButton.setFont(font)
        self.CEButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.CEButton.setObjectName("CEButton")
        self.CButton = QtWidgets.QPushButton(self.centralwidget)
        self.CButton.setGeometry(QtCore.QRect(235, 150, 110, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.CButton.setFont(font)
        self.CButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.CButton.setObjectName("CButton")
        self.BackspaceButton = QtWidgets.QPushButton(self.centralwidget)
        self.BackspaceButton.setGeometry(QtCore.QRect(345, 150, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BackspaceButton.setFont(font)
        self.BackspaceButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.BackspaceButton.setObjectName("BackspaceButton")
        self.SqrtButton = QtWidgets.QPushButton(self.centralwidget)
        self.SqrtButton.setGeometry(QtCore.QRect(235, 230, 110, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SqrtButton.setFont(font)
        self.SqrtButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.SqrtButton.setObjectName("SqrtButton")
        self.DevideButton = QtWidgets.QPushButton(self.centralwidget)
        self.DevideButton.setGeometry(QtCore.QRect(345, 230, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DevideButton.setFont(font)
        self.DevideButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.DevideButton.setObjectName("DevideButton")
        self.Powerof2Button = QtWidgets.QPushButton(self.centralwidget)
        self.Powerof2Button.setGeometry(QtCore.QRect(120, 230, 115, 80))
        self.Powerof2Button.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.Powerof2Button.setObjectName("Powerof2Button")
        self.BracketButton = QtWidgets.QPushButton(self.centralwidget)
        self.BracketButton.setGeometry(QtCore.QRect(5, 230, 50, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BracketButton.setFont(font)
        self.BracketButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.BracketButton.setObjectName("BracketButton")
        self.BracketButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.BracketButton_2.setGeometry(QtCore.QRect(70, 230, 50, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BracketButton_2.setFont(font)
        self.BracketButton_2.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.BracketButton_2.setObjectName("BracketButton_2")
        self.NineButton = QtWidgets.QPushButton(self.centralwidget)
        self.NineButton.setGeometry(QtCore.QRect(235, 310, 110, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.NineButton.setFont(font)
        self.NineButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.NineButton.setObjectName("NineButton")
        self.MultiplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.MultiplyButton.setGeometry(QtCore.QRect(345, 310, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.MultiplyButton.setFont(font)
        self.MultiplyButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.MultiplyButton.setObjectName("MultiplyButton")
        self.EightButton = QtWidgets.QPushButton(self.centralwidget)
        self.EightButton.setGeometry(QtCore.QRect(120, 310, 115, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EightButton.setFont(font)
        self.EightButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.EightButton.setObjectName("EightButton")
        self.SevenButton = QtWidgets.QPushButton(self.centralwidget)
        self.SevenButton.setGeometry(QtCore.QRect(5, 310, 115, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SevenButton.setFont(font)
        self.SevenButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.SevenButton.setObjectName("SevenButton")
        self.MinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.MinusButton.setGeometry(QtCore.QRect(345, 390, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.MinusButton.setFont(font)
        self.MinusButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.MinusButton.setObjectName("MinusButton")
        self.SixButton = QtWidgets.QPushButton(self.centralwidget)
        self.SixButton.setGeometry(QtCore.QRect(235, 390, 110, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SixButton.setFont(font)
        self.SixButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.SixButton.setObjectName("SixButton")
        self.FourButton = QtWidgets.QPushButton(self.centralwidget)
        self.FourButton.setGeometry(QtCore.QRect(5, 390, 115, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.FourButton.setFont(font)
        self.FourButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.FourButton.setObjectName("FourButton")
        self.FiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.FiveButton.setGeometry(QtCore.QRect(120, 390, 115, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.FiveButton.setFont(font)
        self.FiveButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.FiveButton.setObjectName("FiveButton")
        self.ThreeButton = QtWidgets.QPushButton(self.centralwidget)
        self.ThreeButton.setGeometry(QtCore.QRect(235, 470, 110, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ThreeButton.setFont(font)
        self.ThreeButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.ThreeButton.setObjectName("ThreeButton")
        self.PlusButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlusButton.setGeometry(QtCore.QRect(345, 470, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.PlusButton.setFont(font)
        self.PlusButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.PlusButton.setObjectName("PlusButton")
        self.TwoButton = QtWidgets.QPushButton(self.centralwidget)
        self.TwoButton.setGeometry(QtCore.QRect(120, 470, 115, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.TwoButton.setFont(font)
        self.TwoButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.TwoButton.setObjectName("TwoButton")
        self.OneButton = QtWidgets.QPushButton(self.centralwidget)
        self.OneButton.setGeometry(QtCore.QRect(5, 470, 115, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.OneButton.setFont(font)
        self.OneButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.OneButton.setObjectName("OneButton")
        self.DotButton = QtWidgets.QPushButton(self.centralwidget)
        self.DotButton.setGeometry(QtCore.QRect(235, 550, 110, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DotButton.setFont(font)
        self.DotButton.setStyleSheet("""
        QPushButton {
    color: #ffffff;
    background-color: rgb(87,87,87);}
""")

        self.DotButton.setObjectName("DotButton")
        self.EqualButton = QtWidgets.QPushButton(self.centralwidget)
        self.EqualButton.setGeometry(QtCore.QRect(345, 550, 120, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.EqualButton.setFont(font)
        palette = QtWidgets.QApplication.palette()
        accent = palette.color(QtGui.QPalette.Highlight).name()
        self.EqualButton.setStyleSheet(f"""
        QPushButton {{
        color: #f0f0f0;
        background-color: {accent};
        }}
        """)

        self.EqualButton.setObjectName("EqualButton")
        self.ZeroButton = QtWidgets.QPushButton(self.centralwidget)
        self.ZeroButton.setGeometry(QtCore.QRect(120, 550, 115, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ZeroButton.setFont(font)
        self.ZeroButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.ZeroButton.setObjectName("ZeroButton")
        self.PlusMinusButton = QtWidgets.QPushButton(self.centralwidget)
        self.PlusMinusButton.setGeometry(QtCore.QRect(5, 550, 115, 80))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.PlusMinusButton.setFont(font)
        self.PlusMinusButton.setStyleSheet("QPushButton{\n"
"        color:#f0f0f0;\n"
"        background-color:rgb(86,86,86)\n"
"}")
        self.PlusMinusButton.setObjectName("PlusMinusButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -1, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"        color:#f0f0f0;\n"
"}")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 231, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # self.lineEdit.setReadOnly(True)
        self.OneButton.clicked.connect(lambda:self.buttonsPressed("1"))
        self.TwoButton.clicked.connect(lambda:self.buttonsPressed("2"))
        self.ThreeButton.clicked.connect(lambda:self.buttonsPressed("3"))
        self.FourButton.clicked.connect(lambda:self.buttonsPressed("4"))
        self.FiveButton.clicked.connect(lambda:self.buttonsPressed("5"))
        self.SixButton.clicked.connect(lambda:self.buttonsPressed("6"))
        self.SevenButton.clicked.connect(lambda:self.buttonsPressed("7"))
        self.EightButton.clicked.connect(lambda:self.buttonsPressed("8"))
        self.NineButton.clicked.connect(lambda:self.buttonsPressed("9"))
        self.CButton.clicked.connect(lambda:self.buttonsPressed("C"))
        self.CEButton.clicked.connect(self.CEfunction)
        self.DotButton.clicked.connect(self.dotPressed)
        self.BracketButton.clicked.connect(lambda:self.buttonsPressed("("))
        self.BracketButton_2.clicked.connect(lambda:self.buttonsPressed(")"))
        self.PlusMinusButton.clicked.connect(self.plusminusfunction)
        self.BackspaceButton.clicked.connect(self.backspacefunction)
        self.SqrtButton.clicked.connect(self.sqrtfunction)
        self.Powerof2Button.clicked.connect(self.poweof2function)
        self.PrecenntButton.clicked.connect(self.percentfunction)
        self.PlusButton.clicked.connect(lambda:self.buttonsPressed("+"))
        self.MinusButton.clicked.connect(lambda:self.buttonsPressed("-"))
        self.DevideButton.clicked.connect(lambda:self.buttonsPressed("÷"))
        self.MultiplyButton.clicked.connect(lambda:self.buttonsPressed("×"))
        self.EqualButton.clicked.connect(self.equalfunction)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def buttonsPressed(self,pressed):
        if pressed == "C":
                self.lineEdit.setText("")
        else: self.lineEdit.setText(f"{self.lineEdit.text()}{pressed}")
    def CEfunction(self):
        text = str(self.lineEdit.text())
        operators = "+-*/"
       
        last_op_index = -1
        for i in range(len(text)-1, -1, -1):
            if text[i] in operators:
                last_op_index = i
                break

        if last_op_index == -1:
            self.lineEdit.setText("0")
        else:
                result = text[:last_op_index+1]
                self.lineEdit.setText(result)
    def sqrtfunction(self):
        text=int(self.lineEdit.text())
        
        try:
             result=sqrt(text)
             self.lineEdit.setText(str(result))
               
        except:
             self.lineEdit.setText("Error")
             QtCore.QTimer.singleShot(1000, lambda: self.lineEdit.setText(""))
    def poweof2function(self):
        text=int(self.lineEdit.text())
        try:
                result=pow(text,2)
                self.lineEdit.setText(str(result))
        except:
             self.lineEdit.setText("Error")
             QtCore.QTimer.singleShot(1000, lambda: self.lineEdit.setText(""))

    def dotPressed(self):
            text = self.lineEdit.text()
            operators = "+-×÷*/"
            
            
            last_op_index = -1
            for i in range(len(text)-1, -1, -1):
                if text[i] in operators:
                    last_op_index = i
                    break
            
            current_number = text[last_op_index+1:]
            
            if "." not in current_number:
                self.lineEdit.setText(text + ".")

    def plusminusfunction(self):
            self.lineEdit.setText(str(float(self.lineEdit.text())*-1))
    def backspacefunction(self):
        text=self.lineEdit.text()
        result=text[:-1]
        self.lineEdit.setText(str(result))
    def percentfunction(self):
        try:
            value = float(self.lineEdit.text())
            value /= 100
            self.lineEdit.setText(str(value))
        except:
                self.lineEdit.setText("Error")
                QtCore.QTimer.singleShot(1000, lambda: self.lineEdit.setText(""))
    def equalfunction(self):
        text=self.lineEdit.text()
        text = text.replace("×", "*").replace("÷", "/")
        try:
                result=eval(text)
                self.lineEdit.setText(str(result))
        except:
             self.lineEdit.setText("Error")
             QtCore.QTimer.singleShot(1000, lambda: self.lineEdit.setText(""))
  

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PrecenntButton.setText(_translate("MainWindow", "%"))
        self.CEButton.setText(_translate("MainWindow", "CE"))
        self.CButton.setText(_translate("MainWindow", "C"))
        self.BackspaceButton.setText(_translate("MainWindow", " ⌫"))
        self.SqrtButton.setText(_translate("MainWindow", " √"))
        self.DevideButton.setText(_translate("MainWindow", "÷"))
        self.Powerof2Button.setText(_translate("MainWindow", "X^2"))
        self.BracketButton.setText(_translate("MainWindow", "("))
        self.BracketButton_2.setText(_translate("MainWindow", ")"))
        self.NineButton.setText(_translate("MainWindow", "9"))
        self.MultiplyButton.setText(_translate("MainWindow", "X"))
        self.EightButton.setText(_translate("MainWindow", "8"))
        self.SevenButton.setText(_translate("MainWindow", "7"))
        self.MinusButton.setText(_translate("MainWindow", "–"))
        self.SixButton.setText(_translate("MainWindow", "6"))
        self.FourButton.setText(_translate("MainWindow", "4"))
        self.FiveButton.setText(_translate("MainWindow", "5"))
        self.ThreeButton.setText(_translate("MainWindow", "3"))
        self.PlusButton.setText(_translate("MainWindow", "+"))
        self.TwoButton.setText(_translate("MainWindow", "2"))
        self.OneButton.setText(_translate("MainWindow", "1"))
        self.DotButton.setText(_translate("MainWindow", "."))
        self.EqualButton.setText(_translate("MainWindow", "="))
        self.ZeroButton.setText(_translate("MainWindow", "0"))
        self.PlusMinusButton.setText(_translate("MainWindow", "+/-"))
        self.label.setText(_translate("MainWindow", "Calculator"))


if __name__ == "__main__":
    import sys
    import winreg  

    def get_windows_accent_color():
        try:
            
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\DWM")
            value, type = winreg.QueryValueEx(key, "AccentColor")
            
            
            h = "{:08x}".format(value)
           
            r, g, b = h[6:8], h[4:6], h[2:4]
            return f"#{r}{g}{b}"
        except Exception:
           
            return "#0078d4"

    app = QtWidgets.QApplication(sys.argv)
    
    
    real_accent = get_windows_accent_color()
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    
    ui.EqualButton.setStyleSheet(f"""
        QPushButton {{
            color: #ffffff;
            background-color: {real_accent};

        }}
        QPushButton:hover {{
            background-color: {real_accent};

        }}
    """)
    
    MainWindow.show()
    sys.exit(app.exec_())
