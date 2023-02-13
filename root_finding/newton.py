#!/usr/bin/python3
from math import exp
import sys

# Function to consider
def f(x):
    return x*x*x-4*x*x+4.1*x

# Derivative of the function
def df(x):
    return 3*x*x-8*x+4.1

# Starting guess
x=2.2

# Perform ten steps of the Newton iteration
n=100
for i in range(n):

    # Take Newton step
    fv=f(x)
    print(i,x,fv)
    x-=fv/df(x)

# Print solution on the final iteration
print(n,x,f(x))
