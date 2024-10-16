from garage_class import Garage
from truck_class import Truck


class GarageTester(Garage):
    def __init__(self):
        super().__init__()

    def getExample(self):
        #creating object
        truck1 = Truck("green", False)


        #Putting the object in the garage 
        garage1 = Garage()

        garage1.setVehicle(truck1)

        #printing the information 
        print(garage1.toString())

if __name__ == "__main__":
    GarageTester().getExample()