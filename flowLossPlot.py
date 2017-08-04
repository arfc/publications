#!/usr/bin/env python3
# makes a plot for the flow loss plot
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
