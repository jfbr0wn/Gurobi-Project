import os
import sys
import json


#from reporter import Reporter
#from optimizer import Optimizer
#from generator import Generator
#from experimentor import Experimentor

# Intialize our classes
#opt = new Optimizer()
#rep = new Reporter()
#gen = new Generator()
#exp = new Experimentor()

expParams = "expParamaters.json"

def Controller():
	# Read in our experimental parameters
	json_data = json.load(open(expParams))
	params = json_data["Parameters"]
	
	num_models = int(params["num_models"])
	
	for i in range(num_models):
		#model = Optimizer.getModel()
		print(i)




if __name__ == "__main__":
	Controller()
