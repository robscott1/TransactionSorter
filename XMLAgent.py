class xmlAgent():

  '''
  This is a sub module of the PersistentDataManager. Any time a 
  category or planned transaction is made, this module will
  write it into an xml file. Any time the user opens the
  application again, the data saved in the .xml can be retrieved,
  providing continuity of planning and analysis for the user
  over time.
  '''
  
  def parseTransactionData(self, tree):
    root = tree.getroot()
    transactionList = []
    for transaction in root:
      t = TransactionData()
      for element in transaction:
        if element.tag == "name":
          t.name = element.text
        elif element.tag == "amount":
          t.amount = float(element.text)
        elif element.tag == "date":
          t.date = element.text
        elif element.tag == "category":
          t.category = element.text
        elif element.tag == "priority":
          t.priority = element.text
        elif element.tag == "rateOfRecurrence":
          t.rateOfRecurrence = element.text
        elif element.tag == 'paymentMethod':
          t.paymentMethod = element.text

      transactionList.append(t)

    return transactionList

  # same as above, parses the categories
  def parseCategoryData(self, tree):
    root = tree.getroot()
    categoryList = []
    for category in root:
      c = CategoryData()
      for element in category:
        if element.tag == "name":
          c.name = element.text
        elif element.tag == "monthlyAllotment":
          c.monthlyAllotment = element.text
        elif element.tag == "idKeywords":
          keywords = []
          for keyword in element:
            keywords.append(keyword.text)
          c.idKeywords = keywords

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
      priority = et.SubElement(trans, "priority")
      rateOfRecurrence = et.SubElement(trans, "rateOfRecurrence")
      paymentMethod = et.SubElement(trans, "paymentMethod")

      name.text = t.name
      amount.text = str(t.amount)
      date.text = t.date
      category.text = t.category
      priority.text = t.priority
      rateOfRecurrence.text = t.rateOfRecurrence
      paymentMethod.text = t.paymentMethod

    tree = et.ElementTree()
    tree._setroot(root)
    file = open(transactionFilePath, "w")
    tree.write(transactionFilePath)
    file.close()

  def stashCategoryData(self, categoryFilePath, categories):
    root = et.Element("root")
  
    for c in categories:
      if c.name != "Unhandled":
        cat = et.SubElement(root, "category") 
        name = et.SubElement(cat, "name") 
        name.text = c.name
        monthlyAllotment = et.SubElement(cat, "monthlyAllotment")
        monthlyAllotment.text = str(c.monthlyAllotment)
        idKeywords = et.SubElement(cat, "idKeywords")
        if c.keywords != None:
          for key in c.keywords:
            keyword = et.SubElement(idKeywords, "keyword")
            keyword.text = key

    tree = et.ElementTree()
    tree._setroot(root)
    file = open(categoryFilePath, "w")
    tree.write(categoryFilePath)
    file.close()
