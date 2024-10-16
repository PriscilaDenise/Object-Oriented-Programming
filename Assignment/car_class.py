from vehicle_class import Vehicle

class Car(Vehicle):
    def __init__ (self, color:str, is_winter_tires:bool = False):
        super().__init__(color)
        self.is_winter_tires = is_winter_tires

    def toString(self):
        return f"The car is {self.getColor()} \n Has winter tyres: {self.is_winter_tires}"
    
if __name__ == "__main__":
    #Creating an object under car
    car1 = Car("Green", True)

#Printing car data
    car_data = car1.toString()
    print (car_data)

