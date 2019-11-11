#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # I would think making a dictionary would be easier here
    
    for ii in num_products:
        {name: sample(ADJECTIVES,1)}
        products.append(randint(5, 100))
        products.append(randint(5, 100))
        products.append(uniform(0.0, 2.5))
    # the main issue I am running into here is making a list that for each loop
    # it makes a list includeing random names and attribues together

    return products


def inventory_report(products):
    # I need to make a set of the products but I dont have time
    


if __name__ == '__main__':
    inventory_report(generate_products())