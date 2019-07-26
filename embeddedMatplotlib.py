import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QGridLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

import random

from Application import Application

import numpy as np

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
        self.plotPieBtn = QPushButton('Pie Chart')
        self.plotPieBtn.clicked.connect(self.plotPie)

        self.plotBarBtn = QPushButton('Bar Graph')
        self.plotBarBtn.clicked.connect(self.plotBar)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        btnLayout = QGridLayout()
        layout.addLayout(btnLayout)

        btnLayout.addWidget(self.plotPieBtn, 0, 0)
        btnLayout.addWidget(self.plotBarBtn, 0, 1)

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

    def plotBar(self):
        # data to plot
        cats = self.app.getCategoryNamesList()[1:]
        n_groups = len(cats)
        
        amountSpent = [self.app.getAmountSpentByCategory(c) for c in cats]
        amountAllotted = [self.app.getAmountAllottedByCategory(c) for c in cats]

        self.figure.clear()
        # create plot
        self.ax = self.figure.add_subplot(111)

        self.ax.clear()

        index = np.arange(n_groups)
        bar_width = 0.35
        opacity = 0.8

        rects1 = plt.bar(index, amountAllotted, bar_width,
        alpha=opacity,
        color='b',
        label='Allotted')

        rects2 = plt.bar(index + bar_width, amountSpent, bar_width,
        alpha=opacity,
        color='g',
        label='Spent')

        plt.xlabel('Spending')
        plt.ylabel('Category')
        plt.title('Allotment and Spending')
        plt.xticks(index + bar_width, [x for x in self.app.getCategoryNamesList()[1:]])
        plt.legend()

        plt.tight_layout()
        #plt.show()

        self.canvas.draw()


        

if __name__ == '__main__':
    app = QApplication(sys.argv)

    plotWindow = Window()
    plotWindow.show()

    sys.exit(app.exec_())