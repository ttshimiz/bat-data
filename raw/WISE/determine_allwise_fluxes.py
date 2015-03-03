'''
Script to upload all of the WISE fluxes from the AllWise catalog for the BAT sample and 
determine whether to use the point source or elliptical aperture flux.
The chi^2 of the profile fitting in WISE will be used as the determining factor.
If chi^2 > 3 then the elliptical aperture will be used unless the elliptical aperture is 
sufficiently big (30, 40, 50, or 60") for each band.

'''

from pylab import *

#Upload AllWise fluxes
allwise_data = genfromtxt('/Users/ttshimiz/Dropbox/Research/Thesis/Other_surveys/WISE/wise_allwise_bat_agn.tbl', delimiter = '\t', names = True, dtype = None, missing_values = 'null')
names = allwise_data['Name']
ext_flg = allwise_data['ext_flg']

#Profile-Fitting fluxes and chi^2
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

#File to write out the chosen AllWise fluxes
allwise_file = open('/Users/ttshimiz/Dropbox/Research/Thesis/Other_surveys/WISE/allwise_bat_agn_fluxes_greater_flux.txt', 'w')

#Arrays to store all the magnitudes and uncertainties
w1mag = zeros(len(allwise_data))
w1mag_err = zeros(len(allwise_data))
w2mag = zeros(len(allwise_data))
w2mag_err = zeros(len(allwise_data))
w3mag = zeros(len(allwise_data))
w3mag_err = zeros(len(allwise_data))
w4mag = zeros(len(allwise_data))
w4mag_err = zeros(len(allwise_data))
w1extended = zeros(len(allwise_data), dtype = bool)
w2extended = zeros(len(allwise_data), dtype = bool)
w3extended = zeros(len(allwise_data), dtype = bool)
w4extended = zeros(len(allwise_data), dtype = bool)

for i in range(len(allwise_data)):

	#WISE 1 (3.4 micron) flux
	#if ((w1rchi2[i] > 3.0) | (w1rsemi[i] > 30.)) & isfinite(w1rsemi[i]):
	#if (ext_flg[i] != 0) & isfinite(w1rsemi[i]):
	if ((w1mpro[i] > w1gmag[i]) | (w1rsemi[i] > 30.)) & isfinite(w1rsemi[i]):
		w1mag[i] = w1gmag[i]
		w1mag_err[i] = w1gmag_err[i]
		w1extended[i] = True
		
	else:
		
		w1mag[i] = w1mpro[i]
		w1mag_err[i] = w1mpro_err[i]
		w1extended[i] = False
		
	#WISE 2 (4.6 micron) flux
	#if ((w2rchi2[i] > 3.0) | (w2rsemi[i] > 40.)) & isfinite(w2rsemi[i]):
	#if (ext_flg[i] != 0) & isfinite(w1rsemi[i]):
	if ((w2mpro[i] > w2gmag[i]) | (w1rsemi[i] > 40.)) & isfinite(w1rsemi[i]):
		w2mag[i] = w2gmag[i]
		w2mag_err[i] = w2gmag_err[i]
		w2extended[i] = True
		
	else:
		
		w2mag[i] = w2mpro[i]
		w2mag_err[i] = w2mpro_err[i]
		w2extended[i] = False
		
	#WISE 3 (12 micron) flux
	#if ((w3rchi2[i] > 3.0) | (w3rsemi[i] > 50.)) & isfinite(w3rsemi[i]):
	#if (ext_flg[i] != 0) & isfinite(w1rsemi[i]):
	if ((w3mpro[i] > w3gmag[i]) | (w3rsemi[i] > 50.)) & isfinite(w1rsemi[i]):
		w3mag[i] = w3gmag[i]
		w3mag_err[i] = w3gmag_err[i]
		w3extended[i] = True
		
	else:
		
		w3mag[i] = w3mpro[i]
		w3mag_err[i] = w3mpro_err[i]
		w3extended[i] = False
		
	#WISE 4 (22 micron) flux
	#if ((w4rchi2[i] > 3.0) | (w4rsemi[i] > 60.)) & isfinite(w4rsemi[i]):
	#if (ext_flg[i] != 0) & isfinite(w1rsemi[i]):
	if ((w4mpro[i] > w4gmag[i]) | (w4rsemi[i] > 60.)) & isfinite(w1rsemi[i]):
		w4mag[i] = w4gmag[i]
		w4mag_err[i] = w4gmag_err[i]
		w4extended[i] = True
		
	else:
		
		w4mag[i] = w4mpro[i]
		w4mag_err[i] = w4mpro_err[i]
		w4extended[i] = False
		
