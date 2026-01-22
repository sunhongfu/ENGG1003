import numpy as np
# 0==heads & 1==tails
# N integers from [0,2) ie: 0 or 1
N = 100000
x = np.random.randint(0, 2, N)

headCnt = 0
for i in range(0, N):
	if x[i] == 0:
		headCnt += 1

print(f'Expected number of heads: {N/2}')
print(f'Observed number of heads: {headCnt}')