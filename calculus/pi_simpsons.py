#!/usr/bin/python
from math import pi,sqrt

# Pi Day code to compute pi with the Simpson's rule

# Integrand that corresponds to a change of variable on calculating the error
# of a circle
def f(y):
    yy=y*y
    return 8*yy*sqrt(2-yy)

# Composite Simpson rule
def simp(f,a,b,n):

    # Subinterval width
    h=(b-a)/float(n)

    # Simpson's formula
    fi=f(a)+f(b)
    for i in range(1,n):
        fi+=4*f(a+(i-0.5)*h)+2*f(a+i*h)
    fi+=4*f(b-0.5*h)

    # Return scaled answer
    return fi*h/6.0

# Loop over a range of interval sizes and print absolute error
j=1
while j<=4096:

    # Compute Simpson's rule integral with 
    s=simp(f,0,1,j)

    # Print result and absolute error
    print(j,2/float(j),s,s-pi)
    j*=2
