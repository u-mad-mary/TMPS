from abc import ABC, abstractmethod
from chain_of_responsabilities import Barman, Waiter


class Command(ABC):
    @abstractmethod
    def order(self):
        pass


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


class Customer:
    def __init__(self, command: Command):
        self._command = command

    def order_command(self):
        return self._command.order()


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
