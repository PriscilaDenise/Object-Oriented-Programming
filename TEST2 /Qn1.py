# Character Class
class Character:
    def __init__(self, name, health, position):
        self.name = name
        self.health = health
        self.position = position

    # Getter and Setter methods for encapsulated attributes
    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = new_health

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    # Methods
    def move(self, new_position):
        print(f"{self.name} moves to {new_position}.")
        self.position = new_position

    def attack(self, target):
        print(f"{self.name} attacks {target}!")

    def interact(self, object):
        print(f"{self.name} interacts with {object}.")

# Vehicle Class
class Vehicle:
    def __init__(self, type, speed, fuel_level):
        self.type = type
        self.speed = speed
        self.fuel_level = fuel_level

    # Getter and Setter methods for encapsulated attributes
    def get_type(self):
        return self.type

    def get_speed(self):
        return self.speed

    def set_speed(self, new_speed):
        self.speed = new_speed

    def get_fuel_level(self):
        return self.fuel_level

    def refuel(self, amount):
        self.fuel_level += amount
        print(f"The {self.type} refuels by {amount}. Fuel level now: {self.fuel_level}")

    # Methods
    def drive(self):
        if self.fuel_level > 0:
            print(f"The {self.type} drives at {self.speed} Kmh.")
            self.fuel_level -= 1
        else:
            print("The vehicle is out of fuel!")

    def stop(self):
        print(f"The {self.type} stops.")

# Example Implementation
char = Character("Denise", 99, "Jinja")
vehicle = Vehicle("Van", 80, 30)

# Demonstrate Character methods
char.move("Bugembe")
char.attack("Traitor")
char.interact("NPC")

# Demonstrate Vehicle methods
vehicle.drive()
vehicle.refuel(8)
vehicle.stop()


# Extending the Character class for vehicle interaction
class Character:
    # Existing code...

    def get_in(self, vehicle):
        print(f"{self.name} gets into the {vehicle.get_type()}.")
        self.position = "in vehicle"

    def get_out(self, vehicle):
        print(f"{self.name} gets out of the {vehicle.get_type()}.")
        self.position = "outside vehicle"

# Example Implementation
char = Character("Denise", 99, "Jinja")
vehicle = Vehicle("Van", 80, 30)

# Demonstrate Character interacting with Vehicle
char.get_in(vehicle)
vehicle.drive()
char.get_out(vehicle)
