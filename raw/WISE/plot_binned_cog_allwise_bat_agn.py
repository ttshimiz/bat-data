#Script to upload all of the AllWISE photometry and bin the curve of growth measurements by chi^2

from pylab import *

#Upload the AllWISE data
allwise_data = genfromtxt('/Users/ttshimiz/Dropbox/Research/Thesis/Other_surveys/WISE/wise_allwise_bat_agn.tbl', delimiter = '\t', names = True, dtype = None, missing_values = 'null', filling_values = 0)

#Photometric Measurements

#Profile-Fitting
w1mpro = allwise_data['w1mpro']
w1mpro_err = allwise_data['w1sigmpro']
w1rchi2 = allwise_data['w1rchi2']
w2mpro = allwise_data['w2mpro']
w2mpro_err = allwise_data['w2sigmpro']
w2rchi2 = allwise_data['w2rchi2']
w3mpro = allwise_data['w3mpro']
w3mpro_err = allwise_data['w3sigmpro']
w3rchi2 = allwise_data['w3rchi2']
w4mpro = allwise_data['w4mpro']
w4mpro_err = allwise_data['w4sigmpro']
w4rchi2 = allwise_data['w4rchi2']

#Curve of Growth
w1mag_1 = allwise_data['w1mag_1']
w1mag_1_err = allwise_data['w1sigm_1']
w1mag_2 = allwise_data['w1mag_2']
w1mag_2_err = allwise_data['w1sigm_2']
w1mag_3 = allwise_data['w1mag_3']
w1mag_3_err = allwise_data['w1sigm_3']
w1mag_4 = allwise_data['w1mag_4']
w1mag_4_err = allwise_data['w1sigm_4']
w1mag_5 = allwise_data['w1mag_5']
w1mag_5_err = allwise_data['w1sigm_5']
w1mag_6 = allwise_data['w1mag_6']
w1mag_6_err = allwise_data['w1sigm_6']
w1mag_7 = allwise_data['w1mag_7']
w1mag_7_err = allwise_data['w1sigm_7']
w1mag_8 = allwise_data['w1mag_8']
w1mag_8_err = allwise_data['w1sigm_8']

w2mag_1 = allwise_data['w2mag_1']
w2mag_1_err = allwise_data['w2sigm_1']
w2mag_2 = allwise_data['w2mag_2']
w2mag_2_err = allwise_data['w2sigm_2']
w2mag_3 = allwise_data['w2mag_3']
w2mag_3_err = allwise_data['w2sigm_3']
w2mag_4 = allwise_data['w2mag_4']
w2mag_4_err = allwise_data['w2sigm_4']
w2mag_5 = allwise_data['w2mag_5']
w2mag_5_err = allwise_data['w2sigm_5']
w2mag_6 = allwise_data['w2mag_6']
w2mag_6_err = allwise_data['w2sigm_6']
w2mag_7 = allwise_data['w2mag_7']
w2mag_7_err = allwise_data['w2sigm_7']
w2mag_8 = allwise_data['w2mag_8']
w2mag_8_err = allwise_data['w2sigm_8']

w3mag_1 = allwise_data['w3mag_1']
w3mag_1_err = allwise_data['w3sigm_1']
w3mag_2 = allwise_data['w3mag_2']
w3mag_2_err = allwise_data['w3sigm_2']
w3mag_3 = allwise_data['w3mag_3']
w3mag_3_err = allwise_data['w3sigm_3']
w3mag_4 = allwise_data['w3mag_4']
w3mag_4_err = allwise_data['w3sigm_4']
w3mag_5 = allwise_data['w3mag_5']
w3mag_5_err = allwise_data['w3sigm_5']
w3mag_6 = allwise_data['w3mag_6']
w3mag_6_err = allwise_data['w3sigm_6']
w3mag_7 = allwise_data['w3mag_7']
w3mag_7_err = allwise_data['w3sigm_7']
w3mag_8 = allwise_data['w3mag_8']
w3mag_8_err = allwise_data['w3sigm_8']


