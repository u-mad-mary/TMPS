from abc import ABC, abstractmethod

# The Proxy Pattern provides a surrogate or placeholder for another object to control access to it. 

# Subject class
class PayOrder(ABC):
    @abstractmethod
    def pay_order(self):
        pass

# Real Subject
class Payment(PayOrder):
   def __init__(self):
       self.card = None
       self.account = None

   def has_funds(self):
       return True

   def get_account(self):
       self.account = self.card
       return self.account

   def set_card(self, number):
       print("The card with nr. " + str(number) + " was accepted.")
       self.card = number

   def pay_order(self):
       if self.has_funds():
           print("Payment made.\n")
       else:
           print("Payment rejected.\n")

# Proxy
class DebitCard(PayOrder):
    def __init__(self):
        self.payment = Payment()

    def pay_order(self):
        #number = input("Enter debit card number: ")
        number = '123456789'
        self.payment.set_card(number)
        return self.payment.pay_order()
