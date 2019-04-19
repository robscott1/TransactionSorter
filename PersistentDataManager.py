import xml.etree.ElementTree as et
from Transaction import Transaction

class xmlAgent():

  def parseTransactionData(self, tree):
    root = tree.getroot()
    transactionList = []
    for transaction in root:
      t = Transaction( transaction.findtext("name") )
      for element in transaction:
        if element.tag == "amount":
          t.amount = float(element.text)
        elif element.tag == "date":
          t.date = element.text
        elif element.tag == "category":
          t.category = element.text
      transactionList.append(t)

    return transactionList

  def stashTransactionData(self, transactionFilePath, transactions):
    root = et.Element("root")
  
    for t in transactions:
      trans = et.SubElement(root, "transaction") 
      name = et.SubElement(trans, "name") 
      amount = et.SubElement(trans, "amount") 
      date = et.SubElement(trans, "date")
      category = et.SubElement(trans, "category")

      name.text = t.name
      amount.text = str(t.amount)
      date.text = t.date
      category.text = t.category

    tree = et.ElementTree()
    tree._setroot(root)
    file = open(transactionFilePath, "w")
    tree.write(transactionFilePath)
    file.close()

class PersistentDataManager():

  def __init__(self):
    self.xmlAgent = xmlAgent()
    self.transactionList = None

  def retrievePersistentData(self, transactionFilePath):
    transactionTree = et.parse(transactionFilePath)
    self.transactionList = self.xmlAgent.parseTransactionData(transactionTree)

  def stashPersistentData(self, transactionFilePath, tList):
    self.xmlAgent.stashTransactionData(transactionFilePath, tList)

pdm = PersistentDataManager()
pdm.retrievePersistentData("userDataIn.xml")

t = Transaction("Rent")
t.initialize(amount=400.0, category="Rent")
t2 = Transaction("ACL")
t2.initialize(amount=600.0, category="Festivals")

tList = []
tList.append(t)
tList.append(t2)
pdm.stashPersistentData("userDataOut.xml", tList)
 