from abc import ABC, abstractmethod


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

