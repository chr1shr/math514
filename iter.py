#!/usr/bin/python3
from math import sin,cos

# Function to iterate
def g(x):
    return x+cos(x)**2-x*sin(x)**2/(1+x*x)

# Starting value for iteration
x=0.5

# Perform the iteration and print out each step
print("0",x)
for k in range(1,11):
    x=g(x)
    print(k,x)
