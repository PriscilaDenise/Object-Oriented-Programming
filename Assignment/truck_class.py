from vehicle_class import Vehicle

class Truck(Vehicle):
    def __init__ (self, color:str, has_trailer:bool = False):
        super().__init__(color)
        self.has_trailer = has_trailer

    def toString(self):
        return f"The vehicle is {self.getColor()}\n Has trailer: {self.has_trailer}"
    

if __name__ =="__main__":
    #creating object of truck
    truck1 = Truck("Blue", False)

    #printing the truck data
    truck_data = truck1.toString()
    print(truck_data)
