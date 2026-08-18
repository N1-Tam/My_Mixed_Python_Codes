# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 20:34:04 2026

@author: Konstantin.Playford
"""
#This is a code to make a simple plot(Graph)
import matplotlib.pyplot as plt
#The "targets" and the "scores" variables must contain the same amount of values; in this case, 20 each.
targets = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
scores = (1,2,7,5,2,9,0,2,3,5,2,7,9,4,1,4,6,3,5,4)
plt.size = 6,4#This specifies the dimensions of the plot; in this case, 6X4.
plt.title("Targets") #This controls the title.
plt.plot(targets,scores)#This shows the variables that the plot must show.
plt.show#Creates the plot
