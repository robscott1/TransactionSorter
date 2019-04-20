from ExcelManager import ExcelManager
from SortingAgent import Sorter as SortingAgent
from Transaction import Transaction
from Category import Category

class AnalysisManager():

  def __init__(self):
    self.completedTransactions = []
    self.plannedTransactions = None
    unhandled = Category("Unhandled")
    self.categories = dict()
    self.categories[unhandled.name] = unhandled
    self.sortingAgent = SortingAgent()
    self.excelManager = ExcelManager()

  def sortCompletedTransactions(self):
    self.sortingAgent.categorize()

  def getAmountSpentByCategory(self, categoryName):
    c = self.categories[categoryName]
    return c.getTotalAmount()

  def getDeltaByCategory(self, categoryName):
    c = self.categories[categoryName]
    return c.getDelta()

  def getAmountAllottedByCategory(self, categoryName):
    c = self.categories[categoryName]
    return c.getTotalAmountAllotted()

  def getTotalAmountSpent(self):
    total = 0
    for t in self.completedTransactions:
      total += t.amount

    return total

