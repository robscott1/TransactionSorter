import xml.etree.ElementTree as et
from APIData import TransactionData, CategoryData
from XMLAgent import xmlAgent


class PersistentDataManager():
  '''
  This class handles any information that will remain useful across
  several boot-ups. When any new categories are created or planned 
  transactions entered, they are written into an xml file. This job is
  passed down to the xmlAgent (see for more description). The 
  PersistentDataManager keeps useful information at the hands of the
  user by storing it and retrieving it from an xml file.
  '''

  def __init__(self):
    self.xmlAgent = xmlAgent()
    self.transactionList = None
    self.categoryList = None

  def retrievePersistentData(self, transactionFilePath, categoryFilePath):
    transactionTree = et.parse(transactionFilePath)
    self.transactionList = self.xmlAgent.parseTransactionData(transactionTree)

    categoryTree = et.parse(categoryFilePath)
    self.categoryList = self.xmlAgent.parseCategoryData(categoryTree)

    return self.transactionList, self.categoryList

  def stashPersistentData(self, transactionFilePath, categoryFilePath, tList, cList):
    self.xmlAgent.stashTransactionData(transactionFilePath, tList)
    self.xmlAgent.stashCategoryData(categoryFilePath, cList)

 