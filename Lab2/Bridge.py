from abc import ABC, abstractmethod
from Adapter import *
from Decorator import *
from Proxy import *

# Bridge design pattern allows us to separate the Implementation Specific Abstractions and 
# Implementation Independent Abstractions from each other and can be developed considering as single entities.

# separate class hierarchy for Ingredient and Alco, Alco Free classes


# Alco class interface used
class Alco(ABC):
    
    @abstractmethod
    def is_alcohol():
        pass

    @abstractmethod
    def pour_alcohol():
        pass

# AlcoholFreeDrink class interface
class AlcoholFree(ABC):
    
    @abstractmethod
    def is_alcoFree():
        pass

    @abstractmethod
    def pour_liquid():
        pass

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
    
# Alco class interface used
class Alco(ABC):
    
    @abstractmethod
    def is_alcohol():
        pass

    @abstractmethod
    def pour_alcohol():
        pass


# AlcoholFreeDrink class interface
class AlcoholFree(ABC):
    
    @abstractmethod
    def is_alcoFree():
        pass

    @abstractmethod
    def pour_liquid():
        pass
    
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
        

