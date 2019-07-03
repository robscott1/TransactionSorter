class TransactionData():

  def __init__(self):
    self.name = None
    self.date = None
    self.category = None
    self.amount = None
    self.idKeywords = None
    self.recurring = None
    self.rateOfRecurrence = None
    self.location = None

class CategoryData():

  def __init__(self):
    self.name = None
    # If the user changes the name of a category,
    # we need to be able to locate it in the back-end
    # using the previous name as the dictionary key
    self.previousName = None
    self.nameModified = False
    self.idKeywords = None
    self.monthlyAllotment = None
    self.amountSpent = None
    