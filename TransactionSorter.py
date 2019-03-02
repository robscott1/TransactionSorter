import csv

def contains_word(phrase,word):
  return word in phrase

f = open('Feb19.csv')
lines = f.readlines()

categories = {
  "Safeway": [],
  "Starbucks": []

}

amount_charged = []
amount_paid = []
location_ = []
unhandled = []
safeway = []

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
    if contains_word(location,"SAFEWAY"):
      categories.get("Safeway").append(float(amount))
    elif contains_word(location,"STARBUCK"):
      categories.get("Starbucks").append(float(amount))
    else:
      unhandled.append([amount,location])


total_charged = sum(amount_charged)
total_paid = sum(amount_paid)
print("Total charged: " + str(total_charged))
print("Total paid: " + str(total_paid))

for key in categories:
  print("Total charged at " + key + ": " + str(sum(categories.get(key))))

for pair in unhandled:
  print("[UNHANDLED ROW] " + "Location: " + pair[1] + ", Amount: " + pair[0])

print("Total unhandled rows: " + str(len(unhandled)))