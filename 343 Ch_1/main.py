# -*- coding: utf-8 -*-
"""
#@author: Taylor Cole Smith
Edited on Monday Feb  13  2017
"""
#!/usr/bin/python
import matplotlib.pyplot as mp

#opens CSV file for reading
file = open("sympatheticDingo_ch1.csv", "r")
#gets raw data from file
data = file.read()
#splits the list based on lines
data = data.split("\n")

#makes lists for holding the x and y axis
#values to be graphed 
xaxis = []  
yaxis = []

#makes lists for holding the x and y 
#values to be graphed
x = []
y = []

#makes two dictionaries to hold a count and sum of our data
count = {}
sum = {}

#loops through each line of data
for index in range(0, len(data)):  
      #checks if the line of data is empty
      if len(data[index]) == 0:
          #removes empty line at the end of the file
          del(data[index])
          #skips the rest of the loop
          continue
      #splits the line based on commas
      data[index] = data[index].split(",")
      #converts the last three items from int to float
      data[index][0] = float(data[index][0])
      data[index][1] = float(data[index][1])
      data[index][2] = float(data[index][2])
      
#loops through the data list        
for index in range(0, len(data)):
    #checks if the line of data is not equal this float 
    if data[index][2] != 30.169499:
        #appends index zero data to the x axis 
        #appends index one data to the y axis
        xaxis.append(data[index][0])
        yaxis.append(data[index][1])
        
#loops through the data list              
for index in range(0, len(data)):
  if data[index][2] != 30.169499:
      #stores my target as "label" and my judgment as "value"
      label = data[index][0]
      value = data[index][1]
      #tries to add the value to sum
      #also tries to increment count by 1
      try:
          #if the entry for "label" is not in the dictionary yet
          #this code will fail, but my except will take care of it
          sum [label] +=  value
          count [label] += 1
      except:
          # if the try fails, then that means the an entry for
          # "label" isn't in the dictionary, below i make
          # the entry.
          sum[label] = value
          count[label] = 1

#loops through the count dictionary
for key,values in count.items():
   #divides the sum for each key by its corresponding count
   sum[key] /= count[key]
   #later I will divide the sum by key
   #this will give me a divide-by-zero error
   #when key = 0, so for the purposes of my
   #graph I omited this case
   if key == 0:
      continue
   #adds the key to the xaxis list
   x.append(key)
   #adds the sum to the yaxis list
   y.append(sum[key]) 
   
#makes a temporary list that contains our both axes of data
sorted_data = zip(x, y)
#sorts the list based on the first element (the xaxis value)
sorted_data = sorted(sorted_data)
#splits the sorted list back into two separate lists
x, y = zip(*sorted_data) 
   
mp.xlabel("milliseconds")
mp.ylabel("Amplititde")

#draws a red line plot
mp.plot(x, y, color = "red") 
#draws a blue scatter plot
mp.scatter(xaxis, yaxis, color = "blue")
#shows the combined plot
mp.show








