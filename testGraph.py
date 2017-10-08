import FindTriangle
import time
import RandomMatrix

#this file is for testing and running findTrangle on randomly generated bipartite graphs
size_vector = [2,4,8,16,32,64,128,256,512,1024]
time_vector = []
for j in range(0, len(size_vector)):
	print("the size of the matrix: %d"%size_vector[j])
	for count in range(0,20):
		timeSum = 0
		G = RandomMatrix.createRandomMatrix(size_vector[j])
		# createBPMatrix.printMatrix(G)
		start = time.time()
		FindTriangle.findTriangle(G)
		end = time.time()
		print("runtime for %d maytrix : %lf"%(count, end - start))
		timeSum = end - start + timeSum
	time_vector.append(timeSum/20)
	print("\n")
print('\n\n')
for k in range(0, len(time_vector)):
	print(time_vector[k])
