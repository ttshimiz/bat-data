from pylab import *
import os

#Upload our data
execfile('/Users/ttshimiz/Dropbox/Research/Thesis/scripts/upload_bat_ir_database.py')

#Upload all of the WISE data
wise_data = genfromtxt('/Users/ttshimiz/Dropbox/Research/Thesis/data/wise_allsky_bat_agn_fluxes.txt', names = True, dtype = None, delimiter = '\t', missing_values = 'null', filling_values = 0)
cntr_01 = wise_data['cntr_01']
w1mpro = wise_data['w1mpro']
w1rchi2 = wise_data['w1rchi2']
w1gmag = wise_data['w1gmag']
w2mpro = wise_data['w2mpro']
w2rchi2 = wise_data['w2rchi2']
w2gmag = wise_data['w2gmag']
w3mpro = wise_data['w3mpro']
w3rchi2 = wise_data['w3rchi2']
w3gmag = wise_data['w3gmag']
w4mpro = wise_data['w4mpro']
w4rchi2 = wise_data['w4rchi2']
w4gmag = wise_data['w4gmag']
extflg = wise_data['ext_flg']
w1_ellip_semimajor = wise_data['w1rsemi']
w2_ellip_semimajor = wise_data['w2rsemi']
w3_ellip_semimajor = wise_data['w3rsemi']
w4_ellip_semimajor = wise_data['w4rsemi']

ind_w1 = isfinite(w1gmag)
ind_w2 = isfinite(w2gmag)
ind_w3 = isfinite(w3gmag)
ind_w4 = isfinite(w4gmag)

w3cog = loadtxt('/Users/ttshimiz/Dropbox/Research/Thesis/Other_surveys/WISE/W3_curve_of_growth.txt')
w4cog = loadtxt('/Users/ttshimiz/Dropbox/Research/Thesis/Other_surveys/WISE/W4_curve_of_growth.txt')
pnt_extd_ratio_w1 = 10**((w1gmag[ind_w1] - w1mpro[ind_w1])/2.5)
pnt_extd_ratio_w2 = 10**((w2gmag[ind_w2] - w2mpro[ind_w2])/2.5)
pnt_extd_ratio_w3 = 10**((w3gmag[ind_w3] - w3mpro[ind_w3])/2.5)
pnt_extd_ratio_w4 = 10**((w4gmag[ind_w4] - w4mpro[ind_w4])/2.5)

figure()
scatter(w1_ellip_semimajor[ind_w1], pnt_extd_ratio_w1, c =log10( w1rchi2[ind_w1]), s = 40)
xlabel(r'W1 Elliptical Semimajor Axis [arcsec]')
ylabel(r'$F_{\rm{mpro}}/F_{\rm{gmag}}$')
cb3 = colorbar()
cb3.set_label(r'$\log \chi^2$')
axhline(y = 1.0, color = 'k', lw = 2)

figure()
scatter(w2_ellip_semimajor[ind_w2], pnt_extd_ratio_w2, c =log10( w2rchi2[ind_w2]), s = 40)
xlabel(r'W2 Elliptical Semimajor Axis [arcsec]')
ylabel(r'$F_{\rm{mpro}}/F_{\rm{gmag}}$')
cb3 = colorbar()
cb3.set_label(r'$\log \chi^2$')
axhline(y = 1.0, color = 'k', lw = 2)

figure()
scatter(w3_ellip_semimajor[ind_w3], pnt_extd_ratio_w3, c =log10( w3rchi2[ind_w3]), s = 40)
xlabel(r'W3 Elliptical Semimajor Axis [arcsec]')
ylabel(r'$F_{\rm{mpro}}/F_{\rm{gmag}}$')
cb3 = colorbar()
cb3.set_label(r'$\log \chi^2$')
axhline(y = 1.0, color = 'k', lw = 2)
plot(w3cog[0:-1,0], w3cog[-1, 1]/w3cog[0:-1, 1], 'm-', lw = 2)
ylim(0, 2.5)
xlim(0, 200)

figure()
scatter(w4_ellip_semimajor[ind_w4], pnt_extd_ratio_w4, c =w4rchi2[ind_w4], s = 40)
xlabel(r'W4 Elliptical Semimajor Axis [arcsec]')
ylabel(r'$F_{\rm{mpro}}/F_{\rm{gmag}}$')
cb4 = colorbar()
cb4.set_label(r'$\chi^2$')
axhline(y = 1.0, color = 'k', lw = 2)
plot(w4cog[0:-1,0], w4cog[-1, 1]/w4cog[0:-1, 1], 'm-', lw = 2)
ylim(0, 2.5)
xlim(0, 200)
show()
