class Publisher:
    def __init__ (self, name, location, founded_year):
        self.name = name
        self.location =  location
        self.founded_year = founded_year

class Magazine(Publisher):
    def __init__ (self, name, location, founded_year, issue_number = None):
        super().__init__ (name, location, founded_year)
        self.issue_number = issue_number

    def publish(self):
        if self.issue_number == None:
            print(f'{self.name} is publishing their first magazine.')

        else:
            print(f'{self.name} is publishing their {self.issue_number} magazine')

    def display_magazine_info(self):
        print(f'Name:{self.name}\nLocation:{self.location}\nYear:{self.founded_year}\nIssue:{self.issue_number}')


MG1 = Magazine('BUZZ', 'NY', 2015, 'B45')
MG2 = Magazine('Paragon', 'Uganda', 2020, 'P98')
MG3 = Magazine('Excel', 'Mukono', 2010, 'None')

MG1.publish()
MG2.display_magazine_info()