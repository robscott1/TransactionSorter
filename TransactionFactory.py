from APIData import TransactionData
from Transaction import Transaction

class TransactionFactory():

  def createTransaction(self, data):
    transaction = Transaction(data.name)
    transaction.initialize(date=data.date, category=data.category, amount=data.amount,
                           idKeywords=data.idKeywords, recurring=data.recurring, 
                           rateOfRecurrence=data.rateOfRecurrence)
    return transaction

  def createCompletedTransaction(self, data):
    transaction = Transaction()
    transaction.initialize(amount=data.amount, location=data.location)
    return transaction