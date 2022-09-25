from abc import ABC, abstractmethod

#class for counting the purchase sum.
class ArtShop:
    
    names = []
    items = []
    prices = []
    
    def buy(self, name, item, price):
        self.names.append(name)
        self.items.append(item)
        self.prices.append(price)
        
    def sum(self):
        total = 0
        for i in range(len(self.items)):
            total += self.items[i]* self.prices[i]
        return total

#Class for establishing the Order Details.
class OrderDetails:
    def __init__(self, name, width, length, hours_to_paint):
        self.name = name
        self.width = width
        self.length = length
        self.hours_to_paint = hours_to_paint 
        print(f"The client has requested a piece of artwork which represents a {name}.") 
           
#Class with an abstract method.
class ArtPiece(ABC):       
    @abstractmethod       
    def complexity(self, width, length, hours_to_paint):
        pass
 
#Class for calculating the complexity of a piece of artwork, specifically a Painting.  Inherits from ArtPiece class.      
class Painting(ArtPiece):
       
    def complexity(self, width, length, hours_to_paint):
        print('The client specified that he/she wants a painting.')
        canvas_size = width * length
        complexity = canvas_size * hours_to_paint
        return complexity*0.2

#Class for calculating the complexity of a piece of artwork, specifically a Drawing. Inherits from ArtPiece class.            
class Drawing(ArtPiece):
 
    def complexity(self, width, length, hours_to_paint):
        print('The client specified that he/she wants a drawing.')
        canvas_size = width * length
        complexity = canvas_size * hours_to_paint
        return complexity*0.1       

#Class for calculating the complexity of a piece of artwork, specifically a Decorative Artpiece. Inherits from ArtPiece class.            
class DecorativeArt(ArtPiece):
    
    def complexity(self, width, length, hours_to_paint):
        print('The client specified that he/she wants a decorative piece of art.')
        canvas_size = width * length
        complexity = canvas_size * hours_to_paint
        return complexity*0.05
        
#Class for calculating the artwork price.
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

p = PiecePrice()

od = OrderDetails('peisage',2,3,30)
art = Painting()
comp = art.complexity(od.width,od.length,od.hours_to_paint)
p.piece_price(comp, sum)

od = OrderDetails('bird',2,3,5)
art = Drawing()
comp = art.complexity(od.width,od.length,od.hours_to_paint)
p.piece_price(comp, sum)

od = OrderDetails('cat',1,0.5,10)
art = DecorativeArt()
comp = art.complexity(od.width,od.length,od.hours_to_paint)
p.piece_price(comp, sum)



            
    
    