from abc import ABC, abstractmethod

class Discount(ABC):
    def __init__ (self):
        pass

    @abstractmethod
    def apply_discount(self, price):
        self.price = price
        pass

class PercentageDiscount(Discount):
    def __init__ (self, percentage):
        s
