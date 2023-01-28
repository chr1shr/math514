#!/usr/bin/python3
from math import sin,cos,exp

# Function to numerically differentiate
def f(z):
    return exp(z)*sin(z)

# Initial step size, and position to evaluate the derivative at
h=0.1
x=1

# Exact derivative
dfexact=exp(x)*(cos(x)+sin(x))

while h>1e-16:

    # Compute the derivative by evaluating the gradient of f between x and x+h
    df=(f(x+h)-f(x))/h

    # Print the numerical and exact derivatives, and the magnitude of absolute
    # error
    print(h,df,dfexact,abs(df-dfexact))

    # Divide the grid spacing by 10
    h*=0.1
