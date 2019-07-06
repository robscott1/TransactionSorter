from Transaction import CompletedTransaction
from TransactionFactory import TransactionFactory
from APIData import TransactionData, CategoryData
from Category import Category
from CategoryFactory import CategoryFactory

class TransactionManager():

  def __init__(self):
    self.transactionFactory = TransactionFactory()
    self.categoryFactory = CategoryFactory()
    self.transactions = dict()
    self.completedTransactions = dict()
    self.categories = dict()  
    self.categories["Unhandled"] = Category("Unhandled")

  # assigns dictionary key to the name of transaction in transaction dict
  # difference between registering and creating?
  def registerTransaction(self, t):
    self.transactions[t.name] = t
    try: 
      self.categories[t.category].registerTransaction(t)
    except KeyError:
      print("That category does not exist.")

  def registerCompletedTransaction(self, categoryName, transRefNumber):
    t = self.completedTransactions[transRefNumber]
    self.categories[categoryName].registerCompletedTransaction(t)

  def unregisterCompletedTransaction(self, categoryName, transRefNumber):
    t = self.completedTransactions[transRefNumber]
    self.categories[categoryName].unregisterCompletedTransaction(t)

  def registerCategory(self, c):
    self.categories[c.name] = c

  def createTransaction(self, data):
    t = self.transactionFactory.createTransaction(data)
    self.registerTransaction(t)

  def createCategory(self, data):
    c = self.categoryFactory.createCategory(data)
    self.registerCategory(c)

  def updateCategoryData(self, data):
    '''
    Adds/Updates any existing user-defined category

    @data: Category object with additional input from user
    '''
    # Check if this data object contains a modified name
    # which was entered by the user, in which case we 
    # must locate the actual object using the previous name
    # as the dictionary key
    if data.nameModified == True:
      dictKey = data.previousName
    else:
      dictKey = data.name

    modifiedCategory = self.categories[dictKey]
    modifiedCategory.name = data.name
    modifiedCategory.monthlyAllotment = data.monthlyAllotment
    modifiedCategory.keywords = data.idKeywords

    # If the category name was modified by the user,
    # associate the category with the new name as the key,
    # and delete the old key-value pair.
    if data.nameModified == True:
      self.categories[modifiedCategory.name] = modifiedCategory
      del self.categories[data.previousName]

  def deleteCategory(self, name):
    '''
    Deletes a user-defined category. Protects against any 
    system-scope categories from being deleted, such as
    the Unhandled category

    @name: Category name to be deleted
    '''

    # Use a try-block in order to handle a scenario
    # where a non-existent key is entered so the program
    # does not crash
    try:
      if name != "Unhandled":
        del self.categories[name]
    except KeyError:
      print("Key not found")

  def categoryDbg(self):
    for c in self.categories.values():
      print("Category: " + c.name)
      print("Keywords: " + str(c.keywords))

