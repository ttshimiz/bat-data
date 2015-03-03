'''
Script to compare the 3 different methods for determining the which WISE fluxes to use for our
sample. The 3 different methods are 1.) exclusively using the extended flag, if the flag is 
> 0 then use the elliptical aperture, 2.) using the chi-square of the profile fitting of each
band, if chi-square > 3 then use the elliptical aperture, or 3.) use the elliptical aperture only
if it gives a greater flux than the profile fitting.

This script will compare the the WISE fluxes from each of the three methods to the IRAS
12 and 22 micron fluxes we have. 

'''

from pylab import *
dir = '/Users/ttshimiz/Dropbox/Research/Thesis/'

#Upload the WISE fluxes from each of the three methods
method1 = genfromtxt(dir+'Other_surveys/WISE/allwise_bat_agn_fluxes_ext_flg.txt', dtype = None, delimiter = '\t', names = True)
w3_method1 = method1['W3']
w4_method1 = method1['W4']
method2 = genfromtxt(dir+'Other_surveys/WISE/allwise_bat_agn_fluxes_final.txt', dtype = None, delimiter = '\t', names = True)
w3_method2 = method2['W3']
w4_method2 = method2['W4']
method3 = genfromtxt(dir+'Other_surveys/WISE/allwise_bat_agn_fluxes_greater_flux.txt', dtype = None, delimiter = '\t', names = True)
w3_method3 = method3['W3']
w4_method3 = method3['W4']

#Upload the IRAS fluxes
execfile(dir+'scripts/upload_bat_ir_database.py')

#Plot the distribution of W3/IRAS12 and W4/IRAS25 for each method
index_12 = isfinite(w3_method1) & (iras_12 != 0)
index_22 = isfinite(w4_method1) & (iras_25 != 0)

figure(1)
hist(w3_method1[index_12]/iras_12[index_12], bins = 20, histtype = 'step', color = 'b', lw = 2, label = 'Method 1')
hist(w3_method2[index_12]/iras_12[index_12], bins = 20, histtype = 'step', color = 'r', lw = 2, label = 'Method 2')
hist(w3_method3[index_12]/iras_12[index_12], bins = 20, histtype = 'step', color = 'k', lw = 2, label = 'Method 3')
xlabel('W3/IRAS12')
legend()

figure(2)
hist(w4_method1[index_22]/iras_25[index_22], bins = 20, histtype = 'step', color = 'b', lw = 2, label = 'Method 1')
hist(w4_method2[index_22]/iras_25[index_22], bins = 20, histtype = 'step', color = 'r', lw = 2, label = 'Method 2')
hist(w4_method3[index_22]/iras_25[index_22], bins = 20, histtype = 'step', color = 'k', lw = 2, label = 'Method 3')
xlabel('W4/IRAS25')
legend()

show()

#Calculate the statistics for each method and band
print 'Method 1:'
print '\t W3/IRAS12 mean = '+str(mean(w3_method1[index_12]/iras_12[index_12]))
print '\t W3/IRAS12 median = '+str(median(w3_method1[index_12]/iras_12[index_12]))
print '\t W3/IRAS12 stddev = '+str(std(w3_method1[index_12]/iras_12[index_12]))
print ''
print '\t W4/IRAS25 mean = '+str(mean(w4_method1[index_22]/iras_25[index_22]))
print '\t W4/IRAS25 median = '+str(median(w4_method1[index_22]/iras_25[index_22]))
print '\t W4/IRAS25 stddev = '+str(std(w4_method1[index_22]/iras_25[index_22]))
print ''
print ''
print 'Method 2:'
print '\t W3/IRAS12 mean = '+str(mean(w3_method2[index_12]/iras_12[index_12]))
print '\t W3/IRAS12 median = '+str(median(w3_method2[index_12]/iras_12[index_12]))
print '\t W3/IRAS12 stddev = '+str(std(w3_method2[index_12]/iras_12[index_12]))
print ''
print '\t W4/IRAS25 mean = '+str(mean(w4_method2[index_22]/iras_25[index_22]))
print '\t W4/IRAS25 median = '+str(median(w4_method2[index_22]/iras_25[index_22]))
print '\t W4/IRAS25 stddev = '+str(std(w4_method2[index_22]/iras_25[index_22]))
print ''
print ''
print 'Method 3:'
print '\t W3/IRAS12 mean = '+str(mean(w3_method3[index_12]/iras_12[index_12]))
print '\t W3/IRAS12 median = '+str(median(w3_method3[index_12]/iras_12[index_12]))
print '\t W3/IRAS12 stddev = '+str(std(w3_method3[index_12]/iras_12[index_12]))
print ''
print '\t W4/IRAS25 mean = '+str(mean(w4_method3[index_22]/iras_25[index_22]))
print '\t W4/IRAS25 median = '+str(median(w4_method3[index_22]/iras_25[index_22]))
print '\t W4/IRAS25 stddev = '+str(std(w4_method3[index_22]/iras_25[index_22]))
print ''
print ''