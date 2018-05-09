"""
Run energy balance model for single timestep listed in row 1 of the
original EB_AUTO spreadsheet model release.

@author Andrew Tedstone (a.j.tedstone@bristol.ac.uk)

"""

import ebmodel as ebm

##############################################################################
## Input Data, as per first row of Brock and Arnold (2000) spreadsheet

lat = 67.0666
lon = -49.38
lon_ref = 0
summertime = 0
slope = 1.
aspect = 90.
elevation = 1000.
albedo = 0.35
roughness = 0.005
met_elevation = 1000.
lapse = 0.0065

day = 178
time = 100
inswrad = 1.572
avp = 660
airtemp = 5.612
windspd = 3.531
##############################################################################


SWR,LWR,SHF,LHF = ebm.calculate_seb(
	lat, lon, lon_ref, day, time, summertime,
	slope, aspect, elevation, met_elevation, lapse,
	inswrad, avp, airtemp, windspd, albedo, roughness)

sw_melt, lw_melt, shf_melt, lhf_melt, total = ebm.calculate_melt(
	SWR,LWR,SHF,LHF, windspd, airtemp)

print('Melt components ... SWR:%s, LWR:%s, SHF:%s, LHF:%s, MLT:%s' %(sw_melt,lw_melt,shf_melt,lhf_melt,total))