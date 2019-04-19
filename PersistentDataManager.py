from lxml import etree as et

class ParseAgent():

  def parseTransactionData(self, tree):
    root = tree.getroot()
    for transaction in root:
      for element in transaction:
        print(str(element.tag) + ": " + element.text)

class PersistentDataManager():

  def __init__(self):
    self.parseAgent = ParseAgent()

  def retrievePersistentData(self, transactionFilePath):
    transactionTree = et.parse(transactionFilePath)
    self.parseAgent.parseTransactionData(transactionTree)

pdm = PersistentDataManager()
pdm.retrievePersistentData("userData.xml")
 