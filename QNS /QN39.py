from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__ (self, name, capacity):
        self.name = name
        self.capacity = capacity

    @abstractmethod
    def calculate_speed(self, distance, time):
        pass

class Bus(Transport):
    def __init__ (self,name, capacity, traffic = 1):
        super().__init__(name, capacity)
        self.traffic = traffic

    def calculate_speed(self, distance, time):
        speed = distance/time * self.traffic
        return speed
    
    def route_planning(self):
        print(f'The {self.name} is moving soon.')
    

class Train(Transport):
    def __init__ (self, name, capacity, stops = 10):
        super().__init__ (name, capacity)
        self.stops = stops

    def calculate_speed(self, distance, time):
        speed1 = distance/time / self.stops
        return speed1
    
    def seat_reservation(self):
        print (f'Some seats are reserved.')

tata = Bus('Tata', 100, 0.5)

print(tata.calculate_speed(100, 2))

