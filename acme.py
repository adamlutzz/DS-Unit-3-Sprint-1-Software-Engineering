import random


class Product:

    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = 0.5
        self.identifier = random.randint(1000000, 9999999)
    
    def stealability(self):
        if self.price / self.weight < 0.5:
            return 'Not so stealable...'
        else:
            if self.price / self.weight > 1:
                return 'Very stealable!'
            else:
                return 'Kinda stealable.'

    def explode(self):
        if self.flammability * self.weight < 10:
            return '...fizzle.'
        else:
            if self.flammability * self.weight > 50:
                return '...BABOOM!!'
            else:
                return '...boom!'


class BoxingGlove(Product):

    def __init__(self, weight=10):
        super().__init__(name, price, flammability, identifier)
    
    def explode(self):
        return "...it's a glove."
    
    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        else:
            if self.weight > 15:
                return 'OUCH!'
            else:
                return 'Hey that hurt!'

 
