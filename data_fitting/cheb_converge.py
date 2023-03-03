#!/usr/bin/python3
from math import *
import matplotlib.pyplot as plt
import numpy as np

# Function to interpolate
def f(x):
    return 1/(1+25*x*x)

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

# Evaluate the infinity norm between the function and the Lagrange interpolant
# based on Chebyshev points
def cheb_inf_error(n):

    # Set up Chebyshev points and corresponding function values
    xp=np.array([cos((2*j+1)*pi/(2*n)) for j in range(n)]) 
    yp=np.array([f(x) for x in xp])

    # Sample the difference between the function and the interpolant at many
    # points, to approximate the infinity norm
    xx=np.linspace(-1,1,2049)
    yy=np.array([l_inter(x,xp,yp)-f(x) for x in xx])

    # Return the infinity norm of the sampled differences
    return np.linalg.norm(yy,np.inf)

# Compute the difference over a range of interpolation points
n=1
while n<60:

    # Compute infinity norm between Chebyshev interpolant and function
    print(n,cheb_inf_error(n))

    # Increase interpolation points, adding a multiplicative factor
    n+=1+n//4
