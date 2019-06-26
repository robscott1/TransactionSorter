

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_manualSortingWindow(object):
    def setupUi(self, manualSortingWindow):
        manualSortingWindow.setObjectName("manualSortingWindow")
        manualSortingWindow.resize(504, 359)
        self.label = QtWidgets.QLabel(manualSortingWindow)
        self.label.setGeometry(QtCore.QRect(90, 10, 151, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(manualSortingWindow)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 71, 20))
        self.label_2.setObjectName("label_2")
        self.tList = QtWidgets.QListWidget(manualSortingWindow)
        self.tList.setGeometry(QtCore.QRect(40, 40, 256, 192))
        self.tList.setObjectName("tList")

        self.retranslateUi(manualSortingWindow)
        QtCore.QMetaObject.connectSlotsByName(manualSortingWindow)

    def retranslateUi(self, manualSortingWindow):
        _translate = QtCore.QCoreApplication.translate
        manualSortingWindow.setWindowTitle(_translate("manualSortingWindow", "Form"))
        self.label.setText(_translate("manualSortingWindow", "Unhandled Transactions"))
        self.label_2.setText(_translate("manualSortingWindow", "Categories"))

##############################################################################################
                            # end of auto-generated code
##############################################################################################

    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manualSortingWindow = QtWidgets.QWidget()
    ui = Ui_manualSortingWindow()
    ui.setupUi(manualSortingWindow)
    manualSortingWindow.show()
    sys.exit(app.exec_())
