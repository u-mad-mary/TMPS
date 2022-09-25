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
    
class PiecePrice:          
            
    def piece_price(self, name, canvas_area, sum):
        print("The client has requested a piece of artwork which represents a " + name +".\n")
        total = sum * canvas_area * 0.5
        print("The art piece will cost " + str(total) + " $.")    
        
    
spendings =  ArtShop()
spendings.buy('brushes',3, 5)
spendings.buy('oilpaint',5, 10)
spendings.buy('palette',1, 5)
sum = spendings.sum()
print("The shop spendings are " + str(sum) + " $.")

art = PiecePrice()
art.piece_price("peisage", 6.5, sum)


            
    
    