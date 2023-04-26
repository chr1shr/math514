#!/usr/bin/python3
from math import sqrt,exp

# Initial variables and constants
t=0
h=0.05
l=0

# Constants in the method
c1=(3-sqrt(3))/6.
c2=(3+sqrt(3))/6.
a12=(3-2*sqrt(3))/12.
a21=(3+2*sqrt(3))/12.

# Function to integrate
def f(t,y):
    return exp(-0.5*t*t)-y*t

# Starting value, and initial guess for k1 and k2
y=0
k1=0
k2=0

# Apply timesteps until t>6
while t<=6:

    # Analytical solution
    yexact=t*exp(-0.5*t*t)

    # Print the solutions and error
    print(t,y,yexact,y-yexact,l)

    # Fixed-point iteration for k1 and k2
    l=0
    while True:

        # Compute new k1 and k2 using previous values
        # as a starting guess
        k1new=f(t+c1*h,y+h*(0.25*k1+a12*k2))
        k2new=f(t+c2*h,y+h*(a21*k1+0.25*k2))

        # Compute change in k1 and k2, to determine if they have
        # converged
        (dk1,dk2)=(k1new-k1,k2new-k2)
        (k1,k2)=(k1new,k2new)
        if(dk1*dk1+dk2*dk2<1e-25):
            break
        
        # Check for too many iterations
        l+=1
        if l>4096:
           print("Fixed point iteration failed to converge\n")

    # Update solution and time 
    y+=0.5*h*(k1+k2)
    t+=h
