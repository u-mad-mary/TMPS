# Facade pattern that provides a simpler unified interface to a more complex system. 
# The word Facade means the face of a building or particularly an outer lying interface of a complex system, 
# consists of several sub-systems.

class Shake:

    def shake(self):
        print("Shaking ...")
 
class Ice:
    
    def add_ice(self):
        print("Adding Ice...")
        
class Pour:
    
    def pour(self):
        print("Pouring into the glass...")
        
# Facade
class DrinkPreparation:
    
    def __init__(self):
        self.shake = Shake()
        self.pour = Pour()
        self.ice = Ice()
 
    def startPreparation(self):
        self.shake.shake()
        self.pour.pour()
        self.ice.add_ice()
 
