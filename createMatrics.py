import random
import time

def createRandomMatrix(n):
	# create a matrix and set all values of the matrix to 0
	randomMatrix = [[0 for x in range(n)] for y in range(n)]
	for i, row in enumerate(randomMatrix):
		for j, col in enumerate(randomMatrix):
			matrixRand = random.random()

			if matrixRand >= 0.5:
				randomMatrix[i][j] = 1
			else:
				randomMatrix[i][j] = 0
	return randomMatrix

def printMatrix(G):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in G]))

start = time.time()
printMatrix(createRandomMatrix(4))
end = time.time()

print(end-start)