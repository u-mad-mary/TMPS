# Behavioural Design Patterns


## Objectives:

* Get familiar with the Behavioural Design Patterns;
* Implement at least 5 BDPs for a specific domain;

## Used Design Patterns:

* State
* Visitor
* Strategy
* Command
* Chain of Responsibilities


## Implementation

The design patterns mentioned above have been implemented in a context of a Cocktail Bar, where the client may request an alcohol-free drink or one that contains alcohol, making the order by speaking with the waiter or with the barman. 


### Chain of  Responsibilities

It is a behavioural design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

This pattern involves an interface for handlers named "Handler" and an "AbstractHandler" for the concrete ones. Below can be seen the concrete handlers, the first one being "newWaiter" which represents an intern at the Cocktail Bar that is getting accustomed to the bar and doesn't know yet the whole menu, so he can't take customers' orders.
```python
class newWaiter(AbstractHandler):
    
    def handle(self, order):
        if self.can_take_order:
            return 'The new waiter took your order and ensured you that it will be done soon.'
        else:
            print("The new waiter can't take your order, try approaching the experienced one.")
            return super().handle(order)
```
If the Client tries to approach him, he would not be able to make the order and will be passed one of the following concrete handlers:
```python
class Waiter(AbstractHandler):
    can_take_order = True
    
    def handle(self, order):
        if self.can_take_order:
            return 'Waiter took your order.'
        else:
            print('Waiter can\'t take your order, he is busy with another table, try ordering from the bar.')
            return super().handle(order)
```
The employed waiter is able to take the order and will eventually pass it to the barman, who can also take orders and make customer's drinks.
```python
class Barman(AbstractHandler):
    can_take_order = True
    
    def handle(self, order):
        if self.can_take_order:
            return 'The barman took your order.'
        else:
            return super().handle(order)
```
This pattern is also used in command method, which is responsible for handling an active order of a Waiter or Barman.

### Command Method

It is a behavioural design pattern that encapsulates a request as an object, thereby allowing for the parameterization of clients with different requests and the queuing or logging of requests.

Everything starts with an interface, in this case with a concrete commands interface which holds the "order" method.

The process of a customer order is the following, the Customer sends the command (order):

```python
class Customer:
    def __init__(self, command: Command):
        self._command = command

    def order_command(self):
        return self._command.order()
```
There are two command receivers Barman and Waiter that are responsible for receiving the order. The Barman can take the order and make drinks:

```python
class BarmanRecieve(Barman):     
    @staticmethod
    def take_order():
        return Barman().handle('order')
    
    @staticmethod
    def make_drink():
        return 'The barman started to prepare your drink.'

```
And the waiter can only take the orders:
```python
class WaiterRecieve(Waiter):
    @staticmethod
    def take_order():
        return Waiter().handle('order')
```
The concrete commands which are performed in the process of ordering are OrderBar and OrderWaiter which simulates the actions made by getting the order.

```python
class OrderBar(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def order(self):
        return self._receiver.make_drink()


class OrderWaiter(Command):
    def __init__(self, receiver):
        self._receiver = receiver

    def order(self):
        return self._receiver.take_order()
```
So if a person orders from bar, or the waiter will pass the order from a table to the bar, will be started the process of making a drink, otherwise the order will be taken and the customer informed. The types of drinks that can be made during the order are listed in the strategy pattern.

### Strategy Pattern

It is a behavioral design pattern that turns a set of behaviors into objects and makes them interchangeable inside original context object.

As mentioned before the order can be made by speaking with the waiter or directly approaching the barman, but the barman will be the one that prepares drinks. The concrete drink that can be made is difined by the command of the client.

Starting with the context class "Drink" that is responsible for setting the concrete drink desired by the client:

```python
class Drink:
    def __init__(self, drink_type: Command):
        self.__drink_type = drink_type

    @property
    def drink_type(self):
        return self.__drink_type

    @drink_type.setter
    def drink_type(self, drink_type: Command):
        self.__drink_type = drink_type

    def clients_order(self):
        self.__drink_type.order() 
```
The concrete strategy classes are the ones that represent the concrete drinks and can be ordered:

```python
class BloodyMary(Command):
    @staticmethod
    def order():
        print('Bloody Mary')
        return 'Bloody Mary'
        
class PinaColada(Command):
    @staticmethod
    def order():
        print('Pina Colada')
        return 'Pina Colada'

class SpiritFreeBellini(Command):
    @staticmethod
    def order():
        print('Spirit Free Bellini')
        return 'Spirit Free Bellini'
```
So the client may have a Bloody Mary, a Pina Colada or a Spirit Free Belinni, the first two being alcoholic drinks and the last one alcohol free. 

### Visitor Pattern

It is a behavioral design pattern that lets you separate algorithms from the objects on which they operate. It helps us to add new features to an existing class hierarchy dynamically without changing it.

It was used for serving to the client the types of drinks, alcoholic or nonalcoholic ones and to a specific type of zone, the rerace or the indoor zone.

Starting with the visitor interface that portrays the methods of serving alcoholic and nonalcoholic drinks:
```python
class ServeTables(ABC):
    @abstractmethod
    def serve_alco_drinks(self, barman):
        pass

    @abstractmethod
    def serve_non_alco_drinks(self, barman):
        pass
```
Another interface illustrates the preparation and serving methods of an order:

```python
class TheBarman(ABC):
    @staticmethod
    @abstractmethod
    def prepare():
        pass

    @abstractmethod
    def send(self, send: ServeTables):
        pass
```

Here are the concrete way of preparting alcoholic and nonalcoholic drinks:

