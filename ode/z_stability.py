#!/usr/bin/python3
from math import exp,sin,cos
import numpy as np

# Method:
# 0: stable
# 1: exponentially unstable
# 2: algebraically unstable
method=1

# Total steps
M=101

# Function right hand side
def fun(x,y):
    return sin(x)-y

# Exact solution
def y_exact(x):
    return 0.5*(sin(x)-cos(x))+1.5*exp(-x)

# Step size, and arrays for solution
h=10/(M-1)
x=np.linspace(0,10,M)
f=np.empty((M))
y=np.empty((M))

# Populate the first few entries with the exact solution
y[0:3]=[y_exact(z) for z in x[0:3]]
f[0:3]=[fun(x[i],y[i]) for i in range(0,3)]

# Perform the steps of the method
for n in range(0,M-3):

    if method==0:
        y[n+3]=(y[n+2]+h*(9*sin(x[n+3])+19*f[n+2]-5*f[n+1]+f[n])/24) \
               /(1+9*h/24)

    elif method==1:
        y[n+3]=(-27*y[n+2]+27*y[n+1]+11*y[n] \
               +3*h*(sin(x[n+3])+9*f[n+2]+9*f[n+1]+f[n])) \
               /(11+3*h)
    else:
        y[n+3]=-y[n+2]+y[n+1]+y[n]+2*h*(f[n+2]+f[n+1])
    f[n+3]=fun(x[n+3],y[n+3])

# Output the results
for n in range(0,M):
    ye=y_exact(x[n])
    print(x[n],y[n],f[n],ye,y[n]-ye)
