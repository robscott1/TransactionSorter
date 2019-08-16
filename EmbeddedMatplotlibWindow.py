import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import datetime

import random

from Application import Application

import numpy as np

import pandas as pd

class PlottingWindow(QDialog):
    def __init__(self, App, parent=None):
        super(PlottingWindow, self).__init__(parent)

        self.app = App

        # A figure instance to plot on
        self.figure = plt.figure()

        # This is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Plot pie chart button
        self.plotPieBtn = QPushButton('Pie Chart')
        self.plotPieBtn.clicked.connect(self.plotPie)

        # Plot bar graph button
        self.plotBarBtn = QPushButton('Bar Graph')
        self.plotBarBtn.clicked.connect(self.plotBar)

        # Plot time series button
        self.plotTimeSeriesBtn = QPushButton('Time Series')
        self.plotTimeSeriesBtn.clicked.connect(self.plotTimeSeries)

        # Set the plottingWindow layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        # Within the layout, create horizontal
        # layout for various plotting functionality
        btnLayout = QHBoxLayout()
        layout.addLayout(btnLayout)

        btnLayout.addWidget(self.plotPieBtn)
        btnLayout.addWidget(self.plotBarBtn)
        btnLayout.addWidget(self.plotTimeSeriesBtn)

        self.setLayout(layout)

    def plotPie(self):
        # Get data to plot
        cats = self.app.getCategoryNamesList()[1:]
        data = [self.app.getAmountSpentByCategory(c) for c in cats]
        
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        
        self.ax.pie(data, labels=cats)
        self.ax.set_title("Spending by Category")
        self.canvas.draw()

    def plotBar(self):
        # Get data to plot
        cats = self.app.getCategoryNamesList()[1:]
        n_groups = len(cats)
        amountSpent = [self.app.getAmountSpentByCategory(c) for c in cats]
        amountAllotted = [self.app.getAmountAllottedByCategory(c) for c in cats]
        
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()\
        
        # Format preparation
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
        plt.xticks(rotation=40)
        plt.legend()

        plt.tight_layout()
        self.canvas.draw()

    def plotTimeSeries(self):
        # Get data to plot
        spendingByDay, listOfDates = self.app.getTimeSeriesData()
        
        # Prepare figure
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)
        self.ax.clear()
        plt.xlabel('Time')
        plt.ylabel('Total Spending')
        plt.title('Charges Over Time')
        plt.tight_layout()
        plt.xticks(rotation=60)
        
        plt.plot(listOfDates, spendingByDay)
        self.canvas.draw()

class ProjectionWidget(QDialog):

    def __init__(self, App, parent=None):
        super(ProjectionWidget, self).__init__(parent)


        self.app = App

        # A figure instance to plot on
        self.figure = plt.figure()

        # This is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.plot3MonthProjectionBtn = QPushButton('3 Month')
        self.plot3MonthProjectionBtn.clicked.connect(self.plot3Month)

        # Set the plottingWindow layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)

        # Within the layout, create horizontal
        # layout for various plotting functionality
        btnLayout = QHBoxLayout()
        layout.addLayout(btnLayout)

        btnLayout.addWidget(self.plot3MonthProjectionBtn)

        self.setLayout(layout)


    def plot3Month(self):
        print("well den..")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    plotWindow = PlottingWindow()
    plotWindow.show()

    sys.exit(app.exec_())