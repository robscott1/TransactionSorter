from Transaction import Transaction
from TransactionFactory import TransactionFactory
from APIData import TransactionData
from Category import Category
from lxml import etree as et

class TransactionManager():

  def __init__(self):
    self.transactionFactory = TransactionFactory()
    self.transactions = dict()
    self.categories = dict()

  def registerTransaction(self, t):
    self.transactions[t.name] = t
    if self.categories[t.category] != None:
      self.categories[t.category].registerTransaction(t)

  def registerCategory(self, c):
    self.categories[c.name] = c

  def createTransaction(self, data):
    t = self.transactionFactory.createTransaction(data)
    self.registerTransaction(t)

