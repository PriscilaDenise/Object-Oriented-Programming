class car: 
    def __init__ (self, brand:str, model:str, year:int, mileage:int):
        self.brand = brand
        self.model = model 
        self.year = year 
        self.mileage = mileage

    def display_info(self):
        print (f"Car: {self.brand}, {self.model} \n Year: {self.year}\n Mileage: {self.mileage}Km")

    def drive(self, distance):
        self.mileage += distance 

        print(f"You've driven a distance of {distance} Km.")

car1 = car("Toyota", "Corolla", 2021, 25670)
car2 = car("Honda", "Civic", 2006, 14000)
car3 = car("Ford", "Mustang", 2012, 120000)
car4 = car("Nissan", "Altima", 2022, 5000)

car1.display_info()
car2.display_info()
car3.display_info()

car4.drive (100)
car4.display_info()


#QN 3

class Electric_car(car):
    def __init__(self, brand:str, model:str, year:int, mileage:int, battery_capacity:int, charge_level:int):
        super().__init__(brand, model, year, mileage)
        self.battery_capacity = battery_capacity
        self.charge_level = charge_level

    def charge(self, amount):
        self.charge_level = min(self.charge_level + amount, 100)
        print(f"Car has charged to {self.charge_level}%.")

    def display_info(self):
        super().display_info()  
        print(f"Battery Capacity: {self.battery_capacity} kWh, Charge Level: {self.charge_level}%")


electric_car = Electric_car("Tesla", "Model S", 2023, 12000, 100, 75)


electric_car.display_info()
electric_car.charge(20)
electric_car.display_info()

"""
The Electric_car class demonstrates modularity by separating the electric car's specific behavior
such as charging) into its own class while inheriting common car attributes and methods from the Car class.
This allows for reusability since the Car class can be used to define multiple types of vehicles,
and Electric_car can extend that functionality without duplicating code.
Additionally, OOP enhances maintainability because if changes are needed (e.g., updating how cars display information),
we can modify the parent Car class, and all child classes will automatically inherit these changes without needing 
to adjust each one individually.
"""


#QN 4 
# Procedural approach for car functionality

# Function to create a car (dictionary)
def create_car(brand, model, year, mileage):
    return {'brand': brand, 'model': model, 'year': year, 'mileage': mileage}

# Function to display car details
def display_car_info(car):
    print(f"Car: {car['brand']} {car['model']}, Year: {car['year']}, Mileage: {car['mileage']} km")

# Function to update the mileage after driving
def drive_car(car, distance):
    car['mileage'] += distance
    print(f"You've driven {distance} km.")

# Creating cars using the procedural approach
car1 = create_car("Toyota", "Corolla", 2020, 25000)
car2 = create_car("Honda", "Civic", 2019, 30000)
car3 = create_car("Ford", "Mustang", 2021, 15000)

# Displaying car info and driving the cars
display_car_info(car1)
drive_car(car1, 100)
display_car_info(car1)




#QUESTION 4 b

""""
DIFFERENCES NOTICED BETWEEN OOP AND PROCEDURAL PROGRAMMING
--> OOP uses classes, Methods and Objects to structure the code while procedural uses functions and dictionaries
--> OOP uses encapsulation within objects while procedural programming uses separate entities

--> Procedural programming doesn't support inheritance while OOP supports inheritance

--> Procedural programming comprises of functions while OOP comprises of objects

-->In procedural programming code is typically divided into modules or subroutines while OOP is typically
    divided into classes and objects"""


"""How does OOP provide benefits like modularity, reusability, and maintainability compared to procedural programming?

OOP has modularity provides encapsulation of data and methods that are used within the class and this
creates organized self contained units while procedural programming functions are all separated

OPP enables reusability of methods and attributes like in the case of inheritance a child class is
able to reuse the methods and attributes of its parent class while this functionality is no available
in procedural programming

OOP provides easier maintainability in terms of modifications ie; changes can be made to specific objects or
their methods without affecting the entire program, reducing the risk of unintended side effects while this is
not applicable in procedural programming."""


# ============================= QUESTION 5 ===============================================

class StudentManagement:
    def __init__(self):
        self.student_info = {} # Instance variable to to store student data

    def add_students(self, reg_no: int, name: str, gender: str, course: str):
        try:
            if reg_no in self.student_info.keys():
                print(f'Student with reg_no {reg_no} is already registered')
                return

            self.student_info[reg_no] = [name, gender, course]
            print(f'{self.student_info[reg_no][0]} has been registered successfully')
        except ValueError: # raise Value error if there are arguments missing
            print(f'Missing some arguments. Please try again')

    def update_student(self, reg_no: int, name: str, gender: str, course: str):
        if reg_no not in self.student_info.keys():
            # Raise ValueError when no reg_no in the list of dictionary keys
            raise ValueError(f'No student with registration number {reg_no}')
        self.student_info[reg_no] = [name, gender, course]

    def delete_students(self, reg_no):
        try:
            print(f'{self.student_info[reg_no][0]} has been deleted successfully')
            del self.student_info[reg_no]
        except KeyError:
            print(f'No student with registration number {reg_no}')


student_system = StudentManagement()

"""Adding students"""
student_system.add_students(1, 'ATWIJUKIRE APOPHIA', 'Female', 'BSCS')
student_system.add_students(2, 'YAWE DAVID', 'Female', 'BSIT')
student_system.add_students(3, 'KUNDAKWE JOSHUA', 'Female', 'BSDT')
student_system.add_students(3, 'HELLEN JANES', 'Male', 'DIT')
try:
    student_system.add_students(4, 'ARINDA LINDA', 'Female')
except TypeError: # Raise TypeError when there are some missing arguments in the method
    print('Student is missing some information')

"""Updating students"""
try:
    student_system.update_student(5, 'PRETTY NICOLE', 'Female', 'BSDT')
except ValueError as e:
    print(f'Ooops {e}')


"""Deleting a student"""
student_system.delete_students(3)

student_system.delete_students(5)