w4mag_1 = allwise_data['w4mag_1']
w4mag_1_err = allwise_data['w4sigm_1']
w4mag_2 = allwise_data['w4mag_2']
w4mag_2_err = allwise_data['w4sigm_2']
w4mag_3 = allwise_data['w4mag_3']
w4mag_3_err = allwise_data['w4sigm_3']
w4mag_4 = allwise_data['w4mag_4']
w4mag_4_err = allwise_data['w4sigm_4']
w4mag_5 = allwise_data['w4mag_5']
w4mag_5_err = allwise_data['w4sigm_5']
w4mag_6 = allwise_data['w4mag_6']
w4mag_6_err = allwise_data['w4sigm_6']
w4mag_7 = allwise_data['w4mag_7']
w4mag_7_err = allwise_data['w4sigm_7']
w4mag_8 = allwise_data['w4mag_8']
w4mag_8_err = allwise_data['w4sigm_8']

#2MASS XSC Elliptical Aperture Photometry
w1gmag = allwise_data['w1gmag']
w1gmag_err = allwise_data['w1gerr']
w1rsemi = allwise_data['w1rsemi']
w2gmag = allwise_data['w2gmag']
w2gmag_err = allwise_data['w2gerr']
w2rsemi = allwise_data['w2rsemi']
w3gmag = allwise_data['w3gmag']
w3gmag_err = allwise_data['w3gerr']
w3rsemi = allwise_data['w3rsemi']
w4gmag = allwise_data['w4gmag']
w4gmag_err = allwise_data['w4gerr']
w4rsemi = allwise_data['w4rsemi']

#Bin up the curve of growth aperture photometry in each band by rchi2
#Use rchi2 < 1, 1-2, 2-3, 3-4, >4

#W1 bins
index_w1_1 = (w1rchi2 <= 1)
index_w1_2 = ((w1rchi2 > 1) & (w1rchi2 <= 2))
index_w1_3 = ((w1rchi2 > 2) & (w1rchi2 <= 3))
index_w1_4 = ((w1rchi2 > 3) & (w1rchi2 <= 4))
index_w1_5 = (w1rchi2 > 4)

#Create normalized curves of growth, normalized to the first aperture
norm_1 = w1mag_1[index_w1_1]
norm_2 = w1mag_1[index_w1_2]
norm_3 = w1mag_1[index_w1_3]
norm_4 = w1mag_1[index_w1_4]
norm_5 = w1mag_1[index_w1_5]

w1cog_1 = vstack([norm_1 - w1mag_1[index_w1_1], norm_1 - w1mag_2[index_w1_1], norm_1 - w1mag_3[index_w1_1], norm_1 - w1mag_4[index_w1_1], norm_1 - w1mag_5[index_w1_1], norm_1 - w1mag_6[index_w1_1], norm_1 - w1mag_7[index_w1_1], norm_1 - w1mag_8[index_w1_1]])
w1cog_2 = vstack([norm_2 - w1mag_1[index_w1_2], norm_2 - w1mag_2[index_w1_2], norm_2 - w1mag_3[index_w1_2], norm_2 - w1mag_4[index_w1_2], norm_2 - w1mag_5[index_w1_2], norm_2 - w1mag_6[index_w1_2], norm_2 - w1mag_7[index_w1_2], norm_2 - w1mag_8[index_w1_2]])
w1cog_3 = vstack([norm_3 - w1mag_1[index_w1_3], norm_3 - w1mag_2[index_w1_3], norm_3 - w1mag_3[index_w1_3], norm_3 - w1mag_4[index_w1_3], norm_3 - w1mag_5[index_w1_3], norm_3 - w1mag_6[index_w1_3], norm_3 - w1mag_7[index_w1_3], norm_3 - w1mag_8[index_w1_3]])
w1cog_4 = vstack([norm_4 - w1mag_1[index_w1_4], norm_4 - w1mag_2[index_w1_4], norm_4 - w1mag_3[index_w1_4], norm_4 - w1mag_4[index_w1_4], norm_4 - w1mag_5[index_w1_4], norm_4 - w1mag_6[index_w1_4], norm_4 - w1mag_7[index_w1_4], norm_4 - w1mag_8[index_w1_4]])
w1cog_5 = vstack([norm_5 - w1mag_1[index_w1_5], norm_5 - w1mag_2[index_w1_5], norm_5 - w1mag_3[index_w1_5], norm_5 - w1mag_4[index_w1_5], norm_5 - w1mag_5[index_w1_5], norm_5 - w1mag_6[index_w1_5], norm_5 - w1mag_7[index_w1_5], norm_5 - w1mag_8[index_w1_5]])

