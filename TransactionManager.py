from Transaction import Transaction
from TransactionFactory import TransactionFactory
from APIData import TransactionData, CategoryData
from Category import Category
from CategoryFactory import CategoryFactory

class TransactionManager():

  def __init__(self):
    self.transactionFactory = TransactionFactory()
    self.categoryFactory = CategoryFactory()
    self.transactions = dict()
    self.categories = dict()

  # assigns dictionary key to the name of transaction in transaction dict
  # difference between registering and creating?
  def registerTransaction(self, t):
    self.transactions[t.name] = t
    if self.categories[t.category] != None:
      self.categories[t.category].registerTransaction(t)

  def registerCategory(self, c):
    self.categories[c.name] = c

  def createTransaction(self, data):
    t = self.transactionFactory.createTransaction(data)
    self.registerTransaction(t)

  def createCategory(self, data):
    c = self.categoryFactory.createCategory(data)
    self.registerCategory(c)

