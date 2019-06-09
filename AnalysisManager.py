from ExcelManager import ExcelManager
from SortingAgent import SortingAgent
from Transaction import Transaction
from Category import Category
from CSVAgent import CSVAgent
from APIData import TransactionData
from TransactionFactory import TransactionFactory

class AnalysisManager():

  def __init__(self):
    self.completedTransactions = []
    self.plannedTransactions = None
    unhandled = Category("Unhandled")
    self.categories = dict()
    self.categories[unhandled.name] = unhandled
    self.sortingAgent = SortingAgent()
    self.excelManager = ExcelManager()
    self.csvAgent = CSVAgent()
    self.transactionFactory = TransactionFactory()

  def sortCompletedTransactions(self, fileName):
    amountList, locationList = self.csvAgent.parseFile(fileName)
    for index in range(len(amountList)):
      parsedData = TransactionData()
      parsedData.amount = amountList[index]
      parsedData.location = locationList[index]
      completedTransaction = self.transactionFactory.createTransaction(parsedData)
      self.completedTransactions.append(completedTransaction)
      
    self.sortingAgent.categorize(self.completedTransactions, self.categories)

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

