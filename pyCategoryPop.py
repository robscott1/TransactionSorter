# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categoryPop.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from APIData import CategoryData



class Ui_createDialog(object):
    def setupUi(self, Dialog, App):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.newCategoryName = QtWidgets.QLineEdit(Dialog)
        self.newCategoryName.setGeometry(QtCore.QRect(40, 80, 141, 21))
        self.newCategoryName.setText("")
        self.newCategoryName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.newCategoryName.setObjectName("newCategoryName")
        self.newCategoryAllotment = QtWidgets.QLineEdit(Dialog)
        self.newCategoryAllotment.setGeometry(QtCore.QRect(40, 120, 141, 21))
        self.newCategoryAllotment.setText("")
        self.newCategoryAllotment.setObjectName("newCategoryAllotment")
        self.keywordsLabel = QtWidgets.QLabel(Dialog)
        self.keywordsLabel.setGeometry(QtCore.QRect(260, 20, 91, 20))
        self.keywordsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.keywordsLabel.setObjectName("keywordsLabel")
        self.newCategoryKeywords = QtWidgets.QListWidget(Dialog)
        self.newCategoryKeywords.setGeometry(QtCore.QRect(230, 40, 151, 191))
        self.newCategoryKeywords.setObjectName("newCategoryKeywords")
        self.saveCategoryInfo = QtWidgets.QPushButton(Dialog)
        self.saveCategoryInfo.setGeometry(QtCore.QRect(250, 250, 113, 32))
        self.saveCategoryInfo.setObjectName("saveCategoryInfo")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 160, 207, 33))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newCategoryKeywordField = QtWidgets.QLineEdit(self.widget)
        self.newCategoryKeywordField.setText("")
        self.newCategoryKeywordField.setObjectName("newCategoryKeywordField")
        self.horizontalLayout.addWidget(self.newCategoryKeywordField)
        self.addNewCategoryKeyword = QtWidgets.QPushButton(self.widget)
        self.addNewCategoryKeyword.setObjectName("addNewCategoryKeyword")
        self.horizontalLayout.addWidget(self.addNewCategoryKeyword)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

##############################################################################################
                    # end of auto-generated code
##############################################################################################
        # inlcude app argument in setupUi func
        self.app = App

##############################################################################################
                    # begin auto-generated code
##############################################################################################

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.newCategoryName.setPlaceholderText(_translate("Dialog", "Category Name"))
        self.newCategoryAllotment.setPlaceholderText(_translate("Dialog", "Monthly Allotment"))
        self.keywordsLabel.setText(_translate("Dialog", "Key Words"))
        self.saveCategoryInfo.setText(_translate("Dialog", "Save"))
        self.newCategoryKeywordField.setPlaceholderText(_translate("Dialog", "Add Keyword"))
        self.addNewCategoryKeyword.setText(_translate("Dialog", "Add"))

##############################################################################################
                    # end of auto-generated code
##############################################################################################
    

        self.keywordList = []
        self.addNewCategoryKeyword.clicked.connect(self.appendKeyword)
        self.saveCategoryInfo.clicked.connect(self.createNewCategory)

    def appendKeyword(self):
        '''
        Simultaneously adds keyword to idKeywords list for respective category
        and displays new words in list widget in pop up window
        '''
        self.newCategoryKeywords.addItem(str(self.newCategoryKeywordField.text()))
        self.keywordList.append(self.newCategoryKeywordField.text())
        self.newCategoryKeywordField.setText("")

    def createNewCategory(self):
        category = CategoryData()
        category.name = str(self.newCategoryName.text())
        category.monthlyAllotment = float(self.newCategoryAllotment.text())
        category.idKeywords = self.keywordList
        self.newCategoryName.setText("")
        self.newCategoryAllotment.setText("")
        self.newCategoryKeywords.clear()
        self.app.createNewCategory(category)

##############################################################################################
                    # begin auto-generated code
##############################################################################################




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
