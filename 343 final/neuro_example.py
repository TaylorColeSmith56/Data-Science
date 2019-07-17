from __future__ import division
import neuro
import sys
import numpy as np

#input values for training
inputs=[ [0, 0], [0, 1], [1, 0], [1, 1] ]
#target values for each input
targets=[ [0], [0], [0], [1] ]
#number of repetitions to train the network
reps=10000

print "AND-gate Neural Network Example"
val0=raw_input("\tEnter a 1 or 0: ")
val1=raw_input("\tEnter another 1 or 0: ")
#converts input to float
val0=float(val0)
val1=float(val1)

network=[] #makes an empty list to contain the neural net

#sets up the network to accommodate the size of your inputs
network=neuro.setup_network(inputs)

#trains the network for some number of repetitions on your
#training input and targets
neuro.train(network, inputs, targets, reps)

#your input to the neural network has to be in the form of
#a list of input values
test_input=[val0, val1]

#predicts the outcome based on the input
pred=neuro.predict(network, test_input)
#rounds to nearest value (0 or 1) since the outcomes
#are binary
pred=np.round(pred)

print "The network thinks",int(val0),"&&",int(val1),"=",int(pred)
