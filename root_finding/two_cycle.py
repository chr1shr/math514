#!/usr/bin/python3

a=2.4

def f(x):
    return a*x*(1-x)

x=0.5
print(0,x)
for i in range(51):
    x=f(x)
    print(i,x)
