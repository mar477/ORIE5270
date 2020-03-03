## ORIE 5270
## Spring 2020
## Homework 3
## Name: Mrinal Ramsaha
## NetID: mar477

Problem 1:
Libraries to import: numpy | Matplotlib | time
a) The mergesort function is included in p1.py
b) We can observe that the graph does actually look close to a O(nlogn) graph. The graph
obtained is also in the github repository as p1_plot.png

Problem 2: 
We have two solutions here (assuming we can use sorted or not)
a) Using Sorted
We check the length of the two strings to compare. Then we simply use the sorted function
and compare the two strings. This is O(nlogn)
b) Using array
If we cannot use Sorted, we can iterate through the first string and add it to an array.
Then we can iterate through the other string and remove each letter in the array.
This is O(n^2)

Problem 3:
Libraries to import: collections
Simply, a counter is used for the word and the text. Then the word-counter is subtracted
from the word-counter repeatedly until a negative number is found. This is O(n)