#Convert to flux ratio
w1cog_1 = 10**(w1cog_1/2.5)
w1cog_2 = 10**(w1cog_2/2.5)
w1cog_3 = 10**(w1cog_3/2.5)
w1cog_4 = 10**(w1cog_4/2.5)
w1cog_5 = 10**(w1cog_5/2.5)

w1cog_1_median = median(w1cog_1, axis = 1)
w1cog_2_median = median(w1cog_2, axis = 1)
w1cog_3_median = median(w1cog_3, axis = 1)
w1cog_4_median = median(w1cog_4, axis = 1)
w1cog_5_median = median(w1cog_5, axis = 1)

w1cog_1_n = sum(isfinite(w1cog_1), axis = 1)
w1cog_2_n = sum(isfinite(w1cog_2), axis = 1)
w1cog_3_n = sum(isfinite(w1cog_3), axis = 1)
w1cog_4_n = sum(isfinite(w1cog_4), axis = 1)
w1cog_5_n = sum(isfinite(w1cog_5), axis = 1)

w1cog_1_std = nanstd(w1cog_1, axis = 1)/sqrt(w1cog_1_n)
w1cog_2_std = nanstd(w1cog_2, axis = 1)/sqrt(w1cog_2_n)
w1cog_3_std = nanstd(w1cog_3, axis = 1)/sqrt(w1cog_3_n)
w1cog_4_std = nanstd(w1cog_4, axis = 1)/sqrt(w1cog_4_n)
w1cog_5_std = nanstd(w1cog_5, axis = 1)/sqrt(w1cog_5_n)

figure(1)
radius = array([5.5, 8.25, 11, 13.75, 16.5, 19.25, 22, 24.75, ])
errorbar(radius, w1cog_1_median, yerr = w1cog_1_std, fmt = 'o', color = 'k', label = r'$\chi^2 \le 1$, n = '+str(median(w1cog_1_n)))
errorbar(radius, w1cog_2_median, yerr = w1cog_2_std, fmt = 'o', color = 'b', label = r'$1 < \chi^2 \le 2$, n = '+str(median(w1cog_2_n)))
errorbar(radius, w1cog_3_median, yerr = w1cog_3_std, fmt = 'o', color = 'r', label = r'$2 < \chi^2 \le 3$, n = '+str(median(w1cog_3_n)))
errorbar(radius, w1cog_4_median, yerr = w1cog_4_std, fmt = 'o', color = 'g', label = r'$3 < \chi^2 \le 4$, n = '+str(median(w1cog_4_n)))
errorbar(radius, w1cog_5_median, yerr = w1cog_5_std, fmt = 'o', color = 'm', label = r'$\chi^2 > 4$, n = '+str(median(w1cog_5_n)))
xlabel(r'W1 Aperture Radius [arcsec]')
ylabel(r'Normalized Curve of Growth')
legend(loc = 'upper left', fontsize = 12)

#W2 bins
index_w2_1 = (w2rchi2 <= 1)
index_w2_2 = ((w2rchi2 > 1) & (w2rchi2 <= 2))
index_w2_3 = ((w2rchi2 > 2) & (w2rchi2 <= 3))
index_w2_4 = ((w2rchi2 > 3) & (w2rchi2 <= 4))
index_w2_5 = (w2rchi2 > 4)

#Create normalized curves of growth, normalized to the first aperture
norm_1 = w2mag_1[index_w2_1]
norm_2 = w2mag_1[index_w2_2]
norm_3 = w2mag_1[index_w2_3]
norm_4 = w2mag_1[index_w2_4]
norm_5 = w2mag_1[index_w2_5]

