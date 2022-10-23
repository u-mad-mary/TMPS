# Singleton allows to be sure that there is only one single instantiation of one class and it is accessible globally.

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
        



