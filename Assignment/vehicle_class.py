class Vehicle:
    def __init__(self, color:str):
        self.color = color

    def getColor(self):
        return self.color

    def toString (self):
        return f"This vehicle is {self.getColor()}"
    
if __name__ == "__main__":
    vehicle1 = Vehicle("red")

    vehiclecolor = vehicle1.toString()
    print (vehiclecolor)







