import os
from pathlib import Path
from dotenv import load_dotenv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from google import genai
current_dir = Path(__file__).resolve().parent
env_path = current_dir / ".env"
load_dotenv(dotenv_path=env_path)
class AIWorker(QThread):
    response_received = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, history): 
        super().__init__()
        self.history = history

    def run(self):
        try:
            from google.genai.types import HttpOptions 
            api_key = os.getenv("GOOGLE_API_KEY") 
            client = genai.Client(
                api_key=api_key,
                http_options=HttpOptions(api_version="v1")
            )
            
            
            response = client.models.generate_content(
                model="gemini-2.5-flash-lite", 
                contents=self.history
            )
            
            self.response_received.emit(response.text)
        except Exception as e:
            self.error_occurred.emit(str(e))
class Ui_MainWindow(QtCore.QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("QMainWindow{\n"
"        color: #f0f0f0;\n"
"       background-color: rgb(86,86,86);   \n"
"        border-radius: 5px;}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setStyleSheet("QTextBrowser {\n"
"        color: #f0f0f0;\n"
"       background-color: rgb(86,86,86);   \n"
"        border-radius: 5px;}\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_4.addWidget(self.textBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("QTextEdit {\n"
"        color: #f0f0f0;\n"
"       background-color: rgb(70,70,70);   \n"
"        border-radius: 5px;}\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        self.SendButton.setFixedWidth(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SendButton.sizePolicy().hasHeightForWidth())
        self.SendButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.SendButton.setFont(font)
        self.SendButton.setStyleSheet("QPushButton {\n"
"        color: #f0f0f0;\n"
"       background-color: rgb(70,70,70);   \n"
"        border-radius: 5px;}\n"
"QPushButton:Hover{background-color: rgb(100,100,100);}\n"
"\"\"\")\n"
"")
        self.SendButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/5582878.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SendButton.setIcon(icon)
        self.SendButton.setIconSize(QtCore.QSize(40, 40))
        self.SendButton.setObjectName("SendButton")
        self.horizontalLayout_2.addWidget(self.SendButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.setStretch(0, 20)
        self.verticalLayout_4.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.textEdit.installEventFilter(self)
        self.SendButton.clicked.connect(self.start_ai_task)
        self.retranslateUi(MainWindow)
        self.chat_history = []
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def start_ai_task(self):
        user_input = self.textEdit.toPlainText().strip()
        if user_input:
            self.textEdit.clear()
            self.chat_history.append({"role": "user", "parts": [{"text": user_input}]})

            
            user_html = f"""<div align="right"><table border="0" cellpadding="10" style="background-color: #0078d4; border-radius: 15px;"><tr><td style="color: white;">{user_input}</td></tr></table></div>"""
            self.textBrowser.insertHtml(user_html)

            
            self.textBrowser.insertHtml("""
                <div align="left">
                    <table border="0" cellpadding="10" style="background-color: #444444; border-radius: 15px;">
                        <tr><td style="color: #4285F4;"><i>ID_THINKING</i></td></tr>
                    </table>
                </div><br>
            """)

            self.worker = AIWorker(self.chat_history)
            self.worker.response_received.connect(self.handle_response)
            self.worker.error_occurred.connect(self.handle_response)
            self.worker.start()

    def handle_response(self, text):
        
        self.chat_history.append({
            "role": "model", 
            "parts": [{"text": text}]
        })
        
       
        all_html = self.textBrowser.toHtml()
        
      
        if "ID_THINKING" in all_html:
            new_html = all_html.replace("ID_THINKING", text)
        else:
          
            new_html = all_html.replace("Gemini is thinking...", text)
        
        
        self.textBrowser.setHtml(new_html)
        self.textBrowser.moveCursor(QtGui.QTextCursor.End)
    def eventFilter(self, obj, event):
        if obj is self.textEdit and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Return and not event.modifiers() & QtCore.Qt.ShiftModifier:
                self.start_ai_task()
                return True
        return super().eventFilter(obj, event)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


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
    ui.SendButton.setStyleSheet(f"""
                                QPushButton {{
                                color: #ffffff;
                background-color: {real_accent};
                border-radius: 5px;

                 }}QPushButton:hover {{
            background-color: rgb(100,100,100);
            border-radius: 5px;

        }}
                         """)
    
    MainWindow.show()
    sys.exit(app.exec_())
