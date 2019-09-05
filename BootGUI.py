from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from Application import Application
from CategoryPopUpWindow import Ui_createDialog
from EditCategoryPopUpWindow import Ui_editDialog
from APIData import TransactionData
from EmbeddedMatplotlibWindow import PlottingWindow
from EmbeddedMatplotlibWindow import ProjectionWidget
from pandas import to_datetime

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
    date = self.mainWindow.tableWidget.item(row, 1).text()
    location = self.mainWindow.tableWidget.item(row, 2).text()
    amount = self.mainWindow.tableWidget.item(row, 3).text()
    
    self.mainWindow.tableWidget.removeRow(row)
    c = self.app.getCategoryNamesList()[self.mainWindow.categoryWidget.currentIndex() + 1]
    self.app.registerCompletedTransaction(c, referenceNumber)
    self.app.saveData()
    self.autoSortAfterDrop(location, c)
    self.mainWindow.updateAnalysisTable(c)
    self.mainWindow.moveRowToDropDestination(referenceNumber, date, location, amount, c)

  def autoSortAfterDrop(self, location, c):
    tableSize = self.mainWindow.tableWidget.rowCount() - 1
    i = 0
    while i <= tableSize:
      print("Index of tableWidget: ", i)
      loc = self.mainWindow.tableWidget.item(i, 2).text()
      if loc == location:
        referenceNumber = int(self.mainWindow.tableWidget.item(i, 0).text())
        date = self.mainWindow.tableWidget.item(i, 1).text()
        location = self.mainWindow.tableWidget.item(i, 2).text()
        amount = self.mainWindow.tableWidget.item(i, 3).text()
        self.app.registerCompletedTransaction(c, referenceNumber)
        self.mainWindow.tableWidget.removeRow(i)
        self.mainWindow.moveRowToDropDestination(referenceNumber, date, location, amount, c)
        tableSize -= 1
      else:
        i += 1


