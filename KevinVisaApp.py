import csv
import xlsxwriter
from ExcelManager import ExcelManager
from Category import Category
from Sorter import Sorter

class KevinVisaApp():

  def __init__(self, sorter):
    self.sorter = sorter
    self.parser = Parser()

    self.umbrellaInsurance =   Category("Umbrella Insurance")
    self.autoTransportation =  Category("Auto Transportation Costs")
    self.uberTransportation =  Category("Uber Transportation Costs")
    self.autoRepairs =         Category("Auto Repairs")
    self.autoRegistration =    Category("Auto Registration")
    self.autoInsurance =       Category("Auto Insurance")
    self.autoLoanPayment =     Category("Auto Loan Payment")
    self.hbo =                 Category("Amazon Prime HBO")
    self.tech =                Category("Technology Replace/Upgrade Costs")
    self.essentials =          Category("Toiletries/Essentials", ["ROGUE"])
    self.contacts =            Category("Contacts", ["SARATOGA VISION"])
    self.medicalOOP =          Category("Medical OoP Costs", ["LABCORP"])
    self.mdvip =               Category("MDVIP Membership")
    self.payments =            Category("Online Payments", ["ONLINE PAYMENT","PAYPAL"])
    self.safeway =             Category("Safeway", ["SAFEWAY"])
    self.groceries =           Category("Groceries/Food/Sundry Items", ["SAFEWAY","STARBUCK","SPECIALTYS","BLACKHORSE","PEET'S","SOBERDOUGH"])
    self.bars =                Category("Bars", ["MCLINTOCK","CREEKY","BULL'S","JAXSON",
      "FROG & PEACH","BLUELIGHT","BARRELHOUSE","MILK BAR","CORK N BOTTLE","CAMPUS BOTTLE","BRIXTON"])
    self.breakfast =           Category("Breakfast",["HOMEGROWN", "GOOD EATS", "LINCOLNMARKETDELI"])
    self.coffee =              Category("Coffee", ["STARBUCK","SPECIALTYS","BLACKHORSE","PEET'S"])
    self.restaurants =         Category("Restaurants", ["PATRIOT HOUSE","CHIPOTLE","IN N OUT",
      "SQ *","SOMA CHICKEN","DOMINO'S","TAQUERIA SANTA CRUZ","PRESSED","HOMEGROWN", "GOOD EATS", "LINCOLNMARKETDELI",
      "MEAT CO","THE BIRD","JOANNAS","IRISH TIMES","GAMBINOS","SPECIALTY'S"])
    self.movies =              Category("Movies", ["Prime Video"])
    self.pharmacy =            Category("Prescription Drug Costs", ["WALGREENS"])
    self.internet =            Category("Cable/Internet", ["COMCAST"])
    self.entertainment =       Category("Entertainment", ["BROWNPAPERTICKETS","FISHER CATCH","MCLINTOCK","CREEKY","BULL'S","JAXSON",
      "FROG & PEACH","BLUELIGHT","BARRELHOUSE","MILK BAR","CORK N BOTTLE","CAMPUS BOTTLE","BRIXTON","BLUE LIGHT","MEZZANINE",
      "STUBHU","FIELDWORK","RUSSIAN RIVER"])
    self.laundry =             Category("Laundry", ["LAUNDRY"])
    self.shopping =            Category("Clothes/Shoes (me)", ["ADIDAS","CALVIN KLEIN","CONVERSE","LEVI","POLO","LULULEMON","RUNNER'S MIND"])
    self.amazon =              Category("Amazon Prime", ["Amzn","Amazon", "Prime Video"])
    self.travel =              Category("Personal Travel/Vacation Costs", ["HOSTEL","TRIP.COM","VIETJET","UNITED","SWISS INTL","THAI SKY","ALASKA AIR"])
    self.workExpense =         Category("Work Expenses", ["AUTOMATIONDIRECT"])
    self.total =               Category("Total")
    
    
    self.categories = [self.umbrellaInsurance,
                       self.groceries,
                       self.autoTransportation,
                       self.uberTransportation,
                       self.autoRepairs,
                       self.autoRegistration,
                       self.autoInsurance,
                       self.autoLoanPayment,
                       self.internet,
                       self.amazon,
                       self.hbo,
                       self.tech,
                       self.essentials,
                       self.laundry,
                       self.shopping,
                       self.contacts,
                       self.pharmacy,
                       self.medicalOOP,
                       self.mdvip,
                       self.travel,
                       self.restaurants,
                       self.entertainment,
                       self.workExpense,
                       self.payments]

  def run(self):
    self.sorter.execute("../KevinVisaMarch2019", "../Kevin Cash Flow Forecasting - Credit Card Charges", self.parser, self.categories)


class Parser():

  def execute(self, lines, categories):
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

    return amount_charged, amount_paid, unhandled


sorter = Sorter()

app = KevinVisaApp(sorter)

app.run()

