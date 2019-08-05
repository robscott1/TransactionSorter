from ExcelManager import ExcelManager
from SortingAgent import SortingAgent
from Transaction import CompletedTransaction
from Category import Category
from CSVAgent import CSVAgent
from APIData import TransactionData
from TransactionFactory import TransactionFactory
from pandasModuleAgent import PandasModuleAgent

class AnalysisManager():

  # intitializes lower functioning tools within analysis manager
  def __init__(self):
    self.completedTransactions = dict()
    self.plannedTransactions = None
    self.categories = dict()
    self.sortingAgent = SortingAgent()
    self.excelManager = ExcelManager()
    self.csvAgent = CSVAgent()
    self.transactionFactory = TransactionFactory()
    self.pandasModuleAgent = PandasModuleAgent()
    self.completedTransactionsDataFrame = None

  # takes parsed data from CSV agent and records amount and
  # location of transaction
  # createCompletedTransaction uses the TransactionData object
  # to get all of the necessary information to store it
  def sortCompletedTransactions(self, fileName):
    dateList, amountList, locationList = self.csvAgent.parseFile(fileName)
    for index in range(len(amountList)):
      parsedData = TransactionData()
      parsedData.date = dateList[index]
      parsedData.amount = amountList[index]
      parsedData.location = locationList[index]
      completedTransaction = self.transactionFactory.createCompletedTransaction(parsedData)
      self.completedTransactions[completedTransaction.referenceNumber] = completedTransaction
    
    self.sortingAgent.categorize(self.completedTransactions, self.categories)

  def getAmountSpentByCategory(self, categoryName):
    c = self.categories[categoryName]
    return c.getTotalAmountSpent()

  # finds difference between amount allotted and amount spent
  def getDeltaByCategory(self, categoryName):
    c = self.categories[categoryName]
    return c.getDelta()

  # retrieves amount alloted
  def getAmountAllottedByCategory(self, categoryName):
    c = self.categories[categoryName]
    return c.getTotalAmountAllotted()

  def getAmountPlannedByCategory(self, categoryName):
    c = self.categories[categoryName]
    return c.getPlannedTransactionAmount()

  # retrives total amount spent, used for categories
  def getTotalAmountSpent(self):
    total = 0
    for t in self.completedTransactions.values():
      total += float(t.amount)

    return total * -1

  def getKeywordsByCategory(self, categoryName):
    return self.categories[categoryName].keywords
    
  def getTimeSeriesData(self):
    return self.pandasModuleAgent.getTimeSeriesData()

