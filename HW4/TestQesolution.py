## ORIE 5270
## Spring 2020
## Homework 4
## Name: Mrinal Ramsaha
## NetID: mar477


import unittest
import math
import qesolution # Same dir
import qesolutionRevise # Same dir

class TestQesolution(unittest.TestCase):
    def test_x1_times_x2(self):

        # Value 1
        x1,x2 = qesolution.qesolution(0,25)
        t1 = x1*x2
        t2 = -5*5.0
        diff = abs(t1-t2)
        self.assertTrue(diff <= 1e-12)

        # Value 2
        x1,x2 = qesolution.qesolution(1,8)
        t1 = x1*x2
        t2 = -2*4.0
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)

        # Value 3 
        x1,x2 = qesolution.qesolution(-2,60)
        t1 = x1*x2
        t2 = 6*-10
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)


    def test_x1_plus_x2(self):

        # Value 1
        x1,x2 = qesolution.qesolution(0,25)
        t1 = x1+x2
        t2 = -5+5.0
        diff = abs(t1-t2)
        self.assertTrue(diff <= 1e-12)

        # Value 2
        x1,x2 = qesolution.qesolution(1,8)
        t1 = x1+x2
        t2 = -2+4.0
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)

        # Value 3 
        x1,x2 = qesolution.qesolution(-2,60)
        t1 = x1+x2
        t2 = 6+-10
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)

    def test_fail(self):

        # FAIL (Plus)
        x1,x2 = qesolution.qesolution(123451234,21)
        t1 = x1+x2
        t2 = 246902468.00000006 + -8.5053827813499e-8
        print(t1)
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)

        # FAIL (Plus)
        x1,x2 = qesolution.qesolution(123451234,21)
        t1 = x1*x2
        t2 = 246902468.00000006 * -8.5053827813499e-8
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)

class TestQesolutionRevise(unittest.TestCase):
    def test_x1_times_x2(self):

        # Value 1
        x1,x2 = qesolutionRevise.qesolutionRevise(0,25)
        t1 = x1*x2
        t2 = -5*5.0
        diff = abs(t1-t2)
        self.assertTrue(diff <= 1e-12)

        # Value 2
        x1,x2 = qesolutionRevise.qesolutionRevise(1,8)
        t1 = x1*x2
        t2 = -2*4.0
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)

        # Value 3 
        x1,x2 = qesolutionRevise.qesolutionRevise(-2,60)
        t1 = x1*x2
        t2 = 6*-10
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)


    def test_x1_plus_x2(self):

        # Value 1
        x1,x2 = qesolutionRevise.qesolutionRevise(0,25)
        t1 = x1+x2
        t2 = -5+5.0
        diff = abs(t1-t2)
        self.assertTrue(diff <= 1e-12)

        # Value 2
        x1,x2 = qesolutionRevise.qesolutionRevise(1,8)
        t1 = x1+x2
        t2 = -2+4.0
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)

        # Value 3 
        x1,x2 = qesolutionRevise.qesolutionRevise(-2,60)
        t1 = x1+x2
        t2 = 6+-10
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)


    def test_fail(self):

        # Pass (Plus)
        x1,x2 = qesolutionRevise.qesolutionRevise(123451234,21)
        t1 = x1+x2
        t2 = 246902468.00000006 + -8.5053827813499e-8
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)

        # Pass (Plus)
        x1,x2 = qesolutionRevise.qesolutionRevise(123451234,21)
        t1 = x1*x2
        t2 = 246902468.00000006 * -8.5053827813499e-8
        diff = abs(t1-t2)
        self.assertTrue(diff<=1e-12)
