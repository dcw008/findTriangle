import random
import time
import FindTriangle

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


G = createRandomMatrix(256)
start = time.time()
for i in range(0, 10000):
	FindTriangle.findTriangle(G)
end = time.time()

run_time = (end - start)/10000

print(run_time)
