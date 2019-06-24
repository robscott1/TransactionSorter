import csv
import xlsxwriter
from Category import Category
from Transaction import Transaction
from ExcelManager import ExcelManager

class SortingAgent():

  # takes completed transactions and are appended to 
  # the Category "completed transactoins" with any of 
  # the idKeywords matching the location of transaction
  # unhandled transactions (no matching keywords) are 
  # put into unhandled category object
  # GUI will allow user to assign unhandled transactions
  def categorize(self, completedTransactions, categories):
    for t in completedTransactions:
      match = False
      for category in categories.values():
        if category.checkKeywords(t.location) == True:
          category.registerCompletedTransaction(t)
          match = True
          break

      if match == False:
        categories["Unhandled"].registerCompletedTransaction(t)


  def execute(self, importFileName, categoryFileName, parser, categories):
    categoryFile = open(categoryFileName + ".csv")
    lines = categoryFile.readlines()

    ExpectedCategories = {}

    firstLine = True
    for line in lines:
      if firstLine == True:
        firstLine = False
      else:
        listLine = line.split(',')
        categoryName = listLine[0]
        if listLine[4] != "":
          alottedAmt = float(listLine[4])
        else:
          alottedAmt = float(0)

        ExpectedCategories[categoryName] = alottedAmt

    f = open(importFileName + ".csv")
    lines = f.readlines()
    
    amount_charged, amount_paid, unhandled = parser.execute(lines, categories)
    
    
    total_charged = sum(amount_charged)
    total_paid = sum(amount_paid)
    
    exportFileName = importFileName + "Report.xlsx"
    with open(exportFileName, 'w', newline='') as exportFile:
      workbook = xlsxwriter.Workbook(exportFileName)
      worksheet = workbook.add_worksheet()
      red_highlight = workbook.add_format()
      red_highlight.set_bg_color('red')
      bold_text = workbook.add_format({'bold': True})
      w = ExcelManager(worksheet)
    
      w.writerow(["Category Overview"], bold_text)
      w.writerow(["Status", "Expenditure Category", "Alotted Amount", "Amount Spent", "Delta"], bold_text)
    
      delta = total_charged + ExpectedCategories.get("Total")
      print("Total charged: " + str(total_charged))
      if delta >= 0:
        w.writerow([None, "Total charged:", ExpectedCategories.get("Total"), total_charged, delta])
      else:
        w.writerow([None, "Total charged:", ExpectedCategories.get("Total"), total_charged, delta], red_highlight)
    
      print("Total paid: " + str(total_paid))
      w.writerow([None, "Total paid:", None, total_paid])
    
      for key in ExpectedCategories:
        for category in categories:
          if key == category.name:
            delta = category.total + ExpectedCategories.get(key)
            if delta < 0:
              print( "OVER-SPENDING OCCURRED! Category: " + key + ", Delta: $" + str(delta) )
              w.writerow(["OVER-SPENDING OCCURRED!", key, ExpectedCategories.get(key), category.total, delta], red_highlight)
            else:
              print( "                        Category: " + key + ", Delta: $" + str(delta) )
              w.writerow([None, key, ExpectedCategories.get(key), category.total, delta])
    
      w.writerow()
      w.writerow(["ATTENTION: Kevin's awesome program did not find keyword matches for the following transactions:"], bold_text)  
      print("Total unhandled rows: " + str(len(unhandled)))
      w.writerow(["Total unhandled transactions: " + str(len(unhandled)) + " out of " + str(len(lines)) + " total"], bold_text)
    
      unaccountedSum = 0
      for pair in unhandled:
        print("[UNHANDLED LOCATION] " + pair[0] + ", Amount charged: " + str(pair[1]) )
        unaccountedSum += pair[1]
        w.writerow(["[UNHANDLED TRANSACTION]", "Location:", pair[0], "Amount:", pair[1]])
    
      print("Miscellaneous (Uncategorized amounts): " + str(unaccountedSum))
      w.writerow(["Miscellaneous (Uncategorized amounts):" + str(unaccountedSum)])
    
      workbook.close()