#!/usr/bin/env python
import math
import numpy
import pylab as pl
import csv
from itertools import izip
from string import Template
import scipy

class System(object):
	"""object representing the entire system, composed of multiple layer objects"""
	def __init__(self,tot_thickness,layers,init_temp,final_temp,temp_inc,alpha_g,alpha_a,sim_start,sim_end):
		self.alpha_a = alpha_a #amorphous phase expansion coefficient
		self.alpha_g = alpha_g #glass phase expansion coefficient
		self.tot_thickness = tot_thickness #total thickness of sample
		self.num_layers = layers #number of layers in sample
		#print "number of layers ", self.num_layers
		#print "total thickness", self.tot_thickness
		self.layer_thickness = self.tot_thickness / self.num_layers #initial thickness of each sample
		#print "layer thickness ", self.layer_thickness
		self.temp = sim_start # starting temp for sample
		self.init_temp = init_temp # phase start
		self.final_temp = final_temp # phase end
		self.sim_start = sim_start #star of sim
		self.sim_end = sim_end #end of sim
		self.temp_inc = temp_inc #amount to incremement temperature by
		self.layer = []
		for i in range(self.num_layers): #populate the array self.layer with object of class Layer()
			obj = Layer(self.layer_thickness,self.sim_start	)
			self.layer.append(obj)
		self.critical_temps()
		pass

	def increase_temp(self): #method to increase system temperature
		self.temp = self.temp + self.temp_inc

		for element in self.layer:
			element.current_temp = element.current_temp + self.temp_inc

		pass

	def measure_thickness(self): #method to measure thickness of sample
		i = 0.0
		for element in self.layer:
			i = i + element.thickness
		return i


	def critical_temps(self):
		temp_range = self.final_temp - self.init_temp
		temp_interval = temp_range / self.num_layers
		var = self.init_temp
		for element in self.layer:
			element.critical_temp = var + temp_interval
			var = element.critical_temp
		pass

	def expand_all(self):
		self.increase_temp()
		for element in self.layer:
			element.expand(self.temp_inc)
		pass


class Layer(object):
	"""object representing a single layer"""
	def __init__(self,layer_thickness,init_temp):
		self.init_temp = init_temp
		self.current_temp = init_temp
		self.thickness = layer_thickness
		self.init_thickness = layer_thickness
		self.coefficient = alpha_g
		self.critical_temp = 0.0
		pass

	def expand(self,incremement):
		self.change_phase()
		change = self.coefficient * incremement
		#self.thickness = self.init_thickness + (self.coefficient * (self.current_temp - self.init_temp))
		self.thickness = self.thickness + change
		pass

	def change_phase(self):
		a = self.coefficient
		if self.current_temp > self.critical_temp:
			self.coefficient = alpha_a
		b = self.coefficient

		if a != b:
			self.init_temp = self.current_temp

		#if phase changed, set self.init_temp = self.current_temp THEN DON'T DO IT AGAIN
		pass

num_layers = 50
alpha_g = 2.5641e-2 / num_layers #nm/k
alpha_a = 8.2957e-2 / num_layers #nm/k
sample_thickness = 277.0 #nm
sim_start = 230.0
start_temp = 235.0 #k
end_temp = 270.0 #k
sim_end = 320.0
incremement = 0.01 #k
sample = System(sample_thickness,num_layers,start_temp,end_temp,incremement,alpha_a,alpha_g,sim_start,sim_end)
data = []
T = []

def write_data(yesno):
	if yesno == True:
		with open("/home/megaslippers/Projects/polymer-phase-transition/data/"+name+".csv", 'wb') as f:
			writer = csv.writer(f)
			writer.writerows(izip(T, data))
		f.close()
	else:
		pass

def plot_save(T,data):
	pl.plot(T,data)
	pl.xlabel("Temperature (K)")
	pl.ylabel("Thickness (nm)")
	pl.savefig(("/home/megaslippers/Projects/polymer-phase-transition/figures/"+name+".png"))
	#pl.clf()
temp = end_temp
while start_temp <= 255.0:
	end_temp = temp
	while end_temp <= 305.0:
		sample = System(sample_thickness,num_layers,start_temp,end_temp,incremement,alpha_a,alpha_g,sim_start,sim_end)
	
		data.append(sample.measure_thickness())
		T.append(sample.temp)

		while (sample.temp < sim_end ):
			sample.expand_all()
			data.append(sample.measure_thickness())
			T.append(sample.temp)

		filename = Template("$layers-$phasestart-$phaseend-$incremement")
		name = filename.substitute(layers=num_layers, phasestart=start_temp, phaseend=end_temp, incremement=incremement )

		write_data(True)

		plot_save(T,data)
		T = []
		data = []
		print start_temp, end_temp
		end_temp = end_temp + 5.0

	start_temp = start_temp + 5.0