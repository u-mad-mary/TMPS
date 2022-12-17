from command import Command


# concrete commands interface works as strategy interface

# strategy interface
# class Command(ABC):
#     @staticmethod
#     @abstractmethod
#     def order():
#         pass


# context class
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
        
# concrete strategy
class BloodyMary(Command):
    @staticmethod
    def order():
        print('Bloody Mary')
        return 'Bloody Mary'

# concrete strategy
class PinaColada(Command):
    @staticmethod
    def order():
        print('Pina Colada')
        return 'Pina Colada'

# concrete strategy
class SpiritFreeBellini(Command):
    @staticmethod
    def order():
        print('Spirit Free Bellini')
        return 'Spirit Free Bellini'


def client_code():
    bloodyMary = BloodyMary()
    pinaColada = PinaColada()
    spiritFreeBellini = SpiritFreeBellini()

    drink = Drink(bloodyMary)
    drink.clients_order()

    drink.drink_type = pinaColada
    drink.clients_order()

    drink.drink_type = spiritFreeBellini
    drink.clients_order()


def main():
    client_code()


if __name__ == '__main__':
    main()