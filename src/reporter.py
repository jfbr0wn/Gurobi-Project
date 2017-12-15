import sys
import numpy

class Reporter:
	def __init__(self, run, min_node, max_node, min_prob, max_prob):
		self.run = run
		self.out = "reports/report_" + str(run) + ".txt"
		self.OUTFILE = open(self.out,"w")
		self.time = []

		# Create file and add appropriate headers
		self.OUTFILE.write("Experiment Number: " + str(run) + "\n")
		self.OUTFILE.write("Min Node: " + str(min_node) + "\n")
		self.OUTFILE.write("Max Node: " + str(max_node) + "\n")
		self.OUTFILE.write("Min Probability: " + str(min_prob) + "\n")
		self.OUTFILE.write("Max Probability: " + str(max_prob) + "\n")
		self.OUTFILE.write("\tModel Name:\t Run #\t time\n")


	def log_time(self, name, trial, time): # Log a runtime to file
		self.OUTFILE.write("\t" + name + "\t" + str(trial) + "\t" + str(time) + "\n")
		self.time.append(time)

	def calculate(self, name): # Calculate Mean, std deviation and variance
		#numpy.mean(self.time, axis = 0)

		self.OUTFILE.write(name + " Mean:\t\t" + str(numpy.mean(self.time, axis = 0)) + "\n")
		self.OUTFILE.write(name + " Standard Deviation:\t" + str(numpy.std(self.time, axis = 0)) + "\n")
		self.OUTFILE.write(name + " Variance:\t\t" + str(numpy.var(self.time, axis = 0)) + "\n\n\n")
		self.time = []

	def close(self):
		self.OUTFILE.close()
