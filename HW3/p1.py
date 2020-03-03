## ORIE 5270
## Spring 2020
## Homework 3
## Name: Mrinal Ramsaha
## NetID: mar477

# Libraries
import numpy as np
import matplotlib.pyplot as plt
import time

# Part 1
def mergesort(x):
    i_list = [[i]for i in x] #Initialize list
    while len(i_list) != 1: #Merging
        y_list = [] #merge list
        q = 0 # counter
        while q < len(i_list): 
            if q == (len(i_list)-1): # If odd number of entries
                part_1 = i_list[q]
                part_2 = []
            else: # if even number of entries
                part_1 = i_list[q]
                part_2 = i_list[q+1]
            q += 2 # Step size
            j,k = 0,0 # initialize for merge parameters
            merge = []
            while j <= len(part_1) or k <= len(part_2): # Merge
                if part_2 == []: # If odd, return the array
                    merge += part_1
                    break
                if j >= len(part_1): # If iterated through part_1 already
                    merge += part_2[k:]
                    break
                elif k >= len(part_2): # If iterated through part_2 already
                    merge += part_1[j:]
                    break
                elif part_1[j] < part_2[k]: # Compare part 1 and part 2
                    merge.append(part_1[j])
                    j += 1
                elif part_2[k] <= part_1[j]: # Compare part 2 and part 1 (if above false)
                    merge.append(part_2[k])
                    k +=1
            y_list.append(merge) 
        i_list = y_list # updating i_list
    return i_list[0]

# Part 2

y_coord = [] # empty array for y_coordinates (time)
x_coord = [2**10,2**11,2**12,2**13,2**14,2**15,2**16,2**17,2**18] # array of n

for t in x_coord: # Loop through different n
    x = np.random.rand(1,t) #Creating array
    start_clock = time.time() # Starting the clock
    mergesort(x[0]) # Mergesort function (above)
    stop_clock = time.time() # Stopping the clock
    y_coord.append(stop_clock-start_clock)

# Plot
plt.plot(x_coord,y_coord)
plt.show()



