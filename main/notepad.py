
import winreg
from datetime import datetime,timezone
from PyQt5 import QtCore, QtGui, QtWidgets
from Calculator import Ui_MainWindow as Ui_CalculatorWindow
from aichat import Ui_MainWindow as Ui_AIWindow
from notepad_backend import create_db,new_note,database,set_app_state,get_app_state

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(86, 86, 86);\n"
"}")    
        self.mainwindow=MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.mainLayout = QtWidgets.QHBoxLayout()
       

       
       
        self.mainLayout2 = QtWidgets.QVBoxLayout()
        self.centralwidget.setObjectName("centralwidget")



        self.Calculator = QtWidgets.QPushButton(self.centralwidget)

        self.Calculator.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Calculator.setAutoFillBackground(False)
        self.Calculator.setStyleSheet("""QPushButton {
        background-color: rgb(85, 255, 127);  
        border-radius: 5px;

    min-height: 32px;
    min-width: 100px;}
QPushButton:Hover{background-color: rgb(100,100,100);}
""")
        self.Calculator.setObjectName("Calculator")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.textEdit.setStyleSheet("""QTextEdit {
        color: #f0f0f0;
       background-color: rgb(86,86,86);   
        border-radius: 5px;}
""")
        self.textEdit.setObjectName("textEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mainLayout.addWidget(self.listWidget)
        self.listWidget.setFixedWidth(120)
        self.mainLayout.addWidget(self.textEdit, stretch=1)
        self.listWidget.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        self.listWidget.setStyleSheet("""QListWidget{
        color: #f0f0f0;
        background-color: rgb(86,86,86);
        border: 2px solid #f0f0f0;   
        border-radius: 5px;}
""")
        self.listWidget.setObjectName("listWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        layout = QtWidgets.QHBoxLayout(self.groupBox)

        self.mainLayout2.addWidget(self.groupBox)
        self.mainLayout2.addLayout(self.mainLayout) 
        self.centralwidget.setLayout(self.mainLayout2)
        self.groupBox.setStyleSheet("""QGroupBox{
        color: #f0f0f0;
        background-color: rgb(80,80,80);  
        border-radius: 5px;}
""")
        self.groupBox.setObjectName("groupBox")
        self.NewButton = QtWidgets.QPushButton(self.groupBox)
        
        self.groupBox.setMaximumWidth(800)
        self.groupBox.setMaximumHeight(80)
        
        layout.setAlignment(QtCore.Qt.AlignLeft)
        self.NewButton.setStyleSheet("""QPushButton {
        background-color: rgb(0,255,255);  
        border-radius: 5px;}
QPushButton:Hover{background-color: rgb(100,100,100);}
""")
        self.NewButton.setObjectName("NewButton")
        self.SaveLabel = QtWidgets.QPushButton(self.groupBox)
        layout.addWidget(self.SaveLabel)
        self.SaveLabel.setFixedSize(300,30)
        layout.addSpacing(60)
        layout.addWidget(self.NewButton)
        self.NewButton.setFixedSize(70,30)
        self.SaveLabel.setStyleSheet("""QPushButton {
        color: #ffffff;
        background-color: rgb(100, 100, 100);
        border-radius: 5px;}
        QPushButton:Hover{background-color: rgb(110,110,110);}
""")
        self.PlusButton = QtWidgets.QPushButton(self.groupBox)
        self.PlusButton.setObjectName("PlusButton")                  
        layout.addWidget(self.PlusButton)
        self.PlusButton.setFixedSize(40, 30)
        self.PlusButton.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                background-color: rgb(100, 100, 100);
                border-radius: 5px;
            }
            QPushButton:Hover {
                background-color: rgb(110,110,110);
            }
        """)
        self.Sizelabel = QtWidgets.QLabel(self.groupBox)
        self.Sizelabel.setObjectName("PlusButton")                  
        layout.addWidget(self.Sizelabel)
        self.Sizelabel.setFixedSize(30,30)
        self.Sizelabel.setAlignment(QtCore.Qt.AlignCenter)  
        self.Sizelabel.setStyleSheet("""
            QLabel {
                color: #ffffff;
                background-color: rgb(100, 100, 100);
                border-radius: 5px;
            }
        """)
        self.MinusButton = QtWidgets.QPushButton(self.groupBox)
        self.MinusButton.setObjectName("PlusButton")                  
        layout.addWidget(self.MinusButton)
        self.MinusButton.setFixedSize(40, 30)
        self.MinusButton.setStyleSheet("""
            QPushButton {
                color: #ffffff;
                background-color: rgb(100, 100, 100);
                border-radius: 5px;
            }
            QPushButton:Hover {
                background-color: rgb(110,110,110);
            }
        """)
        
        self.AIButton = QtWidgets.QPushButton(self.groupBox)
        self.AIButton.setObjectName("AIButton")                  
        layout.addWidget(self.AIButton)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Google_Gemini_icon_2025.svg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AIButton.setIcon(icon)
        self.AIButton.setFixedSize(40, 30)
        self.AIButton.setStyleSheet("""
    QPushButton {
        color: white;
        
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
            stop:0 #4285F4,  
            stop:0.5 #9b72cb, 
            stop:1 #DB4437); 
        border-radius: 8px;
        font-weight: bold;
        padding: 5px;
    }
    QPushButton:hover {
        /* Slightly brighter on hover */
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
            stop:0 #5a95f5, 
            stop:1 #e35e52);
    }
    QPushButton:pressed {
        background-color: #3c4043; 
        color: #4285F4;
    }
""")
        
        self.DelButton = QtWidgets.QPushButton(self.groupBox)
        
        layout.addWidget(self.DelButton)
        self.DelButton.setFixedSize(70,30)
        
        self.DelButton.setStyleSheet("""QPushButton {
        background-color: rgb(255,0,0);  
        border-radius: 5px;}
QPushButton:Hover{background-color: rgb(100,100,100);}
""")
        self.DelButton.setObjectName("DelButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        spacer = QtWidgets.QSpacerItem(
                10, 10,                         
         QtWidgets.QSizePolicy.Fixed,
        QtWidgets.QSizePolicy.Minimum
        )
        layout.addItem(spacer)        
        layout.addWidget(self.Calculator)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Calculator.clicked.connect(self.OpenCalculator)
        self.NewButton.clicked.connect(self.new_note_clicked)
        self.AIButton.clicked.connect(self.Openai)
        self.textEdit.textChanged.connect(self.on_text_changed)
        self.listWidget.itemClicked.connect(self.load_note)
        self.DelButton.clicked.connect(self.DELete)
        self.PlusButton.clicked.connect(self.plus)
        self.MinusButton.clicked.connect(self.minus)
        conn = database()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title FROM notes")
        self.saveTimer = QtCore.QTimer()
        self.saveTimer.setSingleShot(True)
        self.saveTimer.timeout.connect(self.save)




        conn = database()
        cursor = conn.cursor()
        cursor.execute("SELECT id, title FROM notes")
        for note_id, title in cursor.fetchall():
            item = QtWidgets.QListWidgetItem(title)
            item.setData(QtCore.Qt.UserRole, note_id)
            self.listWidget.addItem(item)
        cursor.close()
        conn.close()




    def on_text_changed(self):
                self.SaveLabel.setText("Editing…")
                self.saveTimer.start(2000)
    def OpenCalculator(self):
                self.calc_window = QtWidgets.QMainWindow()
                self.calc_ui = Ui_CalculatorWindow()
                self.calc_ui.setupUi(self.calc_window)
                def get_windows_accent_color():
                        try:
                                registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
                                key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\DWM")
                                value, _ = winreg.QueryValueEx(key, "AccentColor")
                                h = "{:08x}".format(value)
                                r, g, b = h[6:8], h[4:6], h[2:4]
                                return f"#{r}{g}{b}"
                        except:
                                return "#0078d4"
                accent = get_windows_accent_color()
                self.calc_ui.EqualButton.setStyleSheet(f"""
                                QPushButton {{
                                color: #ffffff;
                background-color: {accent};

                 }}QPushButton:hover {{
            background-color: {accent};

        }}
                         """)

                self.calc_window.show()
    def Openai(self):
                self.ai_window = QtWidgets.QMainWindow()
                self.ai_ui = Ui_AIWindow()
                self.ai_ui.setupUi(self.ai_window)
                def get_windows_accent_color():
                        try:
                                registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
                                key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\DWM")
                                value, _ = winreg.QueryValueEx(key, "AccentColor")
                                h = "{:08x}".format(value)
                                r, g, b = h[6:8], h[4:6], h[2:4]
                                return f"#{r}{g}{b}"
                        except:
                                return "#0078d4"
                accent = get_windows_accent_color()
                self.ai_ui.SendButton.setStyleSheet(f"""
                                QPushButton {{
                                color: #ffffff;
                background-color: {accent};
                border-radius: 5px;

                 }}QPushButton:hover {{
            background-color: rgb(100,100,100);
            border-radius: 5px;

        }}
                         """)

                self.ai_window.show()
    
    def new_note_clicked(self):
        title, ok = QtWidgets.QInputDialog.getText(self.mainwindow, "New Note", "Enter note title:")
        if not ok or not title:
            title = "Untitled"
        note_id = new_note(title)
        
        
        conn = database()
        cursor = conn.cursor()
        cursor.execute("UPDATE notes SET font_size = 15 WHERE id = ?", (note_id,))
        conn.commit()
        conn.close()
        
        item = QtWidgets.QListWidgetItem(title)
        item.setData(QtCore.Qt.UserRole, note_id)
        self.listWidget.addItem(item)
        self.listWidget.setCurrentItem(item)
        self.textEdit.clear()
        
        
        font = self.textEdit.font()
        font.setPointSize(8)
        self.textEdit.setFont(font)
        self.Sizelabel.setText(str(8))

    def load_note(self, item):
        if not item:
            return
    
        note_id = int(item.data(QtCore.Qt.UserRole))
        set_app_state("last_note_id", note_id)
    
        conn = database()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT note, modified, font_size FROM notes WHERE id = ?",
            (note_id,)
        )
        result = cursor.fetchone()
        conn.close()
    
        if result:
            note_text, modified, font_size = result
    
            self.textEdit.blockSignals(True)
            self.textEdit.setPlainText(note_text)
    
            font = self.textEdit.font()
            font.setPointSize(font_size or 8)
            self.textEdit.setFont(font)
            self.Sizelabel.setText(str(font.pointSize()))
    
            readable = self.time_ago(modified)
            self.SaveLabel.setText(f"{item.text()} — Last modified: {readable}")
    
            self.textEdit.blockSignals(False)


   
    def load_note_by_id(self, note_id):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if int(item.data(QtCore.Qt.UserRole)) == note_id:
                self.listWidget.setCurrentItem(item)
                self.load_note(item)
                break



    def DELete(self):
        item = self.listWidget.currentItem()
        if item:
                note_id = int(item.data(QtCore.Qt.UserRole))
                conn = database()
                cursor = conn.cursor()
                cursor.execute("DELETE from notes WHERE id = ?",  (note_id,))
                conn.commit()
                conn.close()
                self.listWidget.takeItem(self.listWidget.row(item))
                self.textEdit.clear()
    def time_ago(self,time):
                if not time or time == "0":
                        return "just now"
                past = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")  # leave it naive (local time)
                now = datetime.now()
                diff = now - past

                seconds = diff.total_seconds()

                if seconds < 60:
                    return "just now"
                elif seconds < 3600:
                    return f"{int(seconds // 60)} minutes ago"
                elif seconds < 86400:
                    return f"{int(seconds // 3600)} hours ago"
                else:
                        return f"{int(seconds // 86400)} days ago"
    def plus(self):
        font = self.textEdit.font()
        size = font.pointSize()+1
        font.setPointSize(size)
        self.textEdit.setFont(font)
        self.Sizelabel.setText(str(size)) 
        self.save_font_size(size + 1)
    def minus(self):
        font = self.textEdit.font()
        size = font.pointSize()-1
        font.setPointSize(size)
        self.textEdit.setFont(font)
        self.Sizelabel.setText(str(size)) 
        self.save_font_size(size + 1)
    
    def save(self):
        result=None
        item = self.listWidget.currentItem()
        if item:
                note_id = int(item.data(QtCore.Qt.UserRole))
                text = self.textEdit.toPlainText()
                conn = database()
                cursor = conn.cursor()
                font_size = self.textEdit.font().pointSize()
                cursor.execute(
                    "UPDATE notes SET note = ?, modified = datetime('now', 'localtime'), font_size = ? WHERE id = ?",
                    (text, font_size, note_id)
                )
                conn.commit()
                cursor.execute("Select modified from notes where id=?",(note_id,))
                result = cursor.fetchone()
                conn.close()
        if result:
                note_name = item.text()
                readable = self.time_ago(result[0])
                self.SaveLabel.setText(f"{note_name} — Last modified: {readable}")
    def save_font_size(self, size):
                item = self.listWidget.currentItem()
                if item:
                    note_id = int(item.data(QtCore.Qt.UserRole))
                    conn = database()
                    cursor = conn.cursor()
                    cursor.execute("UPDATE notes SET font_size = ? WHERE id = ?", (size, note_id))
                    conn.commit()
                    conn.close()
   

                      
    
    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Calculator.setText(_translate("MainWindow", "Calculator"))
        self.groupBox.setTitle(_translate("MainWindow", "Actions"))
        self.NewButton.setText(_translate("MainWindow", "New"))
        self.SaveLabel.setText(_translate("MainWindow", "Last modified:"))
        self.DelButton.setText(_translate("MainWindow", "Delete"))
        self.PlusButton.setText(_translate("MainWindow", "+"))
        self.MinusButton.setText(_translate("MainWindow", "-"))
        self.AIButton.setText(_translate("MainWindow", ""))
        self.Sizelabel.setText(_translate("MainWindow", str(self.textEdit.font().pointSize())))


        
if __name__ == "__main__":
    import sys
    create_db()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    last_id = get_app_state("last_note_id")
    if last_id is not None:
        QtCore.QTimer.singleShot(
            0, lambda: ui.load_note_by_id(int(last_id))
        )

    sys.exit(app.exec_())


