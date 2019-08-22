import pandas as pd
from datetime import datetime

class TransactionPackage():
    
    def __init__(self):
      self.date = None
      self.amount = None
      self.priority = None
      self.rateOfRecurrence = None



class DataProcessor():


  def __init__(self):
    self.freqKey = {'annually': ['A', 1], 'monthly': ['M', 12], 'bi-weekly': ['2W', 26] , 'weekly': ['W', 52]}
    self.plannedDf = pd.DataFrame(columns=['Date', 'Amount', 'Recurrence','Priority'])


  def createDateList(self, startDay, rateOfRecurrence):
    if rateOfRecurrence == None:
      return list(startDay)

    return list(pd.date_range(startDay, periods=self.freqKey[rateOfRecurrence][1], freq=self.freqKey[rateOfRecurrence][0]))

  def packageTransactionData(self, date, name, amount, priority, rateOfRecurrence):
    package = TransactionPackage()
    package.name = name
    package.date = self.createDateList(date, rateOfRecurrence)
    package.amount = amount
    package.rateOfRecurrence = rateOfRecurrence
    package.priority = priority

    return package

  def extractPlannedTransactionData(self, plannedT):
    for item in plannedT:
      package = self.packageTransactionData(item.date, item.name, -1 * item.amount,
                                             item.priority, item.rateOfRecurrence)

      self.plannedDf = self.addTransactionToDataframe(package).sort_values(by='Date')

  def addTransactionToDataframe(self, transaction):
    for item in transaction.date:
      self.plannedDf = self.plannedDf.append({'Date': item, 'Amount': transaction.amount,
                                              'Recurrence': transaction.rateOfRecurrence,
                                              'Priority': transaction.priority}, ignore_index=True)

    return self.plannedDf


  def getUserDataDefinedTransactions(self, allottedAmt, userData):
    creditCardPayment = self.packageTransactionData(userData.nextCreditCardPaymentDate,
                                                     'Credit Card', -1 * allottedAmt, 1, 'monthly')
    
    self.addTransactionToDataframe(creditCardPayment)

    incomeTransaction = self.packageTransactionData(userData.nextPayDate, 'Income',
                                                         userData.incomeAmount, 1, userData.incomeFrequency)
    
    self.plannedDf = self.addTransactionToDataframe(incomeTransaction).sort_values(by='Date')

  def getProjectionData(self, allottedAmt, userData, plannedTransactions):

    self.extractPlannedTransactionData(plannedTransactions)


    chkBal = userData.checkingAccountBal
    incomeAmt = userData.incomeAmount
    incomeFreq = userData.incomeFrequency
    nextPayDate = pd.to_datetime(userData.nextPayDate)
    nextCreditCardPaymentDate = pd.to_datetime(userData.nextCreditCardPaymentDate)
    
    self.getUserDataDefinedTransactions(allottedAmt, userData)

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