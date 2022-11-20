from Bridge import *

if __name__ == '__main__':
    
    ing = Orange()
    ingl = Tomato()  
    
    bm = BloodyMary(ingl,'Vodka')
    bm.pay_order_in_advance()
    bm.print_name()
    bm.glass_type()
    
    client_code(bm)
    
   # Create alcohol free drink and pass it to adapter object
    alcoFree = JuiceBased(ing,'Sprite')
    alcoFree.pay_order_in_advance()
    alcoFree.print_name()
    alcoFree.glass_type()
    
    adapter = Adapter(ing, alcoFree)

    # alcohol free drink acts like alco drink
    check_alcoFree_is_alco = adapter.is_alcohol()
    pour_alcoFree = adapter.pour_alcohol()
    add_alcoFree = adapter.add_to_alco()

    print(check_alcoFree_is_alco)
    print(pour_alcoFree)
    print(add_alcoFree)
    adapter.prepare()