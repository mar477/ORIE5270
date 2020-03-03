## ORIE 5270
## Spring 2020
## Homework 4
## Name: Mrinal Ramsaha
## NetID: mar477

class Sorter:

    """
    Sorter
    """
    # Initializing the sorter
    def __init__(self,reverse=False):
        self.reverse = reverse

    def mergesort(self,x):
        if len(x) == 0: #Empty string
            return []
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
        if self.reverse == False:
            return i_list[0] # Normal
        else:
            return i_list[0][::-1] # Reverse