w2cog_1 = vstack([norm_1 - w2mag_1[index_w2_1], norm_1 - w2mag_2[index_w2_1], norm_1 - w2mag_3[index_w2_1], norm_1 - w2mag_4[index_w2_1], norm_1 - w2mag_5[index_w2_1], norm_1 - w2mag_6[index_w2_1], norm_1 - w2mag_7[index_w2_1], norm_1 - w2mag_8[index_w2_1]])
w2cog_2 = vstack([norm_2 - w2mag_1[index_w2_2], norm_2 - w2mag_2[index_w2_2], norm_2 - w2mag_3[index_w2_2], norm_2 - w2mag_4[index_w2_2], norm_2 - w2mag_5[index_w2_2], norm_2 - w2mag_6[index_w2_2], norm_2 - w2mag_7[index_w2_2], norm_2 - w2mag_8[index_w2_2]])
w2cog_3 = vstack([norm_3 - w2mag_1[index_w2_3], norm_3 - w2mag_2[index_w2_3], norm_3 - w2mag_3[index_w2_3], norm_3 - w2mag_4[index_w2_3], norm_3 - w2mag_5[index_w2_3], norm_3 - w2mag_6[index_w2_3], norm_3 - w2mag_7[index_w2_3], norm_3 - w2mag_8[index_w2_3]])
w2cog_4 = vstack([norm_4 - w2mag_1[index_w2_4], norm_4 - w2mag_2[index_w2_4], norm_4 - w2mag_3[index_w2_4], norm_4 - w2mag_4[index_w2_4], norm_4 - w2mag_5[index_w2_4], norm_4 - w2mag_6[index_w2_4], norm_4 - w2mag_7[index_w2_4], norm_4 - w2mag_8[index_w2_4]])
w2cog_5 = vstack([norm_5 - w2mag_1[index_w2_5], norm_5 - w2mag_2[index_w2_5], norm_5 - w2mag_3[index_w2_5], norm_5 - w2mag_4[index_w2_5], norm_5 - w2mag_5[index_w2_5], norm_5 - w2mag_6[index_w2_5], norm_5 - w2mag_7[index_w2_5], norm_5 - w2mag_8[index_w2_5]])

#Convert to flux ratio
w2cog_1 = 10**(w2cog_1/2.5)
w2cog_2 = 10**(w2cog_2/2.5)
w2cog_3 = 10**(w2cog_3/2.5)
w2cog_4 = 10**(w2cog_4/2.5)
w2cog_5 = 10**(w2cog_5/2.5)

w2cog_1_median = median(w2cog_1, axis = 1)
w2cog_2_median = median(w2cog_2, axis = 1)
w2cog_3_median = median(w2cog_3, axis = 1)
w2cog_4_median = median(w2cog_4, axis = 1)
w2cog_5_median = median(w2cog_5, axis = 1)

w2cog_1_n = sum(isfinite(w2cog_1), axis = 1)
w2cog_2_n = sum(isfinite(w2cog_2), axis = 1)
w2cog_3_n = sum(isfinite(w2cog_3), axis = 1)
w2cog_4_n = sum(isfinite(w2cog_4), axis = 1)
w2cog_5_n = sum(isfinite(w2cog_5), axis = 1)

w2cog_1_std = nanstd(w2cog_1, axis = 1)/sqrt(w2cog_1_n)
w2cog_2_std = nanstd(w2cog_2, axis = 1)/sqrt(w2cog_2_n)
w2cog_3_std = nanstd(w2cog_3, axis = 1)/sqrt(w2cog_3_n)
w2cog_4_std = nanstd(w2cog_4, axis = 1)/sqrt(w2cog_4_n)
w2cog_5_std = nanstd(w2cog_5, axis = 1)/sqrt(w2cog_5_n)

