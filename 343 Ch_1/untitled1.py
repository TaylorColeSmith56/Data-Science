# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:55:25 2017

@author: Jane Chapman
"""
import matplotlib.pyplot as mplot
#opens CSV file for reading
file=open("sympatheticDingo_ch1.csv", "r")
#gets raw data from file
data=file.read()
#gets rid of the space/comma error in the data file
data=data.replace(" ", ",")
#splits the list based on lines
data=data.split("\n")
#makes lists for holding the x and y axis
#values to be graphed
xaxis=[]
yaxis=[]
#loops through each line of data
for index in range(0, len(data)):
#checks if the line of data is empty
    if len(data[index]) == 0:
#removes empty line at the end of the file
        del(data[index])
#skips the rest of the loop
        continue
#displays the line
    print ("Line ",index," - ",data[index])
#splits the line based on commas
    data[index]=data[index].split(",")
#converts the last two items to int and float
    data[index][1]=int(data[index][1])
    data[index][2]=int(data[index][2])
#makes two dictionaries to hold a count and num of our data
count={}
sum={}


#loops through the data list
for index in range(0, len(data)):
#stores our target as "label" and our judgment as "value"
    label=data[index][1]
    value=data[index][2]
#tries to add the value to sum
#also tries to increment count by 1
    try:
#if the entry for "label" is not in the dictionary yet
#this code will fail, but our except will take care of it
        sum[label]+=value
        count[label]+=1
    except:
# if the try fails, then that means the an entry for
# "label" isn't in the dictionary, below we make
# the entry.
        sum[label]=value
        count[label]=1
#loops through the count dictionary
for key,values in count.items():
#divides the sum for each key by its corresponding count
    sum[key]/=count[key]
#later we'll divided the sum by key
#this will give us a divide-by-zero error
#when key = 0, so for the purposes of our
#graph let's omit this case
    if key==0:
        continue
#adds the key to the xaxis list
    xaxis.append(key)
#adds the average to the yaxis list
    yaxis.append(sum[key]/key)

#makes a temporary list that contains our both axes of data
sorted_data=zip(xaxis, yaxis)
#sorts the list based on the first element (the xaxis value)
sorted_data=sorted(sorted_data)
#splits the sorted list back into two separate lists
xaxis,yaxis=zip(*sorted_data)
#draws a red line plot
mplot.plot(xaxis, yaxis, color="red")
#draws a blue scatter plot
mplot.scatter(xaxis, yaxis, color="blue")
#shows the combined plot
mplot.show()