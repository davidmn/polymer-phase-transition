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
sim_files = sorted(os.listdir(sim_path))
obs_files = sorted(os.listdir(obs_path))
#print obs_files

#select which observed file to use
select = 2

#creates empty lists for the data
sim_temp = []
sim_thick = []
obs_temp = []
obs_thick =[]
chi_results = []

#print "using {} as simulation data".format(sim_files[0])
print "using {} as observed data".format(obs_files[select])

#open the observed data and fill the lists
#also converts observed temps into kelvin
with open((obs_path+obs_files[select]), 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ",", quotechar = "|")
	for row in reader:
		obs_temp.append(float(row[0])+273.0)
		obs_thick.append(float(row[1]))


for element in sim_files:
	sim_temp = []
	sim_thick = []
	#open the simulation data and fill the lists
	with open((sim_path+element), 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in reader:
			sim_temp.append(float(row[0]))
			sim_thick.append(float(row[1]))

	selected_temp = []
	selected_thick = []
	#chi square stuff
	for value in obs_temp:
		if value in sim_temp:
			selected_temp.append(value)
			selected_thick.append(sim_thick[obs_temp.index(value)])

	fudge_temp = []
	fudge_thick = []

	for value in selected_temp:
		if value in obs_temp:
			fudge_temp.append(value)
			fudge_thick.append(obs_thick[obs_temp.index(value)])

	#for i in range(len(fudge_temp)):
	#	print fudge_temp[i],fudge_thick[i], selected_thick[i]

	obs = numpy.array([fudge_thick]).T
	sim = numpy.array([selected_thick]).T
	thing = scipy.stats.chisquare(obs, f_exp=sim)
	#print element
	print thing[0][0], element
	chi_results.append(thing[0][0])
	#pl.clf()
	#pl.plot(selected_temp,sim)
	#pl.plot(selected_temp,obs)
	#pl.xlabel("Temperature (K)")
	#pl.ylabel("Thickness (nm)")
	#pl.savefig("/home/megaslippers/Projects/polymer-phase-transition/tests/"+str(thing[0][0])+"-"+element+".png")
	#print element
	#pl.clf()


result = chi_results.index(min(chi_results))
good_file = sim_files[result]

sim_temp = []
sim_thick = []

with open((sim_path+good_file), 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ",", quotechar = "|")
	for row in reader:
		sim_temp.append(float(row[0]))
		sim_thick.append(float(row[1]))

pl.plot(sim_temp,sim_thick)
pl.plot(obs_temp,obs_thick)
pl.xlabel("Temperature (K)")
pl.ylabel("Thickness (nm)")
pl.show()
pl.clf()