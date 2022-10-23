#This pattern restricts the instantiation of a class to one object. 
#It is a type of creational pattern and involves only one class to create methods and specified objects.
#It provides a global point of access to the instance created.

class Singleton(type):

    painters = dict()

    def __call__(cls, *args, **kwargs):

        if cls not in cls.painters:
            cls.painters[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.painters[cls]

class Artist(metaclass=Singleton):
    
    def painter(self, name):
        print(f'{name} is the artist that is currently working.\n')
        return name
        



