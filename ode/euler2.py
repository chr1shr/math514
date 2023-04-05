#!/usr/bin/python3
from math import atan,pi,exp
import numpy as np
from scipy.integrate import odeint

# Constants
yinit=0.02
n=30
T=3.

# Right hand side of the ODE
def f(y,x):
    return atan(y)

# Create reference solution using library 'odeint' function. This function uses
# tolerances of 1e-8. Since this is much smaller than the errors in the Euler
# method, the 'odeint' result can be treated as a proxy for the exact answer.
yref=odeint(f,yinit,np.linspace(0,T,n+1))

# Initial variables and constants
h=T/n

# Apply Euler step until t>2
x=0
i=0
y=yinit
while i<=n:

    # Print the numerical solution, reference solution, and error bound
    print(x,y,yref[i][0],y-yref[i][0],0.25*pi*(exp(x)-1)*h)

    # Euler step
    y+=h*f(y,x)

    # Update time
    x+=h
    i+=1
