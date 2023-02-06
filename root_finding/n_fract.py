import numpy as np
from skimage import io
import matplotlib.pyplot as plt
import cmath

# Function to consider
def f(z):
    return z*z*z-1

# Derivative
def df(z):
    return 3*z*z

# Finds the root of the function starting from a given complex number x+yi
def nroot(x,y):
    z=complex(x,y)
    i=0

    # Perform a number of Newton iterations
    while i<256:

        # If we are close to a root, then return its phase
        fz=f(z)
        if abs(fz)<1e-13:
            return cmath.phase(z)

        # If the derivative is close to zero, then terminate
        dfz=df(z)
        if abs(dfz)<1e-13:
            return 0

        # Perform Newton step
        z-=fz/df(z)
        i+=1

    # If a root wasn't found after a large number of iterations, then terminate
    return 0

# Create a large grid to scan over
n=800
X=np.linspace(-1.5,1.5,n)
Y=np.linspace(-1.5,1.5,n)
Z=np.zeros((n,n))

# Scan over each point in the grid and compute the phase of the root that the
# Newton method converges to
for i in range(n):
    for j in range(n):
        Z[i,j]=nroot(Y[j],X[i])

# Save the results to an image
plt.imsave("nroot.png",Z,vmin=-np.pi,vmax=np.pi,cmap=plt.cm.gist_rainbow)
