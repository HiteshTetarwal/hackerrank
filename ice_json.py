import warnings
warnings.filterwarnings("ignore")

import os
from django.conf import settings
import numpy as np
from datetime import datetime, timedelta
import pickle
import pprint
import json
import math
from netCDF4 import Dataset
class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
            np.int16, np.int32, np.int64, np.uint8,
            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32, 
            np.float64)):
            return float(obj)
        elif isinstance(obj,(np.ndarray,)): #### This is the fix
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

def save_daily_current_data():
	current_path='20200401120000-UKMO-L4_GHRSST-SSTfnd-OSTIA-GLOB-v02.0-fv02.0.nc'
	sd_file = Dataset(current_path, mode='rb')
	print(sd_file.variables)
	return
	lons = sd_file.variables['lon'][:]
	lats = sd_file.variables['lat'][:]
	sd_file.variables['sea_ice_fraction'] = sd_file.variables['sea_ice_fraction'][:]*100.0
	lons_non_negative = (lons + 360) % 360
	lon_all = range(0,360)
	lat_all = range(90,-91,-1)
	print(lat_all)
	# asdsd
	data = [] 
	lat_len = len(lat_all)-1 
	all_fraction = sd_file.variables['sea_ice_fraction']
	np_lons, np_lats = np.meshgrid(lons, lats)
	print(lats.min(),lats.max())
	# brekpasdjosiadn
	while lat_len>=0:
		for lon in lon_all:
			lat = lat_all[lat_len]
			print(lat,lon)

			# if lon < min(lons_non_negative) or lon > max(lons_non_negative):
			# 	sea_ice = "N/A"
			# if lat < min(lats) or lat > max(lats):
			# 	sea_ice = "N/A"
			# if sea_ice != "N/A":
				
			pos_dist = (np_lats - lat)**2 + (lons_non_negative - lon)**2
			minindex_flattened = pos_dist.argmin()
			lt_index, ln_index = np.unravel_index(minindex_flattened, np_lons.shape)
			sea_ice = all_fraction[-1,lt_index,ln_index]
				# print lat,lon,sea_ice
			# if sea_ice == "N/A" or sea_ice == "--" and sea_ice is None:
			# 	sea_ice = 0
			if str(float(sea_ice))=="nan":
				sea_ice = 0.0

			data.append(float(sea_ice))
		lat_len-=1
	header = {
		"nx" : 360.0,
		"ny" : 181,
		"lo1" : lon_all[0],
		"lo2" : lon_all[-1],
		"la1" : lat_all[-1],
		"la2" : lat_all[0],
		"dx"  : 1.0,
		"dy"  : 1.0
	}
	# lons_non_negative = (lons + 360) % 360
	# sea_ice = sd_file.variables['sea_ice_fraction'][-1,:,:]
	# sea_ice_list = []
	# lti = 0
	# ny = 0
	# while lti < len(lats):
	# 	lni = 0
	# 	nx = 0
	# 	while lni < len(lons):
	# 		sea_ice[lti, lni] *= 60.0
	# 		if math.isnan(sea_ice[lti, lni]):
	# 			sea_ice[lti, lni] = 0.0
	# 		sea_ice_list.append( sea_ice[lti, lni] )
	# 		lni += 3
	# 		nx += 1
	# 	ny += 1
	# 	lti += 3
	# header = {
	# 	"nx" : nx,
	# 	"ny" : ny,
	# 	"lo1" : lons[0],
	# 	"lo2" : lons[0] + nx - 1,
	# 	"la1" : lats[0],
	# 	"la2" : lats[0] - ny + 1,
	# 	"dx"  : 1.0,
	# 	"dy"  : 1.0
	# }
	final_sea_ice_data = {
		"header" : header,
		"data" : data
	}
	# print final_sea_ice_data
	# print "length==============",min(data),max(data),len(data)
	sea_ice_data_json = json.dumps(final_sea_ice_data,cls=NumpyEncoder)
	
	f = open("sea_ice_data.json", "w")
	f.write(sea_ice_data_json)
	f.close()
	return "done"
		# break

save_daily_current_data()

