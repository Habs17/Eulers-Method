# importing the required module 
import matplotlib.pyplot as plt 
import math
from math import e

def IVP11(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T < 5:
        y1.append(X)
        x1.append(T)
        X = X+stepSize*(2-2*(X)-e**(-4*T))
        T = T+stepSize
def IVP12(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T < 5:
        y2.append(X)
        x2.append(T)
        X = X+stepSize*(2-2*(X)-e**(-4*T))
        T = T+stepSize
def IVP13(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T < 5:
        y3.append(X)
        x3.append(T)
        X = X+stepSize*(2-2*(X)-e**(-4*T))
        T = T+stepSize
def IVP21(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T < 5:
        y4.append(X)
        x4.append(T)
        X = X+stepSize*(X+(5*(e**(T/2))*math.cos(5*T))-((1/2)*(e**(T/2))*math.sin(5*T)))
        T = T+stepSize
def IVP22(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T < 5:
        y5.append(X)
        x5.append(T)
        X = X+stepSize*(X+(5*(e**(T/2))*math.cos(5*T))-((1/2)*(e**(T/2))*math.sin(5*T)))
        T = T+stepSize
def IVP23(stepSize,X,T):
    #x1 = x0+hf(x0,t0)
    while T < 5:
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
IVP13(.001,1,0)
IVP21(.1,0,0)
IVP22(.05,0,0)
IVP23(.001,0,0)
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
print("h = .001 solution: ", solution3)
print("IVP2:")
print("h = .1 solution: ", solution4)
print("h = .05 solution: ", solution5)
print("h = .001 solution: ", solution6)
# plotting the points  
plt.plot(x7, y7, label = "IVP1") 
plt.plot(x8, y8, label = "IVP2")
# naming the x axis 
plt.xlabel('t') 
# naming the y axis 
plt.ylabel('x(t)')
  
# giving a title to my graph 
plt.title('Exact x(t) for each function') 
plt.legend()
# function to show the plot 
plt.show()
