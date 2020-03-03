# ORIE 5270
# Spring 2020
# Mrinal Ramsaha (mar477)

# Citations
# https://stackoverflow.com/q/39213597/
# https://stackoverflow.com/q/1393324/
# guru99.com/reading-and-writing-files-in-python.html

# Import modules
import requests
import pandas as pd
import io
import gzip
import numpy as np
import matplotlib.pyplot as plt

# Opening names file
link = ("https://people.cam.cornell.edu/md825/names.txt")
urlData = requests.get(link).content
names = pd.read_csv(io.StringIO(urlData.decode('utf-8')),header=None)
names.columns = ['Number','Names'] #changing header names

# Opening network (pairs of integers)
link = ("https://snap.stanford.edu/data/facebook_combined.txt.gz")
urlData = requests.get(link).content
data = gzip.decompress(urlData)
edges = pd.read_csv(io.StringIO(data.decode('utf-8')),header=None)

# Splitting pairs of integers into two columns
new = edges[0].str.split(" ",n=1,expand=True)
edges["Node 1"] = new[0]
edges["Node 2"] = new[1]
edges.drop(columns=0,inplace=True)

## Part (1)

# Number of Friends Array
nbr_friends = []
for x in range(names["Number"].max()+1):
    a = len(edges.loc[edges["Node 2"]== str(x)])
    b = len(edges.loc[edges["Node 1"]== str(x)])
    nbr_friends.append(a+b)

#New Dataframe
number_of_friends = names.copy()
number_of_friends.drop(columns=['Number'],inplace=True)
number_of_friends['NbrFriends'] = nbr_friends

print(number_of_friends.head(10))

# Part (2)
max_friends = number_of_friends.loc[number_of_friends["NbrFriends"] == number_of_friends["NbrFriends"].max()]
min_friends = number_of_friends.loc[number_of_friends["NbrFriends"] == number_of_friends["NbrFriends"].min()]
max_num = number_of_friends["NbrFriends"].max()
min_num = number_of_friends["NbrFriends"].min()

for i in max_friends["Names"]:
    print(str(i) + " is a very sociable person, he has "+ str(max_num)+ " friends")
for j in min_friends["Names"]:
    print(str(j) + " is a solitary person, he has only "+ str(min_num)+ " friends")

# Part (3)

# Text File
f = open("output2.txt","w+")
f.write("The average number of friends is " + str(number_of_friends["NbrFriends"].mean()))
f.write("\n")
f.write("The median number of friends is " + str(number_of_friends["NbrFriends"].median()))
f.write("\n")
f.write("The variance number of friends is " + str(number_of_friends["NbrFriends"].var()))
f.write("\n")

# PDF File
g = plt.figure();
plt.hist(number_of_friends["NbrFriends"],bins=100)
plt.xlabel('NbrFriends')
plt.ylabel('Number of People')
g.savefig("output2.pdf",bbox_inches='tight')