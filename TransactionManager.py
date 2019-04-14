from Transaction import Transaction
from Category import Category

class TransactionManager():

  def __init__(self):
    self.transactions = dict()
    self.categories = dict()

  def registerTransaction(self, t):
    self.transactions[t.name] = t
    self.categories[t.category].registerTransaction(t)

  def registerCategory(self, c):
    self.categories[c.name] = c


t = Transaction("OSL Ticket")
t.initialize(date="05/20/2019", amount=400.0, category="Festivals")
c = Category("Festivals")
tm = TransactionManager()
tm.registerCategory(c)
tm.registerTransaction(t)
print(tm.transactions[t.name].name)