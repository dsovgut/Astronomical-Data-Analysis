# -*- coding: utf-8 -*-
"""
Created on Sun Mar 08 17:13:10 2020

@author: Danylo
"""
import numpy as np
import matplotlib.pyplot as plt

from astropy.cosmology import LambdaCDM
from astropy.table import Table
from astropy.io import ascii
from astropy import units as u
from astropy.io import fits
from matplotlib.gridspec import GridSpec

lab = fits.open('labdata.fits')
data = Table(lab[1].data)
data2 = Table(lab[1].data)
data2.remove_column('REDSHIFT')
data2['name'] = np.arange(len(data))
search = data2[('name','RA','DEC')]

ascii.write(data, 'data.txt', overwrite = True)
ascii.write(search, 'data2.txt', overwrite = True)
file = ascii.read('stars.csv')
X = LambdaCDM (H0=70 * u.km / u.s / u.Mpc, Om0=0.3, Ode0=0.7)
i1 = 0
while i1 < len(data2):
    if data2['name'][i1] not in file['NAME']:
        data.remove_row(i1)
    i1+=1
    
Lum = []
MAGN = []
absMag = []
for i in data["REDSHIFT"]:
    Lum.append(X.luminosity_distance(i))
for i in Lum:
    MAGN.append((5*np.log10(i/(10 * u.pc))))
for mag, dist_mod in zip(file['modelMag_i'], MAGN):
    absMag.append(mag - dist_mod.value)
#%%
RA = data['RA']
DECL = data['DEC']

def projection(RA, DECL, proj = 'aitoff', org = 0, facecolor = 'white', mcolor = 'b', alpha = 0.3, title = ''):
    RA = np.remainder(RA+360-org,360) 
    RA[RA>180] -=360    
    RA=-RA    
    ticks1 = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
    ticks1 = np.remainder(ticks1+360+org,360)
    labels =[]
    for label in ticks1: 
        labels.append(str(int(label*(1/15))) + '$^h$')  
    fig = plt.figure(figsize=(8,4.2))
    ax = fig.add_subplot(111, projection= proj, facecolor = facecolor)
    plt.plot(np.radians(RA),np.radians(DECL), 'o', color = mcolor , markersize=5, alpha=0.5)  
    ax.set_title(title, y=1.08, fontsize = 14)        
    ax.set_xticklabels(labels, visible = True)
    ax.set_xlabel("RA")
    ax.xaxis.label.set_fontsize(15)
    ax.set_ylabel("Dec")
    ax.yaxis.label.set_fontsize(15)
    ax.grid(True)
    return fig

projection(RA, DECL, org = 120, facecolor = 'white', mcolor = 'darkcyan', alpha = 0.5).savefig('Quasar.png', dpi=300)
#%%
fig=plt.figure(figsize=(8,8))
gs=GridSpec(6,6) 
ax1=fig.add_subplot(gs[0:5:,0]) 
ax2=fig.add_subplot(gs[5,1:6])
ax3=fig.add_subplot(gs[0:5, 1:6])

ax3.plot(data['REDSHIFT'], absMag, 'o', color = 'black', markersize=5, alpha=0.3)
ax2.hist(data['REDSHIFT'], bins = 75, color = 'black', alpha=0.3, histtype='step', ec='black')
ax1.hist(absMag, bins = 50, orientation = 'horizontal', alpha=0.5, histtype='step', ec='black')

ax3.invert_yaxis()
ax1.invert_yaxis()
plt.title('Redshift vs Absolute Magnitude', y=1.02,fontsize = 20)
ax1.set_xlabel('N',fontsize = 17)
ax1.set_ylabel('$M_{i}$', fontsize = 17)
ax2.set_xlabel('Redshift (z)', fontsize = 17)
ax3.grid(which ='both')

ax1.xaxis.tick_top()
ax2.yaxis.tick_right()

x_major_ticks = np.arange(0,5.25, 1)
x_minor_ticks = np.arange(0,5.25, 0.2)

y_major_ticks = np.arange(-31., -21.75, 1)
y_minor_ticks = np.arange(-31, -21.75, 0.2)

ax1.set_ylim(-22, -30)
ax3.set_ylim(-22, -30)

ax2.set_xlim(0, 5)
ax3.set_xlim(0, 5)

ax2.set_ylim(0,45)
ax1.set_xlim(0,50)

ax1.set_xlim(0,60)
ax2.set_ylim(0,50)

ax1.tick_params(which = 'major', direction = 'inout', length = 12)
ax1.tick_params(which = 'minor', direction = 'inout', length = 6) 

ax2.tick_params(which = 'major', direction = 'inout', length = 12)
ax2.tick_params(which = 'minor', direction = 'inout', length = 6)

ax3.tick_params(which = 'major', direction = 'inout', length = 24)
ax3.tick_params(which = 'minor', direction = 'inout', length = 6)

ax2.set_xticks(x_major_ticks)
ax2.set_xticks(x_minor_ticks, minor=True)

ax1.set_yticks(y_major_ticks)
ax1.set_yticks(y_minor_ticks, minor=True)

ax2.set_xticks(x_major_ticks)
ax2.set_xticks(x_minor_ticks, minor=True)

ax3.set_yticks(y_major_ticks)
ax3.set_yticks(y_minor_ticks, minor=True)

ax3.set_xticks(x_major_ticks)
ax3.set_xticks(x_minor_ticks, minor=True)

xticklabels = ax3.get_xticklabels()
plt.setp(xticklabels, visible=False)

yticklabels = ax3.get_yticklabels()
plt.setp(yticklabels, visible=False)
plt.tight_layout(pad=0, w_pad=-1.8, h_pad=-2.2)
fig.savefig('RvsA.png', dpi=300)
