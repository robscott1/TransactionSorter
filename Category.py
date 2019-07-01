from Transaction import CompletedTransaction

class Category():

  def __init__(self, name, monthlyAllotment = 0, keywords=[]):
    self.name = name
    self.keywords = keywords
    self.total = 0
    self.plannedTransactions = dict()
    self.completedTransactions = []
    self.monthlyAllotment = monthlyAllotment

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
    # update the keywords of the category to associate
    # with the location of the registered transaction
    self.keywords.append(t.location)

  def getTotalAmountSpent(self):
    amount = 0
    for t in self.completedTransactions:
      amount += float(t.amount)

    return amount

  def getTotalAmountAllotted(self):
    return self.monthlyAllotment

  def getPlannedTransactionAmount(self):
    amountPlanned = 0
    for t in self.plannedTransactions.values():
      amountPlanned += t.amount

    return amountPlanned

  def getDelta(self):
    return self.getTotalAmountAllotted() - self.getTotalAmountSpent()