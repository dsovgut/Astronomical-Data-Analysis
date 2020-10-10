#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from astropy.io import fits

image_file= "/Users/Danya/Desktop/HW8-ASTR414/DESJ053816.9-503050.8_r.fits"
hbu_list = fits.open(image_file)
hbu_list.info()


# In[5]:


image_data = hbu_list[0].data
print('Min:', np.min(image_data[465:665, 480:680]))
print('Max:', np.max(image_data[465:665, 480:680]))
print('Mean:', np.mean(image_data[465:665, 480:680]))
print('Stdev:', np.std(image_data[465:665, 480:680]))


# In[21]:


from matplotlib.colors import LogNorm
plt.imshow(image_data[465:665,480:680], cmap='gray', vmin=1, vmax=50, origin='lower')
cbar = plt.colorbar(ticks=[1,10,20,30,40,50])
plt.title('Original Image')
plt.savefig('og.png', dpi=300)


# In[22]:


from astropy.convolution import convolve, Box2DKernel
box_2D_kernel = Box2DKernel(3)
smoothed_data = convolve(image_data, box_2D_kernel)
plt.imshow(smoothed_data[465:665,480:680], cmap='gray', vmin=1, vmax=50, origin='lower')
cbar=plt.colorbar(ticks=[1,10,20,30,40,50])
plt.title('3x3 Pixel Smoothed Image')
plt.savefig('3x3.png', dpi=300)


# In[23]:


from astropy.convolution import convolve, Box2DKernel
box_2D_kernel = Box2DKernel(7)
smoothed_data = convolve(image_data, box_2D_kernel)
plt.imshow(smoothed_data[465:665,480:680], cmap='gray', vmin=1, vmax=50, origin='lower')
cbar=plt.colorbar(ticks=[1,10,20,30,40,50])
plt.title('7x7 Pixel Smoothed Image')
plt.savefig('7x7.png', dpi=300)


# In[24]:


from astropy.convolution import convolve, Box2DKernel
box_2D_kernel = Box2DKernel(11)
smoothed_data = convolve(image_data, box_2D_kernel)
plt.imshow(smoothed_data[465:665,480:680], cmap='gray', vmin=1, vmax=50, origin='lower')
cbar=plt.colorbar(ticks=[1,10,20,30,40,50])
plt.title('11x11 Pixel Smoothed Image')
plt.savefig('11x11.png', dpi=300)


# In[ ]:




