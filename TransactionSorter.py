import csv
from Category import Category

payments = Category("Online Payments", ["ONLINE PAYMENT","PAYPAL"])
safeway = Category("Safeway", ["SAFEWAY"])
groceries = Category("Groceries", ["SAFEWAY","STARBUCK"])
bars = Category("Bars", ["MCLINTOCK","CREEKY","BULL'S","JAXSON",
  "FROG & PEACH","BLUELIGHT","BARRELHOUSE","MILK BAR","CORK N BOTTLE","CAMPUS BOTTLE"])
breakfast = Category("Breakfast",["HOMEGROWN", "GOOD EATS", "LINCOLNMARKETDELI"])
coffee = Category("Coffee", ["STARBUCK","SPECIALTYS","BLACKHORSE","PEET'S"])
restaurants = Category("Restaurants", ["PATRIOT HOUSE","CHIPOTLE","IN N OUT",
  "SQ *","SOMA CHICKEN","DOMINO'S","TAQUERIA SANTA CRUZ","PRESSED"])
movies = Category("Movies", ["Prime Video"])
pharmacy = Category("Pharmacy", ["WALGREENS"])
internet = Category("Internet", ["COMCAST"])
entertainment = Category("Entertainment", ["BROWNPAPERTICKETS","FISHER CATCH"])
shopping = Category("Clothes/Shoes", ["ADIDAS","CALVIN KLEIN"])
amazon = Category("Amazon", ["Amzn","Amazon"])
travel = Category("Personal Travel/Vacation", ["HOSTEL"])


f = open('../Feb19.csv')
lines = f.readlines()

categories = [payments,safeway,groceries,bars,breakfast,coffee,restaurants,movies,
              pharmacy,internet,entertainment,shopping,amazon,travel]

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



# fileName = "../CategoryGeneration.csv"
# with open(fileName, 'w', newline='') as exportFile:
#   w = csv.writer(exportFile, quoting=csv.QUOTE_ALL)
#   for category in categories:
#     w.writerow([category.name,category.total])
