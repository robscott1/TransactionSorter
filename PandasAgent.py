import pandas as pd
from datetime import date

class PandasAgent():

	def __init__(self, df=None, plannedDf=None):
		self.completedDf = None
		self.plannedDf = pd.DataFrame(columns=['Date', 'Amount'])
		self.userData = None

	def getUserData(self, data):
		self.userData = data

	def getCompletedTransactionsDataframe(self, fileName):
	 	self.completedDf = pd.read_csv(fileName, sep=',', header = None)

	def createPlannedTransactionsDataframe(self, planned):

		for item in planned:
			item.date = pd.to_datetime(item.date)
			self.plannedDf.loc[item.name] = ({'Date': item.date, 'Amount': item.amount})
			self.plannedDf.sort('Date')
	
	def updatePlannedTransactionsDataframe(self, data):
		print(data.location)
		data.date = pd.to_datetime(data.date)
		self.plannedDf.loc[data.name] = ({'Date': data.date, 'Amount': data.amount})
		self.plannedDf.sort('Date')


	def getProjectionData(self, allottedAmt):
		checkingBalance = self.userData.checkingAccountBal
		incomeAmt = self.userData.incomeAmount
		incomeFreq = self.userData.incomeFrequency
		nextPayDate = pd.to_datetime(self.userData.nextPayDate)
		nextCreditPaymentDate = pd.to_datetime(self.userData.nextCreditCardPaymentDate)

		today = date.today()
		today = pd.to_datetime(today)

		dates = list(pd.date_range(today, freq='D', periods=365))
		runningBalance = []

		for i in range(365):
			if dates[i] in plannedDf['Dates']:
				print(plannedDf.loc[dates[i]])
				balance -= row.amount
			if i % 14 == 0 and i != 0:
				balance += incomeAmt
			if row.date.is_month_start():
				balance -= allottedAmt
			runningBalance.append(balance)

		return dates, runningBalance

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

