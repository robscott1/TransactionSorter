import pandas as pd

class PandasAgent():

	def __init__(self, df=None, plannedDf=None):
		self.completedDf = None
		self.plannedDf = pd.DataFrame(columns=['Date', 'Amount', 'Priority'])
		self.userData = None

	def getUserData(self, data):
		self.userData = data

	def getCompletedTransactionsDataframe(self, fileName):
	 	self.completedDf = pd.read_csv(fileName, sep=',', header = None)

	def createPlannedTransactionsDataframe(self, planned):

		for item in planned:
			print(item.date)
			plannedDf.loc[item.location] = ({'Date': item.date, 'Amount': item.amount,
											 'Priority': item.priority})
	
	def updatePlannedTransactionsDataframe(self, data):
		plannedDf.loc[date.location] = ({'Date': data.date, 'Amount': data.amount,
										 'Priority': data.priority})

	def getProjectionData(self):



	def getTimeSeriesData(self):
		self.completedDf.columns = ['date', 'amount', 'bye', 'felicia', 'location']
		del self.completedDf['bye']
		del self.completedDf['felicia']

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

