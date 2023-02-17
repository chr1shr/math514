#!/usr/bin/python3
from math import *
import matplotlib.pyplot as plt
import numpy as np

# Function to evaluate the H_k and K_k polynomials
def herm_poly(x,xp,k):

    # Compute L_k(x) and L'_k(x_k)
    li=1;ld=0
    for l in range(xp.size):
        if k!=l:
            li*=(x-xp[l])/(xp[k]-xp[l])
            ld+=1/(xp[k]-xp[l])
    
    # H_k(x) = [L_k(x)]^2 (1 - 2L'_k(x_k) (x-x_k))
    Hk=li*li*(1-2*ld*(x-xp[k]))
   
    # K_k(x) = [L_k(x)]^2 (x-x_k)
    Kk=li*li*(x-xp[k])
    return (Hk,Kk)

# Hermite interpolation for points xp with function values yp and derivatives dyp, evaluated at x
def herm_inter(x,xp,yp,dyp):
    s=0
    for k in range(xp.size):
        (Hk,Kk)=herm_poly(x,xp,k)
        s+=yp[k]*Hk+dyp[k]*Kk
    return s

# Control points and Runge function
n=7
#xp=np.linspace(-1,1,n)
xp=np.array([cos((2*j+1)*pi/(2*n)) for j in range(n)]) 
yp=np.array([1/(1+25*x*x) for x in xp])
dyp=np.array([-50*x/(1+25*x*x)**2 for x in xp])

# Sample points
xx=np.linspace(-1,1,500)
yy=np.array([herm_inter(x,xp,yp,dyp) for x in xx])
yf=np.array([1/(1+25*x*x) for x in xx])

# Plot figure using Matplotlib
plt.figure()
plt.plot(xx,yf,'--',xx,yy,'--',xp,yp,'o')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
