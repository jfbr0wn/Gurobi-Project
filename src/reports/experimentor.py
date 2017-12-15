
from optimizer import *

class Experimentor:
	def __init__(self, rpt, file):
		self.reporter = rpt
		self.file = file


	def experiment(self, name):
		for j in range(len(self.file)):
			opt = Optimizer(self.file[j])

			### Call Experiments Here
			if name == "base":
				time = opt.base_solve()

			if name == "ccb":
				time = opt.ccb_solve()

			if name == "mip1":
				time = opt.mip_solve(1)

			if name == "mip2":
				time = opt.mip_solve(2)

			if name == "mip3":
				time = opt.mip_solve(3)

			if name == "tuner":
				time =opt.tune_solve(False)

			if name == "gap":
				time = opt.gap_solve()

			if name == "branch":
				time = opt.branch_solve()

			# Log each run in our reporter
			self.reporter.log_time(name, j+1, time)
		# Get mean, std dev, and variance
		self.reporter.calculate(name)