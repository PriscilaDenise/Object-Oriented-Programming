from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__ (self, species, age):
        self.species = species
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def __init__ (self, species, age):
        super().__init__ (species, age)

    def make_sound(self):
        return "Roar!"
    
    def feeds(self, food):
        self.food = food
        print(f'Zoo keeper feeds the lion with {self.food}.')

    

class Elephant(Animal):
    def __init__ (self, species, age):
        super(). __init__ (species, age)

    def make_sound(self):
        return 'Trumpets!'
    
    def happy(self):
        print('The elephant is happy when the zoo visitors give it a treat.😀 ')

    def display_info(self):
        print(f'Elephant species: {self.species}\nage: {self.age}\nsound: {self.make_sound()}')


Animal1 = Lion('Carnivore', 12)
Animal2 = Elephant('Herbivore', 15)

Animal1.feeds('meat')
Animal2.happy()
Animal2.display_info()  