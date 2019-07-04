# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Application import Application
from pyCategoryPop import Ui_Dialog
from pyEditCategoryPop import Ui_Dialog

class DragDropTableWidget(QtWidgets.QTableWidget):
  '''
  This class utilizes the concept of inheritance. It is
  the child class of QTableWidget, which means that it 
  has all of the functionality of QTableWidget, but has
  the ability to implement its own extra methods that
  QTableWidget does not have, and re-implement QTableWidget
  methods in its own specialized way. In our case,
  we are re-implementing the dropEvent() method so that
  it carries out our own specified functionality when called -
  I believe it does nothing by default.
  '''
  def __init__(self, app, mainWindow, parent = None):
    self.app = app
    self.mainWindow = mainWindow
    super(DragDropTableWidget, self).__init__(parent)

  def dropEvent(self, event):
    event.accept()
    row = self.mainWindow.tableWidget.currentRow()
    referenceNumber = int(self.mainWindow.tableWidget.item(row, 0).text())
    location = self.mainWindow.tableWidget.item(row, 1).text()
    amount = self.mainWindow.tableWidget.item(row, 2).text()
    self.mainWindow.tableWidget.removeRow(row)
    c = self.app.getCategoryNamesList()[self.mainWindow.categoryWidget.currentIndex() + 1]
    self.app.registerCompletedTransaction(c, referenceNumber)
    self.app.saveData()
    # print the keywords of the updated category for debugging purposes
    print(c, self.app.getKeywordsByCategory(c))
    self.mainWindow.moveRowToDropDestination(referenceNumber, location, amount, c)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 720)
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
        self.listLabel.setGeometry(QtCore.QRect(440, 300, 71, 16))
        self.listLabel.setObjectName("listLabel")
        self.deleteCategory = QtWidgets.QPushButton(self.tab_2)
        self.deleteCategory.setGeometry(QtCore.QRect(340, 560, 113, 32))
        self.deleteCategory.setObjectName("deleteCategory")
        self.editCategory = QtWidgets.QPushButton(self.tab_2)
        self.editCategory.setGeometry(QtCore.QRect(220, 560, 113, 32))
        self.editCategory.setObjectName("editCategory")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(400, 50, 151, 16))
        self.label.setObjectName("label")
        self.categoryWidget = QtWidgets.QTabWidget(self.tab_2)
        self.categoryWidget.setGeometry(QtCore.QRect(30, 330, 881, 191))
        self.categoryWidget.setAcceptDrops(True)
        self.categoryWidget.setObjectName("categoryWidget")
        self.Unhandled = QtWidgets.QWidget()
        self.Unhandled.setObjectName("Unhandled")
        self.categoryWidget.addTab(self.Unhandled, "")
        self.Groceries = QtWidgets.QWidget()
        self.Groceries.setObjectName("Groceries")
        self.categoryWidget.addTab(self.Groceries, "")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(250, 80, 431, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.setDragEnabled(True)
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
        self.label.setText(_translate("MainWindow", "Unhandled Transactions"))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.Unhandled), _translate("MainWindow", "Unhandled"))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.Groceries), _translate("MainWindow", "Groceries"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Transaction ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Location"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount"))
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
        # self.filename = "../KevinVisaMay2019"
        # self.app.sortCompletedTransactions(self.filename)
        self.createCategoryWidget()
        # self.printUnhandledTransactions()
    

        self.openCatPopUp.clicked.connect(self.openNewCatPop)
        self.editCategory.clicked.connect(self.openEditCatPop)
        self.deleteCategory.clicked.connect(self.deleteSelectedCategory)
        self.importCsvBtn.clicked.connect(self.fileOpen)

    def fileOpen(self):
      filePath, _ = QtWidgets.QFileDialog.getOpenFileName()
      self.app.sortCompletedTransactions(filePath)
      self.printUnhandledTransactions()

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
        self.editUi = Ui_Dialog()
        self.editUi.setupUi(self.Dialog, self.app)
        self.Dialog.show()

        self.editUi.newCategoryName.setText(self.index)
        self.editUi.newCategoryAllotment.setText(str(self.app.getAmountAllottedByCategory(self.index)))

        # First, check if there are any keywords to be added.
        # Add items only if an iterable list of keywords is returned.
        keywords = self.app.getKeywordsByCategory(self.index)
        if keywords != None:
            self.editUi.newCategoryKeywords.addItems(keywords)


    def updateCategoryWidget(self):
        # bugger
        self.app.saveData()
        self.createCategoryWidget()

    def createCategoryWidget(self):
        self.categoryWidget.clear()
        for category in self.app.getCategoryNamesList():
            if category != "Unhandled":
                tab = DragDropTableWidget(self.app, self)
                tab.setAcceptDrops(True)
                self.categoryWidget.addTab(tab, category)
                self.categoryWidget.setCurrentWidget(tab)
                for i in range(3):
                    self.categoryWidget.currentWidget().insertColumn(i)
                self.fillCategoryWidget(category)

    def moveRowToDropDestination(self, referenceNumber, location, amount, category):
        rowPos = self.categoryWidget.currentWidget().rowCount()
        self.categoryWidget.currentWidget().insertRow(rowPos)
        self.categoryWidget.currentWidget().setItem(rowPos, 0, QtWidgets.QTableWidgetItem(str(referenceNumber)))
        self.categoryWidget.currentWidget().setItem(rowPos, 1, QtWidgets.QTableWidgetItem(location))
        self.categoryWidget.currentWidget().setItem(rowPos, 2, QtWidgets.QTableWidgetItem(amount))


        

    def fillCategoryWidget(self, category):
        #self.categoryWidget.currentWidget().clear()
        for t in self.app.getCompletedTransactionsByCategory(category).values():
            rowPos = self.categoryWidget.currentWidget().rowCount()
            self.categoryWidget.currentWidget().insertRow(rowPos)
            self.categoryWidget.currentWidget().setItem(rowPos, 0, QtWidgets.QTableWidgetItem(str(t.referenceNumber)))
            self.categoryWidget.currentWidget().setItem(rowPos, 1, QtWidgets.QTableWidgetItem(t.location))
            self.categoryWidget.currentWidget().setItem(rowPos, 2, QtWidgets.QTableWidgetItem(t.amount))


    def printUnhandledTransactions(self):
        for t in self.app.getUnhandledTransactions().values():
            rowPos = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPos)
            self.tableWidget.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(str(t.referenceNumber)))
            self.tableWidget.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(t.location))
            self.tableWidget.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(t.amount))


    def deleteSelectedCategory(self):
        self.tab = self.categoryWidget.currentIndex() + 1        
        self.index = self.app.getCategoryNamesList()[self.tab]
        self.app.deleteCategory(self.index)
        self.updateCategoryWidget()

    

    def updateCategoryListOfTransactions(self):
        self.tab = self.categoryWidget.currentIndex() + 1
        self.index = self.app.getCategoryNamesList()[self.tab]
        

##############################################################################################
                    # beginning of auto-generated code
##############################################################################################





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
