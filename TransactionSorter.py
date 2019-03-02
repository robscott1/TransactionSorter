import csv
from Category import Category

def contains_word(phrase,word):
  return word in phrase

safeway = Category("Safeway", ["SAFEWAY"])
groceries = Category("Groceries", ["SAFEWAY","STARBUCK"])
bars = Category("Bars", ["MCLINTOCK","CREEKY","BULL'S","JAXSON","FROG & PEACH","BLUELIGHT","BARRELHOUSE"])
breakfast = Category("Breakfast",["HOMEGROWN", "GOOD EATS", "LINCOLNMARKETDELI"])
coffee = Category("Coffee", ["STARBUCK","SPECIALTYS","BLACKHORSE","PEET'S"])
restaurants = Category("Restaurants", ["PATRIOT HOUSE","CHIPOTLE","IN N OUT","SQ *","SOMA CHICKEN","DOMINO'S"])
movies = Category("Movies", ["Prime Video"])
pharmacy = Category("Pharmacy", ["WALGREENS"])
internet = Category("Internet", ["COMCAST"])

f = open('../Feb19.csv')
lines = f.readlines()

categories = [safeway,groceries,bars,breakfast,coffee,restaurants,movies,pharmacy,internet]

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
      unhandled.append(location)


total_charged = sum(amount_charged)
total_paid = sum(amount_paid)
print("Total charged: " + str(total_charged))
print("Total paid: " + str(total_paid))

print("Total unhandled rows: " + str(len(unhandled)))

for category in categories:
  print(category.name + ": " + str(category.total))

for location in set(unhandled):
  print("[UNHANDLED LOCATION] " + location)