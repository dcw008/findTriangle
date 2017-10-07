import random
import time
import FindTriangle


#this function generates a matrix that represents a bipartite graph
#where the rows and columns are the two different sets.
#param: n is the number of elements in one set

def createBPMatrix(n):
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


