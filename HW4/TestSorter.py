## ORIE 5270
## Spring 2020
## Homework 4
## Name: Mrinal Ramsaha
## NetID: mar477

import unittest
import Sorter # Same dir

# Testing Sorter 
class TestSorter(unittest.TestCase):

    def test_blank_reverse(self):
        # Blank + Reverse
        y = Sorter.Sorter(reverse=True)
        x = []
        self.assertEqual(y.mergesort(x),[])

    def test_blank_no_reverse(self):
        # Blank + No Reverse
        y = Sorter.Sorter(reverse=False)
        x = []
        self.assertEqual(y.mergesort(x),[])
    
    def test_no_reverse_set(self):
        # Reversing default (False)
        y = Sorter.Sorter()
        x = [10,9,8,7,6]
        self.assertEqual(y.mergesort(x),[6,7,8,9,10])

        y = Sorter.Sorter()
        x = [6,7,9,8,10]
        self.assertEqual(y.mergesort(x),[6,7,8,9,10])

    def test_no_reverse(self):
        # Reversing set to False
        y = Sorter.Sorter(reverse=False)
        x = [10,9,8,7,6]
        self.assertEqual(y.mergesort(x),[6,7,8,9,10])

        y = Sorter.Sorter(reverse=False)
        x = [6,7,9,8,10]
        self.assertEqual(y.mergesort(x),[6,7,8,9,10])

    def test_reverse(self):
        # Reversing set to True
        y = Sorter.Sorter(reverse=True)
        x = [10,9,8,6,7]
        self.assertEqual(y.mergesort(x),[10,9,8,7,6])

        y = Sorter.Sorter(reverse=True)
        x = [6,7,9,8,10]
        self.assertEqual(y.mergesort(x),[10,9,8,7,6])

    