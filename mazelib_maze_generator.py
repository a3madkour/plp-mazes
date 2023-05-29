from mazelib import Maze
import sys as sys
import multiprocessing as mp
import pandas as pd
import os
from mazelib.solve.BacktrackingSolver import BacktrackingSolver
from mazelib.generate.AldousBroder import AldousBroder
from mazelib.generate.BacktrackingGenerator import BacktrackingGenerator
from mazelib.generate.BinaryTree import BinaryTree
from mazelib.generate.CellularAutomaton import CellularAutomaton
from mazelib.generate.Division import Division
from mazelib.generate.DungeonRooms import DungeonRooms
from mazelib.generate.Ellers import Ellers
from mazelib.generate.GrowingTree import GrowingTree
from mazelib.generate.HuntAndKill import HuntAndKill
from mazelib.generate.Kruskal import Kruskal
from mazelib.generate.Prims import Prims
from mazelib.generate.Sidewinder import Sidewinder
from mazelib.generate.TrivialMaze import TrivialMaze
from mazelib.generate.Wilsons import Wilsons
import imageio.v3 as iio
import numpy as np
from PIL import Image
import networkx as nx
import matplotlib.pyplot as plt
from util import gridToGraph,posToIndx,maze_props,sol_props
import uuid

                
alg_names = ["AldousBroder", "BacktrackingGenerator", "BinaryTree","CellularAutomaton","Division","DungeonRooms","Ellers","GrowingTree","HuntAndKill","Kruskal","Prims","Sidewinder","TrivialMaze","Wilsons"]
alg_dict = {"AldousBroder": AldousBroder , "BacktrackingGenerator": BacktrackingGenerator , "BinaryTree": BinaryTree ,"CelluarAutomaton": CellularAutomaton ,"Division": Division ,"DungeonRooms": DungeonRooms ,"Ellers": Ellers ,"GrowingTree": GrowingTree ,"HuntAndKill": HuntAndKill ,"Kruskal": Kruskal ,"Prims": Prims ,"Sidewinder": Sidewinder ,"TrivialMaze": TrivialMaze ,"Wilsons": Wilsons }

def gen_mazes(args):
    m = Maze()
    alg_name = args['alg_name']
    maze_size = args['maze_size']
    m.generator = alg_dict[alg_name](int(maze_size/2), int(maze_size/2))
    m.generate()
    grid = m.grid
    new_grid = 1 - grid
    graph,graph2,cell_type = gridToGraph(grid)
    if not os.path.exists("imgs/mazes/"+alg_name):
        os.mkdir("imgs/mazes/"+alg_name)

    im = Image.fromarray(np.uint8(new_grid*255))
    uid_str = str(uuid.uuid4())

    iio.imwrite(('imgs/mazes/'+alg_name+'/'+uid_str+'.jpg'), im)

    maze_pops = maze_props(cell_type)

    st = posToIndx((0,0),maze_size)
    nd = posToIndx((maze_size-1,maze_size-1), maze_size)

    sol_path = nx.shortest_path(graph, st,nd, weight="weight")


    sol_pops = sol_props(sol_path,cell_type)

    pos = {str((i*maze_size)+j): (j,-i) for i in range(maze_size) for j in range (maze_size)}
    nx.draw(graph,pos, labels = cell_type)

    if not os.path.exists("imgs/graphs/"+alg_name):
        os.mkdir("imgs/graphs/"+alg_name)
    plt.savefig("imgs/graphs/"+alg_name+"/"+uid_str+".png")
    plt.clf()


    pos = {str((i*maze_size)+j): (j,-i) for i in range(maze_size) for j in range (maze_size)}
    nx.draw(graph2,pos, labels = cell_type)

    if not os.path.exists("imgs/graphs-2/"+alg_name):
        os.mkdir("imgs/graphs-2/"+alg_name)
    plt.savefig("imgs/graphs-2/"+alg_name+"/"+uid_str+".png")
    plt.clf()
    if not os.path.exists("edgelists/"+alg_name):
        os.mkdir("edgelists/"+alg_name)

    if not os.path.exists("edgelists-2/"+alg_name):
        os.mkdir("edgelists-2/"+alg_name)

    nx.write_edgelist(graph,"edgelists/"+alg_name+"/"+ uid_str+ ".txt")
    nx.write_edgelist(graph2,"edgelists-2/"+alg_name+"/"+ uid_str+ ".txt")

    result = {}
    result["id"] = uid_str
    result["alg"] = alg_name
    result["cell_type_maze_tu"] = maze_pops['tu']
    result["cell_type_maze_s"] = maze_pops['s'] 
    result["cell_type_maze_T"] = maze_pops['T']
    result["cell_type_maze_c"] = maze_pops['c']

    result["sol_type_maze_tu"] = sol_pops['tu']
    result["sol_type_maze_s"] = sol_pops['s'] 
    result["sol_type_maze_d"] = sol_pops['d']
    result["sol_type_maze_len"] = sol_pops['len']
    return result

