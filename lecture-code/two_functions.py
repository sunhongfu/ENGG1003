# imports first
import numpy as np # We will learn more about these soon.

# function definitions are next
def f(x):
	return np.sin(x)

def g(x):
	return x**2

# main code starts here
t = 1.2345
print(f(t))
print(g(t))