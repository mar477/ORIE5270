## ORIE 5270
## Spring 2020
## Homework 4
## Name: Mrinal Ramsaha
## NetID: mar477


# Citations: https://www.youtube.com/watch?v=tx-M_rqhuUA
# Citations: http://weitz.de/ieee/

def getBinaryRepresentation(x):
    num = x # Initializing number
    # Sign 
    if num >= 0 :
        sign = "0"
    else:
        sign = "1"
        num = -num

    # Digit (Correct)
    if num >= 1:
        int_num = int(num) # Find integer
        string = ""
        while int_num != 0: # Compute remainder 
            string += str(int_num%2) # Add mod
            int_num = int_num // 2
        string_num = string[::-1] # Reverse order
    else:
        string_num = "" # Else empty string

    # Decimal (Correct)
    if int(num) != num:
        dec_num = num - int(num) # Decimal number part
        string_dec = "" # Empty string
        exponent_1 = 0
        for p in range(0,150): # Range of mantissa (max) assuming above is empty
            dec_num = dec_num * 2 
            if dec_num < 1:
                if string_dec != "" or string_num != "" :
                    string_dec += "0" # Zero found
                if string_dec == "":
                    exponent_1 += 1

            elif dec_num >= 1:
                string_dec += "1" # One found
                dec_num -= 1
    else:
        string_dec = "" # If no decimal, string is empty

    # Number converted to binary
    string_final = string_num + string_dec # Merging the two sides 
    string_binary_1 = string_final[1:] # Remove the one at the start
    if len(string_binary_1) >= 52:
        string_binary = string_binary_1[:52] # Limit length to 52
    elif len(string_binary_1) < 52: # If length less, adds zeroes
        string_binary = string_binary_1
        while len(string_binary) != 52:
            string_binary += "0"

    # Exponent
    exponent = len(string_num) - 1 # Finding where the "." is
    if exponent == -1: # In case only decimal
        exponent = -(exponent_1+1)
    binary_number = "{:b}".format(1023+exponent) # Converting to binary
    while len(binary_number) != 11: # Adding to add up to 0
        binary_number = '0' + binary_number 

    final_answer = sign + binary_number + string_binary
    final_array = []
    for i in final_answer:
        final_array.append(int(i))

    return final_array
