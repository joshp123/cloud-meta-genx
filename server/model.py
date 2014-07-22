'''meta_genx MODEL (MVC) (View is bootstrap, Controller is flask)
 j.palmer 2k14 
 lets get meta programming!
'''

from genx import data, model, parameters, diffev

class MetaGenx(object):
	"""wrapper class for genx to automate stuff, and expose a simple API for scaling in the cloud"""
	def __init__(self, dotgxfile=None):
		super(MetaGenx, self).__init__()

		# i'm gonna use C# style variables for all my stuff cos its way nicer than python haha

		self.dotgxfile = dotgxfile

		# initialising the class with filename is optional.

class ModelParameters(object):
	"""docstring for ModelParameters"""
	def __init__(self, arg):
		super(ModelParameters, self).__init__()
		self.arg = arg
		

	def LoadFromFile():
		'''

		'''
		pass

	python reflection

	def ExposeSubClasses(filter)

	def ExposeParameters(method)

	def GetModelParams():
		pass

	def ExposeMutationSchemes():
		pass

	def ExposeConfiguration():
		pass

	def SetUp():
		# get the logs

		# default config

		#
		pass

		# We take the .gx file that's already been created as an argument.

        self.Solver = diffev.DiffEv()
        self.Solver.model.load(path)
        self.Solver.pickle_load(self.Solver.model.load_addition('optimizer'))



		