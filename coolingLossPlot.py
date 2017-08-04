#!/usr/bin/env python3
# makes a plot for the cooling loss case
# note: you need to comment out the header on the csv file
import matplotlib.pyplot as pl
from matplotlib import rc
import numpy as np

# directory with output data:
outdir = ('/home/gav/projects/moltres/problems/'
          'publication_level_cases/LOSCA/HXFail/')

data = np.loadtxt(outdir+'out.csv', delimiter=',')

# get colnames:
with open(outdir+'out.csv') as fh:
    line1 = fh.readline().rstrip()
colnames = line1[1:].split(sep=',')
print("Found these data columns:")
print(colnames)

# maps colnames to column index
colname2col = dict(zip(colnames, range(len(colnames))))

# latex
rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica'], 'size': 20})
rc('text', usetex=True)
pl.style.use('ggplot')  # mwahaha, now people think i know R

tmax = 200.0
fig, ax = pl.subplots( figsize=(6,4))
ax.set_title('Power and temperatures in core')
ax.set_xlabel('Time (s)')
ax2 = ax.twinx()
ax.set_ylabel('Temperature (K)', color='b')
ax2.set_ylabel('Average nuclear power (W/cm$^3$)', color='r')
for a in [ax, ax2]:
    a.set_xlim([0,tmax])
ax.plot(data[:,0], data[:,1], 'r-*')
ax2.plot(data[:,0], data[:,2], 'b-*', data[:,0], data[:,3], 'g-*')
ax2.legend(['Inlet Mean Temp.', 'Fuel Average Temp.'])

fig.savefig('coolingLoss.png')
