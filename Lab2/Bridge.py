from abc import ABC, abstractmethod
from Adapter import *
from Decorator import *
from Proxy import *

# Bridge design patternwhich splits the abstraction from the implementation.

# separates the abstraction for Ingredient and Alco, Alco Free classes that are used in the
# Adapter file with their implementations in separate classes,
# that are inherited by BLoodyMary and JuiceBased classes.

class Ingredient(ABC):
    
    @abstractmethod
    def __str__(self):
        pass
        
class Orange(Ingredient):
    
    def __init__(self):
        pass
    
    def __str__(self):
        return 'Orange'
        
class Tomato(Ingredient):
    
    def __init__(self):
        pass
    
    def __str__(self):
        return 'Tomato'   
    
   
class BloodyMary(AlcoDrink):
            
    def pay_order_in_advance(self):
        print("===The client orders a Bloody Mary.===\n")
        payment = DebitCard()
        payment.pay_order()
               
    def glass_type(self):
        glass = BasicCocktailGlass()
        client_code_alco(glass)
        
    def print_name(self):
        print(str(self.ingredient) + ' and ' + str(self.item) + ' are used for making Bloody Mary.')
        
       
class JuiceBased(AlcoholFreeDrink):
       
    def pay_order_in_advance(self):
        print("===The client orders a Juice Based drink.===\n")
        payment = DebitCard()
        payment.pay_order()
        
    def glass_type(self):
        glass = BasicCocktailGlass()
        client_code_non_alco(glass)
        
    def print_name(self):
        print(str(self.ingredient) + ' and ' + str(self.item) + ' are used for making a Juice Based Drink.')
        

