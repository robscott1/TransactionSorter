from ExcelManager import ExcelManager
from SortingAgent import SortingAgent
from Transaction import CompletedTransaction
from Category import Category
from CSVAgent import CSVAgent
from APIData import TransactionData
from TransactionFactory import TransactionFactory
from PlottingDataFactory import PlottingDataFactory
from UserData import UserData

class AnalysisManager():
  '''
  This main branch is responsible for all analysis functions. It has
  several sub-modules for several distinct uses. That includes parsing,
  sorting, preparing useful information from different sources of data. 
  It holds a dictionary of category objects that can return important
  spending information as well as items planned by the user. It also
  holds all completed transactions that were parsed from the CSV chosen
  by the user. They are held in a dictionary with their "reference number"
  as their key. Any information asked for by the user will be called
  through here.
  '''

  def __init__(self):
    self.completedTransactions = dict()
    self.plannedTransactions = None
    self.categories = dict()
    self.sortingAgent = SortingAgent()
    self.excelManager = ExcelManager()
    self.csvAgent = CSVAgent()
    self.transactionFactory = TransactionFactory()
    self.plottingDataFactory = PlottingDataFactory()
    self.userData = UserData()

  def saveUserSetupData(self, chkAccBal, incomeAmt, incomeFreq, payDate, ccDate):
    self.userData.checkingAccountBal = chkAccBal
    self.userData.incomeAmount = incomeAmt
    self.userData.incomeFrequency = incomeFreq
    self.userData.nextPayDate = payDate
    self.userData.nextCreditCardPaymentDate = ccDate
    self.plottingDataFactory.getUserData(self.userData)

  def sortCompletedTransactions(self, fileName):
    '''
    Takes parsed data from CSV agent and records 
    amount and location of transaction. Uses APIData
    object to pass transaction details to TransactionFactory
    
    @fileName: path to CSV file
    '''
    dateList, amountList, locationList = self.csvAgent.parseFile(fileName)
    for index in range(len(amountList)):
      parsedData = TransactionData()
      parsedData.date = dateList[index]
      parsedData.amount = amountList[index]
      parsedData.location = locationList[index]
      completedTransaction = self.transactionFactory.createCompletedTransaction(parsedData)
      self.completedTransactions[completedTransaction.referenceNumber] = completedTransaction
    
    self.sortingAgent.categorize(self.completedTransactions, self.categories)


  def getAmountSpentByCategory(self, categoryName):
    c = self.categories[categoryName]
    return c.getTotalAmountSpent()

  def getDeltaByCategory(self, categoryName):
    '''
    Finds difference between amount allotted and amount spent

    @categoryName: string used to reference the name of 
    Category object in dictionary

    @returns: Integer value of difference between
    amount spent and amount allotted

    '''
    c = self.categories[categoryName]
    return c.getDelta()

  
  def getAmountAllottedByCategory(self, categoryName):
    '''
    Gets amount allotted for particular category

    @categoryName: string used to reference the name of 
    Category object in dictionary

    @returns: Integer value money allotted for
    category of interest

    '''
    c = self.categories[categoryName]
    return c.getTotalAmountAllotted()

  def getAmountPlannedByCategory(self, categoryName):
    '''
    Gets sum of PlannedTransactions for 
    particular category

    @categoryName: string used to reference the name of 
    Category object in dictionary

    @returns: Sum of all PlannedTransactions for 
    that category

    '''
    c = self.categories[categoryName]
    return c.getPlannedTransactionAmount()

  def getTotalAmountSpent(self):
    total = 0
    for t in self.completedTransactions.values():
      total += float(t.amount)

    return total * -1

  def getKeywordsByCategory(self, categoryName):
    '''
    Gets list of category keywords

    @categoryName: string used to reference the name of 
    Category object in dictionary

    @returns: List of keywords associated with
    category of interest

    '''
    return self.categories[categoryName].keywords
    
  def getTimeSeriesData(self):
    '''
    Equivalent call to plottingDataFactory that prepares
    dates and total expenditures to plot in plottingWindow.py
    '''
    return self.plottingDataFactory.getTimeSeriesData()

  def getProjectionData(self):
    totalAllotted = 0
    for c in self.categories.values():
      if c != 'Unhandled':
        totalAllotted += c.getTotalAmountAllotted()
    return self.plottingDataFactory.getProjectionData(totalAllotted, list(self.plannedTransactions.values()))


  def getCompletedTransactionsDataframe(self):

    self.plottingDataFactory.getCompletedTransactionsDataframe(list(self.completedTransactions.values()))