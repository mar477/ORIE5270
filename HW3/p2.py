## ORIE 5270
## Spring 2020
## Homework 3
## Name: Mrinal Ramsaha
## NetID: mar477

# Assumption: Case insensitive & sort can be used
# Complexity: O(n log n ) because of the sort function

def isAnagram(s,t):
    # Length not same means not possible to be anagram
    if len(s) != len(t):
        return False

    # Sort strings
    word_1 = sorted(s.lower()) #case sensitive
    word_2 = sorted(t.lower()) #case sensitive
    if (word_1 == word_2):
        return True
    else:
        return False

## If sort cannot be used, a set may be used instead 
## Complexity: O(n^2)

def isAnagram2(s,t):
    #Length check
    if len(s) != len(t):
        return False
    
    bag = []
    # Iterate through s
    for c in s.lower():
        bag.append(c)
    
    # Iterate through t
    for c in t.lower():
        if c in bag:
            bag.remove(c)
        else: 
            return False
    
    if len(bag) == 0: return True
    else: return False

