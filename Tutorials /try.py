class Employee:
    def __init__ (self, salary: float, department:str):
        self.__salary = salary
        self.__department = department

    def getSalary(self):
        return self.__salary
    
    def getDepartment(self):
        return self.__department
    
    def setSalary(self, amount):
        return self.__salary
    

Emp1 = Employee(5000.30, 'HR')

Emp1.setSalary()
# Emp1.getDepartment()
# print ('Salary received is USD ', Emp1.getSalary())
print(f'Salary received is USD {Emp1.getSalary()}')