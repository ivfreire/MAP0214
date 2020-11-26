import numpy as np

def func(x, k):
	return 1 / np.sqrt(1 - (k * np.sin(x))**2)

N = 10
for i in range(N):
	theta = np.pi * (i / N)
	k = np.sin(theta / 2)
	S = 0

	M = 101
	for j in range(M):
		weight = 1
		if j != 0 and j != M - 1:
			if j % 2 == 0: weight = 4
			if j % 2 != 0: weight = 2
		S += weight * func((np.pi / 2) * (j / M), k)
	S = S * ((np.pi / 2) / (M - 1)) / 3

	print('{}\t{}'.format(theta, 4 * np.sqrt(1 / 9.81) * S))