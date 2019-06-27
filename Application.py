from PersistentDataManager import PersistentDataManager
from TransactionManager import TransactionManager
from AnalysisManager import AnalysisManager

class Application():

  # intitializes 3 managers with specialized tools in each of their layers
  def __init__(self):
    self.pdm = PersistentDataManager()
    self.transactionManager = TransactionManager()
    self.analysisManager = AnalysisManager()

  # retrieves past transactions and categorys from xml files from past uses of the app
  # recreates categories and transactions
  def initialize(self):
    tList, cList = self.pdm.retrievePersistentData("transactionDataIn.xml", "categoryDataIn.xml")

    for c in cList:
      self.transactionManager.createCategory(c)
    self.analysisManager.categories = self.transactionManager.categories

    for t in tList:
      self.transactionManager.createTransaction(t)
    self.analysisManager.plannedTransactions = self.transactionManager.transactions

  # takes in data that is already parsed and 
  # saves the location it was spent at and the amount spent
  # location name will allow for the categories to pick up relevant transactions
  def sortCompletedTransactions(self, fileName):
    self.analysisManager.sortCompletedTransactions(fileName)

  # writes both transactions and categories into xml files
  def saveData(self):
    self.pdm.stashPersistentData("transactionDataOut.xml", "categoryDataOut.xml", 
                                  self.transactionManager.transactions.values(), self.transactionManager.categories.values())

  # allows totals to be tracked through each category
  # transactions are picked up and put in Category objects
  # in the form of a list
  def getAmountSpentByCategory(self, category):
    return self.analysisManager.getAmountSpentByCategory(category)

  # retieves list of categories
  def getCategoryList(self):
    return self.analysisManager.categories

  # retrieves the list of transactions that were not picked up
  # by Category objects
  # this will happen because these transactions belong to a new 
  # Category that has yet to be created, or this transaction location
  # was not part of the idKeywords list for the respective category
  def getUnhandledTransactions(self):
    return self.analysisManager.categories["Unhandled"]

  #called from GUI to create Category object
  def createNewCategory(self, data):
    self.transactionManager.createCategory(data)
    
"""
app = Application()
app.initialize()
app.sortCompletedTransactions("../CreditCard3")
cats = app.getCategoryList()
for c in cats.values():
  print(c.name + ": " + str(c.getTotalAmountSpent()))
for t in app.getUnhandledTransactions().completedTransactions:
  print("[UNHANDLED] Amount: " + t.amount + ", Location: " + t.location)
app.saveData()
"""

