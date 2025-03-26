class Animal:
    def __init__ (self, species, name, habitat):
        self.species = species
        self.name = name 
        self.habitat = habitat


class Mammal(Animal):
    def __init__ (self, species, name, habitat, fur_color):
        super().__init__(species, name, habitat)
        self.fur_color = fur_color
        self.state = 'not fed'

    def feed(self):
        if self.state == 'fed':
            print(f'{self.name} is already fed')

        else: 
            self.state = 'fed'
            print(f'{self.name} has been fed')


    def display_animal_info(self):
        print(f'Species: {self.species}\nName: {self.name}\n Current state: {self.state}')


Animal1 = Mammal('Reptile', 'Snake', 'Forest', 'NULL')
Animal2 = Mammal('Carnivore', 'Lion', 'Game park', 'Brown')

Animal1.display_animal_info()
Animal2.feed()
Animal2.display_animal_info() 
Animal2.feed()