figure(2)
radius = array([5.5, 8.25, 11, 13.75, 16.5, 19.25, 22, 24.75, ])
errorbar(radius, w2cog_1_median, yerr = w2cog_1_std, fmt = 'o', color = 'k', label = r'$\chi^2 \le 1$, n = '+str(median(w2cog_1_n)))
errorbar(radius, w2cog_2_median, yerr = w2cog_2_std, fmt = 'o', color = 'b', label = r'$1 < \chi^2 \le 2$, n = '+str(median(w2cog_2_n)))
errorbar(radius, w2cog_3_median, yerr = w2cog_3_std, fmt = 'o', color = 'r', label = r'$2 < \chi^2 \le 3$, n = '+str(median(w2cog_3_n)))
errorbar(radius, w2cog_4_median, yerr = w2cog_4_std, fmt = 'o', color = 'g', label = r'$3 < \chi^2 \le 4$, n = '+str(median(w2cog_4_n)))
errorbar(radius, w2cog_5_median, yerr = w2cog_5_std, fmt = 'o', color = 'm', label = r'$\chi^2 > 4$, n = '+str(median(w2cog_5_n)))
xlabel(r'W2 Aperture Radius [arcsec]')
ylabel(r'Normalized Curve of Growth')
legend(loc = 'upper left', fontsize = 12)

#W3 bins
index_w3_1 = (w3rchi2 <= 1)
index_w3_2 = ((w3rchi2 > 1) & (w3rchi2 <= 2))
index_w3_3 = ((w3rchi2 > 2) & (w3rchi2 <= 3))
index_w3_4 = ((w3rchi2 > 3) & (w3rchi2 <= 4))
index_w3_5 = (w3rchi2 > 4)

#Create normalized curves of growth, normalized to the first aperture
norm_1 = w3mag_1[index_w3_1]
norm_2 = w3mag_1[index_w3_2]
norm_3 = w3mag_1[index_w3_3]
norm_4 = w3mag_1[index_w3_4]
norm_5 = w3mag_1[index_w3_5]

w3cog_1 = vstack([norm_1 - w3mag_1[index_w3_1], norm_1 - w3mag_2[index_w3_1], norm_1 - w3mag_3[index_w3_1], norm_1 - w3mag_4[index_w3_1], norm_1 - w3mag_5[index_w3_1], norm_1 - w3mag_6[index_w3_1], norm_1 - w3mag_7[index_w3_1], norm_1 - w3mag_8[index_w3_1]])
w3cog_2 = vstack([norm_2 - w3mag_1[index_w3_2], norm_2 - w3mag_2[index_w3_2], norm_2 - w3mag_3[index_w3_2], norm_2 - w3mag_4[index_w3_2], norm_2 - w3mag_5[index_w3_2], norm_2 - w3mag_6[index_w3_2], norm_2 - w3mag_7[index_w3_2], norm_2 - w3mag_8[index_w3_2]])
w3cog_3 = vstack([norm_3 - w3mag_1[index_w3_3], norm_3 - w3mag_2[index_w3_3], norm_3 - w3mag_3[index_w3_3], norm_3 - w3mag_4[index_w3_3], norm_3 - w3mag_5[index_w3_3], norm_3 - w3mag_6[index_w3_3], norm_3 - w3mag_7[index_w3_3], norm_3 - w3mag_8[index_w3_3]])
w3cog_4 = vstack([norm_4 - w3mag_1[index_w3_4], norm_4 - w3mag_2[index_w3_4], norm_4 - w3mag_3[index_w3_4], norm_4 - w3mag_4[index_w3_4], norm_4 - w3mag_5[index_w3_4], norm_4 - w3mag_6[index_w3_4], norm_4 - w3mag_7[index_w3_4], norm_4 - w3mag_8[index_w3_4]])
w3cog_5 = vstack([norm_5 - w3mag_1[index_w3_5], norm_5 - w3mag_2[index_w3_5], norm_5 - w3mag_3[index_w3_5], norm_5 - w3mag_4[index_w3_5], norm_5 - w3mag_5[index_w3_5], norm_5 - w3mag_6[index_w3_5], norm_5 - w3mag_7[index_w3_5], norm_5 - w3mag_8[index_w3_5]])

#Convert to flux ratio
w3cog_1 = 10**(w3cog_1/2.5)
w3cog_2 = 10**(w3cog_2/2.5)
w3cog_3 = 10**(w3cog_3/2.5)
w3cog_4 = 10**(w3cog_4/2.5)
w3cog_5 = 10**(w3cog_5/2.5)

