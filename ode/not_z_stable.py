#!/usr/bin/python3
from math import exp,sin,cos
import numpy as np

M=101

def fun(x,y):
    return sin(x)-y

def y_exact(x):
    return 0.5*(sin(x)-cos(x))+1.5*exp(-x)

h=1/(M-1)
x=np.linspace(0,10,M)
f=np.empty((M))
y=np.empty((M))

y[0:3]=[y_exact(z) for z in x[0:3]]
f[0:3]=[fun(x[i],y[i]) for i in range(0,3)]

for n in range(0,M-3):
    y[n+3]=(-27*y[n+2]+27*y[n+1]+11*y[n] \
           +3*h*(sin(x[n+3])+9*f[n+2]+9*f[n+1]+f[n])) \
           /(11+3*h)

for n in range(0,M):
    ye=y_exact(x[n])
    print(x[n],y[n],f[n],ye,y[n]-ye)
