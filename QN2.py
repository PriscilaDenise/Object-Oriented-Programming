class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 

class car(Vehicle):
    def __init__(self, make, model, year, fuel_type, tank_capacity=50):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
        self.fuel_level = 0
        self.tank_capacity = tank_capacity

    def refuel(self, amount):
        self.fuel_level += amount
        if self.fuel_level + amount > self.tank_capacity:
            print('Cannot add fuel!!')
            self.fuel_level = self.tank_capacity
        else:
            self.fuel_level += amount
            print(f'Added {amount} liters. \n Current fuel level: {self.fuel_level} liters')

    def drive(self, distance):
        fuel_taken = distance * 0.1 
        if fuel_taken > self.fuel_level:
            print('Not enough fuel to drive this distance')
        else:
            self.fuel_level -= fuel_taken
            print(f'Driven: {distance} miles. \n New fuel level: {self.fuel_level} liters')

    def display_vehicle_info(self):
        print(f'Make: {self.make} \nModel: {self.model} \nYear: {self.year} \n Fuel level: {self.fuel_level}')


car1 = car('Toyota', 'Land Cruiser', 2015, 'Diesel')
# car1.display_vehicle_info()

car1.refuel(300)


