# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyCategoryPop import Ui_Dialog
from Application import Application


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.importTab = QtWidgets.QTabWidget(self.centralwidget)
        self.importTab.setGeometry(QtCore.QRect(20, 10, 961, 641))
        self.importTab.setObjectName("importTab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newCatInput = QtWidgets.QLineEdit(self.tab)
        self.newCatInput.setObjectName("newCatInput")
        self.horizontalLayout.addWidget(self.newCatInput)
        self.toolButton = QtWidgets.QToolButton(self.tab)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.importCsvBtn = QtWidgets.QPushButton(self.tab)
        self.importCsvBtn.setObjectName("importCsvBtn")
        self.gridLayout.addWidget(self.importCsvBtn, 9, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.importTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.instructionsLabel = QtWidgets.QLabel(self.tab_2)
        self.instructionsLabel.setGeometry(QtCore.QRect(280, 20, 361, 21))
        self.instructionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionsLabel.setObjectName("instructionsLabel")
        self.unhandledT = QtWidgets.QListWidget(self.tab_2)
        self.unhandledT.setGeometry(QtCore.QRect(500, 100, 81, 221))
        self.unhandledT.setObjectName("unhandledT")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.unhandledT.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.unhandledT.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.unhandledT.addItem(item)
        self.typeNewCat = QtWidgets.QLineEdit(self.tab_2)
        self.typeNewCat.setGeometry(QtCore.QRect(90, 80, 113, 21))
        self.typeNewCat.setObjectName("typeNewCat")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 100, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.importTab.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 22))
        self.menubar.setObjectName("menubar")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        self.menuCategories = QtWidgets.QMenu(self.menubar)
        self.menuCategories.setObjectName("menuCategories")
        self.menuTransactions = QtWidgets.QMenu(self.menubar)
        self.menuTransactions.setObjectName("menuTransactions")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_CSV = QtWidgets.QAction(MainWindow)
        self.actionImport_CSV.setObjectName("actionImport_CSV")
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuCategories.menuAction())
        self.menubar.addAction(self.menuTransactions.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())

        self.retranslateUi(MainWindow)
        self.importTab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

##############################################################################################
                    # end of auto-generated code
##############################################################################################
        
        # placed here to instantiate the backend in the GUI at the start, 
        # it makes it easier for the backed to be passed into the popup windows
        # where several functions are called
        self.app = Application()
        self.app.initialize()


        self.importCsvBtn.clicked.connect(self.runApp)
        self.pushButton_2.clicked.connect(self.openCatPop)


    def openCatPop(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog, self.app)
        self.Dialog.show()



    def runApp(self):
        self.filename = "../" + str(self.newCatInput.text())
        self.app.sortCompletedTransactions(self.filename)
        print("I think its fine....")
        for t in self.app.getUnhandledTransactions().completedTransactions:
            print("[UNHANDLED] Amount: " + t.amount + ", Location: " + t.location)
    

##############################################################################################
                    # begin auto-generated code
##############################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label.setText(_translate("MainWindow", "Enter CSV file"))
        self.importCsvBtn.setText(_translate("MainWindow", "Import CSV"))
        self.label_3.setText(_translate("MainWindow", "Kinda Dope.."))
        self.importTab.setTabText(self.importTab.indexOf(self.tab), _translate("MainWindow", "Import"))
        self.instructionsLabel.setText(_translate("MainWindow", "Create New Categories and Sort Unhandles Transactions"))
        __sortingEnabled = self.unhandledT.isSortingEnabled()
        self.unhandledT.setSortingEnabled(False)
        item = self.unhandledT.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.unhandledT.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.unhandledT.item(2)
        item.setText(_translate("MainWindow", "New Item"))
        self.unhandledT.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.importTab.setTabText(self.importTab.indexOf(self.tab_2), _translate("MainWindow", "Categorize"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuCategories.setTitle(_translate("MainWindow", "Categories"))
        self.menuTransactions.setTitle(_translate("MainWindow", "Transactions"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.actionImport_CSV.setText(_translate("MainWindow", "Import CSV"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
