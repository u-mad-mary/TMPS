# Creational Design Patterns

## Objectives

* Get familiar with the Creational Design Patterns;
* Implement at least 5 CDPs for a specific domain;

## Used Design Patterns

* Singleton
* Object Pool
* Builder
* Factory Method
* Abstract Factory

## Implementation

The design patterns mentioned above have been implemented in a context of an Art Studio, where a painter can work on different types of artworks with several materials.

### Singleton Pattern

The singleton pattern ensures that there is only one single instantiation of one class, and it is accessible globally.

To create a Singleton is used the Metaclass mechanism, where Singleton class inherits from type, that makes it a metaclass.

The metaclass has a dictionary of instances named “painters” that it maintains, so for every class that is a singleton it maintains the instance in this dictionary and call method, calls the instance, acting like a constructor, creating a new instance when there is none.

```python
class Singleton(type):

    painters = dict()
    
    def __call__(cls, *args, **kwargs):

        if cls not in cls.painters:
            cls.painters[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.painters[cls]
```

The Artist class uses Singleton as metaclass which makes it a Singleton.

```python

class Artist(metaclass=Singleton):
    def painter(self, name):
        print(f"{name} is the artist that is currently working.\n")
        return name

```

It returns the name of the painter who is working in the studio.

### Object Pool

The Object Pool design pattern uses a pool of initialized objects that are ready to be used rather than creating a new object all the time. The main idea of an Object Pool is that instead of creating instances of the class you can reuse them by getting them from the pool.

It manages a fixed number of instances.

Below can be seen the ToolPool class that manages the objects that are free and in use, it uses the acquire() and release() methods that return the Tool instance that can be reused and if the free list is empty then there will be no objects to acquire and an error will be produced.

```python
class ToolPool:
    def __init__(self, number):
        self.number = number
        self.free = []
        self.in_use = []

        for _ in range(number):
            self.free.append(Tool())

    def acquire(self) -> Tool:
        if len(self.free) <= 0:
            raise Exception("No more available tools.")

        t = self.free[0]
        self.free.remove(t)
        self.in_use.append(t)
        return t

    def release(self, t: Tool):
        self.in_use.remove(t)
        self.free.append(t)
        return t
```

In order to automatize the process of acquirement and release of the object is used a context manager represented by PoolManager class:

```python
class PoolManager:  # automaticlly acquires and releases objects
    def __init__(self, pool):
        self.pool = pool

    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj

    def __exit__(self, type, value, trace):
        self.pool.release(self.obj)
```

This design pattern is used to set the available and used canvases and easels from the studio.

### Builder Pattern

The builder as a creational design pattern allows constructing a complex system step by step. It allows construction of different objects, each out of a subset of already-built components.

In this work, the builder design pattern was used to create and choose the tools used by the painter.

Below can be seen the class of the desired built product ArtPiece that has as object canvas, easel, and tools.

```python
class ArtPiece:
    def __init__(self):
        self.canvas = None
        self.easel = None
        self.tools = None

    def set_canvas(self, canvas):
        self.canvas = canvas

    def set_easel(self, easel):
        self.easel = easel

    def set_tools(self, tool):
        self.tools = tool
```

The builder interface can be seen below:

```python

class ArtBuilder(ABC):

    @abstractmethod
    def get_canvas(self):
        pass

    @abstractmethod
    def get_easel(self):
        pass

    @abstractmethod
    def get_tools(self):
        pass
 ```

It will be used for creating concrete builders that will have established canvas size, easel brand and the material for drawing.

Next can be seen the Creation class that is responsible for setting the needed objects using the ArtPiece class.

```python
class Creation:

    builder = None

    def set_builder(self, builder):
        self.builder = builder

    def get_artsupply(self):
        creation = ArtPiece()

        canvas = self.builder.get_canvas()
        creation.set_canvas(canvas)

        easel = self.builder.get_easel()
        creation.set_easel(easel)

        tool = self.builder.get_tools()
        creation.set_tools(tool)

        return creation
  ```

### Factory Method

The factory method is a creational design pattern that provides an interface for a superclass to call and create an object, with the type of the object created can be controlled and determined by the subclass.

The factory method was used in this work for establishing the Artwork Type selected by the painter (Drawing, Painting, Decorative Art).

The base class used in implementation for setting the art work types and the artist name (given by the Singleton).

```python
class ArtType(ABC):

    @abstractmethod
    def artpiece(self, artist):
        pass
```

There are 3 subclasses that are used in the ArtTypeFactory() class for choosing the desired type:

```python
class ArtTypeFactory:
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
```

In case a type other than a listed one is used, the program will output an error message.

This class is also used in Abstract Factory for establishing the art piece characteristics.

### Abstract Factory

The abstract factory allows creation of a family of related objects without specifying the concrete class. In other words, you can call the families of class just via one single interface.

The painter created through the Singleton has to establish the proprieties of canvas, easel, and the main tool for painting, choosing at the start the art type (set in Factory) of the artwork that establishes which proprieties will be convenient for the mentioned tools.

The class ArtPieceFactory() serves as Abstract Factory that puts together families of objects (different objects of base classes (Canvas, Easel, Tools)) that should be established:

```python
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

```

Here is the implementation of the Abstract Factory named CreateArtFactory that returns the objects of concrete factories(ChooseArt - represented by the Factory Method mentioned earlier,  ChooseCanvas, ChooseEasel, ChooseTools).

```python
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

```

Here is also used the Object Pool pattern for establishing the available and used canvases and easels, along with the characteristics of these objects that were set in Builder.

## Conclusions/Results

The results of the mentioned implementation of different Creational Design Patterns can be viewed after running the ```main.py``` file, the output showld be the following:

```txt
============ Welcome to the Art Studio. ============

Here you can take a glance at the working processs of an artist!

The proposed tools are Canvas: 1x2m, Easel: Mont Marte, Tools: Oil Paint.

Bob Ross is the artist that is currently working.

A Painting will be created by Bob Ross.

Canvas 1 of size 1x2m was successfully chosen.
Easel 1 of brand Mont Marte is now in use.
The artist works with Oil Paint.

============ The artist is actively working on his artwork. ============
```

Here the proposed tools are given by the implementation of Builder pattern, the name of the artist that is currently working is established by Singleton, the art type "Painting"  is given by the Factory Method, the numbers of available and used canvases and easels are given by Abstract Factory implementation with the characteristics set in the Builder.

This laboratory work was useful because it got me more familiar with Creational Design Patterns that I intend to use in my future works.
