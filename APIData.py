'''
The purpose for these API Data objects is to use "lighter weight"
objects to pass into the back-end. There, these objects pass the
information over to a more versatile version of that respective
object(transaction or category). These are instantiated when the 
user defines a new object, and passed along into the backend.

'''

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
    self.priority = None
    self.paymentMethod = None

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
    