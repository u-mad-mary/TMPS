from Facade import *
from Bridge import Alco, AlcoholFree

# This pattern involves a single class which is responsible to join functionalities 
# of independent or incompatible interfaces. 


class AlcoDrink(Alco):
    
    def __init__(self, item, ingredient):
        self.item = item
        self.ingredient = ingredient

    def is_alcohol(self):
        if isinstance(self, AlcoDrink):
            return f'{self.ingredient} contains alcohol.'
        else:
            return f'{self.ingredient} does not contain alcohol.'

    def pour_alcohol(self):
        return f'{self.ingredient} is poured into the shaker.'

    def add_to_alco(self):
        return f'{self.item} is added into the drink.'


class AlcoholFreeDrink(AlcoholFree):
    
    def __init__(self, item, ingredient):
        self.item = item
        self.ingredient = ingredient

    def is_alcoFree(self):
        if isinstance(self, AlcoholFreeDrink):
            return f'{self.ingredient} does not contain alcohol'
        else:
            return f'{self.ingredient} contains alcohol'

    def pour_liquid(self):
        return f'{self.ingredient} is poured into the shaker.'

    def add_to_drink(self):
        pass


class Adapter(AlcoDrink):
    
    def __init__(self, item, stuff: AlcoholFree):
        self.item = item
        self.stuff = stuff
        self.ingredient = stuff.ingredient

    def is_alcohol(self):
        if isinstance(self, AlcoDrink):
            return f'{self.stuff.is_alcoFree()}, it is a non alcoholic liquid that will be added with {self.item} into the drink.'
        else:
            return f'{self.ingredient} is a totally alcohol free drink.'
    
    def prepare(self):
        prep = DrinkPreparation()
        prep.startPreparation()
        print('\nThe drink is ready to be consumed.\n')


# The barman will make a drink that contains alcohol via Alco Class interface
def client_code(AlcoDrink: Alco):
    check_alco = AlcoDrink.is_alcohol()
    pour_alco = AlcoDrink.pour_alcohol()
    add_alco = AlcoDrink.add_to_alco()
      
    prep = DrinkPreparation()
    print(check_alco)
    print(pour_alco)
    print(add_alco)
    prep.startPreparation()
    print('\nThe drink is ready to be consumed.\n')


