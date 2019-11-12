import random

# create product class
class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5,
        identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
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


# create subclass
class BoxingGlove(Product):
    def __init__(self, name, weight=10):
        super().__init__(self)
        self.name = name
        self.weight = weight

    # overwrite explode method
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