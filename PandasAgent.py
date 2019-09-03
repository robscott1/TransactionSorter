import pandas as pd
from datetime import date
from DataPrepSupport import *

class PandasAgent():

  def __init__(self, df=None, plannedDf=None):
    self.completedDf = None
    self.userData = None
    self.dataProcessor = DataProcessor()

  def getUserData(self, data):
    '''
    Saves UserData object with user-defined financial standing while 
    swapping the slashes for apostrophes in order to keep all saved dates
    in the same format

    @data: UserData object that holds user-defined current financial standing
    Used for future cash projections

    '''
    self.userData = data
    self.userData.nextPayDate = self.userData.nextPayDate.replace('/', '-')
    self.userData.nextCreditCardPaymentDate = self.userData.nextCreditCardPaymentDate.replace('/', '-')

  def getCompletedTransactionsDataframe(self, fileName):
    '''
    Reads imported CSV file into a Pandas Dataframe. Pandas will be used
    for all analysis and projection purposes

    See DataPrepSupport.py to see analysis functions 
    '''
    self.completedDf = pd.read_csv(fileName, sep=',', header = None)

  def getProjectionData(self, allottedAmt, plannedT):
    '''
    Calls getProjectionData in DataProcessor to send projection data to ProjectionWindow

    @allottedAmt: total cash allotted for all existing categories, used to project
    credit card charges for each month in ProjectionWindow

    @plannedT: list of PlannedTransaction objects 
    '''
    return self.dataProcessor.getProjectionData(allottedAmt, self.userData, plannedT)

  def getTimeSeriesData(self):
    '''
    Prepares the lists of dates on which credit card transactions 
    took place, and the running total of charges for all
    transactions in the CSV file.

    Extracts all dates and amounts of charges from completedDf
    which is a member of the PandasAgent object

    @returns: 
    - SpendingByDay(list) a list of the runningBalance of
    credit card charges over a period of time
    - ListOfDates(list) a list of dates on which all transactions
    took place
    '''

    # Reverse the order to make the DataFrame chronologically correct
    df1 = self.completedDf[::-1]

    # Getting the items to plot
    trans = df1.loc[:,'date':'amount']

    # Define variables that will be recorded as the function
    # iterates through the completedDf
    previousDate = trans.date[len(trans) - 1]
    spendingByDay = []
    listOfDates = []
    dailyTotal = 0

    for index, row in trans.iterrows():
        
        # Because several charges can happen in one day, the function will
        # total up all charges on the same day before appending it to
        # spendingByDay accurately tracking spending per day
        if previousDate == row.date:
            dailyTotal += row.amount
            previousDate = row.date
        
        else:
            spendingByDay.append(abs(round(dailyTotal, 0)))
            ts = pd.to_datetime(row.date)
            dailyTotal += row.amount
            
            # Remove the year from the timestamp for visual purposes in the plottingWindow
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

