# -*- coding: utf-8 -*-

import numpy as np
from astropy.io import fits

import matplotlib.pyplot as plt
from astropy.io.fits import getheader
from astropy.wcs import WCS


main = 'DECam_00380036_09.fits'
bias1 = fits.open('D_n20131112t1127_c13_r1472p01_biascor.fits')
flat1 = fits.open('D_n20131112t1127_r_c13_r1472p01_dflatcor.fits')
data1 = fits.open(main)

bias = bias1[0].data
flat = flat1[0].data
data = data1[0].data
header = getheader(main)
#%%

trimsecA=data[50:4146, 1080:2104]
trimsecB=data[50:4146, 56:1080]

overscanB=data[50:4146, 6:55]
overscanA=data[50:4146, 2105:2154]
#%%
data2 = []
for i in range(len(overscanA)):
    ampA = (trimsecA[i] - np.median(overscanA[i]))
    ampB = (trimsecB[i] - np.median(overscanB[i]))
    rows = np.append(ampB, ampA)
    data2.append(rows)
#%%
w = WCS(main)
x, y = w.all_world2pix(header['CRVAL1'], header['CRVAL2'], 1)
x2, y2 = w.all_world2pix(header['CRVAL1']+1, header['CRVAL2']+1, 1)     
#%%
NAXIS1 = header['naxis1']
NAXIS2 = header['naxis2']
x = np.arange(NAXIS1)
y = np.arange(NAXIS2)
X, Y = np.meshgrid(x, y)
ra, dec = w.wcs_pix2world(X, Y, 0)
#%%
final = (data2 - bias)/flat
fig = plt.figure(figsize = (3.2,5))

plt.imshow(final, vmin=250, vmax=900, cmap='gray')
plt.colorbar()
plt.title('Reduced DES Image')
plt.savefig('Reduced DES image.jpg', dpi=300)
#%%
header = getheader(main)
fits.writeto('Reduced DES image.fits',final, header, overwrite = True)
newFits = fits.open('Reduced DES image.fits')
#%%
files = [bias1, flat1, data1, newFits]
for f in files:
    f.close()
