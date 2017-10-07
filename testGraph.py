import FindTriangle
import time
import RandomMatrix

# this file is for testing and running findTriangles on randomly generated undirected graph
size_vector = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
time_vector = []
for j in range(0, len(size_vector)):
	G = RandomMatrix.createRandomMatrix(size_vector[j])
	# RandomMatrix.printMatrix(G)
	print('\n')
	
	start = time.time()
	for i in range(0, 200):
	    FindTriangle.findTriangle(G)
	end = time.time()

	run_time = (end - start)/200
	time_vector.append(run_time)
print('\n\n')
for k in range(0, len(time_vector)):
	print(time_vector[k])
