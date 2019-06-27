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
    tList, cList = self.pdm.retrievePersistentData("transactionData.xml", "categoryData.xml")

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
    self.pdm.stashPersistentData("transactionData.xml", "categoryData.xml", 
                                  self.transactionManager.transactions.values(), self.transactionManager.categories.values())

  # allows totals to be tracked through each category
  # transactions are picked up and put in Category objects
  # in the form of a list
  def getAmountSpentByCategory(self, category):
    return self.analysisManager.getAmountSpentByCategory(category)

  def getCategoryNamesList(self):
    '''
    This method can be used to get the keys
    to look up category information using 
    other API functions.

    @returns: A list of keys for a category
    dictionary in the form of category names
    '''
    return list(self.analysisManager.categories.keys())

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

  def getCompletedTransactionsList(self):
    '''
    @returns: The list of completed transactions from the
    most recently imported csv file
    '''
    return self.analysisManager.completedTransactions

  def getTotalAmountSpent(self):
    '''
    @returns: The total amount spent from all the transactions
    in the most recently imported csv file
    '''
    return self.analysisManager.getTotalAmountSpent()

  def getAmountSpentByCategory(self, categoryName):
    '''
    Wrapper function for the AnalysisManager's equivalent
    call

    @categoryName: A string to be used as a dictionary
    key to associate to the corresponding category object

    @returns: The sum of all transactions that have been
    associated with that category
    '''
    return self.analysisManager.getAmountSpentByCategory(categoryName)

  def getDeltaByCategory(self, categoryName):
    '''
    Wrapper function for the AnalysisManager's equivalent
    call

    @categoryName: A string to be used as a dictionary
    key to associate to the corresponding category object

    @returns: The difference between the amount that was
    allotted and the amount that was spent for a given category
    '''
    return self.analysisManager.getDeltaByCategory(categoryName)


def getAmountAllottedByCategory(self, categoryName):
    '''
    Wrapper function for the AnalysisManager's equivalent
    call

    @categoryName: A string to be used as a dictionary
    key to associate to the corresponding category object

    @returns: The amount that the user allotted for a given
    category
    '''
    return self.analysisManager.getAmountAllottedByCategory(categoryName)
