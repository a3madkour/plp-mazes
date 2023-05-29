from util import graphToEvidence
import networkx as nx
import os
from problog.program import PrologString
from problog.tasks import sample
from problog.logic import Term
from problog.learning import lfi


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
           edge_str_0 = "t(0.5)::edge("+str(current_idx+1)+","+str(current_idx+1+1)+",0)"
           edge_str_1 = "t(0.5)::edge("+str(current_idx+1)+","+str(current_idx+1+1)+",1)"
           program_str = program_str + edge_str_0+";"+edge_str_1+".\n" 
           # possible_evidence= possible_evidence + "evidence(path("+str(current_idx+1)+","+str(current_idx+2)+ ")).\n"

        #vertical edges
        if current_idx+maze_size < maze_size * maze_size:
           edge_str_0 = "t(0.5)::edge("+str(current_idx+1)+","+str(current_idx+maze_size+1 )+",0)"
           edge_str_1 = "t(0.5)::edge("+str(current_idx+1)+","+str(current_idx+maze_size+1 )+",1)"
           program_str = program_str + edge_str_0+";"+edge_str_1+".\n" 
           # possible_evidence= possible_evidence + "evidence(path("+str(current_idx+1)+","+str(current_idx+2)+ ")).\n"

program_str = program_str + """
edge(X,Y,V) :- edge(Y,X,V).
path(X,Y) :- edge(X,Y,0).
path(X,Y) :- edge(X,Z,0),
             Y \\= Z,
         path(Z,Y).


"""

# print(possible_evidence)
program_str = program_str + possible_evidence
program_str = program_str + """
query(edge(_,_,0)).
"""


train_set_path = "train_set"
all_ev = []
for fl in os.listdir(train_set_path):
    G = nx.read_edgelist(train_set_path + "/" + fl)
    all_ev.append(graphToEvidence(G,maze_size))
# print(kap)

# all_ev = all_ev[:10]
# print(all_ev[:10])
score, weights, atoms, iteration, lfi_problem = lfi.run_lfi(PrologString(program_str), all_ev)

pro_str = lfi_problem.get_model()
pro_str = pro_str + """
query(edge(_,_,0)).
"""

print(pro_str)