class Ui_MainWindow(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(1224, 947)
    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
    self.gridLayout.setObjectName("gridLayout")
    self.TabWidget = QtWidgets.QTabWidget(self.centralwidget)
    self.TabWidget.setAcceptDrops(True)
    self.TabWidget.setAccessibleName("")
    self.TabWidget.setObjectName("TabWidget")
    self.Setup = QtWidgets.QWidget()
    self.Setup.setObjectName("Setup")
    self.importCSVBtn = QtWidgets.QPushButton(self.Setup)
    self.importCSVBtn.setGeometry(QtCore.QRect(790, 390, 261, 61))
    font = QtGui.QFont()
    font.setPointSize(18)
    self.importCSVBtn.setFont(font)
    self.importCSVBtn.setObjectName("importCSVBtn")
    self.label_9 = QtWidgets.QLabel(self.Setup)
    self.label_9.setGeometry(QtCore.QRect(430, 50, 271, 51))
    font = QtGui.QFont()
    font.setFamily("Segoe UI Black")
    font.setPointSize(28)
    font.setBold(True)
    font.setWeight(75)
    self.label_9.setFont(font)
    self.label_9.setObjectName("label_9")
    self.label_12 = QtWidgets.QLabel(self.Setup)
    self.label_12.setGeometry(QtCore.QRect(30, 90, 81, 31))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(14)
    font.setBold(False)
    font.setUnderline(True)
    font.setWeight(50)
    self.label_12.setFont(font)
    self.label_12.setObjectName("label_12")
    self.label_17 = QtWidgets.QLabel(self.Setup)
    self.label_17.setGeometry(QtCore.QRect(850, 220, 131, 31))
    self.label_17.setObjectName("label_17")
    self.label_18 = QtWidgets.QLabel(self.Setup)
    self.label_18.setGeometry(QtCore.QRect(30, 590, 161, 41))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(14)
    font.setBold(False)
    font.setUnderline(True)
    font.setWeight(50)
    self.label_18.setFont(font)
    self.label_18.setObjectName("label_18")
    self.checkingAccBal = QtWidgets.QLineEdit(self.Setup)
    self.checkingAccBal.setGeometry(QtCore.QRect(470, 180, 151, 51))
    self.checkingAccBal.setMinimumSize(QtCore.QSize(5, 5))
    font = QtGui.QFont()
    font.setPointSize(24)
    self.checkingAccBal.setFont(font)
    self.checkingAccBal.setText("")
    self.checkingAccBal.setObjectName("checkingAccBal")
    self.label_19 = QtWidgets.QLabel(self.Setup)
    self.label_19.setGeometry(QtCore.QRect(20, 160, 431, 81))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(26)
    self.label_19.setFont(font)
    self.label_19.setObjectName("label_19")
    self.label_13 = QtWidgets.QLabel(self.Setup)
    self.label_13.setGeometry(QtCore.QRect(130, 260, 321, 61))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(26)
    self.label_13.setFont(font)
    self.label_13.setObjectName("label_13")
    self.incomeAmount = QtWidgets.QLineEdit(self.Setup)
    self.incomeAmount.setGeometry(QtCore.QRect(470, 260, 151, 51))
    font = QtGui.QFont()
    font.setPointSize(24)
    self.incomeAmount.setFont(font)
    self.incomeAmount.setObjectName("incomeAmount")
    self.label_14 = QtWidgets.QLabel(self.Setup)
    self.label_14.setGeometry(QtCore.QRect(80, 340, 371, 61))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(26)
    self.label_14.setFont(font)
    self.label_14.setObjectName("label_14")
    self.freqPayDay = QtWidgets.QComboBox(self.Setup)
    self.freqPayDay.setGeometry(QtCore.QRect(460, 360, 161, 41))
    font = QtGui.QFont()
    font.setPointSize(14)
    self.freqPayDay.setFont(font)
    self.freqPayDay.setObjectName("freqPayDay")
    self.freqPayDay.addItem("")
    self.freqPayDay.addItem("")
    self.freqPayDay.addItem("")
    self.label_15 = QtWidgets.QLabel(self.Setup)
    self.label_15.setGeometry(QtCore.QRect(130, 420, 281, 71))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(26)
    self.label_15.setFont(font)
    self.label_15.setObjectName("label_15")
    self.nextPayDay = QtWidgets.QLineEdit(self.Setup)
    self.nextPayDay.setGeometry(QtCore.QRect(410, 440, 211, 41))
    font = QtGui.QFont()
    font.setPointSize(16)
    self.nextPayDay.setFont(font)
    self.nextPayDay.setObjectName("nextPayDay")
    self.nextCCPayment = QtWidgets.QLineEdit(self.Setup)
    self.nextCCPayment.setGeometry(QtCore.QRect(520, 670, 191, 41))
    font = QtGui.QFont()
    font.setPointSize(16)
    self.nextCCPayment.setFont(font)
    self.nextCCPayment.setObjectName("nextCCPayment")
    self.label_16 = QtWidgets.QLabel(self.Setup)
    self.label_16.setGeometry(QtCore.QRect(10, 650, 511, 78))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(26)
    self.label_16.setFont(font)
    self.label_16.setObjectName("label_16")
    self.label_11 = QtWidgets.QLabel(self.Setup)
    self.label_11.setGeometry(QtCore.QRect(840, 360, 161, 20))
    self.label_11.setObjectName("label_11")
    self.saveUserDataBtn = QtWidgets.QPushButton(self.Setup)
    self.saveUserDataBtn.setGeometry(QtCore.QRect(790, 260, 261, 61))
    font = QtGui.QFont()
    font.setPointSize(18)
    self.saveUserDataBtn.setFont(font)
    self.saveUserDataBtn.setObjectName("saveUserDataBtn")
    self.savedDataLabel = QtWidgets.QLabel(self.Setup)
    self.savedDataLabel.setGeometry(QtCore.QRect(830, 330, 191, 16))
    self.savedDataLabel.setText("")
    self.savedDataLabel.setObjectName("savedDataLabel")
    self.TabWidget.addTab(self.Setup, "")
    self.Planning = QtWidgets.QWidget()
    self.Planning.setObjectName("Planning")
    self.tabWidget = QtWidgets.QTabWidget(self.Planning)
    self.tabWidget.setGeometry(QtCore.QRect(470, 420, 411, 261))
    self.tabWidget.setObjectName("tabWidget")
    self.tabWidgetPage1 = QtWidgets.QWidget()
    self.tabWidgetPage1.setObjectName("tabWidgetPage1")
    self.tabWidget.addTab(self.tabWidgetPage1, "")
    self.tabWidgetPage2 = QtWidgets.QWidget()
    self.tabWidgetPage2.setObjectName("tabWidgetPage2")
    self.tabWidget.addTab(self.tabWidgetPage2, "")
    self.namePlannedT = QtWidgets.QLineEdit(self.Planning)
    self.namePlannedT.setGeometry(QtCore.QRect(130, 160, 141, 21))
    self.namePlannedT.setObjectName("namePlannedT")
    self.amountPlannedT = QtWidgets.QLineEdit(self.Planning)
    self.amountPlannedT.setGeometry(QtCore.QRect(130, 260, 141, 21))
    self.amountPlannedT.setObjectName("amountPlannedT")
    self.frequencyLabel = QtWidgets.QLabel(self.Planning)
    self.frequencyLabel.setGeometry(QtCore.QRect(60, 330, 261, 21))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    self.frequencyLabel.setFont(font)
    self.frequencyLabel.setObjectName("frequencyLabel")
    self.label_2 = QtWidgets.QLabel(self.Planning)
    self.label_2.setGeometry(QtCore.QRect(530, 370, 301, 31))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    self.label_2.setFont(font)
    self.label_2.setObjectName("label_2")
    self.savePlannedT = QtWidgets.QPushButton(self.Planning)
    self.savePlannedT.setGeometry(QtCore.QRect(130, 670, 113, 32))
    self.savePlannedT.setObjectName("savePlannedT")
    self.label_3 = QtWidgets.QLabel(self.Planning)
    self.label_3.setGeometry(QtCore.QRect(50, 100, 141, 31))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    self.label_3.setFont(font)
    self.label_3.setObjectName("label_3")
    self.recurrenceComboBox = QtWidgets.QComboBox(self.Planning)
    self.recurrenceComboBox.setGeometry(QtCore.QRect(240, 390, 104, 26))
    self.recurrenceComboBox.setObjectName("recurrenceComboBox")
    self.recurrenceComboBox.addItem("")
    self.recurrenceComboBox.addItem("")
    self.recurrenceComboBox.addItem("")
    self.recurrenceComboBox.addItem("")
    self.recurrenceComboBox.addItem("")
    self.recurrenceComboBox.addItem("")
    self.recurrenceComboBox.addItem("")
    self.categoryComboBox = QtWidgets.QComboBox(self.Planning)
    self.categoryComboBox.setGeometry(QtCore.QRect(130, 210, 141, 22))
    self.categoryComboBox.setObjectName("categoryComboBox")
    self.removeBtn = QtWidgets.QPushButton(self.Planning)
    self.removeBtn.setGeometry(QtCore.QRect(270, 670, 111, 31))
    self.removeBtn.setObjectName("removeBtn")
    self.label_10 = QtWidgets.QLabel(self.Planning)
    self.label_10.setGeometry(QtCore.QRect(70, 510, 161, 21))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    self.label_10.setFont(font)
    self.label_10.setObjectName("label_10")
    self.verticalLayoutWidget = QtWidgets.QWidget(self.Planning)
    self.verticalLayoutWidget.setGeometry(QtCore.QRect(130, 560, 160, 80))
    self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
    self.paymentGroup = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
    self.paymentGroup.setContentsMargins(0, 0, 0, 0)
    self.paymentGroup.setObjectName("paymentGroup")
    self.creditRadioBtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
    self.creditRadioBtn.setObjectName("creditRadioBtn")
    self.paymentGroup.addWidget(self.creditRadioBtn)
    self.checkingRadioBtn = QtWidgets.QRadioButton(self.verticalLayoutWidget)
    self.checkingRadioBtn.setObjectName("checkingRadioBtn")
    self.paymentGroup.addWidget(self.checkingRadioBtn)
    self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Planning)
    self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(130, 380, 91, 80))
    self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
    self.frequencyLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
    self.frequencyLayout.setContentsMargins(0, 0, 0, 0)
    self.frequencyLayout.setObjectName("frequencyLayout")
    self.recurringBtn = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
    self.recurringBtn.setObjectName("recurringBtn")
    self.frequencyLayout.addWidget(self.recurringBtn)
    self.singularBtn = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
    self.singularBtn.setObjectName("singularBtn")
    self.frequencyLayout.addWidget(self.singularBtn)
    self.calendarWidget = QtWidgets.QCalendarWidget(self.Planning)
    self.calendarWidget.setGeometry(QtCore.QRect(480, 120, 391, 211))
    self.calendarWidget.setObjectName("calendarWidget")
    self.label_7 = QtWidgets.QLabel(self.Planning)
    self.label_7.setGeometry(QtCore.QRect(310, 20, 491, 51))
    font = QtGui.QFont()
    font.setFamily("Segoe UI Black")
    font.setPointSize(24)
    font.setBold(True)
    font.setWeight(75)
    self.label_7.setFont(font)
    self.label_7.setObjectName("label_7")
    self.TabWidget.addTab(self.Planning, "")
    self.Categorize = QtWidgets.QWidget()
    self.Categorize.setObjectName("Categorize")
    self.instructionsLabel = QtWidgets.QLabel(self.Categorize)
    self.instructionsLabel.setGeometry(QtCore.QRect(230, 20, 471, 21))
    font = QtGui.QFont()
    font.setPointSize(12)
    font.setBold(True)
    font.setWeight(75)
    self.instructionsLabel.setFont(font)
    self.instructionsLabel.setAlignment(QtCore.Qt.AlignCenter)
    self.instructionsLabel.setObjectName("instructionsLabel")
    self.listLabel = QtWidgets.QLabel(self.Categorize)
    self.listLabel.setGeometry(QtCore.QRect(670, 60, 91, 41))
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    self.listLabel.setFont(font)
    self.listLabel.setObjectName("listLabel")
    self.label = QtWidgets.QLabel(self.Categorize)
    self.label.setGeometry(QtCore.QRect(120, 70, 211, 16))
    font = QtGui.QFont()
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    self.label.setFont(font)
    self.label.setObjectName("label")
    self.categoryWidget = QtWidgets.QTabWidget(self.Categorize)
    self.categoryWidget.setGeometry(QtCore.QRect(500, 100, 421, 391))
    self.categoryWidget.setAcceptDrops(True)
    self.categoryWidget.setObjectName("categoryWidget")
    self.tab1 = QtWidgets.QWidget()
    self.tab1.setObjectName("tab1")
    self.categoryWidget.addTab(self.tab1, "")
    self.tab2 = QtWidgets.QWidget()
    self.tab2.setObjectName("tab2")
    self.categoryWidget.addTab(self.tab2, "")
    self.tableWidget = QtWidgets.QTableWidget(self.Categorize)
    self.tableWidget.setGeometry(QtCore.QRect(30, 100, 441, 571))
    self.tableWidget.setDragEnabled(True)
    self.tableWidget.setObjectName("tableWidget")
    self.tableWidget.setColumnCount(4)
    self.tableWidget.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem()
    self.tableWidget.setHorizontalHeaderItem(3, item)
    self.label_4 = QtWidgets.QLabel(self.Categorize)
    self.label_4.setGeometry(QtCore.QRect(510, 520, 97, 34))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    self.label_4.setFont(font)
    self.label_4.setObjectName("label_4")
    self.categoryAllotted = QtWidgets.QLabel(self.Categorize)
    self.categoryAllotted.setGeometry(QtCore.QRect(610, 510, 96, 51))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(16)
    self.categoryAllotted.setFont(font)
    self.categoryAllotted.setText("")
    self.categoryAllotted.setObjectName("categoryAllotted")
    self.label_8 = QtWidgets.QLabel(self.Categorize)
    self.label_8.setGeometry(QtCore.QRect(730, 520, 71, 34))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    self.label_8.setFont(font)
    self.label_8.setObjectName("label_8")
    self.categorySpent = QtWidgets.QLabel(self.Categorize)
    self.categorySpent.setGeometry(QtCore.QRect(810, 510, 96, 51))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(16)
    self.categorySpent.setFont(font)
    self.categorySpent.setText("")
    self.categorySpent.setObjectName("categorySpent")
    self.openCatPopUp = QtWidgets.QPushButton(self.Categorize)
    self.openCatPopUp.setGeometry(QtCore.QRect(960, 130, 91, 41))
    self.openCatPopUp.setObjectName("openCatPopUp")
    self.editCategory = QtWidgets.QPushButton(self.Categorize)
    self.editCategory.setGeometry(QtCore.QRect(960, 190, 91, 41))
    self.editCategory.setObjectName("editCategory")
    self.undoBtn = QtWidgets.QPushButton(self.Categorize)
    self.undoBtn.setGeometry(QtCore.QRect(960, 250, 91, 41))
    self.undoBtn.setObjectName("undoBtn")
    self.deleteCategory = QtWidgets.QPushButton(self.Categorize)
    self.deleteCategory.setGeometry(QtCore.QRect(960, 310, 91, 41))
    self.deleteCategory.setObjectName("deleteCategory")
    self.TabWidget.addTab(self.Categorize, "")
    self.Analysis = QtWidgets.QWidget()
    self.Analysis.setObjectName("Analysis")
    self.categoryAnalysisTable = QtWidgets.QTableWidget(self.Analysis)
    self.categoryAnalysisTable.setGeometry(QtCore.QRect(80, 90, 801, 381))
    self.categoryAnalysisTable.setAutoFillBackground(False)
    self.categoryAnalysisTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    self.categoryAnalysisTable.setTextElideMode(QtCore.Qt.ElideRight)
    self.categoryAnalysisTable.setObjectName("categoryAnalysisTable")
    self.categoryAnalysisTable.setColumnCount(5)
    self.categoryAnalysisTable.setRowCount(0)
    item = QtWidgets.QTableWidgetItem()
    self.categoryAnalysisTable.setHorizontalHeaderItem(0, item)
    item = QtWidgets.QTableWidgetItem()
    self.categoryAnalysisTable.setHorizontalHeaderItem(1, item)
    item = QtWidgets.QTableWidgetItem()
    self.categoryAnalysisTable.setHorizontalHeaderItem(2, item)
    item = QtWidgets.QTableWidgetItem()
    self.categoryAnalysisTable.setHorizontalHeaderItem(3, item)
    item = QtWidgets.QTableWidgetItem()
    self.categoryAnalysisTable.setHorizontalHeaderItem(4, item)
    self.spendingLabel = QtWidgets.QLabel(self.Analysis)
    self.spendingLabel.setGeometry(QtCore.QRect(340, 20, 281, 51))
    font = QtGui.QFont()
    font.setPointSize(20)
    self.spendingLabel.setFont(font)
    self.spendingLabel.setAlignment(QtCore.Qt.AlignCenter)
    self.spendingLabel.setObjectName("spendingLabel")
    self.label_5 = QtWidgets.QLabel(self.Analysis)
    self.label_5.setGeometry(QtCore.QRect(80, 520, 181, 51))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    self.label_5.setFont(font)
    self.label_5.setObjectName("label_5")
    self.amountSpentLabel = QtWidgets.QLabel(self.Analysis)
    self.amountSpentLabel.setGeometry(QtCore.QRect(280, 520, 101, 51))
    font = QtGui.QFont()
    font.setPointSize(12)
    self.amountSpentLabel.setFont(font)
    self.amountSpentLabel.setObjectName("amountSpentLabel")
    self.label_6 = QtWidgets.QLabel(self.Analysis)
    self.label_6.setGeometry(QtCore.QRect(440, 530, 271, 31))
    font = QtGui.QFont()
    font.setFamily("Segoe UI")
    font.setPointSize(10)
    font.setBold(False)
    font.setWeight(50)
    self.label_6.setFont(font)
    self.label_6.setObjectName("label_6")
    self.percentageSpentLabel = QtWidgets.QLabel(self.Analysis)
    self.percentageSpentLabel.setGeometry(QtCore.QRect(720, 530, 91, 31))
    font = QtGui.QFont()
    font.setPointSize(12)
    self.percentageSpentLabel.setFont(font)
    self.percentageSpentLabel.setObjectName("percentageSpentLabel")
    self.plotWindow = QtWidgets.QPushButton(self.Analysis)
    self.plotWindow.setGeometry(QtCore.QRect(920, 110, 151, 51))
    self.plotWindow.setObjectName("plotWindow")
    self.cashProjectionsBtn = QtWidgets.QPushButton(self.Analysis)
    self.cashProjectionsBtn.setGeometry(QtCore.QRect(920, 180, 151, 51))
    self.cashProjectionsBtn.setObjectName("cashProjectionsBtn")
    self.TabWidget.addTab(self.Analysis, "")
    self.gridLayout.addWidget(self.TabWidget, 0, 0, 1, 1)
    MainWindow.setCentralWidget(self.centralwidget)
    self.menubar = QtWidgets.QMenuBar(MainWindow)
    self.menubar.setGeometry(QtCore.QRect(0, 0, 1224, 26))
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
    self.TabWidget.setCurrentIndex(0)
    self.tabWidget.setCurrentIndex(0)
    self.categoryWidget.setCurrentIndex(0)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)

  def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.importCSVBtn.setText(_translate("MainWindow", "Import CSV"))
    self.label_9.setText(_translate("MainWindow", "Get Started"))
    self.label_12.setText(_translate("MainWindow", "Bank:"))
    self.label_17.setText(_translate("MainWindow", "Save your information"))
    self.label_18.setText(_translate("MainWindow", "Credit Card:"))
    self.label_19.setText(_translate("MainWindow", "Checking Acc Balance:"))
    self.label_13.setText(_translate("MainWindow", "Income Amount:"))
    self.label_14.setText(_translate("MainWindow", "Income Frequency:"))
    self.freqPayDay.setItemText(0, _translate("MainWindow", "bi-weekly"))
    self.freqPayDay.setItemText(1, _translate("MainWindow", "weekly"))
    self.freqPayDay.setItemText(2, _translate("MainWindow", "monthly"))
    self.label_15.setText(_translate("MainWindow", "Next Pay Day:"))
    self.nextPayDay.setPlaceholderText(_translate("MainWindow", "mm/dd/yyyy"))
    self.nextCCPayment.setPlaceholderText(_translate("MainWindow", "mm/dd/yyyy"))
    self.label_16.setText(_translate("MainWindow", "Next credit card payment:"))
    self.label_11.setText(_translate("MainWindow", "Choose a CSV file to import"))
    self.saveUserDataBtn.setText(_translate("MainWindow", "Save"))
    self.TabWidget.setTabText(self.TabWidget.indexOf(self.Setup), _translate("MainWindow", "Setup"))
    self.namePlannedT.setPlaceholderText(_translate("MainWindow", "Name"))
    self.amountPlannedT.setPlaceholderText(_translate("MainWindow", "Amount"))
    self.frequencyLabel.setText(_translate("MainWindow", "Recurring or singular expenditure:"))
    self.label_2.setText(_translate("MainWindow", "Categories with planned expenditures"))
    self.savePlannedT.setText(_translate("MainWindow", "Save"))
    self.label_3.setText(_translate("MainWindow", "Enter expenditure:"))
    self.recurrenceComboBox.setItemText(0, _translate("MainWindow", "daily"))
    self.recurrenceComboBox.setItemText(1, _translate("MainWindow", "weekly"))
    self.recurrenceComboBox.setItemText(2, _translate("MainWindow", "bi-weekly"))
    self.recurrenceComboBox.setItemText(3, _translate("MainWindow", "monthly"))
    self.recurrenceComboBox.setItemText(4, _translate("MainWindow", "quarterly"))
    self.recurrenceComboBox.setItemText(5, _translate("MainWindow", "bi-annually"))
    self.recurrenceComboBox.setItemText(6, _translate("MainWindow", "annually"))
    self.removeBtn.setText(_translate("MainWindow", "Remove"))
    self.label_10.setText(_translate("MainWindow", "Method of Payment:"))
    self.creditRadioBtn.setText(_translate("MainWindow", "Credit Card"))
    self.checkingRadioBtn.setText(_translate("MainWindow", "Checking Account"))
    self.recurringBtn.setText(_translate("MainWindow", "Recurring"))
    self.singularBtn.setText(_translate("MainWindow", "Singular"))
    self.label_7.setText(_translate("MainWindow", "Plan Major Transactions"))
    self.TabWidget.setTabText(self.TabWidget.indexOf(self.Planning), _translate("MainWindow", "Planning"))
    self.instructionsLabel.setText(_translate("MainWindow", "Create New Categories and Sort Transactions"))
    self.listLabel.setText(_translate("MainWindow", "Categories"))
    self.label.setText(_translate("MainWindow", "Unhandled Transactions"))
    self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.tab1), _translate("MainWindow", "Category"))
    self.categoryWidget.setTabText(self.categoryWidget.indexOf(self.tab2), _translate("MainWindow", "Category"))
    item = self.tableWidget.horizontalHeaderItem(0)
    item.setText(_translate("MainWindow", "ID"))
    item = self.tableWidget.horizontalHeaderItem(1)
    item.setText(_translate("MainWindow", "Date"))
    item = self.tableWidget.horizontalHeaderItem(2)
    item.setText(_translate("MainWindow", "Location"))
    item = self.tableWidget.horizontalHeaderItem(3)
    item.setText(_translate("MainWindow", "Amount"))
    self.label_4.setText(_translate("MainWindow", "$ Allotted:"))
    self.label_8.setText(_translate("MainWindow", "$ Spent:"))
    self.openCatPopUp.setText(_translate("MainWindow", "New Category"))
    self.editCategory.setText(_translate("MainWindow", "Edit"))
    self.undoBtn.setText(_translate("MainWindow", "Undo"))
    self.deleteCategory.setText(_translate("MainWindow", "Delete"))
    self.TabWidget.setTabText(self.TabWidget.indexOf(self.Categorize), _translate("MainWindow", "Categorize"))
    item = self.categoryAnalysisTable.horizontalHeaderItem(0)
    item.setText(_translate("MainWindow", "Category"))
    item = self.categoryAnalysisTable.horizontalHeaderItem(1)
    item.setText(_translate("MainWindow", "$ Allotted"))
    item = self.categoryAnalysisTable.horizontalHeaderItem(2)
    item.setText(_translate("MainWindow", "$ Spent"))
    item = self.categoryAnalysisTable.horizontalHeaderItem(3)
    item.setText(_translate("MainWindow", "$ Planned"))
    item = self.categoryAnalysisTable.horizontalHeaderItem(4)
    item.setText(_translate("MainWindow", "Balance"))
    self.spendingLabel.setText(_translate("MainWindow", "Spending Analysis"))
    self.label_5.setText(_translate("MainWindow", "Total Amount Spent:"))
    self.amountSpentLabel.setText(_translate("MainWindow", "TextLabel"))
    self.label_6.setText(_translate("MainWindow", "Percentage of Monthly Budget:"))
    self.percentageSpentLabel.setText(_translate("MainWindow", "TextLabel"))
    self.plotWindow.setText(_translate("MainWindow", "Credit Card Analysis"))
    self.cashProjectionsBtn.setText(_translate("MainWindow", "Cash Projections"))
    self.TabWidget.setTabText(self.TabWidget.indexOf(self.Analysis), _translate("MainWindow", "Analysis"))
    self.menuImport.setTitle(_translate("MainWindow", "Import"))
    self.menuCategories.setTitle(_translate("MainWindow", "Categories"))
    self.menuTransactions.setTitle(_translate("MainWindow", "Transactions"))
    self.menuAnalysis.setTitle(_translate("MainWindow", "Analysis"))
    self.actionImport_CSV.setText(_translate("MainWindow", "Import CSV"))

