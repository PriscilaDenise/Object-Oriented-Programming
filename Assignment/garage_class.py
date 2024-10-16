class Garage:
    def __init__(self):
        self.Vehicle =  None 

    def setVehicle(self, Vehicle_parked):
        self.Vehicle = Vehicle_parked
        return self.Vehicle
    
    def toString(self):
        return f"Description of the parked vehicle: \n{self.Vehicle.toString()}"