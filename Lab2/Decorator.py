from abc import ABC, abstractmethod

# Decorator is a structural pattern that allows adding new behaviors to objects 
# dynamically by placing them inside special wrapper objects, called decorators.

class CocktailGlass(ABC):
    
    @abstractmethod
    def type(self):
        pass

class BasicCocktailGlass(CocktailGlass):
    
    def __init__(self, basic_glass = 'Cocktail Glass'):
        self.basic_cocktailGlass = basic_glass

    def type(self):
        result = self.basic_cocktailGlass
        return result


class BaseDecorator(CocktailGlass):
    
    def __init__(self, default_glass: CocktailGlass):
        self._default_glass = default_glass

    @property
    def default_glass(self):
        return self._default_glass

    def type(self):
        return self._default_glass.type()


class NonAlcoDecorator(BaseDecorator):
    
    def type(self):
        non_alco_glass = 'Delmonico'
        return f'Instead of a simple {self.default_glass.type()} the barman uses a {non_alco_glass}.\n'


class AlcoDecorator(BaseDecorator):
    
    def type(self):
        alco_glass = 'Snifter'
        return f'Instead of a simple {self.default_glass.type()} the barman uses a {alco_glass}.\n'


def client_code_base(basic_glass: CocktailGlass):
    base_decorator = BaseDecorator(basic_glass)
    print(base_decorator.type())


def client_code_non_alco(basic_glass: CocktailGlass):
    non_alco_decorator = NonAlcoDecorator(basic_glass)
    print(non_alco_decorator.type())


def client_code_alco(basic_glass: CocktailGlass):
    alco_decorator = AlcoDecorator(basic_glass)
    print(alco_decorator.type())

