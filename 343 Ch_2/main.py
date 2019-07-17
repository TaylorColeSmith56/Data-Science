# -*- coding: utf-8 -*-
"""
@author:Taylor Cole Smith
Edited on Wed Feb 28 2017
"""
#!/usr/bin/python
import matplotlib.pyplot as mp
import string 

#opens CSV file for reading
file = open("sent_lexicon.csv", "r")
#gets raw data from file
data = file.read()
#splits the list based on lines
data = data.split("\n")
#makes three dictionaries to hold a count, sum, lexicon of our data
count = {}
sum = {}
lex = {}

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
      
      #converts the first item from int to float
      lex[data[index][0]] = float(data[index][1])
     

#f3 = ("d08.txt")
# user inputs file name 
f1=input(" Enter the name of your file: ")

#removes punctuation from a string
remove = dict.fromkeys(map(ord, string.punctuation))
# opens user inputs file 
with  open(f1, "r") as iF:
     #removes lower cases and spaces from a string in a file
     f= iF.read().translate(remove).lower().split()
#print(f)
      #keeps count of each key 
     for key in f:
         count[key] = f.count(key)
        
#print(lex)
#initiates the count the "Negative", "Weak Negative", "Neutral",
#"Weak Positive", "Positive" 
neg_ct = 0
wn_ct = 0
ntl_ct = 0
wp_ct = 0
pos_ct = 0
for key,values in count.items():
    
        if key in lex:
            values1 = lex[key]
            #gets the sum the "Negative", "Weak Negative", "Neutral",
            
            #"Weak Positive", "Positive" lexicon counts in a file
            if (values1 < -0.6):
                neg_ct += values
#                print(values1)
            elif(values1 >= -0.6) and  (values1 < -0.2):
                wn_ct += values  
            elif(values1 >= -0.2) and  (values1 <= 0.2):
                ntl_ct += values 
            elif (values1 > 0.2) and  (values1 <= 0.6):
                wp_ct += values  
            else:
                if(values1 > 0.6) and  (values1 <= 1.0):
                   pos_ct += values
                  
#gets the total of all the "Negative", "Weak Negative", "Neutral",
#"Weak Positive", "Positive" lexicon counts in a file put together                     
total = (neg_ct + wn_ct + ntl_ct + wp_ct  + pos_ct)
#puts the labels of the "Negative", "Weak Negative", "Neutral",
#"Weak Positive", "Positive" on each respective bar  
xlabels=["Negative", "Weak Negative", "Neutral", "Weak Positive", "Positive"]   
#gets the average of the "Negative", "Weak Negative", "Neutral",
#"Weak Positive", "Positive" lexicon counts in a file
# length of the blue bars of the bar graph
sent_dist=[ neg_ct/total, wn_ct/total, ntl_ct/total, wp_ct/total, pos_ct/total]
print(sent_dist)

#bar positions on x axis 
bar_pos=[-2.5, -1.2, 0.0, 1.1, 2.3]
#label positions on x axis 
label_pos=[-2.5, -1.2, 0.0, 1.1, 2.3]

mp.xlabel(" Sentiment ")
mp.ylabel(" Percent of Words ")
mp.title("Sentiment Distribution")

#draws a blue bar plot
mp.bar(bar_pos, sent_dist, color = "blue")
#changes yaxis from 0.0 - 0.35 to 0.0 - 0.40
mp.axis([-3.0, 3.0, 0.0, .40])
#puts ticks and labels 
mp.xticks(label_pos, xlabels)
#shows the plot
mp.show()

