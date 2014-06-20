#!/usr/bin/env python
import numpy

class system(object):
	"""object representing the entire system, composed of multiple layer objects"""
	def __init__(self, arg):
		super(system, self).__init__()
		self.arg = arg
		pass

class layer(object):
	"""object representing a single layer"""
	def __init__(self, arg):
		super(layer, self).__init__()
		self.arg = arg
		

system = system(True)
		
	
