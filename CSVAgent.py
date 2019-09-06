import csv

class CSVAgent():

'''
Parses CSV and returns dates, amounts, and locations
that will create completedTransaction objects.
'''

  def parseFile(self, fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    
    dateList = []
    amountList = []
    locationList = []

    for line in lines:
        num_strs = line.split(',')
        date = num_strs[0]
        date = date[1:-1]
        dateList.append(date)
        amount = num_strs[1]
        amount = amount[1:-1]
        amountList.append(amount)
        location = num_strs[4]
        location = location[:-1]
        locationList.append(location)

    f.close()

    print(dateList)
    return dateList, amountList, locationList
    