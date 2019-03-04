import csv
import xlsxwriter
from ExcelManager import ExcelManager
from Category import Category
from Sorter import Sorter
from KevinVisaApp import KevinVisaApp

sorter = Sorter()

app = KevinVisaApp(sorter)

app.run()

  
