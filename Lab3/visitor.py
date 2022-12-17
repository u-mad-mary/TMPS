from abc import ABC, abstractmethod
import random
from strategy import BloodyMary, PinaColada, SpiritFreeBellini


bloodyMary = BloodyMary()
pinaColada = PinaColada()
spiritFreeBellini = SpiritFreeBellini()

alco = [bloodyMary, pinaColada]


class ServeTables(ABC):
    @abstractmethod
    def serve_alco_drinks(self, barman):
        pass

    @abstractmethod
    def serve_non_alco_drinks(self, barman):
        pass


class TheBarman(ABC):
    @staticmethod
    @abstractmethod
    def prepare():
        pass

    @abstractmethod
    def send(self, send: ServeTables):
        pass
    
    
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


