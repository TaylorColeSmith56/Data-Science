# -*- coding: utf-8 -*-
"""
@author: sympatheticDingo/ Taylor Smith
Edited on Wed May 3
challenge Final
"""


#import division
import neuro
import sys
import numpy as np
#training inputs and their respective targest
file = open("dataset.csv", "r")
data = file.read()
#list of rgb
inputs=[ [255, 0, 0], [0, 255, 0], [0, 0, 255], [0, 255, 255], [0, 0, 0], [255, 255, 255], [90, 100, 209], [120, 80, 255], [0, 100, 200], [79, 0, 90], [255, 0, 255], [255, 255, 0], [100, 100, 100], [234, 234, 234], [90, 180, 199], [69, 49, 79], [219, 225, 249], [89, 0, 90], [187, 235, 56], [70, 59, 212], [3, 7, 50], [60, 2, 60], [1, 12, 34], [45, 12, 11]] 
targets=[ [0], [0], [1], [0], [0], [0], [1], [1], [1], [1], [0], [0], [0], [0], [1], [1], [1], [1],[0], [1], [0]]

for index in range(0,len(inputs)):
    inputs[index][0] /= 255.0
    inputs[index][1] /= 255.0
    inputs[index][2] /= 255.0  
        
#number of repetitions to train the network
reps=10000
#print ("AND-gate Neural Network Example")
#raw_input() = 0
 
val0= input("\tEnter Red value: ")
val1= input("\tEnter Green value:  ")
val2= input("\tEnter Blue value: ")
#converts input to float
val0=float(val0)/255.0
val1=float(val1)/255.0
val2=float(val2)/255.0
network=[] #makes an empty list to contain the neural net
#sets up the network to accommodate the size of your inputs
network=neuro.setup_network(inputs)
#trains the network for some number of repetitions on your
#training input and targets
neuro.train(network, inputs, targets, reps)
#your input to the neural network has to be in the form of
#a list of input values
test_input=[val0, val1, val2]
#predicts the outcome based on the input
pred=neuro.predict(network, test_input)
#rounds to nearest value (0 or 1) since the outcomes
#are binary
pred=np.round(pred)
print ("If it is not blue the output will be: 0")
print ("If it is blue the output will be: 1 ")
print ("Is it blue? ",int(pred))