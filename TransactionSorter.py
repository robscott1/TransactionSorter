import csv
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
    alottedAmt = listLine[3]
    ExpectedCategories[categoryName] = alottedAmt
    print(categoryName + ": $" + ExpectedCategories[categoryName])

umbrellaInsurance =   Category("Umbrella Insurance")
autoTransportation =  Category("Auto Transportation Costs")
uberTransportation =  Category("Uber Transportation Costs")
autoRepairs =         Category("Auto Repairs")
autoRegistration =    Category("Auto Registration")
autoInsurance =       Category("Auto Insurance")
autoLoanPayment =     Category("Auto Loan Payment")
hbo =                 Category("Amazon Prime HBO")
tech =                Category("Technology Replace/Upgrade Costs")
essentials =          Category("Toiletries/Essentials")
contacts =            Category("Contacts")
medicalOOP =          Category("Medical OoP Costs")
mdvip =               Category("MDVIP Membership")
payments =            Category("Online Payments", ["ONLINE PAYMENT","PAYPAL"])
safeway =             Category("Safeway", ["SAFEWAY"])
groceries =           Category("Groceries/Food/Sundry Items", ["SAFEWAY","STARBUCK"])
bars =                Category("Bars", ["MCLINTOCK","CREEKY","BULL'S","JAXSON",
  "FROG & PEACH","BLUELIGHT","BARRELHOUSE","MILK BAR","CORK N BOTTLE","CAMPUS BOTTLE"])
breakfast =           Category("Breakfast",["HOMEGROWN", "GOOD EATS", "LINCOLNMARKETDELI"])
coffee =              Category("Coffee", ["STARBUCK","SPECIALTYS","BLACKHORSE","PEET'S"])
restaurants =         Category("Restaurants", ["PATRIOT HOUSE","CHIPOTLE","IN N OUT",
  "SQ *","SOMA CHICKEN","DOMINO'S","TAQUERIA SANTA CRUZ","PRESSED"])
movies =              Category("Movies", ["Prime Video"])
pharmacy =            Category("Prescription Drug Costs", ["WALGREENS"])
internet =            Category("Cable/Internet", ["COMCAST"])
entertainment =       Category("Entertainment", ["BROWNPAPERTICKETS","FISHER CATCH"])
shopping =            Category("Clothes/Shoes (me)", ["ADIDAS","CALVIN KLEIN"])
amazon =              Category("Amazon Prime", ["Amzn","Amazon"])
travel =              Category("Personal Travel/Vacation Costs", ["HOSTEL"])


categories = [umbrellaInsurance,
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
              entertainment]

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

fileName = "../CategoryGeneration.csv"
with open(fileName, 'w', newline='') as exportFile:
  w = csv.writer(exportFile, quoting=csv.QUOTE_ALL)

  print("Total charged: " + str(total_charged))
  print("Total paid: " + str(total_paid))

  print("Total unhandled rows: " + str(len(unhandled)))

  for category in categories:
    print(category.name + ": " + str(category.total))
    w.writerow([category.name,category.total])

  w.writerow(["Unhandled Locations:"])

  unaccountedSum = 0
  for pair in unhandled:
    print("[UNHANDLED LOCATION] " + pair[0] + ", Amount charged: " + str(pair[1]) )
    unaccountedSum += pair[1]
    w.writerow([location])

  print("Miscellaneous: " + str(unaccountedSum))

