from abc import ABC, abstractmethod
from chain_of_responsabilities import Barman, Waiter

# concrete commands interface
class Command(ABC):
    @abstractmethod
    def order(self):
        pass


# concrete commands
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


# command sender
class Customer:
    def __init__(self, command: Command):
        self._command = command

    def order_command(self):
        return self._command.order()


# command receivers
class BarmanRecieve(Barman):
       
    @staticmethod
    def take_order():
        return Barman().handle('order')
    
    @staticmethod
    def make_drink():
        return 'The barman started to prepare your drink.'


class WaiterRecieve(Waiter):
    @staticmethod
    def take_order():
        return Waiter().handle('order')


# def client_code_take_order():
#     waiter = WaiterRecieve()
#     barman = BarmanRecieve()

#     command_waiter = OrderWaiter(waiter)
#     command_waiter_sends_bar = OrderWaiter(barman)

#     customer0 = Customer(command_waiter)
#     customer1 = Customer(command_waiter_sends_bar)

#     order0 = customer0.order_command()
#     order1 = customer1.order_command()

#     print('Order:')
#     print(order0)
#     print(order1)


# def client_code_prepare():
#     barman = BarmanRecieve()

#     command = OrderBar(barman)

#     customer = Customer(command)

#     preparation = customer.order_command()
#     print('Making the order:')
#     print(preparation)

# def main():
#     client_code_take_order()
#     print('')
#     client_code_prepare()


# if __name__ == '__main__':
#     main()