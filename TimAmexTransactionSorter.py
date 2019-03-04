import csv
import xlsxwriter
from ExcelManager import ExcelManager
from Category import Category
from Sorter import Sorter
from TimAmexApp import TimAmexApp

sorter = Sorter()

app = TimAmexApp(sorter)

app.run()
