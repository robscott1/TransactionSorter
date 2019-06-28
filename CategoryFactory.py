from APIData import CategoryData
from Category import Category

class CategoryFactory():

  def createCategory(self, data):
    return Category(data.name, monthlyAllotment = float(data.monthlyAllotment), keywords = data.idKeywords)