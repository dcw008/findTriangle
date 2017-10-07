import random
import time
import FindTriangle


#this function generates a matrix that represents a bipartite graph
#where the rows and columns are the two different sets.
#param: n is the number of elements in one set

def createBPMatrix(n):
	# create a matrix and set all values of the matrix to 0
	bpMatrix = [[0 for x in range(2*n)] for y in range(2*n)]
	symetricSet = set()
	for i, row in enumerate(bpMatrix):
		for j, col in enumerate(bpMatrix):
			matrixRand = random.random()
			if(i == j):
				bpMatrix[i][j] = 0
				continue
			if (j, i) in symetricSet:
				continue
			if((i < n and j > n) or (i > n and j < n)):
				if matrixRand >= 0.5:
					bpMatrix[i][j] = 1
					bpMatrix[j][i] = 1
					symetricSet.add((i,j))
				else:
					bpMatrix[i][j] = 0
					bpMatrix[j][i] = 0
					symetricSet.add((i,j))
			else:
				bpMatrix[i][j] = 0
	return bpMatrix

def printMatrix(G):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in G]))



