from Transaction import CompletedTransaction

class Category():

  def __init__(self, name, monthlyAllotment = 0, keywords=[]):
    self.name = name
    self.keywords = keywords
    self.total = 0
    self.plannedTransactions = dict()
    self.completedTransactions = dict()
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

  def unregisterCompletedTransaction(self, t):
    self.keywords.remove(t.location)
    del self.completedTransactions[t.referenceNumber]

  def registerCompletedTransaction(self, t):
    '''
    Used for manually sorted transactions. Called from TransactionManager to
    sort after the user has dragged and dropped the item into the proper widget.
    This appends the location to the keywords in order to add additional words 
    for the sorting agent. It is used here because this transaction and any repeats
    will now be picked up by the sorting agent and be transferred by automatedSortTransaction.

    @t: transaction object to be added to completedTransactions dict and have .location
    appended to category keywords
    
    '''
    self.completedTransactions[t.referenceNumber] = t
    # update the keywords of the category to associate
    # with the location of the registered transaction
    self.keywords.append(t.location)

  def automatedSortTransaction(self, t):
    '''
    Since the program has automatically sorted a transaction into a particular category,
    the keyword already exists in the keywords list for that respective category. 
    This adds the transaction to the category, but does not append the keywords
    associated like registerCompletedTransaction. This method is called when a 
    transaction is automatically sorted; the above method does it when the user manaully
    sorts

    @t: transaction object with information to assign it into the completed
    transactions dict

    '''
    self.completedTransactions[t.referenceNumber] = t

  def getTotalAmountSpent(self):
    amount = 0
    for t in self.completedTransactions.values():
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