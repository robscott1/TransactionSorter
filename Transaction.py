class PlannedTransaction():

  def __init__(self, name=None):
    self.name = name
    self.initialized = False
    self.key = None

  def initialize(self, date=None, category=None, amount=0.0, location=None, idKeywords=[], recurring=False, rateOfRecurrence=None):
    self.initialized = True
    #for planned, not for completed
    self.date = date
    try:
      splitDate = date.split('/')
      self.month = int(splitDate[0])
      self.day = int(splitDate[1])
      self.year = int(splitDate[2])
      print("Month: " + self.month + ", Day: " + self.day + ", Year: " + self.year)
    except:
      print("Exception occurred.")

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
  
  def __init__(self, location=None, amount=None, referenceNumber=None, date=None):
    self.location = location
    self.amount = float(amount)
    self.referenceNumber = referenceNumber
    self.date = date
    splitDate = date.split('/')
    self.month = int(splitDate[0])
    self.day = int(splitDate[1])
    self.year = int(splitDate[2])
    
