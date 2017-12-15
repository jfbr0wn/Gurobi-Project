import sys
from gurobipy import *

class Optimizer:
	def __init__(self, lp_file):
		self.file = lp_file
		#params = default parameters

	def base_solve(self):
		model = read(self.file)
		model.optimize()
		return model.Runtime

	def ccb_solve(self):
		model = read(self.file)
		model.optimize(mycallback)
		return model.Runtime

	def mip_solve(self, i):
		model = read(self.file)
		model.params.MIPFocus = i
		model.optimize()
		return model.Runtime

	def tune_solve(self, callback):
		model = read(self.file)
		if(callback):
			model.getTuneResult(0)
			model.optimize()

		else:
			model.params.tuneResults = 1
			model.tune()
			model.optimize()
			
	
		return model.Runtime

	def gap_solve(self):
		#MIP is solverd for 5 seconds with different params.
		#Smallest MIP is selected and optimization is resumed
		model = read(self.file)
		# Set a 5 second timelimit
		model.params.timeLimit = 5

		bestGap = GRB.INFINITY
		bestModel = None
		for i in range(4):
			m = model.copy()
			m.params.MIPFocus = i
			m.optimize()
			if bestModel == None or bestGap > gap(m):
				bestModel = m
				bestGap = gap(bestModel)
		bestModel.params.timeLimit = "default"
		bestModel.optimize()
		return bestModel.Runtime


	def branch_solve(self):
		#MIP is solverd for 5 seconds with different branch params
		#Smallest branch is selected and optimization is resumed
		model = read(self.file)
		# Set a 5 second timelimit
		model.params.timeLimit = 5

		bestGap = GRB.INFINITY
		bestModel = None
		for i in range(-1, 3):
			m = model.copy()
			m.params.VarBranch = i
			m.optimize()
			if bestModel == None or bestGap > gap(m):
				bestModel = m
				bestGap = gap(bestModel)
		bestModel.params.timeLimit = "default"
		bestModel.optimize()
		return bestModel.Runtime


# Custom Callback Helper Function
def mycallback(model, where):
	if where == GRB.callback.MIP:
		time = model.cbGet(GRB.callback.RUNTIME)
		best = model.cbGet(GRB.callback.MIP_OBJBST)
		if time > 10 and best < GRB.INFINITY:
			model.terminate()

# Gap Helper function
def gap(model):
	if model.solCount == 0 or abs(model.objVal) < 1e-6:
		return GRB.INFINITY
	return abs(model.objBOund - model.objVal)/abs(model.objVal)
