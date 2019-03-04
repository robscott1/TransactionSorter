class Category():

  def __init__(self, name, keywords=[]):
    self.name = name
    self.keywords = keywords
    self.total = 0

  def addAmount(self, amt):
    self.total += amt

  def containsWord(self,phrase,word):
    return word in phrase

  def checkKeywords(self, location):
    for keyword in self.keywords:
      if self.containsWord(location.casefold(),keyword.casefold()):
        return True
    return False
