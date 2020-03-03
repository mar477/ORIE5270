## ORIE 5270
## Spring 2020
## Homework 4
## Name: Mrinal Ramsaha
## NetID: mar477

import math # Import math

def qesolutionRevise(b,c):
    # Returns an array with the roots

    # X2
    r = math.sqrt(((-2*b)**2) + (4*1*c))
    x2 = -1*2*c/(2*b+r)

    # X1
    bracket = ((-2*b)**2) + (4*1*c)
    bracket_sq_root = math.sqrt(bracket)
    x1_p1 = (2*b) + bracket_sq_root
    x2_p1 = (2*b) - bracket_sq_root
    x1 = x1_p1/2.
    return [x1,x2]




