# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editCategoryPop.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.editCatLabel = QtWidgets.QLabel(Form)
        self.editCatLabel.setGeometry(QtCore.QRect(50, 40, 91, 16))
        self.editCatLabel.setObjectName("editCatLabel")
        self.editCatName = QtWidgets.QLineEdit(Form)
        self.editCatName.setGeometry(QtCore.QRect(20, 70, 141, 21))
        self.editCatName.setObjectName("editCatName")
        self.editCatAllotment = QtWidgets.QLineEdit(Form)
        self.editCatAllotment.setGeometry(QtCore.QRect(20, 120, 141, 21))
        self.editCatAllotment.setObjectName("editCatAllotment")
        self.editCatAddKeyword = QtWidgets.QPushButton(Form)
        self.editCatAddKeyword.setGeometry(QtCore.QRect(30, 210, 113, 32))
        self.editCatAddKeyword.setObjectName("editCatAddKeyword")
        self.editCatKeywordField = QtWidgets.QLineEdit(Form)
        self.editCatKeywordField.setGeometry(QtCore.QRect(22, 180, 141, 21))
        self.editCatKeywordField.setObjectName("editCatKeywordField")
        self.editCatKeywordListWidget = QtWidgets.QListWidget(Form)
        self.editCatKeywordListWidget.setGeometry(QtCore.QRect(180, 50, 111, 201))
        self.editCatKeywordListWidget.setObjectName("editCatKeywordListWidget")
        self.editCatWordLabel = QtWidgets.QLabel(Form)
        self.editCatWordLabel.setGeometry(QtCore.QRect(210, 30, 71, 16))
        self.editCatWordLabel.setObjectName("editCatWordLabel")
        self.editCatSaveInfo = QtWidgets.QPushButton(Form)
        self.editCatSaveInfo.setGeometry(QtCore.QRect(270, 260, 101, 31))
        self.editCatSaveInfo.setObjectName("editCatSaveInfo")
        self.editCatDeleteKeyword = QtWidgets.QPushButton(Form)
        self.editCatDeleteKeyword.setGeometry(QtCore.QRect(310, 50, 71, 31))
        self.editCatDeleteKeyword.setObjectName("editCatDeleteKeyword")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.editCatLabel.setText(_translate("Form", "Edit Category"))
        self.editCatAddKeyword.setText(_translate("Form", "Add Keyword"))
        self.editCatKeywordField.setPlaceholderText(_translate("Form", "Add Keyword"))
        self.editCatWordLabel.setText(_translate("Form", "Keywords"))
        self.editCatSaveInfo.setText(_translate("Form", "Save"))
        self.editCatDeleteKeyword.setText(_translate("Form", "Delete"))

##############################################################################################
                    # end of auto-generated code
##############################################################################################








if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
