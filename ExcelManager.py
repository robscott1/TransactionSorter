import xlsxwriter

class ExcelManager():

  def __init__(self, worksheet):
    self.initColumn = 0
    self.currentRow = 0
    self.worksheet = worksheet


  def writerow(self, data=[], cellFormat=None):
    self.worksheet.write_row(self.currentRow, self.initColumn, data, cellFormat)
    self.currentRow += 1

