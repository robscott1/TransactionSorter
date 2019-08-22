class PlannedTransaction():

  def __init__(self, name=None):
    self.name = name
    self.initialized = False
    self.key = None

  def initialize(self, date=None, category=None, amount=0.0, location=None, 
                 idKeywords=[], rateOfRecurrence=None, priority=3, paymentMethod='Checking'):

    self.initialized = True
    self.date = date
    self.category = category
    self.amount = amount
    self.location = location
    self.idKeywords = idKeywords
    self.priority = priority
    self.paymentMethod = paymentMethod

    if rateOfRecurrence == "annually":
      self.rateOfRecurrence = rateOfRecurrence
    elif rateOfRecurrence == "bi-annually":
      self.rateOfRecurrence = rateOfRecurrence
    elif rateOfRecurrence == "quarterly":
      self.rateOfRecurrence == rateOfRecurrence
    elif rateOfRecurrence == "monthly":
      self.rateOfRecurrence = rateOfRecurrence
    elif rateOfRecurrence == "bi-weekly":
      self.rateOfRecurrence = rateOfRecurrence
    elif rateOfRecurrence == "weekly":
      self.rateOfRecurrence = rateOfRecurrence
    elif rateOfRecurrence == "daily":
      self.rateOfRecurrence = rateOfRecurrence
    else:
      print("Unrecognized rate of recurrence - transaction has defaulted to non-recurring.")
      self.rateOfRecurrence = None


      print("rateOfRecurrence in initialize", self.rateOfRecurrence)

  def printData(self):
    print("Name: " + self.name)
    print("Category: " + self.category)
    print("Amount: " + str(self.amount))

class CompletedTransaction():
  
  def __init__(self, date=None, location=None, amount=None, referenceNumber=None):
    self.date = date
    self.location = location
    self.amount = amount
    self.referenceNumber = referenceNumber
