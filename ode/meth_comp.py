#!/usr/bin/python3
from math import sqrt,exp

# Integration length
L=2

# Constants in the two-stage IRK method
c1=(3-sqrt(3))/6.
c2=(3+sqrt(3))/6.
a12=(3-2*sqrt(3))/12.
a21=(3+2*sqrt(3))/12.

# Function to integrate
def f(x,y):
    return exp(-0.5*x*x)-y*x

# Analytical solution
def yexact(x):
    return x*exp(-0.5*x*x)

# Euler method
def euler(n):

    # Constants and starting values
    h=L/n
    y=0

    # Perform n Euler steps
    for i in range(n):
        x=i*h
        y+=h*f(x,y)

    # Return function evaluations and solution 
    return (n,y)

# Improved Euler method
def imp_euler(n):

    # Constants and starting values
    h=L/n
    y=0

    # Perform n improved Euler steps
    for i in range(n):
        x=i*h
        k1=f(x,y)
        k2=f(x+h,y+h*k1)
        y+=0.5*h*(k1+k2)

    # Return function evaluations and solution
    return (2*n,y)

# Two-stage IRK method
def irk(n):

    # Constants and starting values
    h=L/n
    y=0
    k1=0;k2=0
    feval=0

    # Peform n IRK steps
    for i in range(n):
        x=i*h

        # Perform fixed-point iteration
        while True:

            # Compute new k1 and k2 using previous values
            # as a starting guess
            k1new=f(x+c1*h,y+h*(0.25*k1+a12*k2))
            k2new=f(x+c2*h,y+h*(a21*k1new+0.25*k2))
            feval+=2

            # Compute change in k1 and k2, to determine if they have
            # converged
            (dk1,dk2)=(k1new-k1,k2new-k2)
            (k1,k2)=(k1new,k2new)
            if(dk1*dk1+dk2*dk2<1e-25):
                break

        # Update solution
        y+=0.5*h*(k1+k2)

    # Return function evaluations and solution
    return (feval,y)

# Evaluate error for different numbers of steps
y_ex=yexact(L)
n=1
while n<131072:

    (f1,y1)=euler(n)
    (f2,y2)=imp_euler(n)
    (f3,y3)=irk(n)

    print(n,L/n,f1,abs(y1-y_ex),f2,abs(y2-y_ex),f3,abs(y3-y_ex))
    n+=1+n//4
