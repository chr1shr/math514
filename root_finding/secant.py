#!/usr/bin/python3
from math import exp
import sys

# Function to consider
def f(x):
    return exp(x)-x-4

# Two previous values, required to estimate
# the derivative
x_prev=1.4
f_prev=f(x_prev)
x=1.5

# Perform ten steps of the secant method
for i in range(10):

    # Print current solution
    fv=f(x)
    print(i,x,fv)
    
    # Estimate the gradient using the previous two function values
    grad=(fv-f_prev)/(x-x_prev)
    
    # Update solution
    f_prev=fv;x_prev=x
    x-=fv/grad

# Print solution on the final iteration
print(i,x,f(x))
