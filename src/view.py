

from PyQt5 import QtCore, QtGui, QtWidgets
import presenter

class View(object):
    def __init__(self):
        self.recom = []
        self.listWidget = None
        self.presenter = None

    def set_presenter(self, _presenter: presenter.Presenter):
        self.presenter = _presenter

    def setupUi(self, MainWindow):

        
        """Sets up the UI elements and their properties."""

        MainWindow.setObjectName("MainWindow")  # Sets the object name for the main window
        MainWindow.resize(800, 600)  # Sets the window size
        MainWindow.setStyleSheet("QWidget{background-color: #222831;}")  # Sets the background color



        # **Central Widget:**
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidged{background-color: #393E46;}")  # Sets the background color
        self.centralwidget.setObjectName("centralwidget")  # Sets the object name




        # **Labels:**
        # Main label (presumably for instructions or information)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 50, 311, 91))  # Sets the label's position and size
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)  # Sets the font
        self.label.setStyleSheet("QLabel{color: white;}")  # Sets the text color
        self.label.setWordWrap(True)  # Enables text wrapping
        self.label.setObjectName("label")  # Sets the object name




        # Label for recommended movies section
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 60, 281, 31))  # Sets position and size
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)  # Sets the font
        self.label_3.setStyleSheet("QLabel{color: white;}")  # Sets the text color
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)  # Centers the text
        self.label_3.setObjectName("label_3")  # Sets the object name



        # **Buttons:**
        # Button to trigger an action (presumably related to recommendations)
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(160, 460, 141, 51))  # Sets position and size
        font = QtGui.QFont()
        font.setPointSize(12)
        self.showButton.setFont(font)  # Sets the font
        self.showButton.setStyleSheet("QPushButton{background-color: #00ADB5;border-radius: 10px;}")  # Sets the button style
        self.showButton.setObjectName("showButton")  # Sets the object name
        self.showButton.clicked.connect(lambda: self.presenter.on_button_clicked())  # Connects to the presenter's action



        # **List Widget:**
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(70, 170, 311, 261))  # Sets position and size
        self.listWidget.setObjectName("listWidget")  # Sets the object name
        self.listWidget.setStyleSheet("QListWidget{color: white;}")  # Sets the text color



        # **Movie Labels:**
        # Labels to display recommended movies (initially hidden)
        self.movie1 = QtWidgets.QLabel(self.centralwidget)  # ...
        self.movie2 = QtWidgets.QLabel(self.centralwidget)  # ... (similar for movie3, movie4, movie5)


        self.movie1 = QtWidgets.QLabel(self.centralwidget)
        self.movie1.setGeometry(QtCore.QRect(460, 130, 291, 61))
        self.movie1.setObjectName("movie1")
        self.recom.append(self.movie1)

        self.movie2 = QtWidgets.QLabel(self.centralwidget)
        self.movie2.setGeometry(QtCore.QRect(460, 210, 291, 61))
        self.movie2.setObjectName("movie2")
        self.recom.append(self.movie2)

        self.movie3 = QtWidgets.QLabel(self.centralwidget)
        self.movie3.setGeometry(QtCore.QRect(460, 290, 291, 61))
        self.movie3.setObjectName("movie3")
        self.recom.append(self.movie3)

        self.movie4 = QtWidgets.QLabel(self.centralwidget)
        self.movie4.setGeometry(QtCore.QRect(460, 370, 291, 61))
        self.movie4.setObjectName("movie4")
        self.recom.append(self.movie4)

        self.movie5 = QtWidgets.QLabel(self.centralwidget)
        self.movie5.setGeometry(QtCore.QRect(460, 450, 291, 61))
        self.movie5.setObjectName("movie5")
        self.recom.append(self.movie5)

        for a in self.recom:
            font = QtGui.QFont()
            font.setPointSize(10)
            a.setFont(font)
            a.setStyleSheet("QLabel{border: 2px solid #00ADB5; border-radius: 10px; color: white; padding-left: 5px;}")
            a.hide()
        self.presenter.set_list()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Choose UR favourite Movie and KNN algorithm will recommend you 5 similar movies you might like ^_^ "))
        self.showButton.setText(_translate("MainWindow", "Show"))
        self.label_3.setText(_translate("MainWindow", "Algorithm recommendation"))


