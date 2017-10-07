
import FindTriangle
import time
import createBPMatrix

#this file is for testing and running findTrangle on randomly generated bipartite graphs
G = createBPMatrix.createBPMatrix(256)
start = time.time()
for i in range(0, 10000):
    FindTriangle.findTriangle(G)
end = time.time()

run_time = (end - start)/10000

print(run_time)
