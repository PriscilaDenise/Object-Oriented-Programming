import random

class Roll:
    def __call__(self):

        return random.randint(1,6)
    
dice = Roll()

print (dice())