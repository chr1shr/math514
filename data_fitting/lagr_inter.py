#!/usr/bin/python3
from math import *
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate the kth Lagrange polynomial at x associated with points in
# the vector xp
def lpoly(x,xp,k):
    li=1
    for l in range(xp.size):
        if k!=l:
            li*=(x-xp[l])/(xp[k]-xp[l])
    return li

# Lagrange interpolation for points (xp,yp) evaluated at x
def l_inter(x,xp,yp):
    s=0
    for k in range(xp.size):
        s+=yp[k]*lpoly(x,xp,k)
    return s

# Control points and Runge function
n=11
xp=np.linspace(-1,1,n)
#xp=np.array([cos((2*j+1)*pi/(2*n)) for j in range(n)])
yp=np.array([1/(1+25*x*x) for x in xp])

# Sample points
xx=np.linspace(-1,1,500)
yy=np.array([l_inter(x,xp,yp) for x in xx])
yf=np.array([1/(1+25*x*x) for x in xx])

# Plot figure using Matplotlib
plt.figure()
plt.plot(xx,yf,'--',xx,yy,'--',xp,yp,'o',linewidth=6)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
