class Shopitem:
    def __init__ (self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

class Electronics(Shopitem):
    def __init__ (self, name, price, stock_quantity, warranty_period):
        super().__init__ (name, price, stock_quantity)
        self.warranty_period = warranty_period

    def sell_item(self, quantity):
        if quantity > self.stock_quantity:
            print("Not enough stock!!!")
        else:
            self.stock_quantity -= quantity
            print(f"Sold {quantity} {self.name}.")
        if self.stock_quantity == 0:
            print(f"{self.name} is out of stock!!")

    def display_details(self):
        print(f"Name: {self.name}\nPrice: {self.price}\nStock quantity: {self.stock_quantity}\nWarranty period: {self.warranty_period} years")

obj1 = Electronics('TV', 10000,4, 2)
obj2 = Electronics('Laptop', 50000, 5, 3)

obj1.sell_item(1)
obj2.display_details()