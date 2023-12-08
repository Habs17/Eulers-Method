# importing the required module 
import matplotlib.pyplot as plt 
import math
from math import e
import numpy as np
from matplotlib.ticker import MultipleLocator

def IVP11(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T <= 5:
        y1.append(X)
        x1.append(T)
        X = X+stepSize*(2-2*(X)-e**(-4*T))
        T = T+stepSize
def IVP12(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T <= 5:
        y2.append(X)
        x2.append(T)
        X = X+stepSize*(2-2*(X)-e**(-4*T))
        T = T+stepSize
def IVP13(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T <= 5:
        y3.append(X)
        x3.append(T)
        X = X+stepSize*(2-2*(X)-e**(-4*T))
        T = T+stepSize
def IVP21(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T <= 5:
        y4.append(X)
        x4.append(T)
        X = X+stepSize*(X+(5*(e**(T/2))*math.cos(5*T))-((1/2)*(e**(T/2))*math.sin(5*T)))
        T = T+stepSize
def IVP22(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T <= 5:
        y5.append(X)
        x5.append(T)
        X = X+stepSize*(X+(5*(e**(T/2))*math.cos(5*T))-((1/2)*(e**(T/2))*math.sin(5*T)))
        T = T+stepSize
def IVP23(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T <= 5:
        y6.append(X)
        x6.append(T)
        X = X+stepSize*(X+(5*(e**(T/2))*math.cos(5*T))-((1/2)*(e**(T/2))*math.sin(5*T)))
        T = T+stepSize

# x axis values 
x1 = [] 
# corresponding y axis values 
y1 = []

# x axis values 
x2 = [] 
# corresponding y axis values 
y2 = []

# x axis values 
x3 = [] 
# corresponding y axis values 
y3 = []

# x axis values 
x4 = [] 
# corresponding y axis values 
y4 = []

# x axis values 
x5 = [] 
# corresponding y axis values 
y5 = []

# x axis values 
x6 = [] 
# corresponding y axis values 
y6 = []

def Exact1(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T < 5:
        y7.append(X)
        x7.append(T)
        X = (1 + (1/2)*e**(-4*T)-(1/2)*e**(-2*T))
        T = T+stepSize

def Exact2(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T < 5:
        y8.append(X)
        x8.append(T)
        X = (e**(T/2)*math.sin(5*T))
        T = T+stepSize
x7 = []
y7 = []
x8 = []
y8 = []

IVP11(.1,1,0)
IVP12(.05,1,0)
IVP13(.01,1,0)
IVP21(.1,0,0)
IVP22(.05,0,0)
IVP23(.01,0,0)
Exact1(.001,1,0)
Exact2(.001,0,0)
solution1 = y1[len(y1)-1]
solution2 = y2[len(y2)-1]
solution3 = y3[len(y3)-1]
solution4 = y4[len(y4)-1]
solution5 = y5[len(y5)-1]
solution6 = y6[len(y6)-1]
print("IVP1:")
print("h = .1 solution: ", solution1)
print("h = .05 solution: ", solution2)
print("h = .01 solution: ", solution3)
print("IVP2:")
print("h = .1 solution: ", solution4)
print("h = .05 solution: ", solution5)
print("h = .01 solution: ", solution6)
# plotting the points  
fig, axs = plt.subplots(3, 2, figsize = (8.5,11))
axs[0, 0].set_title('IVP1 with h = 0.1', fontweight = 'bold', fontsize = 10)
axs[0, 0].plot(x7,y7,label = "exact", color = 'black')
axs[0, 0].scatter(x1,y1, facecolors = 'none', label = 'Euler', edgecolors = 'r')
axs[0, 0].legend(loc = 'upper right',fontsize = 8)
axs[0, 0].set_xlim([0, 5])
axs[0, 0].yaxis.set_major_locator(MultipleLocator(0.05))
axs[0, 0].set_ylim(0.81, 1.05)
axs[0, 0].tick_params(left=True, bottom=True, right = True, top = True,direction='in')
axs[0, 1].set_title('IVP2 with h = 0.1', fontweight = 'bold', fontsize = 10)
axs[0, 1].plot(x8,y8,label = "exact", color = 'black')
axs[0, 1].scatter(x4,y4, facecolors = 'none', label = 'Euler', edgecolors = 'r')
axs[0, 1].legend(loc = 'upper right',fontsize = 8)
axs[0, 1].set_xlim([0, 5])
axs[0, 1].set_ylim([-15, 25])
axs[0, 1].yaxis.set_major_locator(MultipleLocator(5))
axs[0, 1].tick_params(left=True, bottom=True, right = True, top = True,direction='in')
axs[1, 0].set_title('IVP1 with h = 0.05', fontweight = 'bold', fontsize = 10)
axs[1, 0].plot(x7,y7,label = "exact", color = 'black')
axs[1, 0].scatter(x2,y2, facecolors = 'none', label = 'Euler', edgecolors = 'r')
axs[1, 0].legend(loc = 'upper right',fontsize = 8)
axs[1, 0].set_xlim([0, 5])
axs[1, 0].yaxis.set_major_locator(MultipleLocator(0.05))
axs[1, 0].set_ylim(0.81, 1.05)
axs[1, 0].tick_params(left=True, bottom=True, right = True, top = True,direction='in')
axs[1, 1].set_title('IVP2 with h = 0.05', fontweight = 'bold', fontsize = 10)
axs[1, 1].plot(x8,y8,label = "exact", color = 'black')
axs[1, 1].scatter(x5,y5, facecolors = 'none', label = 'Euler', edgecolors = 'r')
axs[1, 1].legend(loc = 'upper right',fontsize = 8)
axs[1, 1].set_xlim([0, 5])
axs[1, 1].set_ylim([-15, 25])
axs[1, 1].yaxis.set_major_locator(MultipleLocator(5))
axs[1, 1].tick_params(left=True, bottom=True, right = True, top = True,direction='in')
axs[2, 0].set_title('IVP1 with h = 0.01', fontweight = 'bold', fontsize = 10)
axs[2, 0].plot(x7,y7,label = "exact", color = 'black')
axs[2, 0].scatter(x3,y3, facecolors = 'none', label = 'Euler', edgecolors = 'r')
axs[2, 0].legend(loc = 'upper right',fontsize = 8)
axs[2, 0].set_xlim([0, 5])
axs[2, 0].yaxis.set_major_locator(MultipleLocator(0.05))
axs[2, 0].set_ylim(0.81, 1.05)
axs[2, 0].tick_params(left=True, bottom=True, right = True, top = True,direction='in')
axs[2, 1].set_title('IVP2 with h = 0.01', fontweight = 'bold', fontsize = 10)
axs[2, 1].plot(x8,y8,label = "exact", color = 'black')
axs[2, 1].scatter(x6,y6, facecolors = 'none', label = 'Euler', edgecolors = 'r')
axs[2, 1].legend(loc = 'upper right',fontsize = 8)
axs[2, 1].set_xlim([0, 5])
axs[2, 1].set_ylim([-15, 25])
axs[2, 1].yaxis.set_major_locator(MultipleLocator(5))
axs[2, 1].tick_params(left=True, bottom=True, right = True, top = True,direction='in')
plt.show()
