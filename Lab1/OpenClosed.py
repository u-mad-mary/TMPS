from abc import ABC, abstractmethod
from SingleResponsability import ArtShop

class ArtPiece(ABC):
    
    def type(self, name, width, length, hours_to_paint):
        self.name = name
        self.width = width
        self.length = length
        self.hours_to_paint = hours_to_paint 
        print(f"The client has requested a piece of artwork which represents a {name}.")
        
    @abstractmethod       
    def complexity(self):
        canvas_size = self.width * self.length
        complexity = canvas_size * self.hours_to_paint
        return complexity
      
class Painting(ArtPiece):
    
    def complexity(self):
        print('The client specified that he/she wants a painting.')
        return super().complexity()*0.2
              
class Drawing(ArtPiece):
    
    def complexity(self):
        print('The client specified that he/she wants a drawing.')
        return super().complexity()*0.1       
        
class DecorativeArt(ArtPiece):
    
    def complexity(self):
        print('The client specified that he/she wants a decorative piece of art.')
        return super().complexity()*0.05
        
class PiecePrice():  
                 
    def piece_price(self, comp, sum):
        total = sum * comp * 0.5
        print("The art piece will cost " + str(total) + " $.\n")    
        
    
spendings =  ArtShop()
spendings.buy('creions',3, 1.5)
spendings.buy('brushes',3, 5)
spendings.buy('oilpaint',10, 50)
spendings.buy('palette',1, 10)

sum = spendings.sum()
print("The shop spendings are " + str(sum) + " $.\n")

art = PiecePrice()

dr = Painting()
dr.type('peisage',2,3,30)
comp = dr.complexity()
art.piece_price(comp, sum)

dr = Drawing()
dr.type('bird',2,3,5)
comp = dr.complexity()
art.piece_price(comp, sum)

dr = DecorativeArt()
dr.type('cat',1,0.5,10)
comp = dr.complexity()
art.piece_price(comp, sum)



            
    
    