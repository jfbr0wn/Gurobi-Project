
class model_paramaters:

	def __init__(self, model): # First time declaration,
		self.model = model # Store the model 
		self.model.parameter = 0  # for any paramater give its default


	def AdjnameofParamater(self):
		self.model.paramater = 1 # Increement paramater


	# For binary parameters just increment upwards (or downwards via a python list Google for this informat)

	# FOr numerical parameters increment upwards by a factor of ten

	# Any information that needs to be stored needs to have a self tag aka self.paramaterxyz_value = 5000

	# Pass self in every function def functionname(self):