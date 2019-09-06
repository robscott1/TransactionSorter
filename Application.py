from PersistentDataManager import PersistentDataManager
from TransactionManager import TransactionManager
from AnalysisManager import AnalysisManager

class Application():

  '''
  This class is the bridge to the back-end. All function calls in the GUI
  are in this class. From here, it will split off into three major 
  modules. The functions in this class are plain- they send calls down
  to sub modules where most of the "heavy lifting" occurs. This structure
  allows for separation of distinct functionality/duties of the app. The
  three main branches are the PersistentDataManager, the TransactionManager,
  and the Analysis Manager. 

  See each of those classes to get the description on their distinct functionality.
  '''

  # intitializes 3 managers with specialized tools in each of their layers
  def __init__(self):
    self.pdm = PersistentDataManager()
    self.transactionManager = TransactionManager()
    self.analysisManager = AnalysisManager()

  def initialize(self):
    '''
    Retrieves past transactions and categorys from xml 
    files from past uses of the app recreates categories
    and transactions.
    '''
    tList, cList = self.pdm.retrievePersistentData("TransactionData.xml", "CategoryData.xml")

    for c in cList:
      self.transactionManager.createCategory(c)
    self.analysisManager.categories = self.transactionManager.categories

    for t in tList:
      self.transactionManager.createTransaction(t)
    self.analysisManager.plannedTransactions = self.transactionManager.transactions
  

  def sortCompletedTransactions(self, fileName):
    '''
    Wrapper function for AnalysisManager's equivalent
    call.

    @filename: Path to CSV file that will be parsed
    and used to create completedTransaction objects
    '''
    self.fileName = fileName
    self.analysisManager.sortCompletedTransactions(fileName)
    self.analysisManager.getCompletedTransactionsDataframe()
    self.transactionManager.completedTransactions = self.analysisManager.completedTransactions

  
  def saveData(self):
    '''
    Calls function in PersistentDataManager that writes
    planned transactions and category info to an .xml file

    @transactionData.xml, categoryData.xml: files on which
    planned transactions and category info are stored

    @self.transactionManager.transactions.values(): names
    of plannedTransaction objects

    @self.transactionManager.categories.values(): names
    of Category objects
    '''
    self.pdm.stashPersistentData("TransactionData.xml", "CategoryData.xml", 
                                  self.transactionManager.transactions.values(), self.transactionManager.categories.values())

  def saveUserSetupData(self, chkAccBal, incomeAmt, incomeFreq, payDate, ccDate):

    self.analysisManager.saveUserSetupData(float(chkAccBal), float(incomeAmt), 
                                           str(incomeFreq), str(payDate), str(ccDate))

  def getCategoryNamesList(self):
    '''
    This method can be used to get the keys
    to look up category information using 
    other API functions.

    @returns: A list of keys for a category
    dictionary in the form of category names
    '''
    return list(self.analysisManager.categories.keys())

  
  def getUnhandledTransactions(self):
    '''
    Gets all completedTransaction objects in the 
    "Unhandled" category

    @returns: CompletedTransaction objects that 
    have not been categorized
    '''
    return self.transactionManager.categories["Unhandled"].completedTransactions

  
  def createNewCategory(self, data):
    '''
    pyCategoryPop.py GUI window sends APIData object through here
    to TransactionManager where new Category object is made

    @data: APIData object with name, allotted amount, and keywords
    to make new Category object in back end
    '''
    self.transactionManager.createCategory(data)
    self.analysisManager.categories = self.transactionManager.categories

  def updateCategoryData(self, data):
    '''
    Same functionality as createNewCategory, but firsr
    checks if the name of existing category was changed

    @data: APIData object with name, allotted amount, and keywords
    to make new Category object in back end
    '''
    self.transactionManager.updateCategoryData(data)
    self.analysisManager.categories = self.transactionManager.categories

  def getCompletedTransactionsList(self):
    '''
    @returns: The list of completed transactions from the
    most recently imported csv file
    '''
    return self.analysisManager.completedTransactions

  def getTotalAmountSpent(self):
    '''
    @returns: The total amount spent from all the transactions
    in the most recently imported csv file
    '''
    return abs(self.analysisManager.getTotalAmountSpent())

  def getAmountSpentByCategory(self, categoryName):
    '''
    Wrapper function for the AnalysisManager's equivalent
    call

    @categoryName: A string to be used as a dictionary
    key to associate to the corresponding category object

    @returns: The sum of all transactions that have been
    associated with that category
    '''

    return abs(round(self.analysisManager.getAmountSpentByCategory(categoryName), 2))

  def getDeltaByCategory(self, categoryName):
    '''
    Wrapper function for the AnalysisManager's equivalent
    call

    @categoryName: A string to be used as a dictionary
    key to associate to the corresponding category object

    @returns: The difference between the amount that was
    allotted and the amount that was spent for a given category
    '''
    return round(self.analysisManager.getDeltaByCategory(categoryName), 2)


  def getAmountAllottedByCategory(self, categoryName):
    '''
    Wrapper function for the AnalysisManager's equivalent
    call

    @categoryName: A string to be used as a dictionary
    key to associate to the corresponding category object

    @returns: The amount that the user allotted for a given
    category
    '''
    return self.analysisManager.getAmountAllottedByCategory(categoryName)

  def getAmountPlannedByCategory(self, categoryName):
    '''
    Wrapper function for the AnalysisManager's equivalent
    call

    @categoryName: A string to be used as a dictionary
    key to associate to the corresponding category object

    @returns: The sum of all planned transactions associated with
    the given category
    '''
    return self.analysisManager.getAmountPlannedByCategory(categoryName)

  def getKeywordsByCategory(self, categoryName):
    '''
    Wrapper function for the AnalysisManager's equivalent
    call

    @categoryName: A string to be used as a dictionary
    key to associate to the corresponding category object

    @returns: The list of keywords to identify transactions
    '''
    return self.analysisManager.getKeywordsByCategory(categoryName)

  def deleteCategory(self, categoryName):
    '''
    Wrapper function for the Transaction Manager's equivalent call.
    After the call, the category list of the Analysis Manager is 
    updated to reflect the change. I am not sure if python is copying the
    list over between the 2 managers, or if the Analysis Manager is
    getting a pointer/reference to the Transaction Manager's original
    list of categories. If the situation is the latter, then the second
    line of this method is actually not necessary. For now, I am playing
    it safe and making sure the Analysis Manager is updated accordingly.

    @categoryName: Category name to be deleted
    '''
    self.transactionManager.deleteCategory(categoryName)
    self.analysisManager.categories = self.transactionManager.categories

  def registerCompletedTransaction(self, categoryName, transRefNumber):
    '''
    Registers a completed transaction with a category so that it can be 
    properly sorted next time.

    @categoryName: Name of the category that the 
    transaction will be registered with
    @transRefNumber: Transaction reference number to be used
    as a key by the TransactionManager to locate the Transaction
    '''
    self.transactionManager.registerCompletedTransaction(categoryName, transRefNumber)
    self.analysisManager.categories[categoryName] = self.transactionManager.categories[categoryName]

  def unregisterCompletedTransaction(self, categoryName, transRefNumber):
    '''
    Unregisters a completed transaction from a specified category.

    @categoryName: Name of the category that the 
    transaction will be registered with
    @transRefNumber: Transaction reference number to be used
    as a key by the TransactionManager to locate the Transaction
    '''
    self.transactionManager.unregisterCompletedTransaction(categoryName, transRefNumber)
    self.analysisManager.categories[categoryName] = self.transactionManager.categories[categoryName]

  def getCompletedTransactionsByCategory(self, categoryName):
    '''
    @categoryName: Name of the category to query for 
    completed transactions

    @returns: A dictionary of completed transactions that
    are registered to the specified category
    '''
    return self.transactionManager.getCompletedTransactionsByCategory(categoryName)

  def createPlannedTransaction(self, data):
    '''
    Calls mirror function in TransactionManager. Creates planned transaction within the
    user defined category

    @data: TransactionData API object with identifying members
    '''
    self.transactionManager.createTransaction(data)
    self.analysisManager.plannedTransactions[data.name] = self.transactionManager.transactions[data.name]

  def getPlannedTransactions(self, category):
    '''
    Wrapper function for TransactionManager's
    equivalent

    @category: Name of category of interest

    @returns: All PlannedTransaction objects in
    respective category
    '''
    return self.transactionManager.getPlannedTransactions(category)

  def removePlannedTransaction(self, category, name):
    '''
    Wrapper function for removing a planned transaction for the list
    of plannedTransactions

    @category: specified category of transaction chosen

    @name: name of transaction chosen to be deleted
    '''
    self.transactionManager.removePlannedTransaction(category, name)

  def diagnosticDbg(self):
    self.transactionManager.categoryDbg()

  def getTimeSeriesData(self):
    '''
    Wrapper function for getting time series data to be plotted 
    in the PlottingWindow.
    '''
    return self.analysisManager.getTimeSeriesData()

  def createCompletedTransactionsDataFrame(self):
    return self.analysisManager.getCompletedTransactionsDataframe()

  def getProjectionData(self):
    '''
    Wrapper function for projection data to be plotted in 
    ProjectionWindow.
    '''

    return self.analysisManager.getProjectionData()





if __name__ == "__main__":
  app = Application()
  app.initialize()
  filename = "../KevinVisaMay2019"
  app.sortCompletedTransactions(filename)
  