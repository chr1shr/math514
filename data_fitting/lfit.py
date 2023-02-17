#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm

# Total parameters
n=5

# Total constraints
m=31

# Function samples from cos(x^2)
x=np.linspace(0,3,m)
y=np.cos(x*x)

# Assemble linear system: passing an extra argument n to the numpy.vander
# function makes it return a rectangular matrix with n columns
A=np.vander(x,n)

# Solve using the normal equations
AT=np.transpose(A)
ATA=np.dot(AT,A)
b1=np.linalg.solve(ATA,np.dot(AT,y))
print("Condition number of A^T A =",np.linalg.cond(ATA))

# Solve using the lstsq function
b2=np.linalg.lstsq(A,y,rcond=None)[0]
print("Condition number of A =",np.linalg.cond(A))

# Print the difference between the two parameter sets, and the residuals
print("||b1-b2||/||b1|| =",norm(b1-b2)/norm(b1))
print("||y-A*b1||/||y|| =",norm(y-np.dot(A,b1))/norm(y))
print("||y-A*b2||/||y|| =",norm(y-np.dot(A,b2))/norm(y))

# Vandermonde interpolation function
def vand_f(x,b):
    fx=b[0]
    for i in range(n-1):
        fx*=x
        fx+=b[i+1]
    return fx

# Plot the results
plt.figure()
xnew=np.linspace(0,3,200)
vnew=[vand_f(q,b1) for q in xnew]
v2new=[vand_f(q,b2) for q in xnew]
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y,'o',xnew,vnew,'-',xnew,v2new)
plt.legend(['data','normal eqns.','lstsq routine'],loc='best')
plt.show()
