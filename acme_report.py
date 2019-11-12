#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    
    # Randomize attributes and append to products
    for _ in range(num_products):

        name = (sample(ADJECTIVES,1) + sample(NOUNS,1))
        random_name = name[0] + ' ' + name[1]
        random_price = (randint(5, 100))
        random_weight = (randint(5, 100))
        random_flammability = (uniform(0.0, 2.5))

        # Instanciate Class and append to list
        temp = Product(name=random_name, price=random_price,
                       weight=random_weight, flammability=random_flammability)
        products.append(temp)

    return products


def inventory_report(products):
    unique_prod = set()
    avg_price = []
    avg_weight = []
    avg_flammability = []

    # Gather values into sets and lists
    for i in range(len(products)):
        unique_prod.add(products[i].name)

    for i in range(len(products)):
        avg_price.append(products[i].price)

    for i in range(len(products)):
        avg_weight.append(products[i].weight)

    for i in range(len(products)):
        avg_flammability.append(products[i].flammability)

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print('Unique Products:', len(unique_prod))
    print('Average Price:', sum(avg_price) / len(avg_price))
    print('Average Weight:', sum(avg_weight) / len(avg_weight))
    print('Average Flammability:', sum(avg_flammability) / len(avg_flammability))


if __name__ == '__main__':
    inventory_report(generate_products())