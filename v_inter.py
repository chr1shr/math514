#!/usr/bin/python3
from math import cosh
import numpy as np
import sys

# Initialize points and the function values there
n=7
x=np.linspace(-1,2,n)
y=np.cosh(x)

y[4]+=0.001

# Solve the linear system using the Vandermonde matrix
V=np.vander(x)
b=np.linalg.solve(V,y)

print(b)
sys.exit()

# Save the interpolant to a file
xx=-1
while xx<2:

    # Use Horner's method to compute the polynomial. For a degree m=(n-1)
    # polynomial, this requires m multiplications and m additions. Because of
    # Python's Vandermonde ordering convention, b[0] holds the coefficient of
    # the highest power
    yy=b[0]
    for i in range(1,n):
        yy*=xx
        yy+=b[i]

    # Print the polynomial and the difference compared to original function
    print(xx,yy,cosh(xx),yy-cosh(xx))
    xx+=0.01
