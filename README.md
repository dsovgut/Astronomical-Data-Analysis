# Astronomical Data Analysis
These codes were written for the UIUC Astronomical Techniques class. There is a diverse toolset that could be used to analyze astronomical images, make visualizations, and analyze data. Below are the descriptions and outputs for each program:  

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

![HW2-3](https://user-images.githubusercontent.com/35746740/95646596-bcdaf780-0a8f-11eb-9c7d-bf469117d592.png)

## 4.Hubble Constant Calculation
Using data simulated in the previous program (Monte Carlo Simulation), this program builds a trendline through all the detected points. This plot shows the level of bias in our observations.   
<img width="693" alt="Screen Shot 2020-10-10 at 00 31 35" src="https://user-images.githubusercontent.com/35746740/95646657-789c2700-0a90-11eb-9392-1d2e0ac14b41.png">

## Atmospheric Transmition Plot
This program uses data for the atmospheric transmission at Mauna Kea. I used the filter transmission curves from here:
http://quasar.astro.illinois.edu/teaching/ASTR414/filters/
Using the bands in the IR regime, we build the following plot: 
<img width="689" alt="Screen Shot 2020-10-10 at 00 39 32" src="https://user-images.githubusercontent.com/35746740/95646744-20195980-0a91-11eb-976a-eb9b2472ffa9.png">

## Optical Image Data
This program opens three fits files downloaded from the Dark Energy Survey. The images are of bias, flat, and data files. It calculates the range of pixels values for three image frames; 
![Combined-Frames](https://user-images.githubusercontent.com/35746740/95646888-78049000-0a92-11eb-97a6-f1428bfe4176.png)
It also plots historgram of the pixel values for each image data on a single plot that is normalized using logarithmic scaling for the x-axis: 
![Histogram](https://user-images.githubusercontent.com/35746740/95646894-8783d900-0a92-11eb-9fec-50ec0bfcd1cb.png)
Finally, the three frames and the histogram are used to generate the following reduced image:
![Reduced](https://user-images.githubusercontent.com/35746740/95647167-eb0e0680-0a92-11eb-938c-af50ba270f06.jpg)

## Boxcar Image Smoothing

We are using r-band image data (DESJ053816.9-503050.8_r.fits) from the following source:http://quasar.astro.illinois.edu/teaching/ASTR414/hw5-data.zip
The program loads the r-band fits image, applies a boxcar smoothing of the original image with a kernel size of (1) 3x3 pixels, 7x7 pixels, and 11x11 pixels. For each boxcarsmoothed full-frame images, the central 200x200 pixels are cut out. Boxcar smoothing is taking the arithmetic mean of all the pixel values in the N by N kernel window and assigns the mean to the central pixel; the operation
is applied to all pixels in the image. The original images as well as smoothed images that were output of the program shown below: 
![8-1](https://user-images.githubusercontent.com/35746740/95647311-15ac8f00-0a94-11eb-9364-160da617257e.png)
![8-2](https://user-images.githubusercontent.com/35746740/95647312-16ddbc00-0a94-11eb-9823-c6160cd42f5e.png)
![8-3](https://user-images.githubusercontent.com/35746740/95647313-16ddbc00-0a94-11eb-87a4-2d6425eb4d43.png)
![8-4](https://user-images.githubusercontent.com/35746740/95647314-17765280-0a94-11eb-8b0d-e949969b472b.png)


