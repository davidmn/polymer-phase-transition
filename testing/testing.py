#!/usr/bin/env python
import numpy
import pylab as pl

class System(object):
	"""object representing the entire system, composed of multiple layer objects"""
	def __init__(self,tot_thickness,layers,init_temp,final_temp,temp_inc,alpha_g,alpha_a,sim_start,sim_end):
		self.alpha_a = alpha_a #amorphous phase expansion coefficient
		self.alpha_g = alpha_g #glass phase expansion coefficient
		self.tot_thickness = tot_thickness #total thickness of sample
		self.num_layers = layers #number of layers in sample
		self.layer_thickness = self.tot_thickness / self.num_layers #initial thickness of each sample
		self.temp = sim_start # starting temp for sample
		self.init_temp = init_temp # phase start
		self.final_temp = final_temp # phase end
		self.sim_start = sim_start #star of sim
		self.sim_end = sim_end #end of sim
		self.temp_inc = temp_inc #amount to incremement temperature by
		self.layer = []
		for i in range(self.num_layers): #populate the array self.layer with object of class Layer()
			obj = Layer(self.layer_thickness)
			self.layer.append(obj)
		self.critical_temps()
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
			element.expand(self.temp_inc,self.temp)
		pass


class Layer(object):
	"""object representing a single layer"""
	def __init__(self,layer_thickness):
		self.thickness = layer_thickness
		self.coefficient = alpha_g
		self.critical_temp = 0.0
		pass

	def expand(self,incremement,temp):
		self.change_phase(temp)
		change = self.thickness * self.coefficient * incremement
		self.thickness = self.thickness + change
		pass

	def change_phase(self,temp):
		if temp > self.critical_temp:
			self.coefficient = alpha_a
		pass
		
alpha_g = 2.5641e-2 #nm/k
alpha_a = 8.2957e-2 #nm/k
sample_thickness = 300.0 #nm
num_layers = 300
sim_start = 200.0
start_temp = 290.0 #k
end_temp = 330.0 #k
sim_end = 350.0
incremement = 0.5 #k
sample = System(sample_thickness,num_layers,start_temp,end_temp,incremement,alpha_a,alpha_g,sim_start,sim_end)
data = []
T = []

data.append(sample.measure_thickness())
T.append(sample.temp)

while (sample.temp < sim_end ):
	sample.expand_all()
	data.append(sample.measure_thickness())
	T.append(sample.temp)

#for i in range(1000):
#	sample.expand_all()
#	data.append(sample.measure_thickness())
#	T.append(sample.temp)

#for i in range(15000):
#	print T[i], data[i]

pl.plot(T,data)
pl.show()

