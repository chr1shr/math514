#!/usr/bin/python3
from math import exp
import sys

# Function to consider
def f(x):
    return exp(x)-x-4

# Derivative of the function
def df(x):
    return exp(x)-1

# Starting guess
x=1.5

# Perform ten steps of the Newton iteration
n=10
for i in range(n):

    # Take Newton step
    fv=f(x)
    print(i,x,fv)
    x-=fv/df(x)

# Print solution on the final iteration
print(n,x,f(x))
