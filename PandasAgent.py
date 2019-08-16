import pandas as pd

class PandasAgent():


	def getTimeSeriesData(self, fileName):
		self.df = pd.read_csv(fileName, sep=',', header = None)
		self.df.columns = ['date', 'amount', 'bye', 'felicia', 'location']
		del self.df['bye']
		del self.df['felicia']

		#reverse the order to get df chronologically correct
		df1 = self.df[::-1]
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

