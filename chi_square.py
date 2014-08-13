import os
import csv
import pylab as pl

#change these to the directories/paths of simulation data and observed csv
sim_path = "/home/megaslippers/Projects/polymer-phase-transition/data/"
obs_path = "/home/megaslippers/Projects/polymer-phase-transition/results/csv/"

#lists the files in those paths
sim_files = os.listdir(sim_path)
obs_files = os.listdir(obs_path)

#creates empty lists for the data
sim_temp = []
sim_thick = []
obs_temp = []
obs_thick =[]

#open the simulation data and fill the lists
with open((sim_path+sim_files[0]), 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		sim_temp.append(float(row[0]))
		sim_thick.append(float(row[1]))

#open the observed data and fill the lists
#also converts observed temps into kelvin
with open((obs_path+obs_files[0]), 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter = ",", quotechar = "|")
	for row in reader:
		obs_temp.append(float(row[0])+273.0)
		obs_thick.append(float(row[1]))