w3cog_1_median = median(w3cog_1, axis = 1)
w3cog_2_median = median(w3cog_2, axis = 1)
w3cog_3_median = median(w3cog_3, axis = 1)
w3cog_4_median = median(w3cog_4, axis = 1)
w3cog_5_median = median(w3cog_5, axis = 1)

w3cog_1_n = sum(isfinite(w3cog_1), axis = 1)
w3cog_2_n = sum(isfinite(w3cog_2), axis = 1)
w3cog_3_n = sum(isfinite(w3cog_3), axis = 1)
w3cog_4_n = sum(isfinite(w3cog_4), axis = 1)
w3cog_5_n = sum(isfinite(w3cog_5), axis = 1)

w3cog_1_std = nanstd(w3cog_1, axis = 1)/sqrt(w3cog_1_n)
w3cog_2_std = nanstd(w3cog_2, axis = 1)/sqrt(w3cog_2_n)
w3cog_3_std = nanstd(w3cog_3, axis = 1)/sqrt(w3cog_3_n)
w3cog_4_std = nanstd(w3cog_4, axis = 1)/sqrt(w3cog_4_n)
w3cog_5_std = nanstd(w3cog_5, axis = 1)/sqrt(w3cog_5_n)

figure(3)
radius = array([5.5, 8.25, 11, 13.75, 16.5, 19.25, 22, 24.75, ])
errorbar(radius, w3cog_1_median, yerr = w3cog_1_std, fmt = 'o', color = 'k', label = r'$\chi^2 \le 1$, n = '+str(median(w3cog_1_n)))
errorbar(radius, w3cog_2_median, yerr = w3cog_2_std, fmt = 'o', color = 'b', label = r'$1 < \chi^2 \le 2$, n = '+str(median(w3cog_2_n)))
errorbar(radius, w3cog_3_median, yerr = w3cog_3_std, fmt = 'o', color = 'r', label = r'$2 < \chi^2 \le 3$, n = '+str(median(w3cog_3_n)))
errorbar(radius, w3cog_4_median, yerr = w3cog_4_std, fmt = 'o', color = 'g', label = r'$3 < \chi^2 \le 4$, n = '+str(median(w3cog_4_n)))
errorbar(radius, w3cog_5_median, yerr = w3cog_5_std, fmt = 'o', color = 'm', label = r'$\chi^2 > 4$, n = '+str(median(w3cog_5_n)))
xlabel(r'W3 Aperture Radius [arcsec]')
ylabel(r'Normalized Curve of Growth')
legend(loc = 'upper left', fontsize = 12)

#W4 bins
index_w4_1 = (w4rchi2 <= 1)
index_w4_2 = ((w4rchi2 > 1) & (w4rchi2 <= 2))
index_w4_3 = ((w4rchi2 > 2) & (w4rchi2 <= 3))
index_w4_4 = ((w4rchi2 > 3) & (w4rchi2 <= 4))
index_w4_5 = (w4rchi2 > 4)

#Create normalized curves of growth, normalized to the first aperture
norm_1 = w4mag_1[index_w4_1]
norm_2 = w4mag_1[index_w4_2]
norm_3 = w4mag_1[index_w4_3]
norm_4 = w4mag_1[index_w4_4]
norm_5 = w4mag_1[index_w4_5]

