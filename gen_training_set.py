import pandas as pd
import networkx as nx
import shutil

df = pd.read_csv("CSVs/logic_mazes_size_5.csv")
new_df = df
# new_df = df[df["alg"] == "problog"]
# new_df = df[df["alg"] == "asp"]
training_set = new_df[new_df["sol_type_maze_d"] < 4]
ids = training_set["id"]
training_conditions = []
for id in ids:
    path = "edgelists/" + training_set[training_set["id"] == id]["alg"] + "/" + id + ".txt"
    path = path.item()
    new_path =  "train_set/"+ id + ".txt"

    shutil.copy(str(path),str(new_path))
# print(ids)
