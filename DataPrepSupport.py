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
			package = self.packageTransactionData(item.date, item.name, item.amount,
			                                       item.priority, item.rateOfRecurrence)
		  
			self.plannedDf = self.addTransactionToDataframe(package).sort_values(by='Date')
            
	def addTransactionToDataframe(self, transaction):
		for item in transaction.date:
			self.plannedDf = self.plannedDf.append({'Date': item, 'Amount': transaction.amount,
																							'Recurrence': transaction.rateOfRecurrence,
																						 	'Priority': transaction.priority}, ignore_index=True)

		return self.plannedDf

	def getProjectionData(self, allottedAmt, userData, plannedTransactions):

		self.extractPlannedTransactionData(plannedTransactions)
		print(self.plannedDf)

		today = datetime.today().strftime('%Y-%m-%d')

		chkBal = 2500
		incomeAmt = 800
		incomeFreq = 'bi-weekly'
		nextPayDate = pd.to_datetime('08/23/2019')
		nextCreditPaymentDate = pd.to_datetime('09/01/2019')

		datesOfExpense = []
		runningBalance = []

		runningBalance.append(chkBal)
		datesOfExpense.append(today)

		for index, row in self.plannedDf.iterrows():

			#before transaction
			datesOfExpense.append(str(row.Date))
			runningBalance.append(chkBal)

			#after transaction
			chkBal -= row.Amount
			datesOfExpense.append(str(row.Date))
			runningBalance.append(chkBal)

		return datesOfExpense, runningBalance