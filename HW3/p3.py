## ORIE 5270
## Spring 2020
## Homework 3
## Name: Mrinal Ramsaha
## NetID: mar477

import collections #Importing collections
from collections import Counter #Import Counter from collections

#Assumption: Case insensitive
# Counter works like dictionary and is O(n)

def maxNumberOfWords(text,word):

    # Produces a dictionary with each alphabet and their count in word
    word_counter = Counter(word.lower())
    # Produces a dictionary with each alphabet and their count in text
    text_counter = Counter(text.lower())
    
    # Start of count
    i = 0 
    # Subtracts the counts of text from the word each time until it becomes negative
    # This means that "text' has run out of alphabets to choose from
    while (text_counter[min(text_counter,key=text_counter.get)]) > 0 :
        # Removing word from the text
        text_counter.subtract(word_counter)
        # If the removal was possible, append i (counter)
        if (text_counter[min(text_counter,key=text_counter.get)]) >= 0:
            i += 1 #Counter not negative so added
    return i