w4cog_1 = vstack([norm_1 - w4mag_1[index_w4_1], norm_1 - w4mag_2[index_w4_1], norm_1 - w4mag_3[index_w4_1], norm_1 - w4mag_4[index_w4_1], norm_1 - w4mag_5[index_w4_1], norm_1 - w4mag_6[index_w4_1], norm_1 - w4mag_7[index_w4_1], norm_1 - w4mag_8[index_w4_1]])
w4cog_2 = vstack([norm_2 - w4mag_1[index_w4_2], norm_2 - w4mag_2[index_w4_2], norm_2 - w4mag_3[index_w4_2], norm_2 - w4mag_4[index_w4_2], norm_2 - w4mag_5[index_w4_2], norm_2 - w4mag_6[index_w4_2], norm_2 - w4mag_7[index_w4_2], norm_2 - w4mag_8[index_w4_2]])
w4cog_3 = vstack([norm_3 - w4mag_1[index_w4_3], norm_3 - w4mag_2[index_w4_3], norm_3 - w4mag_3[index_w4_3], norm_3 - w4mag_4[index_w4_3], norm_3 - w4mag_5[index_w4_3], norm_3 - w4mag_6[index_w4_3], norm_3 - w4mag_7[index_w4_3], norm_3 - w4mag_8[index_w4_3]])
w4cog_4 = vstack([norm_4 - w4mag_1[index_w4_4], norm_4 - w4mag_2[index_w4_4], norm_4 - w4mag_3[index_w4_4], norm_4 - w4mag_4[index_w4_4], norm_4 - w4mag_5[index_w4_4], norm_4 - w4mag_6[index_w4_4], norm_4 - w4mag_7[index_w4_4], norm_4 - w4mag_8[index_w4_4]])
w4cog_5 = vstack([norm_5 - w4mag_1[index_w4_5], norm_5 - w4mag_2[index_w4_5], norm_5 - w4mag_3[index_w4_5], norm_5 - w4mag_4[index_w4_5], norm_5 - w4mag_5[index_w4_5], norm_5 - w4mag_6[index_w4_5], norm_5 - w4mag_7[index_w4_5], norm_5 - w4mag_8[index_w4_5]])

#Convert to flux ratio
w4cog_1 = 10**(w4cog_1/2.5)
w4cog_2 = 10**(w4cog_2/2.5)
w4cog_3 = 10**(w4cog_3/2.5)
w4cog_4 = 10**(w4cog_4/2.5)
w4cog_5 = 10**(w4cog_5/2.5)

w4cog_1_median = median(w4cog_1, axis = 1)
w4cog_2_median = median(w4cog_2, axis = 1)
w4cog_3_median = median(w4cog_3, axis = 1)
w4cog_4_median = median(w4cog_4, axis = 1)
w4cog_5_median = median(w4cog_5, axis = 1)

w4cog_1_n = sum(isfinite(w4cog_1), axis = 1)
w4cog_2_n = sum(isfinite(w4cog_2), axis = 1)
w4cog_3_n = sum(isfinite(w4cog_3), axis = 1)
w4cog_4_n = sum(isfinite(w4cog_4), axis = 1)
w4cog_5_n = sum(isfinite(w4cog_5), axis = 1)

w4cog_1_std = nanstd(w4cog_1, axis = 1)/sqrt(w4cog_1_n)
w4cog_2_std = nanstd(w4cog_2, axis = 1)/sqrt(w4cog_2_n)
w4cog_3_std = nanstd(w4cog_3, axis = 1)/sqrt(w4cog_3_n)
w4cog_4_std = nanstd(w4cog_4, axis = 1)/sqrt(w4cog_4_n)
w4cog_5_std = nanstd(w4cog_5, axis = 1)/sqrt(w4cog_5_n)

figure(4)
radius = array([11, 16.5, 22, 27.5, 33, 38.5, 44, 49.5])
errorbar(radius, w4cog_1_median, yerr = w4cog_1_std, fmt = 'o', color = 'k', label = r'$\chi^2 \le 1$, n = '+str(median(w4cog_1_n)))
errorbar(radius, w4cog_2_median, yerr = w4cog_2_std, fmt = 'o', color = 'b', label = r'$1 < \chi^2 \le 2$, n = '+str(median(w4cog_2_n)))
errorbar(radius, w4cog_3_median, yerr = w4cog_3_std, fmt = 'o', color = 'r', label = r'$2 < \chi^2 \le 3$, n = '+str(median(w4cog_3_n)))
errorbar(radius, w4cog_4_median, yerr = w4cog_4_std, fmt = 'o', color = 'g', label = r'$3 < \chi^2 \le 4$, n = '+str(median(w4cog_4_n)))
errorbar(radius, w4cog_5_median, yerr = w4cog_5_std, fmt = 'o', color = 'm', label = r'$\chi^2 > 4$, n = '+str(median(w4cog_5_n)))
xlabel(r'W4 Aperture Radius [arcsec]')
ylabel(r'Normalized Curve of Growth')
legend(loc = 'upper left', fontsize = 12)

show()