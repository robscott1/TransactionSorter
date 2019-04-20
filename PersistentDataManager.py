import xml.etree.ElementTree as et
from Transaction import Transaction
from Category import Category

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

  def parseCategoryData(self, tree):
    root = tree.getroot()
    categoryList = []
    for category in root:
      c = Category( category.findtext("name") )
      for element in category:
        if element.tag == "idkeywords":
          keywords = []
          for keyword in element:
            keywords.append(keyword.text)
          c.keywords = keywords

      categoryList.append(c)

    return categoryList

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

  def stashCategoryData(self, categoryFilePath, categories):
    root = et.Element("root")
  
    for c in categories:
      cat = et.SubElement(root, "category") 
      name = et.SubElement(cat, "name") 
      name.text = c.name
      idkeywords = et.SubElement(cat, "idkeywords")
      for key in c.keywords:
        keyword = et.SubElement(idkeywords, "keyword")
        keyword.text = key

    tree = et.ElementTree()
    tree._setroot(root)
    file = open(categoryFilePath, "w")
    tree.write(categoryFilePath)
    file.close()

class PersistentDataManager():

  def __init__(self):
    self.xmlAgent = xmlAgent()
    self.transactionList = None

  def retrievePersistentData(self, transactionFilePath, categoryFilePath):
    transactionTree = et.parse(transactionFilePath)
    self.transactionList = self.xmlAgent.parseTransactionData(transactionTree)

    categoryTree = et.parse(categoryFilePath)
    self.categoryList = self.xmlAgent.parseCategoryData(categoryTree)

    return self.transactionList, self.categoryList

  def stashPersistentData(self, transactionFilePath, categoryFilePath, tList, cList):
    # self.xmlAgent.stashTransactionData(transactionFilePath, tList)
    self.xmlAgent.stashCategoryData(categoryFilePath, cList)

pdm = PersistentDataManager()
pdm.retrievePersistentData("userDataIn.xml", "categoryDataIn.xml")
for category in pdm.categoryList:
  print(category.name)
  print(category.keywords)

# t = Transaction("Rent")
# t.initialize(amount=400.0, category="Rent")
# t2 = Transaction("ACL")
# t2.initialize(amount=600.0, category="Festivals")

# tList = []
# tList.append(t)
# tList.append(t2)
pdm.stashPersistentData("userDataOut.xml", "categoryDataOut.xml", pdm.transactionList, pdm.categoryList)
 