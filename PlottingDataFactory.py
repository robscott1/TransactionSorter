import pandas as pd
from datetime import date
from DataPrepSupport import *
from APIData import TransactionData

class PlottingDataFactory():
  
  '''
  This module utilizes pandas to store all data in DataFrames.
  The DataFrame allows for quick and specific access to retrieve
  data that the user needs. Right now, this class procures
  data in array form to be plotted in the GUI. The arrays are
  ready to be used in matplotlib once it leaves this class.

  '''

  def __init__(self, df=None, plannedDf=None):
    self.completedDf = pd.DataFrame(columns=['Date', 'Amount'])
    self.userData =  None
    self.freqKey = {'annually': ['A', 1], 'monthly': ['MS', 12], 'bi-weekly': ['2W-FRI', 26] , 'weekly': ['W', 52]}
    self.plannedDf = pd.DataFrame(columns=['Date', 'Amount', 'Recurrence','Priority', 'Method', 'Name'])

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

  def getCompletedTransactionsDataframe(self, completedT):
    '''
    Reads imported CSV file into a Pandas Dataframe. Pandas will be used
    for all analysis and projection purposes

    See DataPrepSupport.py to see analysis functions 
    '''
    for t in completedT:
      self.completedDf = self.completedDf.append({'Date': t.date, 'Amount': t.amount}, ignore_index=True)


  def getUserDataDefinedTransactions(self, allottedAmt):
    '''
    Creates the recurring transactions defined in the user-defined "setup"
    page of the GUI. Instantiates the recurring credit card payment and 
    income based on specified frequency. Those transactions are then added
    to the projection dataframe with recurring dates.
    
    @allottedAmt: total of all allotted amounts for user-created categories.
    Estimates how much will be paid for credit card bill each month for 
    projection purposes

    @userData: user-defined financial standing. Used for cash projection
    See UserData object for details.

    '''
    ccPayment = TransactionData()
    ccPayment.name = "creditCardPayment"
    ccPayment.date = self.createDateList(self.userData.nextCreditCardPaymentDate, 'monthly')
    ccPayment.amount = allottedAmt * -1
    ccPayment.priority = 1
    ccPayment.rateOfRecurrence = 'monthly'

    
    self.addTransactionToDataframe(ccPayment).sort_values(by='Date')


    income = TransactionData()
    income.name = "income"
    income.date = self.createDateList(self.userData.nextPayDate, self.userData.incomeFrequency)
    income.amount = self.userData.incomeAmount
    income.priority = 1
    income.rateOfRecurrence = self.userData.incomeFrequency
        
    self.plannedDf = self.addTransactionToDataframe(income).sort_values(by='Date')


  def getDateOffset(self, startDay):
    '''
    Finds the number day of the month to create the dateOffset when date_ranges
    are made. date_ranges default to the start of the month, so the dateOffset gives
    the correct day that recurring transactions occur on

    @startDay: timestamp used to be the first date in a date_range for getProjectionData

    @returns: number of days that the date_range will offset from 
    month start for monthly transactions
    '''
    startDay = str(startDay)
    startDay = startDay.split()[0]
    startDay = startDay.split('-')
    day = startDay[2]
    return int(day)

  def createDateList(self, startDay, rateOfRecurrence):
    '''
    Creates list of dates that expenditures will occur for each individual transaction
    (recurring or singular event)

    @startDay: for recurring transactions, this is the first charge. For singlular transactions,
    it is just that date the charge will be made on

    @rateOfRecurrence: the rate of recurrence specified in the GUI when planned
    transaction is made. That rate of recurrence links to a dictionary key-value
    that points to the Pandas syntax for frequency of the date_range

    @returns: list of dates that transactions occur on for cash projection analysis

    '''
    if rateOfRecurrence == None:
      return list(startDay)
    
    if rateOfRecurrence == 'monthly':
      return list((pd.date_range(startDay, periods=self.freqKey[rateOfRecurrence][1],
                   freq=self.freqKey[rateOfRecurrence][0]) + pd.DateOffset(days=self.getDateOffset(startDay) - 1)))
    
    if rateOfRecurrence == 'bi-weekly':
      return list(pd.date_range(startDay, periods=self.freqKey[rateOfRecurrence][1],
                   freq=self.freqKey[rateOfRecurrence][0]))

  def extractPlannedTransactionData(self, plannedT):
    '''
    To begin the cash projection analysis, all plannedTransactions are collected and 
    arranged in a dataframe with important transaction information. These are all ordered 
    by date, and prepared to be extracted for plotting purposes.

    @plannedT: list of plannedTransaction objects that are extracted and ordered
    in order to project checking account balance in the future based on other
    user-specified data

    '''
    for item in plannedT:
      if item.paymentMethod == 'Checking':
        item.date = self.createDateList(item.date, item.rateOfRecurrence)

      self.plannedDf = self.addTransactionToDataframe(item).sort_values(by='Date')

  def addTransactionToDataframe(self, transaction):
    for item in transaction.date:
      self.plannedDf = self.plannedDf.append({'Date': item, 'Amount': transaction.amount,
                                              'Recurrence': transaction.rateOfRecurrence,
                                              'Priority': transaction.priority,
                                              'Method': transaction.paymentMethod, 'Name':transaction.name}, ignore_index=True)

    return self.plannedDf


  def getProjectionData(self, allottedAmt, plannedTransactions):
    '''
    Prepares lists of dates and charges associated with any plannedTransactions,
    monthly income, and credit card payments for future projection

    @allottedAmt: total cash allotted monthly for all user-defined categories.
    Used to predict how much user will by paying for their montly credit
    card bill

    @userData: User-defined data oject that describes the user's
    current financial standing

    @plannedTransactions: list of all planned transactions that will be included
    in the plannedDf

    @returns: tuple with a list any dates that have transactions occur, and a list 
    of the working balance of the user's checking acount over time
    '''

    self.extractPlannedTransactionData(plannedTransactions)


    chkBal = self.userData.checkingAccountBal
    incomeAmt = self.userData.incomeAmount
    incomeFreq = self.userData.incomeFrequency
    self.userData.nextPayDate = pd.to_datetime(self.userData.nextPayDate)
    self.userData.nextCreditCardPaymentDate = pd.to_datetime(self.userData.nextCreditCardPaymentDate)
    self.getUserDataDefinedTransactions(allottedAmt)

    self.plannedDf.sort_values(by='Date')
    
    datesOfExpense = []
    runningBalance = []

    runningBalance.append(chkBal)

    today = datetime.today().strftime('%Y-%m-%d')
    datesOfExpense.append(today)

    for index, row in self.plannedDf.iterrows():

      date = str(row.Date).split()[0]

      #before transaction
      datesOfExpense.append(str(date))
      runningBalance.append(chkBal)

      #after transaction
      chkBal += row.Amount
      datesOfExpense.append(str(date))
      runningBalance.append(chkBal)

    return datesOfExpense, runningBalance


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
    self.completedDf = self.completedDf[::-1]

    # Define variables that will be recorded as the function
    # iterates through the completedDf
    previousDate = self.completedDf.Date[len(self.completedDf) - 1]
    spendingByDay = []
    listOfDates = []
    dailyTotal = 0

    for index, row in self.completedDf.iterrows():

      # Because several charges can happen in one day, the function will
      # total up all charges on the same day before appending it to
      # spendingByDay accurately tracking spending per day
      if previousDate == str(row.Date):
        dailyTotal += float(row.Amount)
        previousDate = str(row.Date)
      
      else:
        spendingByDay.append(abs(round(dailyTotal, 0)))
        ts = pd.to_datetime(row.Date)
        dailyTotal += float(row.Amount)
        
        # Remove the year from the timestamp for visual purposes in the plottingWindow
        date = row.Date.split('/')
        date.pop(-1)
        date = '/'.join(date)
        listOfDates.append(date)
        previousDate = row.Date


    return spendingByDay, listOfDates

