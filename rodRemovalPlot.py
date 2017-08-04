#!/usr/bin/env python3
# makes a plot for the control rod removal transient
# note: you need to comment out the header on the csv file
import matplotlib.pyplot as pl
from matplotlib import rc
import numpy as np

# directory with output data:
outdir = ('/home/gavin/projects/moltres/problems/'
          'publication_level_cases/twod_control_rod_yank/')

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

# make da plot
fig, ax = pl.subplots(figsize=(6, 4))
ax.set_title('Rod position and power level over time')
ax.set_ylabel('Average nuclear power (W/cm$^3$)', color='r')
ax.set_xlabel('Time (s)')
ax.plot(data[:, colname2col['time']],
        data[:, colname2col['average_fission_heat']], 'r-*')
ax.set_xlim([0.0, 30.0])
ax2 = ax.twinx()  # separate y scales
ax2.set_ylabel('Rod position (cm)', color='b')
ax2.plot(data[:, colname2col['time']],
         data[:, colname2col['rodPosition']], 'b-*')
ax2.set_xlim([0.0, 30.0])
fig.savefig('rodJerk.png')
