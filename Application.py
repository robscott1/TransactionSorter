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
      self.transactionManager.registerCategory(c)
    self.analysisManager.categories = self.transactionManager.categories

    for t in tList:
      self.transactionManager.registerTransaction(t)
    self.analysisManager.plannedTransactions = self.transactionManager.transactions

  def saveData(self):
    self.pdm.stashPersistentData("transactionDataOut.xml", "categoryDataOut.xml", 
                                  self.transactionManager.transactions.values(), self.transactionManager.categories.values())


app = Application()
app.initialize()
app.saveData()

