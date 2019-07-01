# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QDrag
from Application import Application
from pyCategoryPop import Ui_Dialog
from Transaction import CompletedTransaction

class DragDropListWidget(QtWidgets.QListWidget):
  '''
  This class utilizes the concept of inheritance. It is
  the child class of QListWidget, which means that it 
  has all of the functionality of QListWidget, but has
  the ability to implement its own extra methods that
  QListWidget does not have, and re-implement QListWidget
  methods in its own specialized way. In our case,
  we are re-implementing the dropEvent() method so that
  it carries out our own specified functionality when called -
  I believe it does nothing by default.
  '''
  def __init__(self, app, mainWindow, parent = None):
    self.app = app
    self.mainWindow = mainWindow
    super(DragDropListWidget, self).__init__(parent)

  def dropEvent(self, event):
    event.accept()
    row = self.mainWindow.unhandledTransactionsList.currentRow()
    location = self.mainWindow.unhandledTransactionsList.item(row, 0).text()
    amount = self.mainWindow.unhandledTransactionsList.item(row, 1).text()
    c = self.app.getCategoryNamesList()[self.mainWindow.categoryWidget.currentIndex() + 1]
    self.app.registerCompletedTransaction(c, location, amount)
    self.app.saveData()
    self.mainWindow.printUnhandledTransactions()
    # print the keywords of the updated category for debugging purposes
    print(c, self.app.getKeywordsByCategory(c))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 876)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.importTab = QtWidgets.QTabWidget(self.centralwidget)
        self.importTab.setGeometry(QtCore.QRect(50, 50, 961, 641))
        self.importTab.setAcceptDrops(True)
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
        self.enterCSVLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.enterCSVLabel.setFont(font)
        self.enterCSVLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.enterCSVLabel.setObjectName("enterCSVLabel")
        self.gridLayout.addWidget(self.enterCSVLabel, 2, 0, 1, 1)
        self.importCsvBtn = QtWidgets.QPushButton(self.tab)
        self.importCsvBtn.setObjectName("importCsvBtn")
        self.gridLayout.addWidget(self.importCsvBtn, 9, 0, 1, 1)
        self.titleLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.importTab.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.instructionsLabel = QtWidgets.QLabel(self.tab_2)
        self.instructionsLabel.setGeometry(QtCore.QRect(280, 20, 361, 21))
        self.instructionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionsLabel.setObjectName("instructionsLabel")
        self.openCatPopUp = QtWidgets.QPushButton(self.tab_2)
        self.openCatPopUp.setGeometry(QtCore.QRect(100, 560, 113, 32))
        self.openCatPopUp.setObjectName("openCatPopUp")
        self.listLabel = QtWidgets.QLabel(self.tab_2)
        self.listLabel.setGeometry(QtCore.QRect(420, 300, 71, 16))
        self.listLabel.setObjectName("listLabel")
        self.deleteCategory = QtWidgets.QPushButton(self.tab_2)
        self.deleteCategory.setGeometry(QtCore.QRect(340, 560, 113, 32))
        self.deleteCategory.setObjectName("deleteCategory")
        self.editCategory = QtWidgets.QPushButton(self.tab_2)
        self.editCategory.setGeometry(QtCore.QRect(220, 560, 113, 32))
        self.editCategory.setObjectName("editCategory")
        self.unhandledTransactionsList = QTableWidget(self.tab_2)
        self.unhandledTransactionsList.setGeometry(QtCore.QRect(240, 70, 451, 221))
        self.unhandledTransactionsList.setDragEnabled(True)
        self.unhandledTransactionsList.setObjectName("unhandledTransactionsList")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(430, 50, 91, 16))
        self.label.setObjectName("label")
        self.categoryWidget = QtWidgets.QTabWidget(self.tab_2)
        self.categoryWidget.setGeometry(QtCore.QRect(30, 330, 881, 191))
        self.categoryWidget.setAcceptDrops(True)
        self.categoryWidget.setObjectName("categoryWidget")
        self.importTab.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1224, 22))
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
        self.categoryWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.enterCSVLabel.setText(_translate("MainWindow", "Enter CSV file"))
        self.importCsvBtn.setText(_translate("MainWindow", "Import CSV"))
        self.titleLabel.setText(_translate("MainWindow", "Kinda Dope.."))
        self.importTab.setTabText(self.importTab.indexOf(self.tab), _translate("MainWindow", "Import"))
        self.instructionsLabel.setText(_translate("MainWindow", "Create New Categories and Sort Unhandled Transactions"))
        self.openCatPopUp.setText(_translate("MainWindow", "New Category"))
        self.listLabel.setText(_translate("MainWindow", "Categories"))
        self.deleteCategory.setText(_translate("MainWindow", "Delete"))
        self.editCategory.setText(_translate("MainWindow", "Edit"))
        self.label.setText(_translate("MainWindow", "Transactions"))
        
        self.importTab.setTabText(self.importTab.indexOf(self.tab_2), _translate("MainWindow", "Categorize"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuCategories.setTitle(_translate("MainWindow", "Categories"))
        self.menuTransactions.setTitle(_translate("MainWindow", "Transactions"))
        self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
        self.actionImport_CSV.setText(_translate("MainWindow", "Import CSV"))

##############################################################################################
                    # end of auto-generated code
##############################################################################################
        
        # placed here to instantiate the backend in the GUI at the start, 
        # it makes it easier for the backed to be passed into the popup windows
        # where several functions are called
        self.app = Application()
        self.app.initialize()
        self.filename = "../CreditCard3"
        self.app.sortCompletedTransactions(self.filename)
        self.createCategoryWidget()
        self.printUnhandledTransactions()
    

        self.openCatPopUp.clicked.connect(self.openNewCatPop)
        self.editCategory.clicked.connect(self.openEditCatPop)
        self.deleteCategory.clicked.connect(self.deleteSelectedCategory)


    def openNewCatPop(self):
        '''
        when newCategory button is pushed on categorize tab, this will
        prompt a popup that allows user to enter a new category, monthly allotment
        and a list of potential keywords
        '''
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog, self.app)
        self.ui.saveCategoryInfo.clicked.connect(self.updateCategoryWidget)
        self.Dialog.show()

    def openEditCatPop(self):
        '''
        Opens same window as openNewCatPop but autofills the 
        information and allows it to be edited
        '''

        self.tab = self.categoryWidget.currentIndex()        
        self.index = self.app.getCategoryNamesList()[self.tab+1]
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog, self.app)
        self.ui.saveCategoryInfo.clicked.connect(self.updateCategoryWidget)
        self.Dialog.show()

        self.ui.newCategoryName.setText(self.index)
        self.ui.newCategoryAllotment.setText(str(self.app.getAmountAllottedByCategory(self.index)))

        # First, check if there are any keywords to be added.
        # Add items only if an iterable list of keywords is returned.
        keywords = self.app.getKeywordsByCategory(self.index)
        if keywords != None:
            self.ui.newCategoryKeywords.addItems(keywords)


    def updateCategoryWidget(self):
        self.app.saveData()
        self.createCategoryWidget()

    def createCategoryWidget(self):
        self.categoryWidget.clear()
        self.categoryNamesList = self.app.getCategoryNamesList()
        print(self.categoryNamesList)
        for category in self.categoryNamesList:
            if category != "Unhandled":
                self.tab = DragDropListWidget(self.app, self)
                self.tab.setAcceptDrops(True)
                self.categoryWidget.addTab(self.tab, category)



    def printUnhandledTransactions(self):
        self.unhandledTransactionsList.clear()
        self.unhandledTransactionsList.insertColumn(0)
        self.unhandledTransactionsList.insertColumn(1)
        self.unhandledTransactionsList.insertColumn(2)
        for t in self.app.getUnhandledTransactions():
            rowPos = self.unhandledTransactionsList.rowCount()
            self.unhandledTransactionsList.insertRow(rowPos)
            self.unhandledTransactionsList.setItem(rowPos, 0, QTableWidgetItem(str(t.referenceNumber)))
            self.unhandledTransactionsList.setItem(rowPos, 1, QTableWidgetItem(t.location))
            self.unhandledTransactionsList.setItem(rowPos, 2, QTableWidgetItem(t.amount))
            self.unhandledTransactionsObjects = self.app.getUnhandledTransactions()

    def deleteSelectedCategory(self):
        self.tab = self.categoryWidget.currentIndex() + 1        
        self.index = self.app.getCategoryNamesList()[self.tab]
        self.app.deleteCategory(self.index)
        self.updateCategoryWidget()






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
