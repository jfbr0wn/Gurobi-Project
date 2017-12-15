# graphgen.py for Python 2.7
#
# Build a random undirected graph and the ILP to find a maximum clique in it.
# Also, output the adjacency matrix of the graph.
#
# DG October 30, 2017
#
#
import random # This is a module that contains programs involving random numbers.

def Graphgen(nodenum, prob, graph):
    #nodenum = raw_input("How many nodes in the graph?  ")
    #prob = raw_input("What edge probability? Input a decimal number between 0.01 and 0.99, inclusive. ")
    nodenum = int (nodenum)
    fprob = float (prob)

    #graph = raw_input("What is the name of the file you want to use for the output?  ")
    OUTGRAPH = open(graph, 'w')
    #print "You input: %d, %f, %s" % (nodenum,  fprob, graph)

    rcut = fprob * 100
    nodenump1 = int(nodenum) + 1
    
    matrix = []
    for i in range (0, nodenump1):
        matrix.append(['0']*nodenump1)

    for i in range (1, nodenump1 - 1): 
        for j in range (i+1, nodenump1): 
            randomnum = random.randrange(101) # pick a random integer between 0 and 100
#            print "The random number is", randomnum

            if (randomnum  < rcut):   # if the random number is less than the 
                                      # cutoff, rcut, then create an edge between
                                      # nodes i and j. Otherwise there is no edge between i and j. 
               matrix[i][j] = '1'
               matrix[j][i] = '1'

    for i in range(1,nodenump1):
        for j in range(1,nodenump1):
            OUTGRAPH.write(matrix[i][j])
        OUTGRAPH.write("\n")
    #print "The %d-by-%d adjacency matrix for the graph generated is in file %s" % (nodenum, nodenum, graph)
#main()
