import numpy as np

a = np.linspace(0, 3, num=4)
print(a) # a = [0. 1. 2. 3.]

s = a[2]
print(s) # s = 2.0

a[0] = 4
print(a) # a = [4. 1. 2. 3.]