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

    # Evaluate function at x, x+h, and x+2h
    f1=f(x);f2=f(x+h);f3=f(x+2*h)

    # Compute the first-order one-sided finite difference
    df=(f2-f1)/h

    # Compute the second-order one-sided finite difference
    df2=(-0.5*f3+2*f2-1.5*f1)/h

    # Print the numerical and exact derivatives, and the magnitude of absolute
    # error
    print(h,df,df2,abs(df-dfexact),abs(df2-dfexact))

    # Divide the grid spacing by 10
    h*=0.5
