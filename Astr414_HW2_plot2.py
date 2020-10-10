#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:55:59 2020
@author: Danya
"""
import numpy as np
import matplotlib.pyplot as plt


M=-19 #typical supernovae absolute magnitude
M_dif = 1 #scatter
m=20 #limiting magnitude of the telescope
d= 1000 #Mpc - how far supernovae can be seen
r = 2000 #Mpc - supernovae form in this radius 
H0 = 72 #72 km/s/Mpc - Hubble constant
n = 100 # number of randomly generated SN in radius r

#radius = np.random.uniform(0,1,100)*2000
#scale these into spherical distribution

radii = (np.random.uniform(low=0, high = 1, size = 100))
#scale them spherically
distances = []
for i in radii:
    distances.append(((i)**(1/3))*2000)

x = np.mean(distances)
print('a) the mean distance to the supernovae %s' %x)
    

#B
m = []
M = np.random.normal(-19, 1, 100) 
for i in range(len(distances)):
    m.append(5*np.log10((distances[i]*10**6)/10)+M[i])
    
new_mag = []
new_dist = []
for i in range(len(distances)):
    if m[i]<=20:
        new_mag.append(m[i])
        new_dist.append(distances[i])

x= len(new_dist)

print("Average Apparent Magnitude: " + str(np.average(m)))
print("Detected Average Apparent Magnitude: " + str(np.average(new_mag)))
print("Number of Detected Supernovas: " + str(x))

plt.scatter(new_dist, new_mag)
plt.gca().invert_yaxis()
plt.title('Distance (Mpc) vs Detected Apparent Magnitude')
plt.xlabel('Distance (Mpc)')
plt.ylabel('Apparent Magnitude')
plt.xlim(0, 2000)
plt.show()

plt.scatter(distances, m)
plt.gca().invert_yaxis()
plt.title('Distance (Mpc) vs Theoretical Apparent Magnitude')
plt.xlabel('Distance (Mpc)')
plt.ylabel('Apparent Magnitude')
plt.xlim(0, 2000)
plt.show()

#C
obs_d = []
for i in new_mag:
    obs_d.append((10**(((i+19)/5)+1))*10**(-6))
    
velocity = []
for i in obs_d:
    velocity.append(72*i)
    
plt.scatter(obs_d, velocity)
plt.title('Observed Distance (Mpc) vs Velocity')
plt.xlabel('Observed Distance (Mpc)')
plt.ylabel('Velocity')
plt.show()



