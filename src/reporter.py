import sys
import numpy

class Reporter:
	def __init__(self, run):
		self.run = run
		self.out = "reports/report_" + str(run) + ".txt"
		self.OUTFILE = open(self.out,"w")
		self.time = []


		self.OUTFILE.write("Experiment Number: " + str(run) + "\n")
		self.OUTFILE.write("\tModel Name:\t Run #\t time\n")


	def log_time(self, name, trial, time):
		self.OUTFILE.write("\t" + name + "\t" + str(trial) + "\t" + str(time) + "\n")
		self.time.append(time)

	def calculate(self, name):
		#numpy.mean(self.time, axis = 0)

		self.OUTFILE.write(name + " Mean:\t" + str(numpy.mean(self.time, axis = 0)) + "\n")
		self.OUTFILE.write(name + " Standard Deviation:\t" + str(numpy.std(self.time, axis = 0)) + "\n")
		self.OUTFILE.write(name + " Variance:\t" + str(numpy.var(self.time, axis = 0)) + "\n\n\n")
		self.time = []

	def close(self):
		self.OUTFILE.close()


#def list_mean(l):
#	return sum(l) / float(len(l))