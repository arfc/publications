#!/usr/bin/env python3
# makes a plot for the flow loss case
# note: you need to comment out the header on the csv file
import matplotlib.pyplot as pl
from matplotlib import rc
import numpy as np

# directory with output data:
outdir = ('/home/gav/projects/moltres/problems/'
          'LOFA/')

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

fig, ax = pl.subplots( figsize=(6,4))
ax.set_title('Power and salt flow velocity in core versus time')
ax.set_xlabel('Time (s)')
ax2 = ax.twinx()
ax.set_ylabel('Salt flow velocity (cm/s)', color='b')
ax2.set_ylabel('Average nuclear power (W/cm$^3$)', color='r')
def flowRate(t):
    """ gives fixed flow rate as a function of time
    notice that it depends on pump coastdown time constant, so
    be sure to change that if needed. right now, it's set to 5s """
    tau = 5.0
    return 21.7 * np.exp(-t/tau)
ax.plot(data[:,0], data[:,1], 'r-*')
ax2.plot(data[:,0], flowRate(data[:,0]), 'b-*')

fig.savefig('pumpFail.png')
