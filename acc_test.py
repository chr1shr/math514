#!/usr/bin/python3

# Loop over a range of values of h, to test the limit of floating point
# arithmetic
h=1
while h>1e-20:

    # Check to see whether 1+h is recognized as a different value from 1
    if 1==1+h:
        print("h =",h,",  1==1+h")
    else:
        print("h =",h,",  1!=1+h")

    h*=0.1
