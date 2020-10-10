# -*- coding: utf-8 -*-

from astropy.io import ascii
from astropy import units as u 
import matplotlib.pyplot as plt

NIR_MIR  = ascii.read("mktrans_zm_10_10.dat.txt")
f089m = ascii.read("filters/f098m.IR.tab.txt")
f105w = ascii.read("filters/f105w.IR.tab.txt")
f110w = ascii.read("filters/f110w.IR.tab.txt")
f125w = ascii.read("filters/f125w.IR.tab.txt")
f140w = ascii.read("filters/f140w.IR.tab.txt")
f160w = ascii.read("filters/f160w.IR.tab.txt")



col1 = (NIR_MIR['col1'] * u.micron) #wavelength from Mauna Kea
col2 = (NIR_MIR['col2']) #transmission from Mauna Kea

wavelength = []
transmission = []
for i in range(len(col1)):
    if col1[i].value>=0.9 and col1[i].value<=2.7:
        wavelength.append((col1[i].to(u.AA)).value)
        transmission.append(col2[i])
        
all_wv = []
all_wv.append(wavelength)
all_tr = []
all_tr.append(transmission)
all_filters = [f089m, f105w, f110w, f125w, f140w, f160w]
colors = ['green', 'red', 'orange', 'yellow', 'blue', 'indigo', 'violet']

all_names = ['Atmospheric Transmission at Mauna Kea', 'Filter: f089m', 'Filter: f105w', 'Filter: f110w', 'Filter: f125w', 'Filter: f140w','Filter: f160w']
for value in all_filters:
     all_wv.append(value['col2'])
     all_tr.append(value['col3'])

for i in range(len(all_wv)):
    plt.plot(all_wv[i], all_tr[i], color = colors[i], label = all_names[i])
    
plt.xlim(8500, 27000)
plt.legend(bbox_to_anchor = (0.7, -0.5), loc = 0)
plt.title('IR Wavelength vs Transmission')
plt.xlabel('IR Wavelength (Å)')
plt.ylabel('Transmission')