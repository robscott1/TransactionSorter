from PersistentDataManager import PersistentDataManager
from TransactionManager import TransactionManager
from AnalysisManager import AnalysisManager

class Application():

  def __init__(self):
    self.pdm = PersistentDataManager()
    self.transactionManager = TransactionManager()
    self.analysisManager = AnalysisManager()

  def initialize(self):
    tList, cList = self.pdm.retrievePersistentData("transactionDataIn.xml", "categoryDataIn.xml")

    for c in cList:
      self.transactionManager.createCategory(c)
    self.analysisManager.categories = self.transactionManager.categories

    for t in tList:
      self.transactionManager.createTransaction(t)
    self.analysisManager.plannedTransactions = self.transactionManager.transactions

  def sortCompletedTransactions(self, fileName):
    self.analysisManager.sortCompletedTransactions(fileName)

  def saveData(self):
    self.pdm.stashPersistentData("transactionDataOut.xml", "categoryDataOut.xml", 
                                  self.transactionManager.transactions.values(), self.transactionManager.categories.values())

  def getAmountSpentByCategory(self, category):
    return self.analysisManager.getAmountSpentByCategory(category)

  def getCategoryList(self):
    return self.analysisManager.categories

  def getUnhandledTransactions(self):
    return self.analysisManager.categories["Unhandled"]


app = Application()
app.initialize()
app.sortCompletedTransactions("../KevinVisaMay2019")
cats = app.getCategoryList()
for c in cats.values():
  print(c.name + ": " + str(c.getTotalAmountSpent()))
for t in app.getUnhandledTransactions().completedTransactions:
  print("[UNHANDLED] Amount: " + t.amount + ", Location: " + t.location)
app.saveData()

