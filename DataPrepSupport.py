import pandas as pd
from datetime import datetime

class TransactionPackage():
    
    def __init__(self):
      self.date = None
      self.amount = None
      self.priority = None
      self.rateOfRecurrence = None
      self.paymentMethod = None



class DataProcessor():


  def __init__(self):
    self.freqKey = {'annually': ['A', 1], 'monthly': ['MS', 12], 'bi-weekly': ['2W-FRI', 26] , 'weekly': ['W', 52]}
    self.plannedDf = pd.DataFrame(columns=['Date', 'Amount', 'Recurrence','Priority', 'Method', 'Name'])

  def getDateOffset(self, startDay):
    startDay = str(startDay)
    startDay = startDay.split()[0]
    startDay = startDay.split('-')
    day = startDay[2]
    return int(day)

  def createDateList(self, startDay, rateOfRecurrence):
    print("")
    print("each transaction startDay and rateOfRecurrence: ", startDay, rateOfRecurrence)
    if rateOfRecurrence == None:
      return list(startDay)
    
    if rateOfRecurrence == 'monthly':
      return list((pd.date_range(startDay, periods=self.freqKey[rateOfRecurrence][1],
                   freq=self.freqKey[rateOfRecurrence][0]) + pd.DateOffset(days=self.getDateOffset(startDay) - 1)))
    if rateOfRecurrence == 'bi-weekly':
      return list(pd.date_range(startDay, periods=self.freqKey[rateOfRecurrence][1],
                   freq=self.freqKey[rateOfRecurrence][0]))

  def packageTransactionData(self, date, name, amount, priority, rateOfRecurrence, paymentMethod=None):
    package = TransactionPackage()
    package.name = name
    print("DPS packageTransactionData date: ", name, date)
    package.date = self.createDateList(date, rateOfRecurrence)
    package.amount = amount
    package.rateOfRecurrence = rateOfRecurrence
    package.priority = priority
    package.paymentMethod = paymentMethod
    print("package name and date:", package.name, package.date)
    return package

  def extractPlannedTransactionData(self, plannedT):
    for item in plannedT:
      if item.paymentMethod == 'Checking':
        package = self.packageTransactionData(item.date, item.name, -1 * item.amount,
                                               item.priority, item.rateOfRecurrence,
                                               item.paymentMethod)

      self.plannedDf = self.addTransactionToDataframe(package).sort_values(by='Date')

  def addTransactionToDataframe(self, transaction):
    for item in transaction.date:
      self.plannedDf = self.plannedDf.append({'Date': item, 'Amount': transaction.amount,
                                              'Recurrence': transaction.rateOfRecurrence,
                                              'Priority': transaction.priority,
                                              'Method': transaction.paymentMethod, 'Name':transaction.name}, ignore_index=True)

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