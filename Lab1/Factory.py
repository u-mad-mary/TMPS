from abc import ABC, abstractmethod

#The factory method is a creational design pattern that provides an interface for a 
#superclass to call and create an object with the type of the object created can be controlled and determined by the subclass.

class ArtType(ABC):
    
    @abstractmethod
    def artpiece(self, artist):
        pass

class Drawing(ArtType):
    
    def __init__(self):
        self.art = "Drawing"
        
    def artpiece(self, artist):
        return f"A {self.art} will be created by {artist}.\n"
    
class Painting(ArtType):
    
    def __init__(self):
        self.art = "Painting"
        
    def artpiece(self, artist):
        return f"A {self.art} will be created by {artist}.\n"
    
class Decorative(ArtType):
    
    def __init__(self):
        self.art = "Decorative"
        
    def artpiece(self, artist):
        return f"A {self.art} will be created by {artist}.\n"
      
class ArtTypeFactory():
    
    @staticmethod
    def choose_artpiece(artpiece):
        
        try:
            if artpiece == "Drawing":
                return Drawing()
            elif artpiece == "Painting":
                return Painting()
            elif artpiece == "Decorative":
                return Decorative()
            raise AssertionError("Choosen art type is not applyable.")
        
        except AssertionError as e:
            print(e)
            