# ids = []
# for alg_name in alg_dict:
#     m = Maze()
#     m.generator = alg_dict[alg_name](3,3)
#     for i in range(num_mazes):
#         print("Generating " + alg_name + "'s " + str(i+1) + "-th maze")
# # m.generator = Prims(3,3)
#         uid = uuid.uuid4()
#         uid_str = str(uuid.uuid4())
#         alg_type.append(alg_name)
#         ids.append(uid_str)
#         m.generate()
#         m.solver  = BacktrackingSolver()
#         m.generate_entrances()
#         m.solve()
#         new_grid = 1 - m.grid

#         if not os.path.exists("imgs/mazes/"+alg_name):
#             os.mkdir("imgs/mazes/"+alg_name)

#         im = Image.fromarray(np.uint8(new_grid*255))

#         iio.imwrite(('imgs/mazes/'+alg_name+'/'+uid_str+'.jpg'), im)

#         grid = m.grid
#         graph,cell_type = gridToGraph(grid)
#         maze_pops = maze_props(cell_type)

#         cell_type_maze_tu.append(maze_pops['tu'])
#         cell_type_maze_s.append(maze_pops['s']) 
#         cell_type_maze_T.append(maze_pops['T'])
#         cell_type_maze_c.append(maze_pops['c'])


#         st = posToIndx(m.start,7)
#         nd = posToIndx(m.end, 7)

#         predecs,dists  = nx.floyd_warshall_predecessor_and_distance(graph,weight="weight")
#         sol_path = nx.reconstruct_path(st, nd, predecs)


#         sol_pops = sol_props(sol_path,cell_type)

#         cell_type_sol_tu.append(sol_pops['tu'])
#         cell_type_sol_s.append(sol_pops['s']) 
#         cell_type_sol_d.append(sol_pops['d'])
#         cell_type_sol_len.append(sol_pops['len'])
#         pos = {str((i*7)+j): (j,-i) for i in range(7) for j in range (7)}
#         nx.draw(graph,pos, labels = cell_type)

#         if not os.path.exists("imgs/graphs/"+alg_name):
#             os.mkdir("imgs/graphs/"+alg_name)
#         plt.savefig("imgs/graphs/"+alg_name+"/"+uid_str+".png")

#         if not os.path.exists("edgelists/"+alg_name):
#             os.mkdir("edgelists/"+alg_name)

#         nx.write_edgelist(graph,"edgelists/"+alg_name+"/"+ uid_str+ ".txt")

# maze_data = {
#     "alg_type" : alg_type, 
#     "cell_type_sol_tu" : cell_type_sol_tu,
#     "cell_type_sol_s" : cell_type_sol_s,
#     "cell_type_sol_d" : cell_type_sol_d,
#     "cell_type_sol_len" : cell_type_sol_len,
#     "cell_type_maze_tu" : cell_type_maze_tu,
#     "cell_type_maze_s" : cell_type_maze_s,
#     "cell_type_maze_T" : cell_type_maze_T,
#     "cell_type_maze_c" : cell_type_maze_c,
#     "ids" : ids
# }
# all_short_paths = [p for p in nx.all_shortest_paths(graph,st,nd,weight="weight")]
# print(all_short_paths)
# # print()

# #cell types
# # TODO tu: Turn
# # TODO s: Straight
# # TODO T: T-junction
# # TODO c: Cross-junction
# # TODO tr:Terminal

# mazes_df = pd.DataFrame(maze_data)

# mazes_df.to_csv("benchmark_mazes.csv")
# print(mazes_df)

# new_G = nx.read_edgelist("edgelists/BacktrackingGenerator/5869fa28-c243-4367-aab2-98feaf2d2591.txt")
# print(new_G)

# for edge in new_G.edges:
#     edge_data = new_G.get_edge_data(edge)
#     print(edge_data)


# args = {}
# maze_size = 7
# args["maze_size"] = maze_size
# args["alg_name"] = alg_names[1]
# gen_mazes(args)

    
num_mazes = 1000
# alg_type = []
# cell_type_sol_tu = []
# cell_type_sol_s = []
# cell_type_sol_d = []
# cell_type_sol_len = []
# cell_type_maze_tu = []
# cell_type_maze_s = []
# cell_type_maze_T = []
# cell_type_maze_c = []

args = {}
maze_size = 7
args["maze_size"] = maze_size
results2 = []
def collectResults(result):
    global results2
    results2.append(result)

for alg in alg_dict:
    args["alg_name"] = alg
    print(alg)
    pool = mp.Pool(mp.cpu_count())
    for i in range(num_mazes):
        pool.apply_async(gen_mazes, args=[args], callback=collectResults)
    pool.close()
    pool.join()

df = pd.DataFrame(results2)
df.to_csv("maze_size"+str(maze_size)+".csv")
print(df)
