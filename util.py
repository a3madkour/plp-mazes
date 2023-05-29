import networkx as nx
import sys
from collections import Counter
from problog.logic import Term,Constant

def posToIndx(pos, grid_size):
    x,y = pos
    return str((x*grid_size)+ y)

def graphToEvidence(graph :nx.Graph,maze_size:int):
    tuple_ls = set()
    for i in range(maze_size):
        for j in range(maze_size):
            idx = (i * maze_size) + j

            if (j + 1) < maze_size:
                tpl = str(idx+1), str(idx+2)
                if not graph.has_edge(str(idx+1),str(idx+2)):
                    tuple_ls.add(tpl)
                # tuple_ls.append((str(idx+1), str(idx+2)))

            if (j - 1) > 0:
                tpl = str(idx+1), str(idx)
                if not graph.has_edge(str(idx+1),str(idx)):
                    tuple_ls.add(tpl)
                # tuple_ls.append((str(idx+1), str(idx)))

            if (i + 1) < maze_size:
                tpl = (str(idx+1), str(idx+1 + maze_size))
                if not graph.has_edge(str(idx+1),str(idx + 1 + maze_size)):
                    tuple_ls.add(tpl)
                # tuple_ls.append((str(idx+1), str(idx+1 + maze_size)))

            if (i - 1) > 0:
                tpl = (str(idx+1), str(idx + 1 - maze_size))
                if not graph.has_edge(str(idx+1),str(idx + 1 - maze_size)):
                    tuple_ls.add(tpl)
                # tuple_ls.append((str(idx+1), str(idx + 1 - maze_size)))

    evd_list = []
    for edge in graph.edges:
        u,v = edge
        term = Term("edge", Constant(int(u)), Constant(int(v)), Constant(int(0)))
        evd_list.append((term,True))
    for tpl in tuple_ls:
        u,v = tpl
        term = Term("edge", Constant(int(u)), Constant(int(v)), Constant(int(1)))
        evd_list.append((term,True))
    return evd_list


def gridToGraph(grid):
    G = nx.Graph()
    G2 = nx.Graph()
    node_type = {}
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            idx = i*(len(row))+j
            n_non_zero_neighs = 0
            top_bot = False
            right_left = False
            weight = 0
            if j + 1 < len(row):
                if grid[i][j+1] == 0 and grid[i][j] == 0:
                    n_non_zero_neighs = n_non_zero_neighs + 1
                    weight = 1
                    right_left = True
                    G2.add_edge(str(idx),str(idx+1), weight = weight)
                else:
                    weight = sys.maxsize
                G.add_edge(str(idx),str(idx+1), weight = weight)

            if j - 1 > 0:
                if grid[i][j-1] == 0 and grid[i][j] == 0:
                    n_non_zero_neighs = n_non_zero_neighs + 1
                    weight = 1
                    right_left = True
                    G2.add_edge(str(idx),str(idx-1), weight = weight)
                else:
                    weight = sys.maxsize
                G.add_edge(str(idx),str(idx-1), weight = weight)

            weight = 0
            if i + 1 < len(row):
                if grid[i+1][j] == 0 and grid[i][j] == 0:
                    n_non_zero_neighs = n_non_zero_neighs + 1
                    weight = 1
                    top_bot = True
                    G2.add_edge(str(idx),str(idx+len(row)), weight = weight)
                else:
                    weight = sys.maxsize
                G.add_edge(str(idx),str(idx+len(row)), weight = weight)

            if i - 1 > 0:
                if grid[i-1][j] == 0 and grid[i][j] == 0:
                    n_non_zero_neighs = n_non_zero_neighs + 1
                    weight = 1
                    top_bot = True
                    G2.add_edge(str(idx),str(idx-len(row)), weight = weight)
                else:
                    weight = sys.maxsize
                G.add_edge(str(idx),str(idx-len(row)), weight = weight)


            if grid[i][j] == 0:
                if n_non_zero_neighs == 0:
                    # print("no non-zeros? really")
                    pass
                elif n_non_zero_neighs == 1: 
                    # print("we have one neighbor")
                    node_type[str(idx)] = "tr"
                elif n_non_zero_neighs == 2: 
                    # print("we have two neighbors")
                    if top_bot:
                        if right_left:
                            node_type[str(idx)] = "tu"
                        else:
                            node_type[str(idx)] = "s"

                    elif right_left:
                        node_type[str(idx)] = "s"
                    else:
                        print("what how can you not be either topbot or rightleft")

                elif n_non_zero_neighs == 3: 
                    # print("we have three neighbors")
                    node_type[str(idx)] = "T"
                elif n_non_zero_neighs == 4: 
                    # print("we have four neighbors")
                    node_type[str(idx)] = "c"

    nx.set_node_attributes(G,node_type,"cell_type")
    return G,G2,node_type


def maze_props(cell_type):
    maze_low_level_props = Counter(cell_type.values())
    return maze_low_level_props

def sol_props(sol_path,cell_type):
    sol_path_props = {"tu":0, "s":0, "d":0, "len":0}
    for nod in sol_path:
        if nod not in cell_type:
            continue

        if cell_type[nod] == "tu":
            sol_path_props["tu"] = sol_path_props["tu"] + 1
        if cell_type[nod] == "s":
            sol_path_props["s"] = sol_path_props["s"] + 1
        if cell_type[nod] == "T" or cell_type[nod] == "c":
            sol_path_props["d"] = sol_path_props["d"] + 1
    sol_path_props["len"] = len(sol_path)
    return sol_path_props



def props_from_graph(graph: nx.Graph, maze_size):
    cell_type = {}
    for node in graph.nodes:
        edges = graph.edges(node)
        n_non_zero_neighs = 0
        top_bot = False
        right_left = False
        for edge in edges:
            u,v = edge
            data = graph.get_edge_data(u,v)
            weight = data['weight']
            if weight > 1:
                pass
                # print(edge)
                # print("Infinite")
            else:
                n_non_zero_neighs = n_non_zero_neighs + 1
                if int(v) - int(u) == 1 or int(u) - int(v) == 1 :
                    right_left = True
                    # print("rightleft")
                elif int(v) - int(u) == maze_size or int(u) - int(v) == maze_size:
                    top_bot = True
                    # print("top_bot")
                # print(edge)
                # print("not infinite")
        if n_non_zero_neighs == 1:
            cell_type[node] = "tr"
        elif n_non_zero_neighs == 2:
            if top_bot:
                if right_left:
                    cell_type[node] = "tu"
                else:
                    cell_type[node] = "s"
            elif right_left:
                cell_type[node] = "s"
            else:
                print("this can't happen right?")
        elif n_non_zero_neighs == 3:
            cell_type[node] = "T"
        elif n_non_zero_neighs == 4:
            cell_type[node] = "c"
    return cell_type
 
