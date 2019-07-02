from Transaction import CompletedTransaction
from TransactionFactory import TransactionFactory
from APIData import TransactionData, CategoryData
from Category import Category
from CategoryFactory import CategoryFactory

class TransactionManager():

  def __init__(self):
    self.transactionFactory = TransactionFactory()
    self.categoryFactory = CategoryFactory()
    self.transactions = dict()
    self.completedTransactions = dict()
    self.categories = dict()  
    self.categories["Unhandled"] = Category("Unhandled")

  # assigns dictionary key to the name of transaction in transaction dict
  # difference between registering and creating?
  def registerTransaction(self, t):
    self.transactions[t.name] = t
    if self.categories[t.category] != None:
      self.categories[t.category].registerTransaction(t)

  def registerCompletedTransaction(self, categoryName, transRefNumber):
    t = self.completedTransactions[transRefNumber]
    self.categories[categoryName].registerCompletedTransaction(t)

  def unregisterCompletedTransaction(self, categoryName, transRefNumber):
    t = self.completedTransactions[transRefNumber]
    self.categories[categoryName].unregisterCompletedTransaction(t)

  def registerCategory(self, c):
    self.categories[c.name] = c

  def createTransaction(self, data):
    t = self.transactionFactory.createTransaction(data)
    self.registerTransaction(t)

  def createCategory(self, data):
    c = self.categoryFactory.createCategory(data)
    self.registerCategory(c)

  def deleteCategory(self, name):
    '''
    Deletes a user-defined category. Protects against any 
    system-scope categories from being deleted, such as
    the Unhandled category

    @name: Category name to be deleted
    '''

    # Use a try-block in order to handle a scenario
    # where a non-existent key is entered so the program
    # does not crash
    try:
      if name != "Unhandled":
        del self.categories[name]
    except KeyError:
      print("Key not found")

