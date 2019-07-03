# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editCategoryPop.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from APIData import CategoryData


class Ui_Dialog(object):
    def setupUi(self, Dialog, App):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 141, 16))
        self.label.setObjectName("label")
        self.newCategoryName = QtWidgets.QLineEdit(Dialog)
        self.newCategoryName.setGeometry(QtCore.QRect(40, 70, 141, 21))
        self.newCategoryName.setText("")
        self.newCategoryName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.newCategoryName.setObjectName("newCategoryName")
        self.newCategoryAllotment = QtWidgets.QLineEdit(Dialog)
        self.newCategoryAllotment.setGeometry(QtCore.QRect(40, 110, 141, 21))
        self.newCategoryAllotment.setText("")
        self.newCategoryAllotment.setObjectName("newCategoryAllotment")
        self.keywordsLabel = QtWidgets.QLabel(Dialog)
        self.keywordsLabel.setGeometry(QtCore.QRect(250, 20, 91, 20))
        self.keywordsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.keywordsLabel.setObjectName("keywordsLabel")
        self.newCategoryKeywords = QtWidgets.QListWidget(Dialog)
        self.newCategoryKeywords.setGeometry(QtCore.QRect(220, 40, 151, 191))
        self.newCategoryKeywords.setObjectName("newCategoryKeywords")
        self.saveCategoryInfo = QtWidgets.QPushButton(Dialog)
        self.saveCategoryInfo.setGeometry(QtCore.QRect(240, 250, 113, 32))
        self.saveCategoryInfo.setObjectName("saveCategoryInfo")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 160, 207, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newCategoryKeywordField = QtWidgets.QLineEdit(self.layoutWidget)
        self.newCategoryKeywordField.setText("")
        self.newCategoryKeywordField.setObjectName("newCategoryKeywordField")
        self.horizontalLayout.addWidget(self.newCategoryKeywordField)
        self.addNewCategoryKeyword = QtWidgets.QPushButton(self.layoutWidget)
        self.addNewCategoryKeyword.setObjectName("addNewCategoryKeyword")
        self.horizontalLayout.addWidget(self.addNewCategoryKeyword)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 190, 71, 32))
        self.pushButton.setObjectName("pushButton")


        self.app = App

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Edit Existing Category"))
        self.newCategoryName.setPlaceholderText(_translate("Dialog", "Edit Name"))
        self.newCategoryAllotment.setPlaceholderText(_translate("Dialog", "Edit Allotment"))
        self.keywordsLabel.setText(_translate("Dialog", "Key Words"))
        self.saveCategoryInfo.setText(_translate("Dialog", "Save"))
        self.newCategoryKeywordField.setPlaceholderText(_translate("Dialog", "Add Keyword"))
        self.addNewCategoryKeyword.setText(_translate("Dialog", "Add"))
        self.pushButton.setText(_translate("Dialog", "Del"))


##############################################################################################
                    # end of auto-generated code
##############################################################################################
        
        self.addNewCategoryKeyword.clicked.connect(self.appendKeyword)
        self.saveCategoryInfo.clicked.connect(self.updateCategoryInfo)
        self.app.diagnosticDbg()

    def getExistingKeywords(self):
        self.keywordList = self.app.getKeywordsByCategory(self.newCategoryName.text())

    def appendKeyword(self):
        '''
        Simultaneously adds keyword to idKeywords list for respective category
        and displays new words in list widget in pop up window
        '''
        self.keywordsList = self.getExistingKeywords()
        self.newCategoryKeywords.addItem(str(self.newCategoryKeywordField.text()))
        self.keywordList.append(self.newCategoryKeywordField.text())
        self.newCategoryKeywordField.setText("")

    def updateCategoryInfo(self):
        editedCategory = CategoryData()
        editedCategory.name = str(self.newCategoryName.text())
        editedCategory.monthlyAllotment = float(self.newCategoryAllotment.text())
        editedCategory.idKeywords = []
        keywordList = [self.newCategoryKeywords.item(i).text() for i in range(self.newCategoryKeywords.count())]
        for item in keywordList:
            editedCategory.idKeywords.append(item)
        self.app.updateCategoryData(editedCategory)
        self.app.saveData()
        self.app.diagnosticDbg()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    editUi = Ui_Dialog()
    editUi.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
