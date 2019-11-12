#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        '''Test defauly product flammability being 0.5'''
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)
    
    def test_method_functions(self):
        '''Testing Acme's functions are top shelf'''
        prod = Product('Big Hammer', weight=5, flammability=55)
        self.assertEqual(prod.explode(), '...BABOOM!!')
        self.assertEqual(prod.stealability(), 'Very stealable!')


class AcmeReportTests(unittest.TestCase):
    '''Ensuring Acme reports are in ship shape'''
    def test_default_num_products(self):
        '''Test number of products generated'''
        report = generate_products()
        self.assertEqual(len(report), 30)
    
    def test_legal_names(self):
        '''Test names for legal format'''
        report = generate_products()
        
        # Check  that output is from ADJECTIVES and NOUNS and is separated by list
        for ii in range(len(report)):
            self.assertIn(report[ii].name.split(' ', 1)[0], ADJECTIVES)
            self.assertIn(report[ii].name.split(' ', 1)[1], NOUNS)


if __name__ == '__main__':
    unittest.main()