# Structural Design Patterns

## Objectives:

* Get familiar with the Structural Design Patterns;
* Implement at least 5 SDPs for a specific domain;

## Used Design Patterns:

* Adapter
* Bridge
* Decorator
* Facade
* Proxy


## Implementation
The design patterns mentioned above have been implemented in a context of making a drink by a barman, where the client may request an alcohol-free drink or one that contains alcohol, for example Bloody Mary.


### Adapter Pattern 

This pattern involves a single class (Adapter) which is responsible to join functionalities of independent or incompatible interfaces.

One class is meant for alcoholic drinks:
```python
class AlcoDrink(Alco):
    
    def __init__(self, item, ingredient):
        self.item = item
        self.ingredient = ingredient

    def is_alcohol(self):
        if isinstance(self, AlcoDrink):
            return f'{self.ingredient} contains alcohol.'
        else:
            return f'{self.ingredient} does not contain alcohol.'
```
And another one is dedicated for alcohol-free drinks:

```python
class AlcoholFreeDrink(AlcoholFree):
    
    def __init__(self, item, ingredient):
        self.item = item
        self.ingredient = ingredient

    def is_alcoFree(self):
        if isinstance(self, AlcoholFreeDrink):
            return f'{self.ingredient} does not contain alcohol'
        else:
            return f'{self.ingredient} contains alcohol'
```
The Adapter Class, showed below, permits the use of alcohol-free ingredients as the ones that are alcoholic.

```python
class Adapter(AlcoDrink):
    
    def __init__(self, item, stuff: AlcoholFree):
        self.item = item
        self.stuff = stuff
        self.ingredient = stuff.ingredient

    def is_alcohol(self):
        if isinstance(self, AlcoDrink):
            return f'{self.stuff.is_alcoFree()}, it is a non alcoholic liquid that will be added with {self.item} into the drink.'
        else:
            return f'{self.ingredient} is alcohol free.'
```

In the main file is created an alcohol-free drink that is passed to the adapter:
```pyhton
    alcoFree = JuiceBased(ing,'Sprite')
      
    adapter = Adapter(ing, alcoFree)

    check_alcoFree_is_alco = adapter.is_alcohol()
    pour_alcoFree = adapter.pour_alcohol()
    add_alcoFree = adapter.add_to_alco()

    print(check_alcoFree_is_alco)
    print(pour_alcoFree)
    print(add_alcoFree)

```

The program outputs the following:
```text
Sprite and Orange are used for making a Juice Based Drink.

Sprite does not contain alcohol, it is a non alcoholic liquid that will be added with 
Orange into the drink.
Sprite is poured into the shaker.
Orange is added into the drink.
```

In case of making an alcoholic drink will be executed the following code:

```python
    bm = BloodyMary(ingl,'Vodka')   
    client_code(bm) #client code for making an alco drink
```
Outputting:

```text
Vodka and Tomato are used for making Bloody Mary.
Vodka contains alcohol.
Tomato is added into the drink.
Shaking ...
Pouring into the glass...
Adding Ice...

The drink is ready to be consumed.
```

### Bridge Pattern

Bridge design pattern splits the abstraction from the implementation.

In this implementation, it separates the abstraction for Ingredient and Alco, Alco Free classes that are used in the *Adapter* file with their implementations in separate classes.

Below can be seen the Ingredient class that is used by two classes for particular ingredients:

```python
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
```
The last two classes will be used in main file for defining ingredients as following:
```python
ing = Orange()
ingl = Tomato()
```
The Alco and AlcoFree classes are used through AlcoDrink and AlcoFreeDrink  classes from the *Adapter* file, that are inherited by BloodyMary and JuiceBased classes, that will be showed later.

### Decorator Pattern

Decorator is a structural pattern that allows adding new behaviors to objects dynamically by placing them inside special wrapper objects, called decorators.

It was used for attributing types of glasses according to the alcoholic or alcohol-free drinks.

There was implemented one base decorator that returns a simple cocktail glass by default:

```python
class BaseDecorator(CocktailGlass):
    
    def __init__(self, default_glass: CocktailGlass):
        self._default_glass = default_glass

    @property
    def default_glass(self):
        return self._default_glass

    def type(self):
        return self._default_glass.type()
```

In order to set a glass type for alcoholic drinks was made, another decorator:

```python
class AlcoDecorator(BaseDecorator)
    def type(self):
        alco_glass = 'Snifter'
        return f'Instead of a simple {self.default_glass.type()} the barman uses a {alco_glass}.\n'
```
And for non-alcoholic drinks, another one:

```python
class NonAlcoDecorator(BaseDecorator):
    def type(self):
        non_alco_glass = 'Delmonico'
        return f'Instead of a simple {self.default_glass.type()} the barman uses a {non_alco_glass}.\n'
```
These decorators are called through client codes:

