from abc import ABC, abstractmethod

class User(ABC):
    def __init__ (self, username, password):
        self.username = username 
        self.password = password

    @abstractmethod
    def login():
        pass


class AdminUser(User):
    def __init__ (self, username, password):
        super().__init__ ( username, password)

    def login(self):
        global enter_code, verificationcode
        verificationcode = 1234
        enter_code = int(input(f'Verification code:'))
        if enter_code == verificationcode:
            print('Login successful')
        else:
            print('Incorrect verification code')
        
        Password = 'Changemenow@2231'
        enter_password =  input('Enter password: ')
        if enter_password == Password:
            print ('Login successful!!')
        else:
            print ('Incorrect password')

    def edit_content(self):
        print(f'{self.username} is Editing content...')

    def manage_permissions(self):
        verificationcode = 1234
        enter_code = int(input('Verification code:'))
        if enter_code == verificationcode:
            print('Can manage permissions')
        else:
            print('Incorrect verification code')


class GuestUser(User):
    def __init__ (self, username, password):
        super().__init__ ( username, password)

    def login(self):
        Username = input(f'Username:')
        Guest_password = input(f'Password:')
        print(f'{Username} has logged in.')
        print(f'Welcome, {Username}!!')

    def view_Pages(self):
        print('Welcome to our website!!')

    


admin1 = AdminUser('DEN', '@hello123')
guest1 = GuestUser('LYNN', 'hello123')

admin1.manage_permissions()
guest1.login()