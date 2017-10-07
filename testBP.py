import FindTriangle
import time
import createBPMatrix

#this file is for testing and running findTrangle on randomly generated bipartite graphs
size_vector = [4, 8, 16, 32, 64, 128, 256, 512, 1024]
time_vector = []
for j in range(0, len(size_vector)):
	G = createBPMatrix.createBPMatrix(size_vector[j])
	# createBPMatrix.printMatrix(G)
	print("\n")
	
	start = time.time()
	for i in range(0, 200):
	    FindTriangle.findTriangle(G)
	end = time.time()

	run_time = (end - start)/200
	time_vector.append(run_time)
print('\n\n')
for k in range(0, len(time_vector)):
	print(time_vector[k])

