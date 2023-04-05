#!/usr/bin/python3
from math import exp

lam=0.5
tmax=2

# Calculates the Euler and trapezoid error as a function the number of steps
def e_trap(n):

    # Initial variables
    ye=1
    yt=1
    h=tmax/n

    for i in range(n):

        # Euler method
        ye=ye+h*(lam*ye)

        # Trapezoid method
        yt=yt*(1+0.5*h*lam)/(1-0.5*h*lam)

    # Return error
    yexact=exp(lam*tmax)
    return (abs(yexact-ye),abs(yexact-yt))

n=1
while n<=131072:

    (err_e,err_t)=e_trap(n)
    print(n,tmax/float(n),err_e,err_t)
    n+=1+n//2