```python
def client_code_base(basic_glass: CocktailGlass):
    base_decorator = BaseDecorator(basic_glass)
    print(base_decorator.type())

def client_code_non_alco(basic_glass: CocktailGlass):
    non_alco_decorator = NonAlcoDecorator(basic_glass)
    print(non_alco_decorator.type())

def client_code_alco(basic_glass: CocktailGlass):
    alco_decorator = AlcoDecorator(basic_glass)
    print(alco_decorator.type())

```
The client codes are used in method glass_type() of the BloodyMary and JuiceBased classes from the *Bridge* file.

```python
class BloodyMary(AlcoDrink):
       ...
    def glass_type(self):
        glass = BasicCocktailGlass()
        client_code_alco(glass)
       
class JuiceBased(AlcoholFreeDrink):
       ...
    def glass_type(self):
        glass = BasicCocktailGlass()
        client_code_non_alco(glass)
```


### Facade Pattern

Facade pattern provides a simpler unified interface to a more complex system. The word Facade means the face of a building or particularly an outer lying interface of a complex system, consists of several sub-systems.

In this project Facade is used to simulate the process of preparation of a drink, through DrinkPreparation class:

```python
class DrinkPreparation:  
    def __init__(self):
        self.shake = Shake()
        self.pour = Pour()
        self.ice = Ice()
 
    def startPreparation(self):
        self.shake.shake()
        self.pour.pour()
        self.ice.add_ice()        
```
Where Shake(), Pour() and Ice() classes represent the subsystems:

Facade is called in the method prepare() from the Adapter class:

```python
class Adapter(AlcoDrink):
    ...    
    def prepare(self):
        prep = DrinkPreparation()
        prep.startPreparation()
        print('\nThe drink is ready to be consumed.\n')
```
And in the client code for preparing the alcoholic drinks:

```python
def client_code(AlcoDrink: Alco):
    ...     
    prep = DrinkPreparation()
    prep.startPreparation()
    print('\nThe drink is ready to be consumed.\n')
```

The result is the following:

```text
Shaking ...
Pouring into the glass...
Adding Ice...

The drink is ready to be consumed.
```
### Proxy Pattern

The Proxy Pattern provides a surrogate or placeholder for another object to control access to it.

In this project, the pattern is used for order payments:

```python
class DebitCard(PayOrder):
    def __init__(self):
        self.payment = Payment()

    def pay_order(self):
        #number = input("Enter debit card number: ")
        number = '123456789'
        self.payment.set_card(number)
        return self.payment.pay_order()
 ```
Returning:
```text
The card with nr. 123456789 was accepted.
Payment made.
```

 The subject class is represented by:
```python
class PayOrder(ABC):
    @abstractmethod
    def pay_order(self):
        pass
```
And the Real Subject used by the proxy is the following one:

```python
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
```
The proxy class is called in the method pay_order_in_advance() of the BloodyMary and JuiceBased classes from the *Bridge* file:

```python
class BloodyMary(AlcoDrink): 
    def pay_order_in_advance(self):
        print("===The client orders a Bloody Mary.===\n")
        payment = DebitCard()
        payment.pay_order()
    ...    
       
class JuiceBased(AlcoholFreeDrink): 
    def pay_order_in_advance(self):
        print("===The client orders a Juice Based drink.===\n")
        payment = DebitCard()
        payment.pay_order()      
    ...       
```
## Conclusions/Results

The results of the mentioned implementation of different Structural Design Patterns can be viewed after running the ```main.py``` file, the output should be the following:

```
===The client orders a Bloody Mary.===

The card with nr. 123456789 was accepted.
Payment made.

Vodka and Tomato are used for making Bloody Mary.
Instead of a simple Cocktail Glass the barman uses a Snifter.

Vodka contains alcohol.
Vodka is poured into the shaker.
Tomato is added into the drink.
Shaking ...
Pouring into the glass...
Adding Ice...

The drink is ready to be consumed.

===The client orders a Juice Based drink.===

The card with nr. 123456789 was accepted.
Payment made.

Sprite and Orange are used for making a Juice Based Drink.
Instead of a simple Cocktail Glass the barman uses a Delmonico.

Sprite does not contain alcohol, it is a non alcoholic liquid that will be added with 
Orange into the drink.
Sprite is poured into the shaker.
Orange is added into the drink.
Shaking ...
Pouring into the glass...
Adding Ice...

The drink is ready to be consumed.
```
Here the client makes an order, paying in advance through the method which implements the *Proxy* design pattern, used by BloodyMary and JuiceBased classes from the *Bridge*, that outputs which ingredients are used for making a specific drink. Next is used *Decorator* for setting the type of the glass in what the drink will be poured. The *Adapter* pattern is used when there is the need to adapt non-alcoholic ingredients to alcoholic ones. *Facade* is used to show the process of making a drink.

This laboratory work was useful because it got me more familiar with Structural Design Patterns that I intend to use further.
