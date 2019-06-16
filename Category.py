from Transaction import Transaction

class Category():

  def __init__(self, name, keywords=[]):
    self.name = name
    self.keywords = keywords
    self.total = 0
    self.plannedTransactions = dict()
    self.completedTransactions = []

  def addAmount(self, amt):
    self.total += amt

  def containsWord(self,phrase,word):
    return word in phrase

  def checkKeywords(self, location):
    for keyword in self.keywords:
      if self.containsWord(location.casefold(),keyword.casefold()):
        return True
    return False

  def registerTransaction(self, t):
    self.plannedTransactions[t.name] = t

  def registerCompletedTransaction(self, t):
    self.completedTransactions.append(t)

  def getTotalAmountSpent(self):
    amount = 0
    for t in self.completedTransactions:
      amount += float(t.amount)

    return amount

  def getTotalAmountAllotted(self):
    amountAllotted = 0
    for t in self.plannedTransactions.values():
      amountAllotted += t.amount

    return amountAllotted

  def getDelta(self):
    return self.getTotalAmountAllotted() - self.getTotalAmountSpent()