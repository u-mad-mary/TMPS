from command import Command


# concrete commands interface works as strategy interface

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


