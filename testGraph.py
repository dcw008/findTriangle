import FindTriangle
import time
import RandomMatrix

#this file is for testing and running findTriangles on randomly generated undirected graph
G = RandomMatrix.createRandomMatrix(256)
start = time.time()
for i in range(0, 10000):
    FindTriangle.findTriangle(G)
end = time.time()

run_time = (end - start)/10000

print(run_time)
