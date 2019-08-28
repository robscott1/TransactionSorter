import pandas as pd
from datetime import date
from DataPrepSupport import *

class PandasAgent():

  def __init__(self, df=None, plannedDf=None):
    self.completedDf = None
    self.userData = None
    self.dataProcessor = DataProcessor()

  def getUserData(self, data):
    self.userData = data
    self.userData.nextPayDate = self.userData.nextPayDate.replace('/', '-')
    self.userData.nextCreditCardPaymentDate = self.userData.nextCreditCardPaymentDate.replace('/', '-')

  def getCompletedTransactionsDataframe(self, fileName):
    self.completedDf = pd.read_csv(fileName, sep=',', header = None)

  def getProjectionData(self, allottedAmt, plannedT):
    return self.dataProcessor.getProjectionData(allottedAmt, self.userData, plannedT)

  def getTimeSeriesData(self):

    # Reverse the order to get df chronologically correct
    df1 = self.completedDf[::-1]
    # Getting the items to plot
    trans = df1.loc[:,'date':'amount']

    previousDate = trans.date[len(trans) - 1]
    spendingByDay = []
    listOfDates = []
    dailyTotal = 0
    for index, row in trans.iterrows():
        
        if previousDate == row.date:
            dailyTotal += row.amount
            previousDate = row.date
        
        else:
            spendingByDay.append(abs(round(dailyTotal, 0)))
            ts = pd.to_datetime(row.date)
            dailyTotal += row.amount
            date = row.date.split('/')
            date.pop(-1)
            date = '/'.join(date)
            listOfDates.append(date)
            previousDate = row.date


    return spendingByDay, listOfDates

  def isMonthStart(self, date):
    date = str(date)
    date = date.split('-')
    day = date[2].split()
    return day[0] == '01'

#if __name__ == "__main__":
  #print(pd.to_datetime(date.today()))

