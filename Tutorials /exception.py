# class calculator:
#     def divide(self, numerator, denominator):
#         try:
#             return numerator / denominator
#         except ZeroDivisionError:
#             return 'Cannot divide by zero. '
        
# calc = calculator()
# print(calc.divide(3,2))
# print(calc.divide(10,0))
# print(calc.divide(0,7))



# class InputValidator:
#     def get_positive_number(self):
#         number = int(input('Enter a positive number: '))
#         if number<0:
#             raise ValueError('Number should be positive.')
        
#         return number
    
# validator = InputValidator()
# try:
#     result = validator.get_positive_number()
#     print(f'You entered: {result}')
# except ValueError as e:
#     print(f'Error: {e}')



class FileManager:
    def read_file(self, filename):
        try:
            file = open(filename, 'r')
            return file.read
        
        except FileNotFoundError:
            print(f'File {filename} not found.')
        
        finally:
            print("Closing the file.")
            if file:
                file.close()

manager = FileManager()
content = manager.read_file('text.txt')