import csv

class CSVAgent():

  def parseFile(self, fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    
    amountList = []
    locationList = []
    dateList = []

    for line in lines:
        num_strs = line.split(',')
        amount = num_strs[1]
        amount = amount[1:-1]
        amountList.append(amount)
        location = num_strs[4]
        location = location[:-1]
        locationList.append(location)
        date = num_strs[0]
        date = date[1:-1]
        dateList.append(date)

    f.close()

    return amountList, locationList, dateList
    