# Person class
class person:
    def __init__ (self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# Employee class inheriting class person
class Employee(person):
    def __init__ (self, name, age, gender, employee_id, department):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.department = department

    def assign_task(self,task):
        self.task = task
        print(f"Task assigned to {self.name} : {self.task}")
        try:
            if self.task == task:
                print(f'{self.task} has already been assigned to {self.name}.')
            else:
                self.task = task
        except AttributeError:
            print(f'{self.task} has been assigned to {self.name}.')

    def display_employee_info(self):
        print(f'{self.name}: {self.department}, {self.task}')

# Creating an instance of Employee class
Emp1 = Employee('Deniz', 21, 'Female', 1, 'IT')
Emp1.assign_task('TEACH')
Emp2 = Employee ('Lynn', 23, 'Female', 2, 'ENG')
Emp2.assign_task('SWIM')

Emp1.display_employee_info()
Emp2.display_employee_info()

