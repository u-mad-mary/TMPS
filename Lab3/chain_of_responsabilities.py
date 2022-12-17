from abc import ABC, abstractmethod


# interface for handlers
class Handler(ABC):
    @abstractmethod
    def set_next_handler(self, handler):
        pass

    @abstractmethod
    def handle(self, order):
        pass


# abstract class for concrete handlers
class AbstractHandler(Handler, ABC):
    _next_handler = None
    can_take_order = False

    def set_next_handler(self, handler: Handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, order):
        if self._next_handler:
            return self._next_handler.handle(order)

        return None

class newWaiter(AbstractHandler):
    
    def handle(self, order):
        if self.can_take_order:
            return 'The new waiter took your order and ensured you that it will be done soon.'
        else:
            print("The new waiter can't take your order, try approaching the experienced one.")
            return super().handle(order)

class Waiter(AbstractHandler):
    
    can_take_order = True
    
    def handle(self, order):
        if self.can_take_order:
            return 'The waiter welcomes you.'
        else:
            print('Waiter can\'t take your order, he is busy with another table, try ordering from the bar.')
            return super().handle(order)


class Barman(AbstractHandler):
    
    can_take_order = True
    
    def handle(self, order):
        if self.can_take_order:
            return 'The barman took your order.'
        else:
            return super().handle(order)


def new_waiter_han(handler):
    order = 'Order Details'
    result = handler.handle(order)
    return result

