# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import scipy.stats as scs

m = 10 # mean 
s = 2 # sigma
numb = 100 # number of samples
np.random.seed(12)
x = m + s * np.random.randn(numb)

width = 0.5
n, bin_edges, patches = plt.hist(x, bins = np.arange(min(x), max(x)+ width, width), density=1, facecolor='green')
bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])

y = scs.norm.pdf(bin_centers, m, s)
plt.plot(bin_centers, y, 'g--')

plt.errorbar(bin_centers, y, yerr = y-n, marker = '.', fmt='red')
#plt.errorbar(bin_centers, y, yerr = 1/np.sqrt(numb), marker = '.', fmt='red')


plt.xlabel('X')
plt.ylabel('Probability')

count = 0
count2=0
for observed in y[range(7,12)]:
    count +=((observed-m)/s)**2
    count2+=1

Chi_squared = count/(count2*numb)
plt.title('Gaussian Distribution, # of Samples = ' + str(numb))
plt.text(4,0.25,'Reduced Chi Squared:')
plt.text(4,0.22,0.243)

#str(reduced_Chi_squared)
plt.subplots_adjust(left=0.15)
plt.savefig('Astr414_HW2_plot1a.png', dpi=300)
plt.show()

#For 1M
plt.figure()
numb=10**6
np.random.seed(12)
x = m + s * np.random.randn(numb)

n, bin_edges, patches = plt.hist(x, bins = np.arange(min(x), max(x)+ width, width), density=1, facecolor='green')
bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])

y = scs.norm.pdf(bin_centers, m, s)
plt.plot(bin_centers, y, 'g--')

plt.errorbar(bin_centers, y, yerr = y-n, marker = '.', fmt='red')


plt.xlabel('X')
plt.ylabel('Probability')

count = 0
count2=0
for observed in y[range(7,12)]:
    count +=((observed-m)/s)**2
    count2+=1

Chi_squared = count/(count2*numb)
plt.title('Gaussian Distribution, # of Samples = ' + str(numb))
plt.text(0,0.18,'Reduced Chi Squared:')
plt.text(0,0.15,2.495)

plt.subplots_adjust(left=0.15)
plt.show()
