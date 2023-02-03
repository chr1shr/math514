#!/usr/bin/python3
from math import exp,cos

# Function to perform root-finding on
def f(x):
    return exp(x)-x-4

# Initial bracket, assuming f(a)<0 and f(b)>0
a=0
b=2

# Perform the bisection search
while b-a>1e-10:
    print("[",a,",",b,"]")
    c=0.5*(a+b)
    if f(c)<0:
        
        # New interval is [c,b]
        a=c
    else:

        # New interval is [a,c]
        b=c

# Print the approximation to the root, and evaluate the function there
x=0.5*(a+b)
print("\nRoot at x =",x,"\nf(x) =",f(x))
