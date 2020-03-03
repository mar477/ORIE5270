## ORIE 5270
## Spring 2020
## Homework 4
## Name: Mrinal Ramsaha
## NetID: mar477


import unittest
import getBinaryRepresentation # Same dir


class TestSorter(unittest.TestCase):

    # Passed (Decimal Only)
    def test_decimal_only(self):
        sign = "0"
        # 0.5256
        x = 0.5256
        exp = "01111111110"
        mantissa = "0000110100011011011100010111010110001110001000011001"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # 0.005
        x = 0.005
        mantissa = "0100011110101110000101000111101011100001010001111011"
        exp = "01111110111"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # 0.0005
        x = 0.0005
        exp = "01111110100"
        mantissa = "0000011000100100110111010010111100011010100111111100"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)

    # Passed (Integer Only)
    def test_integer_only(self):
        sign = "0"
        # 1
        x = 1
        exp = "01111111111"
        mantissa = "0000000000000000000000000000000000000000000000000000"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # 101
        x = 101
        mantissa = "1001010000000000000000000000000000000000000000000000"
        exp = "10000000101"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # 21000
        x = 21000
        exp = "10000001101"
        mantissa = "0100100000100000000000000000000000000000000000000000"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
    
    # Passed (Integer and Decimal)
    def test_integer_decimal(self):
        sign = "0"
        # 45.5256
        x = 45.5256
        exp = "10000000100"
        mantissa = "0110110000110100011011011100010111010110001110001000"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # 58.005
        x = 58.005
        mantissa = "1101000000001010001111010111000010100011110101110001"
        exp = "10000000100"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # 21000.0005
        x = 21000.0005
        exp = "10000001101"
        mantissa = "0100100000100000000000001000001100010010011011101001"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)

    # Passed (Negative Integer Only)
    def test_negative_integer_only(self):
        sign = "1"
        # 1
        x = -1
        exp = "01111111111"
        mantissa = "0000000000000000000000000000000000000000000000000000"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # 101
        x = -101
        mantissa = "1001010000000000000000000000000000000000000000000000"
        exp = "10000000101"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # 21000
        x = -21000
        exp = "10000001101"
        mantissa = "0100100000100000000000000000000000000000000000000000"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)

    # Passed (Negative Decimal Only)
    def test_negative_decimal_only(self):
        sign = "1"
        # -0.5256
        x = -0.5256
        exp = "01111111110"
        mantissa = "0000110100011011011100010111010110001110001000011001"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # -0.005
        x = -0.005
        mantissa = "0100011110101110000101000111101011100001010001111011"
        exp = "01111110111"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # -0.0005
        x = -0.0005
        exp = "01111110100"
        mantissa = "0000011000100100110111010010111100011010100111111100"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)

    # Passed (Negative Integer and Decimal)
    def test_negative_integer_decimal(self):
        sign = "1"
        # 45.5256
        x = -45.5256
        exp = "10000000100"
        mantissa = "0110110000110100011011011100010111010110001110001000"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # 58.005
        x = -58.005
        mantissa = "1101000000001010001111010111000010100011110101110001"
        exp = "10000000100"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)
        
        # 21000.0005
        x = -21000.0005
        exp = "10000001101"
        mantissa = "0100100000100000000000001000001100010010011011101001"
        ans_str = sign + exp + mantissa
        ans = [int(i) for i in ans_str]
        self.assertEqual(getBinaryRepresentation.getBinaryRepresentation(x),ans)

