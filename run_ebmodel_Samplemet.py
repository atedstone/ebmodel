"""
Run energy balance model with the meteorological measurements provided
with the original EB_AUTO spreadsheet model release.

@author Andrew Tedstone (a.j.tedstone@bristol.ac.uk)
"""

import pandas as pd
import datetime as dt

import ebmodel as ebm

##############################################################################
## Input Data (as per original EB_AUTO spreadsheet)

met_data = pd.read_excel('Samplmet.xls')

year = 1997

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

##############################################################################

flux_store = {}
melt_store = {}
for ix, ts in met_data.iterrows():

	# Calculate energy balance
	SWR,LWR,SHF,LHF = ebm.calculate_seb(
		lat, lon, lon_ref, ts.DAY, ts.TIME, summertime,
		slope, aspect, elevation, met_elevation, lapse,
		ts.INSWRAD, ts.AVP, ts.AIRTEMP, ts.WINDSPD, albedo, roughness)

	# Calculate melting
	swmelt,lwmelt,shfmelt,lhfmelt,total = ebm.calculate_melt(SWR,LWR,SHF,LHF,
		ts.WINDSPD,ts.AIRTEMP)

	# Deal with timestamp formatting in the Samplmet file so that datetime 
	# can understand
	if ts.TIME == 2400:
		time = 0
	else:
		time = ts.TIME

	# Create date/time index
	dt = pd.datetime.strptime('%s-%s-%s' %(year,int(ts.DAY),str(int(time)).zfill(4)), '%Y-%j-%H%M')

	# Store radiative fluxes and melt rates for this timestep
	flux_store[dt] = {'SWR_Wm2':SWR, 'LWR_Wm2':LWR, 'SHF_Wm2':SHF, 
		'LHF_Wm2':LHF}
	melt_store[dt] = {'SWR_melt':swmelt, 'LWR_melt':lwmelt, 
		'SHF_melt':shfmelt, 'LHF_melt':lhfmelt}

# Convert outputs to pandas DataFrame.
fluxes = pd.DataFrame.from_dict(flux_store, orient='index')
melt_rates = pd.DataFrame.from_dict(melt_store, orient='index')