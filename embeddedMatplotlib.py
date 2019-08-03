import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QHBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import datetime

import random

from Application import Application

import numpy as np

import pandas as pd

class plottingWindow(QDialog):
    def __init__(self, App, parent=None):
        super(plottingWindow, self).__init__(parent)

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

        self.plotTimeSeriesBtn = QPushButton('Time Series')
        self.plotTimeSeriesBtn.clicked.connect(self.plotTimeSeries)

        # set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        btnLayout = QHBoxLayout()
        layout.addLayout(btnLayout)

        btnLayout.addWidget(self.plotPieBtn)
        btnLayout.addWidget(self.plotBarBtn)
        btnLayout.addWidget(self.plotTimeSeriesBtn)

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

    def plotTimeSeries(self):

        self.figure.clear()

        self.ax = self.figure.add_subplot(111)

        self.ax.clear()

        transactions = (r'C:\Users\rober\Downloads\July23Statement.csv')
        df = pd.read_csv(transactions, sep=',', header = None)
        df.columns = ['date', 'amount', 'bye', 'felicia', 'location']
        del df['bye']
        del df['felicia']

        #reverse the order to get df chronologically correct
        df1 = df[::-1]
        # Getting the items to plot
        trans = df1.loc[:,'date':'amount']

        previousDate = trans.date[len(trans) - 1]
        spendingByDay = []
        dailyTotal = 0
        for index, row in trans.iterrows():
            if previousDate == row.date:
                dailyTotal += row.amount
                previousDate = row.date
            else:
                spendingByDay.append(abs(round(dailyTotal, 0)))
                ts = pd.to_datetime(row.date)
                dailyTotal += row.amount
                previousDate = row.date

        # Check
        print(spendingByDay)

        listOfDates = []
        #listOfDates.append(trans.date[len(trans) - 1])
        previousDate = trans.date[len(trans) - 1]
        print(previousDate)
        for index, row in trans.iterrows():
            print(previousDate != row.date)      
            if previousDate != row.date:
                date = row.date.split('/')
                date.pop(-1)
                date = '/'.join(date)
                listOfDates.append(date)
                previousDate = row.date

        # Check
        print(listOfDates)
        for date in listOfDates:
            date = date.split('/')
            date.pop(-1)
            date = '/'.join(date)

        plt.xlabel('Time')
        plt.ylabel('Total Spending')
        plt.title('Charges Over Time')
        plt.tight_layout()
        # Plot
        plt.plot(listOfDates, spendingByDay)
        plt.xticks(rotation=60)
        
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    plotWindow = plottingWindow()
    plotWindow.show()

    sys.exit(app.exec_())