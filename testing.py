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
		self.delt_T = self.critical_temps()
		for i in range(self.num_layers): #populate the array self.layer with object of class Layer()
			obj = Layer(self.layer_thickness)
			self.layer.append(obj)
		for element in self.layer:
			element.critical_temp = start_temp + self.delt_T
			print element.critical_temp
			pass
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
		temp_interval = temp_range / self.num_layers
		return temp_interval
		pass

class Layer(object):
	"""object representing a single layer"""
	def __init__(self,layer_thickness):
		self.thickness = layer_thickness
		self.coefficient = alpha_g
		self.critical_temp = 0.0
		pass
		
alpha_g = 2.5641e-2 #nm/k
alpha_a = 8.2957e-2 #nm/k
sample_thickness = 300.0 #nm
num_layers = 300
start_temp = 290.0 #k
end_temp = 330.0 #k
incremement = 0.005 #k
sample = System(sample_thickness,num_layers,start_temp,end_temp,incremement,alpha_a,alpha_g)		
	
