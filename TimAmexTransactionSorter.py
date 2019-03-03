import csv
from Category import Category

safeway = Category("Safeway", ["SAFEWAY"])
groceries = Category("Groceries", ["SAFEWAY","STARBUCK"])
bars = Category("Bars", ["MCLINTOCK","CREEKY","BULL'S","JAXSON","FROG & PEACH","BLUELIGHT","BARRELHOUSE"])
breakfast = Category("Breakfast",["HOMEGROWN", "GOOD EATS", "LINCOLNMARKETDELI"])
coffee = Category("Coffee", ["STARBUCK","SPECIALTYS","BLACKHORSE","PEET'S"])
restaurants = Category("Restaurants", ["PATRIOT HOUSE","CHIPOTLE","IN N OUT","SQ *","SOMA CHICKEN","DOMINO'S"])
movies = Category("Movies", ["Prime Video"])
pharmacy = Category("Pharmacy", ["WALGREENS"])
internet = Category("Cable/Internet", ["COMCAST"])

f = open('../TimFeb19.csv')
lines = f.readlines()

categories = [safeway,groceries,bars,breakfast,coffee,restaurants,movies,pharmacy,internet]

amount_charged = []
amount_paid = []
location_ = []
unhandled = []

for line in lines:
    num_strs = line.split(',')
    amount = num_strs[-1]
    amount = amount[:-1]
    location = num_strs[0]

    if float(amount) > 0:
      amount_charged.append(-1*float(amount))
      print("$" + amount + " was charged at " + location)
    elif float(amount) < 0:
      amount_paid.append(-1*float(amount))
      print("$" + amount + " was paid at " + location)

    location_.append(location)

    match = False
    for category in categories:
      if category.checkKeywords(location):
        category.addAmount(-1*float(amount))
        match = True

    if match == False:    
      unhandled.append(location)


total_charged = sum(amount_charged)
total_paid = sum(amount_paid)

fileName = "../CategoryGeneration.csv"
with open(fileName, 'w', newline='') as exportFile:
  w = csv.writer(exportFile, quoting=csv.QUOTE_ALL)

  print("Total charged: " + str(total_charged))
  w.writerow(["Total charged: " + str(total_charged)])
  print("Total paid: " + str(total_paid))
  w.writerow(["Total paid: " + str(total_paid)])

  print("Total unhandled rows: " + str(len(unhandled)))
  w.writerow(["Total unhandled rows: " + str(len(unhandled))])

  for category in categories:
    print(category.name + ": " + str(category.total))
    w.writerow([category.name,category.total])

  w.writerow([])
  w.writerow(["Unhandled Locations:"])

  for location in set(unhandled):
    print("[UNHANDLED LOCATION] " + location)
    w.writerow(["[UNHANDLED LOCATION]", location])

