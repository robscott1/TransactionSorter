from ExcelManager import ExcelManager
from SortingAgent import SortingAgent
from Transaction import CompletedTransaction
from Category import Category
from CSVAgent import CSVAgent
from APIData import TransactionData
from TransactionFactory import TransactionFactory
from PandasAgent import PandasAgent
from UserData import UserData

class AnalysisManager():


  def __init__(self):
    self.completedTransactions = dict()
    self.plannedTransactions = None
    self.categories = dict()
    self.sortingAgent = SortingAgent()
    self.excelManager = ExcelManager()
    self.csvAgent = CSVAgent()
    self.transactionFactory = TransactionFactory()
    self.pandasAgent = PandasAgent()
    self.userData = UserData()

  def saveUserSetupData(self, chkAccBal, incomeAmt, incomeFreq, payDate, ccDate):
    self.userData.checkingAccountBal = chkAccBal
    self.userData.incomeAmount = incomeAmt
    self.userData.incomeFrequency = incomeFreq
    self.userData.nextPayDate = payDate
    self.userData.nextCreditCardPaymentDate = ccDate
    self.pandasAgent.getUserData(self.userData)

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
    Equivalent call to PandasAgent that prepares
    dates and total expenditures to plot in plottingWindow.py
    '''
    return self.pandasAgent.getTimeSeriesData()

  def getProjectionData(self):
    totalAllotted = 0
    for c in self.categories.values():
      if c != 'Unhandled':
        totalAllotted += c.getTotalAmountAllotted()
    return self.pandasAgent.getProjectionData(totalAllotted, list(self.plannedTransactions.values()))


  def getCompletedTransactionsDataframe(self, fileName):

    self.pandasAgent.getCompletedTransactionsDataframe(fileName)
