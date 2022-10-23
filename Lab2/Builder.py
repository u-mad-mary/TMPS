from abc import ABC, abstractmethod

#components used for artpiece
class Canvas:
    size = None
    
class Easel:
    brand = None
    
class Tools:
    material = None
    
#Our product the Art Piece
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
        
    def art_tools(self):
        print(f"The proposed tools are Canvas: {self.canvas.size}, Easel: {self.easel.brand}, Tools: {self.tools.material}.\n")

#Builder interface
class ArtBuilder(ABC):
    
    @abstractmethod
    def get_canvas(self):
        "choose canvas"
        
    @abstractmethod
    def get_easel(self):
        "take easel"
        
    @abstractmethod
    def get_tools(self):
        "choose tools"
        
#Concrete builders
class Colored(ArtBuilder):
    
    def get_canvas(self):
        canvas = Canvas()
        canvas.size = '1x2m'
        return canvas
    
    def get_easel(self):
        easel = Easel()
        easel.brand = "Mont Marte"
        return easel
    
    def get_tools(self):
        tool = Tools()
        tool.material = "Oil Paint"
        return tool

class Monochrome(ArtBuilder):
    
    def get_canvas(self):
        canvas = Canvas()
        canvas.size = '0.5x0.5m'
        return canvas
    
    def get_easel(self):
        easel = Easel()
        easel.brand = "Melissa & Doug Deluxe"
        return easel
    
    def get_tools(self):
        tool = Tools()
        tool.material = "Pencils"
        return tool
      

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
    
    


