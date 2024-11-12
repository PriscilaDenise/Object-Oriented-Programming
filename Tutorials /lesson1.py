# class Student:
#     pass 

# Object instantiation
# std1 = Student()
# std2 = Student()

# #Object initialization 
# std1.fname = 'Denise'
# std1.lname = 'Muwanguzi'
# std1.reg = 'B20237'
# std2.fname = 'Vanessa'
# std2.lname = 'Musaasizi'
# std2.reg = 'A23452'


# print(std1.reg)
# print(std2.lname)


# class Student:
#     def initialize(obj, f,l,r):
#         obj.fname = f
#         obj.lname = l
#         obj.reg = r

# # Object instantiation
# std1 = Student()
# std2 = Student()

# #Object initialization 
# Student.initialize(std1, 'Denise', 'Muwanguzi', 'B20237')
# Student.initialize(std2, 'Vanessa', 'Musaasizi', 'A23452')

# print(std1.reg)
# print(std2.lname)


# class Student:
#     def initialize(obj, f,l,r):
#         obj.fname = f
#         obj.lname = l
#         obj.reg = r

# # Object instantiation
# std1 = Student()
# std2 = Student()

# #Object initialization 
# std1.initialize('Denise', 'Muwanguzi', 'B20237')
# std2.initialize('Vanessa', 'Musaasizi', 'A23452')

# print(std1.reg)
# print(std2.lname)


class Student:
    def initialize(self, fname,lname,reg):
        self.fname = fname
        self.lname = lname
        self.reg = reg

# Object instantiation
std1 = Student()
std2 = Student()

#Object initialization 
std1.initialize('Denise', 'Muwanguzi', 'B20237')
std2.initialize('Vanessa', 'Musaasizi', 'A23452')

print(std1.reg)
print(std2.lname)
