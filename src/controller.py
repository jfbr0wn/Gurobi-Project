import os
import sys
import json
import random

from gurobipy import *

from graphgen import Graphgen

from CLgraphfile import MClique 

from experimentor import *

from reporter import *


 # Get the experiment parameters stored a json file
expParams = "Parameters.json"


# Controller tasks:
# 1) Access experiment parameters
# 2)Create an instance of report
# 3) Create an instance of experiment
# 4) Create a set of graphfiles to test on
# 5) Create lp files for gurobi to solve on
# 6) Run all experiments
# 7) Store to report
def Controller():
	# Read in our experimental parameters
	json_data = json.load(open(expParams))
	params = json_data["Parameters"]
	graph_data = json_data["GraphData"]

	# Get the parameters
	runs_per_model = int(params["runs_per_model"])
	find_max_clique = bool(params["find_max_clique"])
	find_near_clique = bool(params["find_inverse_clique"])
	run = int(params["run"])
	mc = params["mclique_file"]
	nc = params["nclique_file"]

	# Get the Graph Data
	max_nodes = graph_data["max_nodes"]
	min_nodes = graph_data["min_nodes"]
	min_prob = graph_data["min_probability"]
	max_prob = graph_data["max_probability"]
	gf = graph_data["graph_file"]

	# Create a report
	rpt = Reporter(run, min_nodes, max_nodes, min_prob, max_prob)
	
	# Init variable lists
	graphfile = []
	mclique_file = []
	nclique_file = []


#Generate a Graphfile for each run so that we can run across similar data points
	for j in range(runs_per_model):
		# name the files appropriately
		graphfile.append(gf + "_" + str(run) + "_" + str(j+1) + ".txt")
		mclique_file.append(mc + "_" + str(run) + "_" + str(j+1) + ".lp")
		
		# Set random nodes and probability to specs
		nodenum = random.randint(int(min_nodes), int(max_nodes))
		nodeprob = random.uniform(float(min_prob), float(max_prob))

		# Create a graph and lp file for each run
		Graphgen(nodenum, nodeprob, graphfile[j])
		MClique(graphfile[j], mclique_file[j])

	# Run Trials for Each example of Max Clique
	if(find_max_clique):

		exp = Experimentor(rpt, mclique_file)

		exp.experiment("base") # Run Base Gurobi, No optimizers

		exp.experiment("ccb") # Run Gurobi using a custom callback function

		exp.experiment("mip1") # Run Gurobi with MIPFocus set to 1

		exp.experiment("mip2") # Run Gurobi with MIPFocus set to 2

		exp.experiment("mip3") # Run Gurobi with MIPFocus set to 3

		exp.experiment("tuner") # Run Gurobi builtin parameter tuning

		exp.experiment("gap") # Run Gurobi with a gap reducing optimizer

		exp.experiment("branch") # Run Gurobi with a branch reducing Optimizer

	# Possible Extension: Add support for other Gurobi Algorithms

 	rpt.close()

 	# Increment run indentifier to avoid overwriting preexisting runs
	json_data["Parameters"]["run"] = str(run + 1)
	json.dump(json_data, open(expParams, "w"), indent = 4)


if __name__ == "__main__":
	Controller()
