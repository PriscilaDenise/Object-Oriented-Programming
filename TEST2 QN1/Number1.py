"""
Part (a): Character and Vehicle Classes

Character class
Create two classes: Character and Vehicle.
For the Character class, include at least three attributes (e.g., name, health, position) and
three methods (e.g., move(), attack(), interact()).

"""

class Character:
    def __init__(self, name, health, position):
        # In these attributes I am focusing on encapsulation, I am using private attributes
        self._name = name
        self._health = health
        self._position = position

    def move(self, new_position): # A character will move to a new position
        self._position = new_position
        print(f"{self._name} moves to {self._position}")

    def attack(self):
        print(f"{self._name} attacks.")

    def interact(self, item): # In this method, the character will be interacting with a given item
        print(f"{self._name} interacts with {item}")

    # Encapsulation: Getter and Setter for health
    def get_health(self):
        return self._health

    def set_health(self, health):
        # If the character loses some health, i will be able to add it from here
        self._health = health
        print(f"{self._name}'s health set to {self._health}.")

    """Part (b): Interaction Between Objects
        Extend the Character class to include methods that allow interaction with vehicles, 
        such as get_in() and get_out().
    """
    def get_in(self, vehicleObject):
        print(f"{self._name} gets into the {vehicleObject._vehicle_type}")
        self.character_in_vehicle = True

    def get_out(self):
        # if hasattr(self, '_in_vehicle') and self._in_vehicle:
        #     print(f"{self._name} gets out of the vehicle")
        #     self.character_in_vehicle = False
        # else:
        #     print(f"{self._name} is not in a vehicle!")
        self.character_in_vehicle = False
        print(f'{self._name} is getting out of the Van.')


# Vehicle class
class Vehicle:
    def __init__(self, vehicle_type, speed, fuel_level):
        self._vehicle_type = vehicle_type
        self._speed = speed
        self._fuel_level = fuel_level

    def drive(self, destination):
        if self._fuel_level > 0:
            print(f"Driving the {self._vehicle_type} to {destination} at speed {self._speed}")
            self._fuel_level -= 10  # reduce fuel on drive
        else:
            print(f"{self._vehicle_type} is out of fuel!")

    def refuel(self, amount):
        self._fuel_level += amount
        print(f"{self._vehicle_type} refueled by {amount} units.\nFuel level: {self._fuel_level}")

    def stop(self):
        # If you want to stop the Van, this method is called
        print(f"{self._vehicle_type} stops.")


# Demonstration of Character and Vehicle
"""    
Example Implementation: Write code that creates an object of each class and demonstrates how to use their methods.
"""
print('\n========= *Demonstration how to use Character class methods* ==========')
my_character = Character("Denise Priscila", 200, "Jinja")
my_character.move("Nile Avenue")
my_character.attack()
my_character.interact("PHONE")
print(f'The current health of Denise Priscila is {my_character.get_health()}')
my_character.set_health(300)

print('\n========= *Demonstration how to use Vehicle class methods* ==========')
vehicle = Vehicle("Van", 150, 110)
vehicle.drive("Mukono")
vehicle.refuel(50)
vehicle.stop()


"""
b. Interaction Between Objects
Example Implementation: Write code showing a Character object getting into a Vehicle, driving it,
                        and then getting out.
"""
print('\n========= *Demonstration on how the character is interacting with the object Vehicle* ==========')
# Interaction demonstration
my_character.get_in(vehicle) # Passing in vehicle object so that some Character methods can access it.
vehicle.drive("Bugembe")
my_character.get_out()

"""
Part (c): Specialized Character Abilities
Create a specialized version of the Character class (e.g., HeroCharacter) that has unique
abilities or methods (e.g., double_jump(), fast_run()).
"""

class HeroCharacter(Character):
    def __init__(self, name, health, position):
        super().__init__(name, health, position) # Inheriting all the attributes and methods from the Character class

    def double_jump(self):
        # My character will have the ability to double jump
        print(f"{self._name} performs a double jump!")

    def fast_run(self):
        # My character will have the ability to run very fast
        print(f"{self._name} runs fast!")


print('\n========= *Demonstration of Specialized Character Abilities* ==========')
my_hero = HeroCharacter("Vanessa Eden", 200, "Freedom square")
my_hero.double_jump()
my_hero.fast_run()


"""
Part (d): Handling Different Types of Objects with Polymorphism
Use polymorphism to create methods that allow the game to handle different types of objects 
(e.g., different character types or vehicles).
"""


class Bike(Vehicle):
    def __init__(self, vehicle_type, speed, fuel_level):
        super().__init__(vehicle_type, speed, fuel_level)

    def drive(self, destination): # I have used same method drive to change what drive will look like here
        if self._fuel_level > 0:
            print(f"Riding the {self._vehicle_type} to {destination} at speed {self._speed}")
            self._fuel_level -= 7  # less fuel usage for bike
        else:
            print(f"{self._vehicle_type} is out of fuel⛽⛽! Please refuel your {self._vehicle_type} now")


print('\n-----Polymorphism demonstration-----')
bike = Bike("Scooter", 40, 28)
bike.drive("Mukono")
vehicle.drive("Namugongo")


"""
Part (e): Simple Game Scenario

Write a brief game scenario that demonstrates how a player might complete a task or mission 
using the objects and methods you've created.

Example Implementation: Include code showing how a Character object interacts with the environment 
and other objects to accomplish the task or mission above.
"""

print('\n----- 🎮SIMPLE GAME SCENARIO🎮 -----')
# Game scenario where HeroCharacter completes a mission using a Vehicle
print("MISSION: GET BACK MY STOLEN PHONE.")

my_character = HeroCharacter("Denise Priscila", 500, "Jinja")
vehicle = Vehicle("Van", 150, 0)
vehicle.refuel(800)
my_character.get_in(vehicle)
vehicle.drive('Mukono')
vehicle.refuel(600)

vehicle.stop() # At this point in Mukono, the Jam is too much, the character will stop the Van.
my_character.get_out()

# Getting a bike because of jam
bike = Bike("Honda", 200, 200)
bike.drive('Mukono Bishop Tucker Stage')
bike.stop()
my_character.move("Main house")
my_character.attack()
my_character.interact("Guard")
my_character.double_jump()
my_character.interact("PHONE")
my_character.fast_run()

new_vehicle = Vehicle("Honda", 300, 600)
my_character.get_in(new_vehicle)
new_vehicle.drive('Jinja')
new_vehicle.stop()
my_character.get_out()

print("\nMISSION COMPLETE: \n THE HERO HAS SUCCESSFULLY FINISHED THE MISSION! THE PHONE HAS BEEN RETRIEVED!!")