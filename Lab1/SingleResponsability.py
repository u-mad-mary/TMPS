#class responsible for counting the total sum of a purchase in an Art Shop
class ArtShop:
    
    names = []
    items = []
    prices = []
    
    def __init__(self, name, item, price):
        self.names.append(name)
        self.items.append(item)
        self.prices.append(price)
        
    def sum(self):
        total = 0
        for i in range(len(self.items)):
            total += self.items[i]* self.prices[i]
        return total

#class responsible for establishing the price of the final artpiece  
class PiecePrice:          
            
    def piece_price(self, name, canvas_area, sum):
        print("The client has requested a piece of artwork which represents a " + name +".\n")
        total = sum * canvas_area * 0.5
        print("The art piece will cost " + str(total) + " $.")    
        
#initialise the class ArtShop   
p = ArtShop('brushes',3, 5)
p = ArtShop('oilpaint',5, 10)
p = ArtShop('palette',1, 5)

#calling the class' method sum()
sum = p.sum()
print("The shop spendings are " + str(sum) + " $.")

#initialise the class PiecePrice
art_price = PiecePrice()
#calling the class's method piece_price()
art_price.piece_price("peisage", 6.5, sum)


            
    
    