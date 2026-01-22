import numpy as np

def f(x):
    return np.exp(x) - 3*x

eps = 1e-6
xLO = 1
xHI = 2

xMID = (xLO + xHI) / 2
iters = 0
while abs(f(xMID)) > eps:
    if f(xMID)*f(xHI) < 0:  # solution in upper half
        xLO = xMID
    else:
        xHI = xMID
    xMID = (xLO + xHI) / 2
    iters += 1

print(f'Solution: {xMID:.5f}')
print(f'Number of iterations: {iters}')
print(f'Check: f({xMID:.5f}) = {f(xMID):.5f}')