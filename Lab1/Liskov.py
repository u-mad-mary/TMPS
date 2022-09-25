from abc import ABC, abstractmethod

#class for initialising art pieces characteristics
class Characteristics:
    def __init__(self, name, oil_paint, pencil, canvas):
        self.name = name
        self.oil_paint = oil_paint
        self.pencil = pencil
        self.canvas = canvas

#abstract class
class Draw(ABC):
    @abstractmethod
    def draw(self, object):
        pass

#class for choosing a canvas for drawing. Inherits from Draw.  
class Canvas(Draw):
    def __init__(self, canvas_size):
        self.canvas_size = canvas_size

    def draw(self, object):
        print(f'The painter choose to {object} {self.canvas_size} sized canvas.')

#class for choosing a pencil for drawing. Inherits from Draw.
class Sketch(Draw):
    def __init__(self, pencil_softness):
        self.pencil_softness = pencil_softness

    def draw(self,object):
        print(f'The artist {object} using {self.pencil_softness} pencils.')
        
#class for choosing oil paint for painting.Inherits from Draw.      
class Painting(Draw):
    def __init__(self, oil_paint_colors):
        self.oil_paint_colors = oil_paint_colors

    def draw(self, object):
        print(f'The painter {object} using {self.oil_paint_colors} oil paint colors.')

#class for starting the painter's drawing process with the given materials.      
class Painter:
    def __init__(self, painter):
        self.painter = painter

    def start(self, object):
        self.painter.draw(object)

#setting artpiece characteristics
art_piece = Characteristics('Dame in red', 'white, red, black, blue, brown', 'HB, B1', '2x3m')

choose_canvas = Canvas(art_piece.canvas)
make_a_sketch = Sketch(art_piece.pencil)
oil_paint_drawing = Painting(art_piece.oil_paint)
paint = Painter(art_piece)

paint.painter = choose_canvas
paint.start('work on')
  
paint.painter = make_a_sketch
paint.start('started the sketching process')

paint.painter = oil_paint_drawing
paint.start('started to paint')

