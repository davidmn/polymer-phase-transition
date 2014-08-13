import os
import csv
import pylab as pl

mypath = "/home/megaslippers/Projects/polymer-phase-transition/data/"

files = os.listdir(mypath)

sim_temp = []
sim_thick = []

with open((mypath+files[0]), 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		sim_temp.append(row[0])
		sim_thick.append(row[1])

print len(sim_temp)
print len(sim_thick)

pl.plot(sim_temp,sim_thick)
pl.show()
