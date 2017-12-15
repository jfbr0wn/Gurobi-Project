import os
import sys
import json
import random

from gurobipy import *

from graphgen import Graphgen

from CLgraphfile import MClique 

from optimizer import *

from reporter import *


 # Get the experiment parameters stored a json file
expParams = "expParamaters.json"


# Controller tasks:
# Access experiment parameters
# Create an instance of report
# Create an instance of experiment
# Create a set of graphfiles to test on
# Create lp files for gurobi to solve on
# Run all experiments
# Store to report
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
	rpt = Reporter(run)
	

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

		# Run Base Model
		for j in range(runs_per_model):
			opt = Optimizer(mclique_file[j])
			base_time = opt.base_solve()
			rpt.log_time("base", j+1, base_time)
		rpt.calculate("base")

		# Run Custom Callback
		for j in range(runs_per_model):
			opt = Optimizer(mclique_file[j])
			ccb_time = opt.ccb_solve()
			rpt.log_time("ccb", j+1, ccb_time)
		rpt.calculate("ccb")

		# Run MIP Focus = 1
		for j in range(runs_per_model):
			opt = Optimizer(mclique_file[j])
			mip_time = opt.mip_solve(1)
			rpt.log_time("mip1", j+1, mip_time)
		rpt.calculate("mip1")

		# Run MIP Focus = 2
		for j in range(runs_per_model):
			opt = Optimizer(mclique_file[j])
			mip_time = opt.mip_solve(2)
			rpt.log_time("mip2", j+1, mip_time)
		rpt.calculate("mip2")

		# Run MIP Focus = 3
		for j in range(runs_per_model):
			opt = Optimizer(mclique_file[j])
			mip_time = opt.mip_solve(3)
			rpt.log_time("mip3", j+1, mip_time)
		rpt.calculate("mip3")

		# Run Gurobi Build in Tuner
		for j in range(runs_per_model):
			opt = Optimizer(mclique_file[j])
			tune_time = opt.tune_solve(False)
			rpt.log_time("tuner", j+1, tune_time)
		rpt.calculate("tuner")

		# Run Gap Solving Algorithm
		for j in range(runs_per_model):
			opt = Optimizer(mclique_file[j])
			gap_time = opt.gap_solve()
			rpt.log_time("gap", j+1, mip_time)
		rpt.calculate("gap")

		# Run Branch solving algorithm
		for j in range(runs_per_model):
			opt = Optimizer(mclique_file[j])
			branch_time = opt.branch_solve()
			rpt.log_time("branch", j+1, mip_time)
		rpt.calculate("branch")

 	rpt.close()

	json_data["Parameters"]["run"] = str(run + 1)
	json.dump(json_data, open(expParams, "w"), indent = 4)


if __name__ == "__main__":
	Controller()
