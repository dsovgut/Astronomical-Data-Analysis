# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:07:53 2020

@author: Danya
"""

import numpy as np
from astropy.io import fits
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt

#open the fits files
bias = fits.open('D_n20131112t1127_c13_r1472p01_biascor.fits')
flat = fits.open('D_n20131112t1127_r_c13_r1472p01_dflatcor.fits')
data = fits.open('DECam_00380036_09.fits')


files = [flat, data, bias]
filename = ['flat', 'data', 'bias']
colors = ['red','blue', 'green']
alpha = [0.9, 0.5, 1]
colors2 = ['gray', 'k', 'b']

#display the images 
for x, y in zip(files, filename):
    fig = plt.figure()
    plt.imshow(x[0].data, cmap = 'gist_gray', norm = LogNorm())
    cbar = plt.colorbar()
    #cbar.ax.set_ytickables()
    plt.title(("%s%s" % (y[0].upper(), y[1:])) + ' Frame')
    fig.savefig(("%s%s" % (y[0].upper(), y[1:]))+ ' image.png')

#normalization
def normalize(p):
    return (p-np.min(p))/(np.max(p)-np.min(p))

files_1 = []
for f1 in files:
    files_1.append(f1[0].data.flat)

#    return v/np.max(v)
files = files_1
files_1 = []
for f in files:
    files_1.append(normalize(f))
files = files_1

#plot the histogram
nbins = 250
fig = plt.figure(figsize = (11, 6))
for x, y, z, d, c in zip(files, filename, colors, alpha, colors2):
    plt.hist(x, nbins, log = True, color = z, alpha = d, ec= c, label = y)
plt.title('Histograms of Pixel Values', fontsize = 20)
plt.xlabel('Normalized Pixels of Data, Bias, and Flat Frames')
plt.xlim(0,1)
plt.ylabel('Logscale Pixels')
plt.text(0.90, 10**5.0, 'Nbins = ' + str(nbins))
plt.legend()
plt.savefig('hw8_histogram.png')
