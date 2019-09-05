import pandas as pd
from datetime import datetime


class DataProcessor():


  def __init__(self):
    self.freqKey = {'annually': ['A', 1], 'monthly': ['MS', 12], 'bi-weekly': ['2W-FRI', 26] , 'weekly': ['W', 52]}
    self.plannedDf = pd.DataFrame(columns=['Date', 'Amount', 'Recurrence','Priority', 'Method', 'Name'])

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
    that points to the Pandas syntax for frequency of the date_range.

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


  def getUserDataDefinedTransactions(self, allottedAmt, userData):
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
    creditCardPayment = self.packageTransactionData(userData.nextCreditCardPaymentDate,
                                                     'Credit Card', -1 * allottedAmt, 1, 'monthly')
    
    self.addTransactionToDataframe(creditCardPayment)


    incomeTransaction = self.packageTransactionData(userData.nextPayDate, 'Income',
                                                         userData.incomeAmount, 1, userData.incomeFrequency)
        
    self.plannedDf = self.addTransactionToDataframe(incomeTransaction).sort_values(by='Date')

    print(self.plannedDf)

  def getProjectionData(self, allottedAmt, userData, plannedTransactions):
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


    chkBal = userData.checkingAccountBal
    incomeAmt = userData.incomeAmount
    incomeFreq = userData.incomeFrequency
    userData.nextPayDate = pd.to_datetime(userData.nextPayDate)
    userData.nextCreditCardPaymentDate = pd.to_datetime(userData.nextCreditCardPaymentDate)
    self.getUserDataDefinedTransactions(allottedAmt, userData)

    self.plannedDf.sort_values(by='Date')
    print(self.plannedDf)
    
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