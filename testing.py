#!/usr/bin/env python
import numpy as np
import random

class System(object):
	"""object representing the entire system, composed of multiple layer objects"""
	def __init__(self,tot_thickness,layers,init_temp):
		self.tot_thickness = tot_thickness #total thickness of sample
		self.num_layers = layers #number of layers in sample
		self.layer_thickness = self.tot_thickness / self.num_layers #initial thickness of each sample
		self.temp = init_temp #initial temperature
		self.layer = np.empty((self.num_layers), dtype=object) #create an array for the layers
		for element in self.layer: #populate the array self.layer with object of class layer()
			element = Layer(layer_thickness,)
		pass

class Layer(object):
	"""object representing a single layer"""
	def __init__(self):
		pass
		

system = system(300,300,290)
		
	
