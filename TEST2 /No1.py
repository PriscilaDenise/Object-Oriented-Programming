class Character:
    def __init__(self,name,health,position):
        self.__name = name
        self.__health = health
        self.__position = position
        
    def move(self,new_position):
        self.__position = new_position
        print(f"{self.__name} has moved up to a {new_position}")
        
    def attack(self):
        self.__health -= 1
        print(f"{self.__name} is attacking! Health is {self.__health}")
        
    def interact(self):
        print(f"{self.__name} is interacting with the open-world environment")
        
    def get_in(self,vehicle):
        vehicle_type = vehicle.vehicle_type
        print(f"{self.__name} is entering the {vehicle_type} and is driving the {vehicle_type} ") 
        
    def get_out(self,vehicle):
        vehicle_type = vehicle.vehicle_type
        print(f"{self.__name} is getting out of the       {vehicle_type}")         
        
class Vehicle:
    def __init__(self,vehicle_type,speed,fuel_level):
        self.__vehicle_type = vehicle_type
        self.__speed = speed
        self.__fuel_level = fuel_level
        
    def drive(self):
        if self.__fuel_level > 0:
            print(f"{self.__vehicle_type} is driving!")
            self.__fuel_level -= 1
        else:
            print(f"{self.__vehicle_type} is out of fuel.")
             
        
    def refuel(self,amount):
        self.__fuel_level += amount
        if self.__fuel_level > 1000:
            self.__fuel_level = 1000
            print(f"{self.__vehicle_type} has been refueled by {amount}") 
        else:
            print(f"{self.__vehicle_type} has been refueled by {amount}")
        
    def stop(self):
        print(f"{self.__vehicle_type} has stopped!")
        
    @property
    def vehicle_type(self):
        return self.__vehicle_type
    
class HeroCharacter(Character):
    def __init__(self,name,health,position):
        super().__init__(name,health,position)
        
        
    def double_jump(self):
        print(f"{self.__name} jumped 3 times.")
        
    def fast_run(self):
        print(f"{self.__name}         ")       
   
       
character1 = Character("Bruce Wayne",234,(0,0))
vehicle1 = Vehicle("Batmobile",433,100)

character1.move((4,6))
character1.attack() 
character1.interact()   

vehicle1.drive() 
vehicle1.refuel(700)  
vehicle1.stop() 

character1.get_in(vehicle1)
character1.get_out(vehicle1)
