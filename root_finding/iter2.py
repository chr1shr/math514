#!/usr/bin/python
from math import exp,log

# Iteration 1
def g1(x):
    return exp(x)-4

# Iteration 2
def g2(x):
    return log(x+4)

# Starting value for iteration
x=2

# Perform the iteration and print out each step
print("0",x)
for k in range(1,11):
    x=g2(x)
    print(k,x)
