#!/usr/bin/env python
import numpy as np
import random

class System(object):
	"""object representing the entire system, composed of multiple layer objects"""
	def __init__(self,tot_thickness,layers,init_temp,final_temp,temp_inc,alpha_g,alpha_a):
		self.alpha_a = alpha_a #amorphous phase expansion coefficient
		self.alpha_g = alpha_g #glass phase expansion coefficient
		self.tot_thickness = tot_thickness #total thickness of sample
		self.num_layers = layers #number of layers in sample
		self.layer_thickness = self.tot_thickness / self.num_layers #initial thickness of each sample
		self.temp = init_temp #initial temperature
		self.final_temp = final_temp #final temperature
		self.temp_inc = temp_inc #amount to incremement temperature by
		self.layer = []
		#self.layer = np.empty((self.num_layers), dtype=object) #create an array for the layers
		for i in range(self.num_layers): #populate the array self.layer with object of class Layer()
			obj = Layer(self.layer_thickness)
			self.layer.append(obj)
		print "initialisation complete"
		pass

	def increase_temp(self): #method to increase system temperature
		self.temp = self.temp + self.temp_inc
		pass

	def measure_thickness(self): #method to measure thickness of sample
		i = 0.0
		for element in self.layer:
			i = i + element.thickness
		return i

	def critical_temps(self):
		temp_range = self.final_temp - self.temp
		
		pass

class Layer(object):
	"""object representing a single layer"""
	def __init__(self,layer_thickness):
		self.thickness = layer_thickness
		pass
		
alpha_g = 1.0
alpha_a = 1.0
sample = System(300.0,300,290.0,0.005,alpha_a,alpha_g)
sample.measure_thickness()
		
	
