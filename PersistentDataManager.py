import xml.etree.ElementTree as et
from APIData import TransactionData, CategoryData
from xmlAgent import xmlAgent


class PersistentDataManager():

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

 