```python
class AlcoDrink(TheBarman):
    @staticmethod
    def prepare():
        a = random.choice(alco)
        name = a.__class__.__name__
        print(f'The alcoholic drink {name} is made.')
        return name       

    def send(self, send):
        send.serve_alco_drinks(self)

class NonAlcoDrink(TheBarman):
    @staticmethod
    def prepare():
        name = spiritFreeBellini.__class__.__name__
        print(f'The alcohol free drink {name} is made.')
        return name

    def send(self, send):
        send.serve_non_alco_drinks(self)
```

Each one displaying the name of the prepared drink and establishing it's serving method through concrete visitors which sends the drink to the outdoor zone, the terace or indoor, in the Cocktail Bar area.

```python
class ServeOutdoorTables(ServeTables):
    def serve_alco_drinks(self, barman: AlcoDrink):
        drink = barman.prepare()
        print(f'The waiter got to the terace to serve {drink}, an alcoholic drink.')

    def serve_non_alco_drinks(self, barman: NonAlcoDrink):
        drink = barman.prepare()
        print(f'The waiter got to the terace to serve {drink}, an alcohol free drink.')

class ServeIndoorTables(ServeTables):
    def serve_alco_drinks(self, barman: AlcoDrink):
        drink = barman.prepare()
        print(f'The waiter serves {drink}, an alcoholic drink, to the bar table.')

    def serve_non_alco_drinks(self, barman: NonAlcoDrink):
        drink = barman.prepare()
        print(f'The waiter serves {drink}, an alcohol free drink, to the bar table.')
```
As mentioned before the waiter can take the order but only the barman can prepare the drink, so to avoid an unwanted intervinience in the order process the responsabilities and possible actions performed by each employee is established througth the State Pattern.

### State Pattern 

Is a behavioral design pattern that allows an object to change the behavior when its internal state changes. The pattern extracts state-related behaviors into separate state classes and forces the original object to delegate the work to an instance of these classes, instead of acting on its own.

The abstract state class is the following one:

```python
class State(ABC):
    def __init__(self):
        self.__employee = None

    @property
    def employee(self):
        return self.__employee

    @employee.setter
    def employee(self, employee):
        self.__employee = employee

    @staticmethod
    @abstractmethod
    def take_order():
        pass

    @staticmethod
    @abstractmethod
    def recieve_payment():
        pass
```
The eployee can change it's state from waiter to barman if the order is receptioned by the barman or if the waiter is also a barman (in case the bar is short of stuff), for this is responsible the Employee class:

```python
class Employee:
    def __init__(self, initial_state):
        self.__state = initial_state
        self.__state.employee = self

    def change_state(self, state: State):
        self.__state = state

    def take_order(self):
        self.__state.take_order()

    def recieve_payment(self):
        self.__state.recieve_payment()

    def prepare_drink(self):
        self.__state.prepare_drink()

    def prepare_table(self):
        self.__state.prepare_table()
```

Which may change the state and perform the needed actions that are available for him. In total there are two states the BarmanState for a barman who can take orders, prepare drinks and recieve payment and the WaiterState for the waiters who can prepare tables for the customers, take orders and recieve payment, but can't make the drink:

```python
class BarmanState(State):
    
    @staticmethod
    def take_order():
        return 
        
    @staticmethod
    def prepare_drink():
        print('Employee prepares the drink...')
       
    @staticmethod
    def recieve_payment():
        print('Employee recieves the payment...')


class WaiterState(State):
    
    @staticmethod
    def prepare_table():
        print('Employee prepares the table...')
    
    @staticmethod
    def take_order():
        print('Employee takes an order...')

    @staticmethod
    def recieve_payment():
        print('Employee recieves the payment...')
```

In case the waiter will try to prepare the drink, a message will appear, and due to the fact that the drink is not made by the waiter the customer will get a new one for free. The whole process can be seen by running the main.py that simulates the ordering of a drink.

## Conclusions/Results

The results of the mentioned implementation of different behavioural Design Patterns can be viewed after running the ```main.py``` file, the output should be the following:

```
...There are some free tables...

The new waiter can't take your order, try approaching the experienced one.     
The waiter welcomes you.
Employee prepares the table...
Employee takes an order...
Employee recieves the payment...
Wrong state... employee can't prepare the drinks...

...It seems that the customer got scammed...

The barman is open for orders...
Employee prepares the drink...
The custumer is in a good mood and chose to serve someone with a free drink.   
The alcoholic drink PinaColada is made.
The waiter serves PinaColada, an alcoholic drink, to the bar table.

The alcohol free drink SpiritFreeBellini is made.
The waiter got to the terace to serve SpiritFreeBellini, an alcohol free drink.
Employee recieves the payment...
```
Here the client approached a new waiter, but due to the fact that he cannot take orders, the customer will be redirected to an already employed waiter, through implementation of *Chain of responsabilities* design pattern.

The order is taken through the implementation of *Command* design pattern where the waiter starts to serve the customer.

The waiter prepares the table and takes the order, recievig the payment in advance, BUT he tries to prepare the drink which is not allowed by his concrete state, so the implemented *State* pattern takes care of it and a message ```"Wrong state... employee can't prepare the drinks..." ```prompts out. Then the state is changed to barman and he prepares the drink.

All the drinks that can be made are established through the implemented *Strategy* pattern that sets the drink type (alcoholic and nonalcoholic). The customer ordered a PinaColada.

The drinks was made by the barman and sent through the implemented *Visitor* design pattern to the corresponding table zone. 

The customer was in good mood so he ordered another drink and sent it to a stranger from the terrace, paying the bill.

This laboratory work was useful because it got me more familiar with Behavioural Design Patterns.
