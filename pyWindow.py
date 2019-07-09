# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Application import Application
from pyCategoryPop import Ui_createDialog
from pyEditCategoryPop import Ui_editDialog
from APIData import TransactionData

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
    self.mainWindow.moveRowToDropDestination(referenceNumber, location, amount, c)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1224, 947)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.importTab = QtWidgets.QTabWidget(self.centralwidget)
        self.importTab.setGeometry(QtCore.QRect(110, 80, 961, 641))
        self.importTab.setAcceptDrops(True)
        self.importTab.setObjectName("importTab")
        self.Import = QtWidgets.QWidget()
        self.Import.setObjectName("Import")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Import)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newCatInput = QtWidgets.QLineEdit(self.Import)
        self.newCatInput.setObjectName("newCatInput")
        self.horizontalLayout.addWidget(self.newCatInput)
        self.toolButton = QtWidgets.QToolButton(self.Import)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 1)
        self.enterCSVLabel = QtWidgets.QLabel(self.Import)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.enterCSVLabel.setFont(font)
        self.enterCSVLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.enterCSVLabel.setObjectName("enterCSVLabel")
        self.gridLayout.addWidget(self.enterCSVLabel, 2, 0, 1, 1)
        self.importCsvBtn = QtWidgets.QPushButton(self.Import)
        self.importCsvBtn.setObjectName("importCsvBtn")
        self.gridLayout.addWidget(self.importCsvBtn, 9, 0, 1, 1)
        self.titleLabel = QtWidgets.QLabel(self.Import)
        font = QtGui.QFont()
        font.setPointSize(72)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.importTab.addTab(self.Import, "")
        self.Categorize = QtWidgets.QWidget()
        self.Categorize.setObjectName("Categorize")
        self.instructionsLabel = QtWidgets.QLabel(self.Categorize)
        self.instructionsLabel.setGeometry(QtCore.QRect(280, 20, 361, 21))
        self.instructionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.instructionsLabel.setObjectName("instructionsLabel")
        self.openCatPopUp = QtWidgets.QPushButton(self.Categorize)
        self.openCatPopUp.setGeometry(QtCore.QRect(100, 560, 113, 32))
        self.openCatPopUp.setObjectName("openCatPopUp")
        self.listLabel = QtWidgets.QLabel(self.Categorize)
        self.listLabel.setGeometry(QtCore.QRect(440, 300, 71, 16))
        self.listLabel.setObjectName("listLabel")
        self.deleteCategory = QtWidgets.QPushButton(self.Categorize)
        self.deleteCategory.setGeometry(QtCore.QRect(340, 560, 113, 32))
        self.deleteCategory.setObjectName("deleteCategory")
        self.editCategory = QtWidgets.QPushButton(self.Categorize)
        self.editCategory.setGeometry(QtCore.QRect(220, 560, 113, 32))
        self.editCategory.setObjectName("editCategory")
        self.label = QtWidgets.QLabel(self.Categorize)
        self.label.setGeometry(QtCore.QRect(400, 50, 151, 16))
        self.label.setObjectName("label")
        self.categoryWidget = QtWidgets.QTabWidget(self.Categorize)
        self.categoryWidget.setGeometry(QtCore.QRect(30, 330, 881, 191))
        self.categoryWidget.setAcceptDrops(True)
        self.categoryWidget.setObjectName("categoryWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.categoryWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.categoryWidget.addTab(self.tab2, "")
        self.tableWidget = QtWidgets.QTableWidget(self.Categorize)
        self.tableWidget.setGeometry(QtCore.QRect(250, 80, 431, 191))
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.undoSorting = QtWidgets.QPushButton(self.Categorize)
        self.undoSorting.setGeometry(QtCore.QRect(460, 560, 113, 32))
        self.undoSorting.setObjectName("undoSorting")
        self.importTab.addTab(self.Categorize, "")
        self.Planning = QtWidgets.QWidget()
        self.Planning.setObjectName("Planning")
        self.tabWidget = QtWidgets.QTabWidget(self.Planning)
        self.tabWidget.setGeometry(QtCore.QRect(120, 390, 741, 181))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.tabWidgetPage2 = QtWidgets.QWidget()
        self.tabWidgetPage2.setObjectName("tabWidgetPage2")
        self.tabWidget.addTab(self.tabWidgetPage2, "")
        self.namePlannedT = QtWidgets.QLineEdit(self.Planning)
        self.namePlannedT.setGeometry(QtCore.QRect(130, 90, 141, 21))
        self.namePlannedT.setObjectName("namePlannedT")
        self.amountPlannedT = QtWidgets.QLineEdit(self.Planning)
        self.amountPlannedT.setGeometry(QtCore.QRect(130, 170, 141, 21))
        self.amountPlannedT.setObjectName("amountPlannedT")
        self.frequencyLabel = QtWidgets.QLabel(self.Planning)
        self.frequencyLabel.setGeometry(QtCore.QRect(130, 210, 211, 16))
        self.frequencyLabel.setObjectName("frequencyLabel")
        self.recurringBtn = QtWidgets.QRadioButton(self.Planning)
        self.recurringBtn.setGeometry(QtCore.QRect(140, 250, 100, 20))
        self.recurringBtn.setObjectName("recurringBtn")
        self.singularBtn = QtWidgets.QRadioButton(self.Planning)
        self.singularBtn.setGeometry(QtCore.QRect(140, 290, 100, 20))
        self.singularBtn.setObjectName("singularBtn")
        self.categoryPlannedT = QtWidgets.QLineEdit(self.Planning)
        self.categoryPlannedT.setGeometry(QtCore.QRect(130, 130, 141, 21))
        self.categoryPlannedT.setObjectName("categoryPlannedT")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.Planning)
        self.calendarWidget.setGeometry(QtCore.QRect(520, 80, 312, 173))
        self.calendarWidget.setObjectName("calendarWidget")
        self.label_2 = QtWidgets.QLabel(self.Planning)
        self.label_2.setGeometry(QtCore.QRect(370, 360, 231, 16))
        self.label_2.setObjectName("label_2")
        self.calendarInstructions = QtWidgets.QLabel(self.Planning)
        self.calendarInstructions.setGeometry(QtCore.QRect(550, 50, 261, 20))
        self.calendarInstructions.setText("")
        self.calendarInstructions.setObjectName("calendarInstructions")
        self.savePlannedT = QtWidgets.QPushButton(self.Planning)
        self.savePlannedT.setGeometry(QtCore.QRect(690, 310, 113, 32))
        self.savePlannedT.setObjectName("savePlannedT")
        self.label_3 = QtWidgets.QLabel(self.Planning)
        self.label_3.setGeometry(QtCore.QRect(130, 60, 141, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.Planning)
        self.comboBox.setGeometry(QtCore.QRect(270, 250, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.importTab.addTab(self.Planning, "")
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
        self.categoryWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.enterCSVLabel.setText(_translate("MainWindow", "Enter CSV file"))
        self.importCsvBtn.setText(_translate("MainWindow", "Import CSV"))
        self.titleLabel.setText(_translate("MainWindow", "Kinda Dope.."))
        self.importTab.setTabText(self.importTab.indexOf(self.Import), _translate("MainWindow", "Import"))
        self.instructionsLabel.setText(_translate("MainWindow", "Create New Categories and Sort Unhandled Transactions"))
        self.openCatPopUp.setText(_translate("MainWindow", "New Category"))
        self.listLabel.setText(_translate("MainWindow", "Categories"))
        self.deleteCategory.setText(_translate("MainWindow", "Delete"))
        self.editCategory.setText(_translate("MainWindow", "Edit"))
        self.label.setText(_translate("MainWindow", "Unhandled Transactions"))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.tab1), _translate("MainWindow", "Category"))
        self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.tab2), _translate("MainWindow", "Category"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Transaction ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Location"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount"))
        self.undoSorting.setText(_translate("MainWindow", "Undo"))
        self.importTab.setTabText(self.importTab.indexOf(self.Categorize), _translate("MainWindow", "Categorize"))
        self.namePlannedT.setPlaceholderText(_translate("MainWindow", "Name"))
        self.amountPlannedT.setPlaceholderText(_translate("MainWindow", "Amount"))
        self.frequencyLabel.setText(_translate("MainWindow", "Recurring or singular expenditure"))
        self.recurringBtn.setText(_translate("MainWindow", "Recurring"))
        self.singularBtn.setText(_translate("MainWindow", "Singular"))
        self.categoryPlannedT.setPlaceholderText(_translate("MainWindow", "Category"))
        self.label_2.setText(_translate("MainWindow", "Categories with planned expenditures"))
        self.savePlannedT.setText(_translate("MainWindow", "Save"))
        self.label_3.setText(_translate("MainWindow", "Enter expenditure:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "daily"))
        self.comboBox.setItemText(1, _translate("MainWindow", "weekly"))
        self.comboBox.setItemText(2, _translate("MainWindow", "bi-Weekly"))
        self.comboBox.setItemText(3, _translate("MainWindow", "monthly"))
        self.comboBox.setItemText(4, _translate("MainWindow", "quarterly"))
        self.comboBox.setItemText(5, _translate("MainWindow", "bi-annually"))
        self.comboBox.setItemText(6, _translate("MainWindow", "annually"))
        self.importTab.setTabText(self.importTab.indexOf(self.Planning), _translate("MainWindow", "Planning"))
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
        self.filename = self.newCatInput.text()
        self.importCsvBtn.clicked.connect(self.fileOpen)
        self.app.initialize()
        self.createCategoryWidget()
        self.openCatPopUp.clicked.connect(self.openNewCatPop)
        self.editCategory.clicked.connect(self.openEditCatPop)
        self.deleteCategory.clicked.connect(self.deleteSelectedCategory)
        self.comboBox.hide()
        self.recurringBtn.toggled.connect(self.comboBox.show)
        self.singularBtn.toggled.connect(self.comboBox.hide)
        self.createPlannedTransactionsWidget()
        self.savePlannedT.clicked.connect(self.savePlannedTransaction)
        self.undoSorting.clicked.connect(self.uncategorizeTransaction)
    

    def uncategorizeTransaction(self):
        row = self.categoryWidget.currentWidget().currentRow()
        location = self.categoryWidget.currentWidget().item(row, 1).text()
        amount = self.categoryWidget.currentWidget().item(row, 2).text()
        referenceNumber = int(self.categoryWidget.currentWidget().item(row, 0).text())
        c = self.app.getCategoryNamesList()[self.categoryWidget.currentIndex() + 1]
        self.app.unregisterCompletedTransaction(c, referenceNumber)
        self.app.registerCompletedTransaction("Unhandled", referenceNumber)
        self.app.diagnosticDbg()
        self.app.saveData()
        self.returnTransactionToUnhandled(referenceNumber, location, amount)
        self.categoryWidget.currentWidget().removeRow(row)

    def returnTransactionToUnhandled(self, referenceNumber, location, amount):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(referenceNumber)))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(location))
        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(amount))



    def fileOpen(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName()
        self.app.sortCompletedTransactions(filePath)
        self.printUnhandledTransactions()
        self.createCategoryWidget()

    def fillTransactionWidget(self, category):
        plannedTransactions = self.app.getPlannedTransactions(category)
        print(plannedTransactions)
        if plannedTransactions != None:
            for t in plannedTransactions:
                print(self.tabWidget.currentIndex())
                rowPos = self.tabWidget.currentWidget().rowCount()          
                self.tabWidget.currentWidget().insertRow(rowPos)
                self.tabWidget.currentWidget().setItem(rowPos, 0, QtWidgets.QTableWidgetItem(t.date))
                self.tabWidget.currentWidget().setItem(rowPos, 1, QtWidgets.QTableWidgetItem(t.name))
                self.tabWidget.currentWidget().setItem(rowPos, 2, QtWidgets.QTableWidgetItem(str(t.amount)))

    def savePlannedTransaction(self):
        transaction = TransactionData()
        transaction.name = self.namePlannedT.text()
        transaction.category = self.categoryPlannedT.text()
        transaction.amount = float(self.amountPlannedT.text())
        if self.recurringBtn.isChecked():
            transaction.recurring = True
            transaction.rateOfRecurrence = self.getToggledFrequency()[1]
        else:
            transaction.recurring = False
        transaction.date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        self.app.createPlannedTransaction(transaction)
        self.createPlannedTransactionsWidget()
        self.app.saveData()

    def getToggledFrequency(self):
        if self.recurringBtn.isChecked():
            return True, self.comboBox.currentText()
        return False


    def createPlannedTransactionsWidget(self):
        self.tabWidget.clear()
        print(self.app.getCategoryNamesList())
        for category in self.app.getCategoryNamesList():
            if category != "Unhandled":
                tab = QTableWidget()
                self.tabWidget.addTab(tab, category)
                self.tabWidget.setCurrentWidget(tab)
                for i in range(3):
                    self.tabWidget.currentWidget().insertColumn(i)
                print(self.tabWidget.currentIndex())
                print(self.tabWidget.currentWidget())
            self.fillTransactionWidget(category)

    def saveCSVPath(self):
        csvPath = self.newCatInput.text()
        self.app.sortCompletedTransactions(csvPath)
        self.printUnhandledTransactions()
        self.createCategoryWidget()

    def openNewCatPop(self):
        '''
        when newCategory button is pushed on categorize tab, this will
        prompt a popup that allows user to enter a new category, monthly allotment
        and a list of potential keywords
        '''
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_createDialog()
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
        self.editUi = Ui_editDialog()
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
        self.app.saveData()
        self.createCategoryWidget()
        self.createPlannedTransactionsWidget()

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
            # resizing the columns
            header = self.tableWidget.horizontalHeader()       
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            
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
################################################################################################



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
