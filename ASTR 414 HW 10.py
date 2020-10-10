# -*- coding: utf-8 -
"""
Created on Sat Apr 20 11:36:02 2020

@author: Danylo-Sovgut
"""
from astropy.io import fits
import matplotlib.pyplot as plt
from astropy.nddata import Cutout2D
from matplotlib_scalebar.scalebar import IMPERIAL_LENGTH
from matplotlib_scalebar.scalebar import ScaleBar

fig = plt.figure()
DES_image = fits.open('Reduced DES image.fits')
data = DES_image[0].data
fig = plt.figure(figsize = (10,10))

size = (230, 230)
position = (1132, 2225)
shape = Cutout2D(data, position, size)
scalebar = ScaleBar(0.26, 'in', IMPERIAL_LENGTH)
plt.gca().add_artist(scalebar)
plt.imshow(shape.data, vmin=250, vmax=900, cmap = 'gray')
plt.title('Image Stamp')
bbox_props = dict(boxstyle="larrow", fc="white", ec="None", lw=-5)

t = plt.text(135, 140, "         Target         ", ha="center", va="center", rotation=(-50), size=10, bbox=bbox_props)
plt.savefig('Image Stamp.jpeg', dpi=300)