#Make aperture corrections of 0.034, 0.041, -0.030, and 0.029 for the ones using elliptical apertures
w1mag[w1extended] = w1mag[w1extended] + 0.034
w2mag[w2extended] = w2mag[w2extended] + 0.041
w3mag[w3extended] = w3mag[w3extended] - 0.030
w4mag[w4extended] = w4mag[w4extended] + 0.029

#Use W2-W3 to make color corrections
color_corrections_w1 = array([1.0283, 1.0084, 0.9961, 0.9907, 0.9921, 1.0, 1.0142, 1.0347])
color_corrections_w2 = array([1.0206, 1.0066, 0.9976, 0.9935, 0.9943, 1.0, 1.0107, 1.0265])
color_corrections_w3 = array([1.1344, 1.0088, 0.9393, 0.9169, 0.9373, 1.0, 1.1081, 1.2687])
color_corrections_w4 = array([1.0142, 1.0013, 0.9934, 0.9905, 0.9926, 1.0, 1.0130, 1.0319])
mir_colors = array([-0.9624, -0.0748, 0.8575, 1.8357, 2.8586, 3.9225, 5.0223, 6.1524])

sample_cc_w1 = ones(len(allwise_data))
sample_cc_w2 = ones(len(allwise_data))
sample_cc_w3 = ones(len(allwise_data))
sample_cc_w4 = ones(len(allwise_data))

#Apply color corrections
for i in range(len(allwise_data)):
	
	mir_color_observed = w2mag[i] - w3mag[i]
	
	if isfinite(mir_color_observed):
		
		index = argmin(abs(mir_colors - mir_color_observed))
		sample_cc_w1[i] = color_corrections_w1[index]
		sample_cc_w2[i] = color_corrections_w2[index]
		sample_cc_w3[i] = color_corrections_w3[index]
		sample_cc_w4[i] = color_corrections_w4[index]
		
#Calculate WISE fluxes and uncertainties in Jy
w1_flux = 306.682/sample_cc_w1*10**(-w1mag/2.5)
w1_err = w1_flux/2.5*log(10)*w1mag_err
w2_flux = 170.663/sample_cc_w2*10**(-w2mag/2.5)
w2_err = w2_flux/2.5*log(10)*w2mag_err
w3_flux = 29.045/sample_cc_w3*10**(-w3mag/2.5)
w3_err = w3_flux/2.5*log(10)*w3mag_err
w4_flux = 8.284/sample_cc_w4*10**(-w4mag/2.5)
w4_err = w4_flux/2.5*log(10)*w4mag_err

#Apply an 8% correction to W4 for red sources ([w2 - w3] > 1.3
red_sources = (w2mag - w3mag) > 1.3
w4_flux[red_sources] = w4_flux[red_sources]*0.92

#Add in 5% and 15% uncertainty for W1/W2 and W3/W4 respectively for calibration uncertainties
w1_err = sqrt(w1_err**2 + (0.05*w1_flux)**2)
w2_err = sqrt(w2_err**2 + (0.05*w2_flux)**2)
w3_err = sqrt(w3_err**2 + (0.15*w3_flux)**2)
w4_err = sqrt(w4_err**2 + (0.15*w4_flux)**2)

#Write out the data to a file
for i in range(len(allwise_data)):

	allwise_file.write(names[i]+'\t'+str(w1_flux[i])+'\t'+str(w1_err[i])+'\t'+str(w1extended[i])+'\t'+str(w2_flux[i])+'\t'+str(w2_err[i])+'\t'+str(w2extended[i])+'\t'+str(w3_flux[i])+'\t'+str(w3_err[i])+'\t'+str(w3extended[i])+'\t'+str(w4_flux[i])+'\t'+str(w4_err[i])+'\t'+str(w4extended[i])+'\n')
allwise_file.close()