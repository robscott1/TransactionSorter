import csv
import xlsxwriter
from ExcelManager import ExcelManager
from Category import Category

categoryFile = open('../Kevin Cash Flow Forecasting - Credit Card Charges.csv')
lines = categoryFile.readlines()

ExpectedCategories = {}

firstLine = True
for line in lines:
  if firstLine == True:
    firstLine = False
  else:
    listLine = line.split(',')
    categoryName = listLine[0]
    if listLine[3] != "":
      alottedAmt = float(listLine[3])
    else:
      alottedAmt = float(0)
    ExpectedCategories[categoryName] = alottedAmt
    # print(categoryName + ": $" + str(ExpectedCategories[categoryName]))

umbrellaInsurance =   Category("Umbrella Insurance")
autoTransportation =  Category("Auto Transportation Costs")
uberTransportation =  Category("Uber Transportation Costs")
autoRepairs =         Category("Auto Repairs")
autoRegistration =    Category("Auto Registration")
autoInsurance =       Category("Auto Insurance")
autoLoanPayment =     Category("Auto Loan Payment")
hbo =                 Category("Amazon Prime HBO")
tech =                Category("Technology Replace/Upgrade Costs")
essentials =          Category("Toiletries/Essentials", ["ROGUE"])
contacts =            Category("Contacts")
medicalOOP =          Category("Medical OoP Costs")
mdvip =               Category("MDVIP Membership")
payments =            Category("Online Payments", ["ONLINE PAYMENT","PAYPAL"])
safeway =             Category("Safeway", ["SAFEWAY"])
groceries =           Category("Groceries/Food/Sundry Items", ["SAFEWAY","STARBUCK","SPECIALTYS","BLACKHORSE","PEET'S"])
bars =                Category("Bars", ["MCLINTOCK","CREEKY","BULL'S","JAXSON",
  "FROG & PEACH","BLUELIGHT","BARRELHOUSE","MILK BAR","CORK N BOTTLE","CAMPUS BOTTLE"])
breakfast =           Category("Breakfast",["HOMEGROWN", "GOOD EATS", "LINCOLNMARKETDELI"])
coffee =              Category("Coffee", ["STARBUCK","SPECIALTYS","BLACKHORSE","PEET'S"])
restaurants =         Category("Restaurants", ["PATRIOT HOUSE","CHIPOTLE","IN N OUT",
  "SQ *","SOMA CHICKEN","DOMINO'S","TAQUERIA SANTA CRUZ","PRESSED","HOMEGROWN", "GOOD EATS", "LINCOLNMARKETDELI",
  "MEAT CO"])
movies =              Category("Movies", ["Prime Video"])
pharmacy =            Category("Prescription Drug Costs", ["WALGREENS"])
internet =            Category("Cable/Internet", ["COMCAST"])
entertainment =       Category("Entertainment", ["BROWNPAPERTICKETS","FISHER CATCH","MCLINTOCK","CREEKY","BULL'S","JAXSON",
  "FROG & PEACH","BLUELIGHT","BARRELHOUSE","MILK BAR","CORK N BOTTLE","CAMPUS BOTTLE"])
shopping =            Category("Clothes/Shoes (me)", ["ADIDAS","CALVIN KLEIN"])
amazon =              Category("Amazon Prime", ["Amzn","Amazon", "Prime Video"])
travel =              Category("Personal Travel/Vacation Costs", ["HOSTEL"])
total =               Category("Total")


categories = [umbrellaInsurance,
              groceries,
              autoTransportation,
              uberTransportation,
              autoRepairs,
              autoRegistration,
              autoInsurance,
              autoLoanPayment,
              internet,
              amazon,
              hbo,
              tech,
              essentials,
              shopping,
              contacts,
              pharmacy,
              medicalOOP,
              mdvip,
              travel,
              restaurants,
              entertainment,
              payments,
              total]

f = open('../Feb19.csv')
lines = f.readlines()


amount_charged = []
amount_paid = []
location_ = []
unhandled = []

for line in lines:
    num_strs = line.split(',')
    amount = num_strs[1]
    amount = amount[1:-1]
    location = num_strs[4]
    location = location[:-1]

    if float(amount) < 0:
      amount_charged.append(float(amount))
      print("$" + amount + " was charged at " + location)
    elif float(amount) > 0:
      amount_paid.append(float(amount))
      print("$" + amount + " was paid at " + location)

    location_.append(location)

    match = False
    for category in categories:
      if category.checkKeywords(location):
        category.addAmount(float(amount))
        match = True

    if match == False:    
      unhandled.append([location,float(amount)])


total_charged = sum(amount_charged)
total_paid = sum(amount_paid)

fileName = "../Feb19Report.xlsx"
with open(fileName, 'w', newline='') as exportFile:
  workbook = xlsxwriter.Workbook(fileName)
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
  

  
