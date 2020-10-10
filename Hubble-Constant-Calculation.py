# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pylab

def truedist():
    rad = (np.random.uniform(low=0, high = 1, size = 100))
    true_d = []
    for value in rad:
        true_d.append(((8*value)**(1/3))*10**3)
    return true_d
    
true_d = truedist()
m = []
abs_magnitudes = np.random.normal(-19, 1, 100) 
for i in range(len(true_d)):
    m.append(5*np.log10(true_d[i]*10**5)+abs_magnitudes[i])

app_mags = []
dist = []
for i in range(len(true_d)):
    if m[i]<=20:
        app_mags.append(m[i])
        dist.append(true_d[i])

x = len(app_mags)

print("Original Average Apparent Magnitude: " + str(np.average(m)))
print("Detected Average Apparent Magnitude: " + str(np.average(app_mags)))
print("Number of Detected Supernovas: " + str(x))

obs_d = []
velocity = []
tv = []

for i in obs_d:
    velocity.append(72*i)  
for i in dist:
    tv.append(72*i)
for i in app_mags:
    obs_d.append((10**(((i+19)/5)+1))*10**-6)
    


(m,b) = pylab.polyfit(dist, tv,1)
yp1 = pylab.polyval([m,b],dist)
plt.plot(dist,yp1, label= 'True Distance vs Velocity')

plt.scatter(dist, tv)

(m2,b2) = pylab.polyfit(obs_d, tv,1)
yp2 = pylab.polyval([m2,b2],obs_d)
plt.plot(obs_d,yp2,label = 'Observed Distance vs Velocity')



plt.text(400, 90000, "H0 = " + str(m2))
plt.scatter(obs_d, tv)
plt.title('Distance (Mpc) vs Velocity')
plt.xlabel('Distance (Mpc)')
plt.ylabel('Velocity')
plt.errorbar(obs_d, tv, yerr = np.abs(yp2-tv), fmt = 'o')
plt.legend()

print("H0 = " + str(m2))




    
    
