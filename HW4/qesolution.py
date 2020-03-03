## ORIE 5270
## Spring 2020
## Homework 4
## Name: Mrinal Ramsaha
## NetID: mar477

import math # Import math

def qesolution(b,c):
    # Returns an array with the roots
    bracket = ((-2*b)**2) + (4*1*c)
    bracket_sq_root = math.sqrt(bracket)
    x1_p1 = (2*b) + bracket_sq_root
    x2_p1 = (2*b) - bracket_sq_root
    x1 = x1_p1/2.
    x2 = x2_p1/2.
    return [x1,x2]

