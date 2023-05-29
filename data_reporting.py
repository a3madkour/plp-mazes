import pandas as pd
import matplotlib.pyplot as plt

xlabel_dict = {
    "cell_type_maze_tu" : "Number of Turn Nodes in Maze",
    "cell_type_maze_s" : "Number of Straight Nodes in Maze",
    "cell_type_maze_T" :"Number of Straight Nodes in Maze",
    "cell_type_maze_c" :"Number of Cross-Junction Nodes in Maze",
    "sol_type_maze_tu" :"Number of Turn Nodes in Solution Path",
    "sol_type_maze_s" :"Number of Straight Nodes in Soultion Path",
    "sol_type_maze_d" :"Number of Desicion Nodes in Solution Path",
    "sol_type_maze_len" :"Length of Solution Path"
} 
logic_df = pd.read_csv("CSVs/logic_mazes_size_5-pr.csv")
asp_df = logic_df[logic_df["alg"] == "asp"]
problog_df = logic_df[logic_df["alg"] == "problog"]
learnt_df = pd.read_csv("CSVs/learnt_mazes_size_5.csv")
print("------------------------------------------------------------------------ ")
print("Hashes")
print()
print("Number of unique ASP Hashes: ", len(asp_df["hash"].unique()))
print("Number of unique Problog Hashes: ",len(problog_df["hash"].unique()))
print("Number of unique Learnt Problog Hashes: ",len(learnt_df["hash"].unique()))
print("------------------------------------------------------------------------ ")
print("Maze Properties")
print()
print("Number of Turn Nodes in ASP: ", len( asp_df["cell_type_maze_tu"].unique()) )
print("Number of Straight Nodes in ASP: ", len( asp_df["cell_type_maze_s"].unique()) )
print("Number of T-Junction Nodes in ASP: ", len( asp_df["cell_type_maze_T"].unique()) )
print("Number of Cross-Junction Nodes in ASP: ", len( asp_df["cell_type_maze_c"].unique()) )
print()
print("Number of Turn Nodes in Problog: ", len( problog_df["cell_type_maze_tu"].unique()) )
print("Number of Straight Nodes in Problog: ", len( problog_df["cell_type_maze_s"].unique()) )
print("Number of T-Junction Nodes in Problog: ", len( problog_df["cell_type_maze_T"].unique()) )
print("Number of Cross-Junction Nodes in Problog: ", len( problog_df["cell_type_maze_c"].unique()) )

print()
print("Number of Turn Nodes in Learnt Problog: ", len( learnt_df["cell_type_maze_tu"].unique()) )
print("Number of Straight Nodes in Learnt Problog: ", len( learnt_df["cell_type_maze_s"].unique()) )
print("Number of T-Junction Nodes in Learnt Problog: ", len( learnt_df["cell_type_maze_T"].unique()) )
print("Number of Cross-Junction Nodes in Learnt Problog: ", len( learnt_df["cell_type_maze_c"].unique()) )
print("------------------------------------------------------------------------ ")
print("Solution Path Properties")
print()
print("Number of Turn Nodes in Solution Path of ASP: ", len(asp_df["sol_type_maze_tu"].unique()))
print("Number of Straight Nodes in Solution Path of ASP: ", len(asp_df["sol_type_maze_s"].unique()))
print("Number of Decision Nodes in Solution Path of ASP: ", len(asp_df["sol_type_maze_d"].unique()))
print("Length of Solution Path of ASP: ", len(asp_df["sol_type_maze_len"].unique()))
print()
print("Number of Turn Nodes in Solution Path of Problog: ",len(problog_df["sol_type_maze_s"].unique()))
print("Number of Straight Nodes in Solution Path of Problog: ",len(problog_df["sol_type_maze_tu"].unique()))
print("Number of Decision Nodes in Solution Path of Problog: ",len(problog_df["sol_type_maze_d"].unique()))
print("Length of Solution Path of Problog: ",len(problog_df["sol_type_maze_len"].unique()))
print()
print("Number of Turn Nodes in Solution Path of Learnt Problog: ",len(learnt_df["sol_type_maze_tu"].unique()))
print("Number of Straight Nodes in Solution Path of Learnt Problog: ",len(learnt_df["sol_type_maze_s"].unique()))
print("Number of Decision Nodes in Solution Path of Learnt Problog: ",len(learnt_df["sol_type_maze_d"].unique()))
print("Length of Solution Path of Learnt Problog: ",len(learnt_df["sol_type_maze_len"].unique()))
print("------------------------------------------------------------------------ ")
print("Misc.")
print()
print("Number of mazes with decision nodes of the solution path less than 4 in Problog: ",len(problog_df[problog_df["sol_type_maze_d"] < 4]))
print("Number of mazes with decision nodes of the solution path less than 4 in Learnt Problog: ",len(learnt_df[learnt_df["sol_type_maze_d"] < 4]))
print()
print()
print("Mean and std of number of Decision nodes in Solution path Problog: ", problog_df["sol_type_maze_d"].mean(), "+- ", problog_df["sol_type_maze_d"].std())
print("Mean and std of number of Decision nodes in Solution path Learnt Problog: ", learnt_df["sol_type_maze_d"].mean(), "+-", learnt_df["sol_type_maze_d"].std())
print("------------------------------------------------------------------------ ")

for col in asp_df.columns:

    if col not in xlabel_dict:
        continue
    ax = asp_df[col].plot.hist(xlabel=col)
    ax.set_xlabel(xlabel_dict[col])

    plt.savefig("plots/asp_" + col + ".png")

    plt.cla()

    ax = problog_df[col].plot.hist(xlabel = col)
    ax.set_xlabel(xlabel_dict[col])

    plt.savefig("plots/problog_" + col + ".png")
    plt.cla()

    ax = learnt_df[col].plot.hist(xlabel = col)
    ax.set_xlabel(xlabel_dict[col])

    plt.savefig("plots/learnt_" + col + ".png")
    plt.cla()
