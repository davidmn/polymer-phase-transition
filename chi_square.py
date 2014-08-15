import os
import csv
import pylab as pl
import scipy.stats
import numpy
import random

#change these to the directories/paths of simulation data and observed csv
sim_path = "/home/megaslippers/Projects/polymer-phase-transition/data/"
obs_path = "/home/megaslippers/Projects/polymer-phase-transition/results/csv/"

#lists the files in those paths
sim_files = os.listdir(sim_path)
obs_files = sorted(os.listdir(obs_path))
#print obs_files

#select which observed file to use
select = 2

#creates empty lists for the data
sim_temp = []
sim_thick = []
obs_temp = []
obs_thick =[]

print "using {} as simulation data".format(sim_files[0])
print "using {} as observed data".format(obs_files[select])

#open the simulation data and fill the lists
with open((sim_path+sim_files[12]), 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		sim_temp.append(float(row[0]))
		sim_thick.append(float(row[1]))

#open the observed data and fill the lists
#also converts observed temps into kelvin
with open((obs_path+obs_files[select]), 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ",", quotechar = "|")
	for row in reader:
		obs_temp.append(float(row[0])+273.0)
		obs_thick.append(float(row[1]))

#chi square stuff
size = len(obs_temp)
selection = []
while len(selection) < size:
	element = random.randint(0,len(sim_temp)-1)
	if element not in selection:
		selection.append(element)
temp_temp = []
temp_thick = []
for element in selection:
		temp_temp.append(sim_temp[element])
		temp_thick.append(sim_thick[element])

obs = numpy.array([obs_temp,obs_thick]).T
sim = numpy.array([temp_temp,temp_thick]).T
print scipy.stats.chisquare(obs, f_exp=sim)

pl.plot(sim_temp,sim_thick)
pl.plot(obs_temp,obs_thick)
pl.xlabel("Temperature (K)")
pl.ylabel("Thickness (nm)")
pl.show()
pl.clf()