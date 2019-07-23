import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

from Application import Application

class Window(QDialog):
    def __init__(self, App, parent=None):
        super(Window, self).__init__(parent)

        self.app = App

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to `plot` method
        self.button = QPushButton('Plot')
        self.button.clicked.connect(self.plotPie)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def plotPie(self):
        cats = self.app.getCategoryNamesList()[1:]
        data = [self.app.getAmountSpentByCategory(c) for c in cats]

        self.figure.clear()

        self.ax = self.figure.add_subplot(111)

        self.ax.clear()

        self.ax.pie(data, labels=cats)
        self.ax.set_title("Spending by Category")

        self.canvas.draw()


        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    plotWindow = Window()
    plotWindow.show()

    sys.exit(app.exec_())