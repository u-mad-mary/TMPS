from abc import ABC, abstractmethod
from ObjPool import *
from Singleton import *
from Factory import ArtTypeFactory
from Builder import *

# The abstract factory lets you create a family of related objects without specifying the concrete class. In other words, 
# you can call the families of class just via one single interface.

class Canvas(ABC):
    
    @abstractmethod
    def take(self):
        pass

    def availability(self):
        return True


class Easel(ABC):
    
    @abstractmethod
    def get(self):
        pass

    def check_state(self):
        return True


class Tools(ABC):
    
    @abstractmethod
    def get_material(self):
        pass

class ChooseArt(ArtTypeFactory):
    
    def get_type(self, artist):
        artpieces = ["Drawing", "Painting", "Decorative"]
        return ArtTypeFactory.choose_artpiece(artpieces[1]).artpiece(artist)
           
class ChooseCanvas(Canvas):
    
    def take(self, c, size):
        return f'Canvas {c} of size {size} was successfully chosen.'


class ChooseEasel(Easel):
    
    def get(self, e, brand):
        return f'Easel {e} of brand {brand} is now in use.'
    
    
class ChooseTools(Tools):

    def get_material(self, materials):
        return f'The artist works with {materials}.'
    

class ArtPieceFactory(ABC): 
    
    @abstractmethod
    def get_artpiece_type():
        pass
    
    @abstractmethod
    def get_canvas():
        pass

    @abstractmethod
    def get_easel():
        pass

    @abstractmethod
    def get_tools():
        pass


class CreateArtFactory(ArtPieceFactory):
    
    @staticmethod
    def get_artpiece_type():
        return ChooseArt()
    
    @staticmethod
    def get_canvas():
        return ChooseCanvas()

    @staticmethod
    def get_easel():
        return ChooseEasel()

    @staticmethod
    def get_tools():
        return ChooseTools()



