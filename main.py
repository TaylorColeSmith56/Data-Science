# -*- coding: utf-8 -*-
"""
edited on Wed Mar  1 12:44:54 2017
@author: TaylorColeSmith
"""
#!/usr/bin/python

from PIL import Image
import matplotlib.pyplot as mp
import numpy as np
import os 

#opens folder in operating system
files=os.listdir("podatlamar")
#list of average image
avg_img = []
#instantiates file count
file_ct = 0
#img=Image.open("")

# user inputs change threshold number
th = input(" Enter your change threshold: ")
# parse user unput into int 
th_num =int(th)
# checks if treshold  is between 0 and 255
if(th_num > 0) and  (th_num < 255):

    #instantiates list of images
    list_img = []
    #loops through length of files
    for i in range(0, len(files)):
        # checks if a file is a jpg image in a list of files
        if ".jpg" in files[i]:
        #print(files[i])
         #opens files and adds them to a list of files
            img = Image.open("podatlamar/"+files[i])
            #changes each file to a float32 images
            list_img.append(np.float32(img))
     #instantiates list of atandard images
    std_img = []
    # loops through list of images
    for img in list_img:
       try:
           avg_img = avg_img + img 
#std_img.append(img)
       except:
           avg_img = img
#std_img.append(img)
 
       
    avg_img /= len(list_img)

    std_img = np.std(list_img, axis = 0)
    for row in range(len(avg_img)):
        for col in range(len(avg_img[row])):
            cur_ind = sum(std_img[row][col])
            if (cur_ind > th_num):
                avg_img[row][col]=[255.0, 0.0, 0.0]  
# print (files[row][col])

    avg_img=avg_img.clip(0, 255)
    
    avg_img=np.uint8(avg_img)
  
    #shows the average image
    mp.imshow(avg_img)
    #shows the plot
    mp.show()
# print if number is outside the theshold
else:
    print("Number not in theshold")