#!/usr/bin/python3
from math import exp

# Initial variables and constants
y=1
t=0
h=0.2
lam=-3

# Apply Euler step until t>2
while t<=2:

    # Analytical solution
    yexact=exp(lam*t)

    # Print the solutions and error
    print(t,y,yexact,y-yexact)

    # Euler step
    y=y+h*(lam*y)

    # Update time
    t+=h
