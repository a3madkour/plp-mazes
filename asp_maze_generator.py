import subprocess
import json
import uuid
import os
import networkx as nx
import matplotlib.pyplot as plt
import random
from util import props_from_graph

 

num_mazes = 1000
program_path = "ASP Programs/asp_mazes.lp"

for i in range(num_mazes):
    maze_size = 5
    print("Generating maze number: ", i)
    output_file = "output.json"
    seed = int(random.random() * 100)
    run_command = "clingo"
    command_args = ["-n 1",'--sign-def=rnd', "--rand-freq=0.5","--rand-prob=100000,10000","--save-progres=0","--seed=" + str(seed) , program_path , "--outf=2"]
    process = subprocess.Popen([run_command] + command_args, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output, error = process.communicate()
    result = json.loads(output.decode())
    list_edges =result["Call"][0]["Witnesses"][0]["Value"]
    G = nx.Graph()
    uid_str = str(uuid.uuid4())
    for edge in list_edges:
        tuple_str = edge.strip("edge(").strip(")")
        nodes = tuple_str.split(",")
        G.add_edge(nodes[0], nodes[1], weight = 1)


    if not os.path.exists("imgs/graphs-2/asp"):
        os.mkdir("imgs/graphs-2/asp")

    node_type = props_from_graph(G,maze_size)
    pos = {str((i*maze_size)+j+1): (j,-i) for i in range(maze_size) for j in range (maze_size)}
    nx.draw_networkx(G,pos, labels = node_type)
    plt.savefig("imgs/graphs-2/asp/"+uid_str+".png")
    plt.clf()


    if not os.path.exists("edgelists/asp"):
        os.mkdir("edgelists/asp")
    nx.write_edgelist(G,"edgelists/asp/"+ uid_str+ ".txt")