##############################################################################################
                    # end of auto-generated code
##############################################################################################


    self.app = Application()

    # Import Tab
    self.app.initialize()
    self.saveUserDataBtn.clicked.connect(self.saveStartInfo)
    self.importCSVBtn.clicked.connect(self.fileOpen)

    # Categorize Tab
    self.createCategoryWidget()
    self.openCatPopUp.clicked.connect(self.openNewCatPop)
    self.editCategory.clicked.connect(self.openEditCatPop)
    self.deleteCategory.clicked.connect(self.deleteSelectedCategory)
    self.undoBtn.clicked.connect(self.uncategorizeCompletedTransaction)
    # self.showCategorySummary()

# Planning Tab
    self.recurrenceComboBox.hide()
    self.recurringBtn.toggled.connect(self.recurrenceComboBox.show)
    self.singularBtn.toggled.connect(self.recurrenceComboBox.hide)
    self.createPlannedTransactionsWidget()
    self.savePlannedT.clicked.connect(self.savePlannedTransaction)
    self.updateCategoryBox()
    self.removeBtn.clicked.connect(self.removePlannedTransaction)

# Analysis Tab
    self.plotWindow.clicked.connect(self.openPlottingWindow)

# Projection Tab
    self.cashProjectionsBtn.clicked.connect(self.openProjectionWindow)


  '''
  Setup Tab Functions - uses basic information mainly for predictive analysis.
  Put it all in one tab to consolidate arbitrary user input.

  '''


  def saveStartInfo(self):
    checkingAccBal = 0
    incomeAmt = 0
    payDayFreq = None
    payDay = None
    payCreditDate = None

    invalidEntries = 0
    # Validating proper checking acc input
    try:
      checkingAccBalance = int(self.checkingAccBal.text())
    except ValueError:
      invalidEntries += 1
      self.checkingAccBal.setText("")
      self.checkingAccBal.setPlaceholderText("Enter an integer or float value")

    # Validating proper income amt input
    try:
      incomeAmt = int(self.incomeAmount.text())
      
    except ValueError:
      invalidEntries += 1
      self.incomeAmount.setText("")
      self.incomeAmount.setPlaceholderText("Enter an integer or float value")
    
    # ComboBox wont allow for bad input
    payDayFreq = self.freqPayDay.currentText()

    # Validating proper date format for nextPayDay
    # This isnt perfect but if its this close to format
    # I will assume the user properly entered a date
    # Can be refined to make sure dates are valid
    try:
      payDay = to_datetime(self.nextPayDay.text())
       
    except:
      invalidEntries += 1
      self.nextPayDay.setText("")
      self.nextPayDay.setPlaceholderText("Use format mm/dd/yyyy")

    # See block above
    try:
      payCreditDate = to_datetime(self.nextCCPayment.text())
        
    except:
      invalidEntries += 1
      self.nextCCPayment.setText("")
      self.nextCCPayment.setPlaceholderText("Use format mm/dd/yyyy")

    self.app.saveUserSetupData(checkingAccBalance, incomeAmt, payDayFreq,
                               payDay, payCreditDate)

    self.savedDataLabel.setText("Last saved: " + str(time.ctime))



      
  '''

  Analysis Table Funcs - handles all functions that deal with the analysis tab and analysis
  QTableWidget; pulls data from API and updates concurrently with categorization method calls.
  
  '''
  def openProjectionWindow(self):
    self.projectionWidget = ProjectionWidget(self.app) 
    self.projectionWidget.show()


  def createAnalysisTable(self):
    self.categoryAnalysisTable.setRowCount(0)
    categories = self.app.getCategoryNamesList()
    for c in categories:
      if c != "Unhandled":
        row = self.categoryAnalysisTable.rowCount()
        self.categoryAnalysisTable.insertRow(row)
        self.categoryAnalysisTable.setItem(row, 0, QtWidgets.QTableWidgetItem(c))
        self.categoryAnalysisTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.app.getAmountAllottedByCategory(c))))
        self.categoryAnalysisTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.app.getAmountSpentByCategory(c))))
        self.categoryAnalysisTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.app.getAmountPlannedByCategory(c))))
        self.categoryAnalysisTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(self.app.getDeltaByCategory(c))))
        if row != 0:
          self.flagCategory(c)
        self.updateSpendingLabels()

    header = self.categoryAnalysisTable.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)


  def addNewRowToAnalysis(self, c):
    row = self.categoryAnalysisTable.rowCount()
    self.categoryAnalysisTable.setItem(row, 0, QtWidgets.QTableWidgetItem(c))
    self.categoryAnalysisTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.app.getAmountAllottedByCategory(c))))
    self.categoryAnalysisTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.app.getAmountSpentByCategory(c))))
    self.categoryAnalysisTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.app.getAmountPlannedByCategory(c))))
    self.categoryAnalysisTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(self.app.getDeltaByCategory(c))))
    self.flagCategory(row)



  def updateAnalysisTable(self, category):
    row = self.app.getCategoryNamesList().index(category) - 1
    self.categoryAnalysisTable.setItem(row, 0, QtWidgets.QTableWidgetItem(category))
    self.categoryAnalysisTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.app.getAmountAllottedByCategory(category))))
    self.categoryAnalysisTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.app.getAmountSpentByCategory(category))))
    self.categoryAnalysisTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.app.getAmountPlannedByCategory(category))))
    self.categoryAnalysisTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(self.app.getDeltaByCategory(category))))
    self.flagCategory(category)
    self.updateSpendingLabels()


  def fillAnalysisTable(self):
    categories = self.app.getCategoryNamesList()
    for c in categories:
      if c != "Unhandled": 

        row = self.categoryAnalysisTable.rowCount()
        self.categoryAnalysisTable.insertRow(row)

        self.categoryAnalysisTable.setItem(row, 0, QtWidgets.QTableWidgetItem(c))
        self.categoryAnalysisTable.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.app.getAmountAllottedByCategory(c))))
        self.categoryAnalysisTable.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.app.getAmountSpentByCategory(c))))
        self.categoryAnalysisTable.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.app.getAmountPlannedByCategory(c))))
        self.categoryAnalysisTable.setItem(row, 4, QtWidgets.QTableWidgetItem(str(self.app.getDeltaByCategory(c))))

    # resizing
    header = self.categoryAnalysisTable.horizontalHeader()
    header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)    
    header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
    header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)


  def flagCategory(self, category):
  
    row = self.app.getCategoryNamesList().index(category) - 1

    '''
    Turns QTableWidgetItem yellow to alert user that the sum their planned transactions 
    and completed Transactions for a given category exceed the allotted amount
    '''
    if self.app.getAmountAllottedByCategory(category) < self.app.getAmountSpentByCategory(category) + self.app.getAmountPlannedByCategory(category):
      self.categoryAnalysisTable.item(row, 0).setBackground(QtGui.QColor(240, 240, 5))

    '''
    Turns QTableWidgetItem red to alert user that the sum their 
    completed Transactions for a given category exceed the allotted amount
    '''
    if self.app.getAmountAllottedByCategory(category) < self.app.getAmountSpentByCategory(category):
      self.categoryAnalysisTable.item(row, 0).setBackground(QtGui.QColor(240, 5, 5))


  def createPlannedTransactionsWidget(self):
    self.tabWidget.clear()
    for category in self.app.getCategoryNamesList():
      if category != "Unhandled":
        tab = QTableWidget()
        self.tabWidget.addTab(tab, category)
        self.tabWidget.setCurrentWidget(tab)
        for i in range(3):
          self.tabWidget.currentWidget().insertColumn(i)
        self.fillTransactionWidget(category)


  def removePlannedTransaction(self):
    row = self.tabWidget.currentWidget().currentRow()
    index = self.tabWidget.currentIndex()
    category = self.app.getCategoryNamesList()[index + 1]
    name = self.tabWidget.currentWidget().item(row, 1).text()
    self.app.removePlannedTransaction(category, name)
    self.tabWidget.currentWidget().removeRow(row)
    self.app.saveData()


  def savePlannedTransaction(self):
    transaction = TransactionData()
    transaction.name = self.namePlannedT.text()
    transaction.category = self.categoryComboBox.currentText()
    # Validate amount by user input
    try:
      transaction.amount = float(self.amountPlannedT.text())
    except ValueError:
      invalidEntries += 1
      self.amountPlannedT.setText("")
      self.amountPlannedT.setPlaceholderText("Enter a float or an integer")

    if self.recurringBtn.isChecked():
      transaction.recurring = True
      transaction.rateOfRecurrence = self.getToggledFrequency()[1]
    else:
      transaction.recurring = False
        
    transaction.date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
    if self.checkingRadioBtn.isChecked():
      transaction.paymentMethod = 'Checking'
      transaction.paymentMethod
    else:
      transaction.paymentMethod = 'Credit'

    if invalidEntries == 0:

      self.app.createPlannedTransaction(transaction)
      self.createPlannedTransactionsWidget()
      self.app.saveData()


  def getToggledFrequency(self):
    if self.recurringBtn.isChecked():
      return True, self.recurrenceComboBox.currentText()
    return False


  def updateCategoryBox(self):
    self.categoryComboBox.clear()
    categoryNamesList = self.app.getCategoryNamesList()
    for c in categoryNamesList:
      if c != "Unhandled":
        self.categoryComboBox.addItem(c)


  def updateSpendingLabels(self):
    categories = self.app.getCategoryNamesList()
    totalSpent = 0
    totalAllotted = 0
    for c in categories:
      if c != "Unhandled":
        totalSpent += self.app.getAmountSpentByCategory(c)
        totalAllotted += self.app.getAmountAllottedByCategory(c)
    pctSpent = round(totalSpent / totalAllotted, 1) * 100
    self.amountSpentLabel.setText("$" + str(round(totalSpent, 2)))
    self.percentageSpentLabel.setText(str(pctSpent) + "%")

    if pctSpent <= 65:
      self.percentageSpentLabel.setStyleSheet("color: green;")
    elif 65 < pctSpent < 90:
      self.percentageSpentLabel.setStyleSheet("color: rgb(255, 200, 0);")
    else:
      self.percentageSpentLabel.setStyleSheet("color: red;")


 
  '''

  Categorize Transactions Funcs - uses the DragAndDropTableWidget Object to categorize 
  transaction objects into user-defined categories which are then used for analysis
 
  '''


  def uncategorizeCompletedTransaction(self):
    row = self.categoryWidget.currentWidget().currentRow()

    if type(self.categoryWidget.currentWidget().item(row, 0)) == QTableWidgetItem:
      date = self.categoryWidget.currentWidget().item(row, 1).text()
      referenceNumber = int(self.categoryWidget.currentWidget().item(row, 0).text())
      location = self.categoryWidget.currentWidget().item(row, 2).text()
      amount = self.categoryWidget.currentWidget().item(row, 3).text()
      c = self.app.getCategoryNamesList()[self.categoryWidget.currentIndex() + 1]
      self.app.unregisterCompletedTransaction(c, referenceNumber)
      self.app.registerCompletedTransaction("Unhandled", referenceNumber)
      self.app.diagnosticDbg()
      self.app.saveData()
      self.returnTransactionToUnhandled(referenceNumber, date, location, amount)
      self.categoryWidget.currentWidget().removeRow(row)
      self.updateCategorySummary(c)


  def returnTransactionToUnhandled(self, referenceNumber, date, location, amount):
    row = self.tableWidget.rowCount()
    self.tableWidget.insertRow(row)
    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(referenceNumber)))
    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(date))
    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(location))
    self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(amount))


  def fillTransactionWidget(self, category):
    plannedTransactions = self.app.getPlannedTransactions(category)
    if plannedTransactions != None:
      for t in plannedTransactions:
        rowPos = self.tabWidget.currentWidget().rowCount()          
        self.tabWidget.currentWidget().insertRow(rowPos)
        self.tabWidget.currentWidget().setItem(rowPos, 0, QtWidgets.QTableWidgetItem(str(t.date)))
        self.tabWidget.currentWidget().setItem(rowPos, 1, QtWidgets.QTableWidgetItem(t.name))
        self.tabWidget.currentWidget().setItem(rowPos, 2, QtWidgets.QTableWidgetItem(str(t.amount)))

      header = self.tabWidget.currentWidget().horizontalHeader()
      header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)    
      header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
      header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)


  def getToggledFrequency(self):
    if self.recurringBtn.isChecked():
      return True, self.recurrenceComboBox.currentText()
    return False


  def createPlannedTransactionsWidget(self):
    self.tabWidget.clear()
    for category in self.app.getCategoryNamesList():
      if category != "Unhandled":
        tab = QTableWidget()
        self.tabWidget.addTab(tab, category)
        self.tabWidget.setCurrentWidget(tab)
        for i in range(3):
          self.tabWidget.currentWidget().insertColumn(i)
        self.fillTransactionWidget(category)



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
    self.updateCategoryBox()
    self.createAnalysisTable()


  def createCategoryWidget(self):
    self.categoryWidget.clear()
    for category in self.app.getCategoryNamesList():
      if category != "Unhandled":
        tab = DragDropTableWidget(self.app, self)
        tab.setAcceptDrops(True)
        self.categoryWidget.addTab(tab, category)
        self.categoryWidget.setCurrentWidget(tab)
        for i in range(4):
          self.categoryWidget.currentWidget().insertColumn(i)

        self.fillCategoryWidget(category)

        header = self.categoryWidget.currentWidget().horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)    
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)

  def moveRowToDropDestination(self, referenceNumber, date, location, amount, category):
    rowPos = self.categoryWidget.currentWidget().rowCount()
    self.categoryWidget.currentWidget().insertRow(rowPos)
    self.categoryWidget.currentWidget().setItem(rowPos, 0, QtWidgets.QTableWidgetItem(str(referenceNumber)))
    self.categoryWidget.currentWidget().setItem(rowPos, 1, QtWidgets.QTableWidgetItem(date))
    self.categoryWidget.currentWidget().setItem(rowPos, 2, QtWidgets.QTableWidgetItem(location))
    self.categoryWidget.currentWidget().setItem(rowPos, 3, QtWidgets.QTableWidgetItem(amount))
    self.updateCategorySummary(category)


  def showCategorySummary(self):
    index = self.categoryWidget.currentIndex()
    category = self.app.getCategoryNamesList()[index + 1]
    self.categorySpent.setText(str(self.app.getAmountSpentByCategory(category)))
    self.categoryAllotted.setText(str(self.app.getAmountAllottedByCategory(category)))


  def updateCategorySummary(self, category):
    self.categoryAllotted.setText(str(self.app.getAmountAllottedByCategory(category)))
    self.categorySpent.setText(str(self.app.getAmountSpentByCategory(category)))

      
  def fillCategoryWidget(self, category):
    for t in self.app.getCompletedTransactionsByCategory(category).values():
      rowPos = self.categoryWidget.currentWidget().rowCount()
      self.categoryWidget.currentWidget().insertRow(rowPos)
      self.categoryWidget.currentWidget().setItem(rowPos, 0, QtWidgets.QTableWidgetItem(str(t.referenceNumber)))
      self.categoryWidget.currentWidget().setItem(rowPos, 1, QtWidgets.QTableWidgetItem(t.date))
      self.categoryWidget.currentWidget().setItem(rowPos, 2, QtWidgets.QTableWidgetItem(t.location))
      self.categoryWidget.currentWidget().setItem(rowPos, 3, QtWidgets.QTableWidgetItem(t.amount))


  def printUnhandledTransactions(self):
    for t in self.app.getUnhandledTransactions().values():
      rowPos = self.tableWidget.rowCount()
      self.tableWidget.insertRow(rowPos)
      self.tableWidget.setItem(rowPos, 0, QtWidgets.QTableWidgetItem(str(t.referenceNumber)))
      self.tableWidget.setItem(rowPos, 1, QtWidgets.QTableWidgetItem(t.date))
      self.tableWidget.setItem(rowPos, 2, QtWidgets.QTableWidgetItem(t.location))
      self.tableWidget.setItem(rowPos, 3, QtWidgets.QTableWidgetItem(t.amount))
      # resizing the columns
      header = self.tableWidget.horizontalHeader()       
      header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
      header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
      header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
      header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)


  def deleteSelectedCategory(self):
    self.tab = self.categoryWidget.currentIndex() + 1        
    self.index = self.app.getCategoryNamesList()[self.tab]
    self.app.deleteCategory(self.index)
    self.updateCategoryWidget()
    self.createAnalysisTable()
    

 
  '''

  Open Dialog Window Funcs - Opens all popup windows for analytics and user input
  
  '''

  def openPlottingWindow(self):
    plotWindow = PlottingWindow(self.app)
    plotWindow.show()


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


  '''

  Other Funcs - Miscellaneous Supporting Funcs

  '''


  def fileOpen(self):
    self.filePath, _ = QtWidgets.QFileDialog.getOpenFileName()
    self.app.sortCompletedTransactions(self.filePath)
    self.printUnhandledTransactions()
    self.createCategoryWidget()
    self.createAnalysisTable()


      



      

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

