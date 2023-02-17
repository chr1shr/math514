#!/usr/bin/python3
from math import cosh
import numpy as np
import sys

# Amount to perturb by
ydis=0.001

# Initialize points and the function values there
n=7
x=np.linspace(-1,2,n)
y=np.cosh(x)

# Solve the linear system using the Vandermonde matrix
V=np.vander(x)
b=np.linalg.solve(V,y)

# Perturb the function values and solve again
y[4]+=ydis
b2=np.linalg.solve(V,y)

# Print out the two sets of coefficients
print("Coefficients of original b:")
for i in range(n):
    print(i,b[i])
print("\nCoefficients of perturbed b:")
for i in range(n):
    print(i,b2[i])

# Print out diagnostics
print("\nRelative change in y:",ydis/np.linalg.norm(y))
print("Relative change in b:",np.linalg.norm(b-b2)/np.linalg.norm(b))
print("Condition number of V:",np.linalg.cond(V))
