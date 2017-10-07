import time
import random
#Given a graph G in the form of a adjacency matrix, determine if the Graph contains a triangle.


testMatrix = [[0,1,0,0,1], [1,0,1,0,1], [0,1,0,1,0], [0,0,1,0,1], [0,1,0,1,0]]
bpMatrix = [[0,0,1,0,1], [0,0,0,1,0], [0,0,1,1,1], [1,1,0,0,0], [0,1,0,0,0]]


#This algorithm uses a bucketing approach such that we will process the entire matrix and add edges into buckets.
#We only add buckets to our bucket list if a bucket has at least 2 edges because in order to form a triangle, a bucket
#must have at least two edges in the form (u, v) (u, w). After processing the all the edges from the matrix,
#we iterate through each bucket and for each pair of edges we check if there an edge exists (v,w) by checking our matrix
#If there is, return true. Else, return false
def findTriangle(G):
    start = time.time()
    print("Searching for triangle . . .")

    #a list of all the buckets
    allBuckets = []
    #set of edges (u, v) so that if we see edge (v, u) we don't need to process that edge
    symmetricSet = set()

    #iterate through each row
    for i, row in enumerate(G):
        #form the bucket for each row
        bucket = []
        #check for edges in each column
        for j, col in enumerate(G):
            #ignore the edge if we have seen it
            if((j, i) in symmetricSet):
                continue
            else:
                if(G[i][j] == 1):
                    #append the edge (u,v) to the bucket list
                    bucket.append((i, j))
                    #add the edge to the set
                    symmetricSet.add((i,j))

        #iterate through the bucket to find a triangle
        if(len(bucket) >= 2):
            allBuckets.append(bucket)

    #process the buckets to find the triangles
    for bucket in allBuckets:
        # print(bucket)
        #for given nodes (u,v) and (u,w) try to find (v,w)
        it = iter(bucket)
        for edge in it:
            firstEdge = edge
            secondEdge = next(it)
            u = firstEdge[1]
            v = secondEdge[1]
            if(G[u][v] == 1):
                end = time.time()
                print(end - start)
                return True

    end = time.time()
    print(end - start)
    return False

print(findTriangle(bpMatrix))

