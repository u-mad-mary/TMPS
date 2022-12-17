from chain_of_responsabilities import *
from command import *
from state import *
from visitor import *

def main():
    print('...There are some free tables...\n')
    new_waiter = newWaiter()
    waiter = Waiter()
    barman = Barman()

    new_waiter.setting_next_handler(waiter).setting_next_handler(barman)
    new_waiter_han(new_waiter)
  
    waiter_rec = WaiterRecieve()

    command_waiter = OrderWaiter(waiter_rec)

    customer0 = Customer(command_waiter)

    order0 = customer0.order_command()
    print(order0)

    waiter_state = WaiterState()
    employee = Employee(waiter_state)

    try:
        
        employee.prepare_table()
        employee.take_order()
        employee.recieve_payment()
        employee.prepare_drink()
        
    except AttributeError:
        print('Wrong state... employee can\'t prepare the drinks...\n')

    print("...It seems that the customer got scammed...\n")
    print('The barman is open for orders...')

    bar_state = BarmanState()
    bar_state.employee = employee
    employee.change_state(bar_state)
    employee.take_order()
    employee.prepare_drink()
    
    alco_drink = AlcoDrink()
    alco_free_drink = NonAlcoDrink()

    serve_terace = ServeOutdoorTables()
    serve_bar = ServeIndoorTables()
     
    print("The custumer is in a good mood and chose to serve someone with a free drink.")

    alco_drink.send(serve_bar)
    print('')
    alco_free_drink.send(serve_terace)
    employee.recieve_payment()






if __name__ == '__main__':
    main()