import numpy as np
import os
import imageio.v3 as iio
from PIL import Image
from problog.program import PrologString
from problog.tasks import sample
from problog.learning import lfi
import matplotlib.pyplot as plt
import networkx as nx
import sys
import uuid

# pl_file = open("test.pl", 'r')
# pl_string = pl_file.read()



maze_size = 5

possible_evidence = ""
program_str = ""
for i in range(maze_size):
    for j in range(maze_size):
        current_idx = (i*maze_size)+j 
        program_str = program_str + "d(" + str(current_idx+1) + ").\n"
        if current_idx > 0:
            possible_evidence= possible_evidence + "evidence(path(1,"+str(current_idx + 1)+ ")).\n"
        #horizontal edges
        if j+1 < maze_size:
           edge_str_0 = "0.5::edge("+str(current_idx+1)+","+str(current_idx+1+1)+",0)"
           edge_str_1 = "0.5::edge("+str(current_idx+1)+","+str(current_idx+1+1)+",1)"
           program_str = program_str + edge_str_0+";"+edge_str_1+".\n" 
           # possible_evidence= possible_evidence + "evidence(path("+str(current_idx+1)+","+str(current_idx+2)+ ")).\n"

        #vertical edges
        if current_idx+maze_size < maze_size * maze_size:
           edge_str_0 = "0.5::edge("+str(current_idx+1)+","+str(current_idx+maze_size+1 )+",0)"
           edge_str_1 = "0.5::edge("+str(current_idx+1)+","+str(current_idx+maze_size+1 )+",1)"
           program_str = program_str + edge_str_0+";"+edge_str_1+".\n" 
           # possible_evidence= possible_evidence + "evidence(path("+str(current_idx+1)+","+str(current_idx+2)+ ")).\n"

program_str = program_str + """
edge(X,Y,V) :- edge(Y,X,V).
path(X,Y) :- edge(X,Y,0).
path(X,Y) :- edge(X,Z,0),
             Y \\= Z,
         path(Z,Y).

path(X,Y) :- path(Y,X).
"""

# # print(possible_evidence)
# program_str = program_str + possible_evidence
program_str = program_str + """
query(edge(_,_,0)).
"""

# print(program_str)
num_samples = 1
model = PrologString(program_str)
result = sample.sample(model, n=num_samples, format='dict')

edge_tuples = []
counter = 0
for re in result:
    counter = counter + 1
    G = nx.Graph()
    for li in re:
        # print(li)
        u = str(li.args[0])
        v = str( li.args[1] )
        G.add_edge(u,v,weight = 1)

    node_type = {}
    grid = []
    for i in range(maze_size):
        grid.append([])
        for j in range(maze_size):
            grid[i].append(1)
            idx = (i*(maze_size)+j)+1
            top_bot = False
            right_left = False
            n_non_zero_neighs = 0
            if j + 1 < maze_size:
                if not G.has_edge(str(idx),str(idx+1)): 
                    pass
                    # G.add_edge(str(idx),str(idx+1),weight = sys.maxsize)
                else:
                    # grid[i][j+1] = 0
                    # print("edge:", (str(idx),str(idx+1)))
                    n_non_zero_neighs = n_non_zero_neighs + 1
                    weight = 1
                    right_left = True

            if j - 1 > 0:
                if not G.has_edge(str(idx),str(idx-1)): 
                    pass
                    # G.add_edge(str(idx),str(idx-1),weight = sys.maxsize)
                else:
                    # grid[i][j-1] = 0
                    n_non_zero_neighs = n_non_zero_neighs + 1
                    weight = 1
                    right_left = True


            if i + 1 < maze_size:
                if not G.has_edge(str(idx),str(idx+maze_size)): 
                    pass
                    # G.add_edge(str(idx),str(idx+maze_size),weight = sys.maxsize)
                else:
                    n_non_zero_neighs = n_non_zero_neighs + 1
                    # grid[i+1][j] = 0
                    weight = 1
                    top_bot = True

            if i - 1 > 0:
                if not G.has_edge(str(idx),str(idx-maze_size)): 
                    pass
                    # G.add_edge(str(idx),str(idx-maze_size),weight = sys.maxsize)
                else:
                    n_non_zero_neighs = n_non_zero_neighs + 1
                    # grid[i-1][j] = 0
                    weight = 1
                    top_bot = True
            if n_non_zero_neighs == 0:
                # print("no non-zeros? really")
                pass
            elif n_non_zero_neighs == 1: 
                # print("we have one neighbor")
                node_type[str(idx)] = "tr"
                # print("1: i,j: ", i,j)
            elif n_non_zero_neighs == 2: 
                # print("we have two neighbors")
                # print("2: i,j: ", i,j)
                grid[i][j] = 0
                # print(grid)
                if top_bot:
                    if right_left:
                        node_type[str(idx)] = "tu"
                    else:
                        node_type[str(idx)] = "s"

                elif right_left:
                    node_type[str(idx)] = "s"
                else:
                    print("what how can you not be either topbot")

            elif n_non_zero_neighs == 3: 
                grid[i][j] = 0
                # print("we have three neighbors")
                node_type[str(idx)] = "T"
            elif n_non_zero_neighs == 4: 
                grid[i][j] = 0
                # print("we have four neighbors")
                node_type[str(idx)] = "c"


    # print(node_type)

    uid_str = str(uuid.uuid4())

    if not os.path.exists("edgelists/problog"):
        os.mkdir("edgelist/problog")
    
    nx.write_edgelist(G,"edgelists/problog/"+ uid_str+ ".txt")

    pos = {str((i*maze_size)+j+1): (j,-i) for i in range(maze_size) for j in range (maze_size)}
    nx.draw(G,pos, labels = node_type)



    if not os.path.exists("imgs/graphs-2/problog"):
        os.mkdir("imgs/graphs-2/problog")

    plt.savefig("imgs/graphs-2/problog/"+uid_str+".png")
    plt.clf()

# print(program_str)

#taxonmy of interaction modalities 
#structued priors 
#programable generator space
#formal way of doing both things jointly
#think about the phrasing from abstract and the title or the intro
#mention filtering vs generation
#how are all the cases of interaction mechanisms can be encoded in problog
#emphasize the global properties can be captured
#here is how model each of the global properties
#we don't have to change what we have written
#the dataset has not changed
#now we adjust the model
#adjust the prior
#if there is more data it goes to the data 
#establish what the other tools fail to do as we go at each step of the modeling
#keep adding one layer of complexity at a time
