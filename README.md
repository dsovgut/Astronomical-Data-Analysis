# Astronomical-Data-Analysis
These codes were written for the UIUC Astronomical Techniques class. There is a diverse toolset that could be used to analyze astronomical images, make visualizations, and analyze data. Below are the description and output for each program:  

## 1. Electromagnetic Spectrum
This code generates the following plot of the electromagnetic spectrum.  
<img width="791" alt="Electromagnetic-Spectrum-plot" src="https://user-images.githubusercontent.com/35746740/95646372-5ead1500-0a8d-11eb-853a-20c10c9236b1.png">

## 2. Reduced Chi-Squared Test
Code generating Gaussian distribution with 100 samples with mean = 10 and a standard deviation of 2; calculation of Poisson counting error for each bin; calculation of reduced Chi squared test from the central 10 bins at the peak of the distribution. This code generates the following two plots: 

![HW2-1](https://user-images.githubusercontent.com/35746740/95646496-9cf70400-0a8e-11eb-96f6-c04dce6441d2.png)

![HW2-2](https://user-images.githubusercontent.com/35746740/95646498-a1232180-0a8e-11eb-935e-3bcce07fc875.png)

## 3. Monte Carlo Simulation
This is a Monte Carlo program generating 100 randomly placed supernovae within a given volume. The program generates the true distances, d, to the supernovae and then calculates the mean distance for the supernova. 
Assuming that each supernovae has a brightness governed by M = -19 +G(1) where G(1) is a random number with Gaussian distribution and standard deviation of one magnitude, it calculates the apparent magnitude of each supernovae using the distance generated in part. If m>20, the program rejects the sample as too faint. The plot of magnitude for the distance of all supernovae is shown below. Also displayed on the plot: the average magnitude of the original and detected sample, calculated velocity from the Hubble's law.
