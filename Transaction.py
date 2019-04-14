class Transaction():

  def __init__(self, name):
    self.name = name

  def initialize(self, date, category=None, amount=0.0, idKeywords=[], recurring=False, rateOfRecurrence=None):
    self.date = date
    self.category = category
    self.amount = amount
    self.idKeywords = idKeywords

    if recurring == True:
      if rateOfRecurrence == "annually":
        self.recurring = recurring
        self.rateOfRecurrence = rateOfRecurrence
      elif rateOfRecurrence == "bi-annually":
        self.recurring = recurring
        self.rateOfRecurrence = rateOfRecurrence
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
