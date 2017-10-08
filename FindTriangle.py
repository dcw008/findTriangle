import time
import random
#Given a graph G in the form of a adjacency matrix, determine if the Graph contains a triangle.


testMatrix = [[0,1,0,0,1], [1,0,1,0,1], [0,1,0,1,0], [0,0,1,0,1], [0,1,0,1,0]]
bpMatrix = [[0,1,1,1],[1,0,0,1], [1,0,0,1], [1,1,1,0]]


#This algorithm uses a bucketing approach such that we will process the entire matrix and add edges into buckets.
#We only add buckets to our bucket list if a bucket has at least 2 edges because in order to form a triangle, a bucket
#must have at least two edges in the form (u, v) (u, w). After processing the all the edges from the matrix,
#we iterate through each bucket and for each pair of edges we check if there an edge exists (v,w) by checking our matrix
#If there is, return true. Else, return false
def findTriangle(G):
    #start = time.time()
    # print("Searching for triangle . . .")

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
    # print ("Number of buckets with size greater than 2 is: " + str(len(allBuckets)))
    #process the buckets to find the triangles
    
    for bucket in allBuckets:
        # print(bucket)
        # for given nodes (u,v) and (u,w) try to find (v,w)

        # store iterator for the first edge
        it = iter(bucket)
        second_iter = iter(bucket)
        # for each edge check if another edge in the bucket forms a triangle
        # so check (0,1) with (0,2), (0,1) with (0,3).....
        for i in it:
            first_edge = i
            for j in second_iter:
                # we dont want (0,1) and (0,1) right?
                if j == i:
                    continue
                else:
                    second_edge = j
                    u = first_edge[1]
                    v = second_edge[1]
                    # do triangle check
                    if(G[u][v] == 1):
                        #end = time.time()
                        return True 
    #end = time.time()
    # print(end - start)
    return False

def printMatrix(G):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in G]))

#printMatrix(bpMatrix)
#print(findTriangle(bpMatrix))

'''
            firstEdge = edge
            print("First vertex in first edge is " + str(firstEdge[0]) + "\n")
            print("Second vertex in first edge is " + str(firstEdge[1]) + "\n")
            print("first edge is: "+ str(firstEdge))
            #print(it.next())
            try:
                secondEdge = it.next()
            except(StopIteration):
                break
            print("second edge is: " + str(secondEdge))
            print("First vertex in second edge is " + str(secondEdge[0]) + "\n")
            print("Second vertex in second edge is " + str(secondEdge[1]) + "\n")
            u = firstEdge[1]
            v = secondEdge[1]
            print(str(u) + ',' + str(v))
            if(G[u][v] == 1):
                end = time.time()
                print(end - start)
                return True
'''