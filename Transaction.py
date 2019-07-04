class PlannedTransaction():

  def __init__(self, name=None):
    self.name = name
    self.initialized = False
    self.key = None

  def initialize(self, date=None, category=None, amount=0.0, location=None, idKeywords=[], recurring=False, rateOfRecurrence=None):
    self.initialized = True
    #for planned, not for completed
    self.date = date
    self.category = category
    self.amount = amount
    self.location = location
    self.idKeywords = idKeywords

    if recurring == True:
      if rateOfRecurrence == "annually":
        self.recurring = recurring
        self.rateOfRecurrence = rateOfRecurrence
      elif rateOfRecurrence == "bi-annually":
        self.recurring = recurring
        self.rateOfRecurrence = rateOfRecurrence
      elif rateOfRecurrence == "quarterly":
        self.recurring = recurring
        self.rateOfRecurrence == rateOfRecurrence
      elif rateOfRecurrence == "monthly":
        self.recurring = recurring
        self.rateOfRecurrence = rateOfRecurrence
      elif rateOfRecurrence == "bi-weekly":
        self.recurring = recurring
        self.rateOfRecurrence = rateOfRecurrence
      elif rateOfRecurrence == "weekly":
        self.recurring = recurring
        self.rateOfRecurrence = rateOfRecurrence
      elif rateOfRecurrence == "daily":
        self.recurring = recurring
        self.rateOfRecurrence = rateOfRecurrence
      else:
        print("Unrecognized rate of recurrence - transaction has defaulted to non-recurring.")
        self.recurring = False
        self.rateOfRecurrence = None
    else:
      self.recurring = False
      self.rateOfRecurrence = None

  def printData(self):
    print("Name: " + self.name)
    print("Category: " + self.category)
    print("Amount: " + str(self.amount))

class CompletedTransaction():
  
  def __init__(self, location=None, amount=None, referenceNumber=None):
    self.location = location
    self.amount = amount
    self.referenceNumber = referenceNumber
