
import numpy as np

import pandas as pd



df = pd.read_csv('datasets/cleaned_data_final.csv')


########################		DESIRABLE VALUES FOR FISHES 	########################

desirable_ph_upper = 9

desirable_ph_lower = 6.5

desirable_bod_upper = 2

desirable_bod_lower = 1

desirable_do_upper = 5

desirable_do_lower = 5

desirable_nitrate_upper = 4.5

desirable_nitrate_lower = 0.1

desirable_conductivity_upper = 2000

desirable_conductivity_lower = 100

desirable_totalcoli_upper = 10000

desirable_totalcoli_lower = 28

#########################################################################################




################################## 			ACCEPTABLE VALUES FOR FISHES 	#########################


acceptable_ph_upper = 9.5

acceptable_ph_lower =  7

acceptable_bod_upper = 6

acceptable_bod_lower = 3

acceptable_do_upper = 5

acceptable_do_lower = 3

acceptable_nitrate_upper = 100

acceptable_nitrate_lower = 0

acceptable_conductivity_upper = 50000

acceptable_conductivity_lower = 30

acceptable_totalcoli_upper = 10000

acceptable_totalcoli_lower = 0






#########################################################################################




def ph(ph_val):
	if (8.5>=ph_val>=7):
		npH_fish = 100
	elif (8.6>=ph_val>=8.5) or (6.9>=ph_val>=6.8):
		npH_fish = 80
	elif (8.8>=ph_val>=8.6) or (6.8>=ph_val>=6.7):
		npH_fish = 60
	elif (9>=ph_val>=8.8) or (6.7>=ph_val>=6.5):
		npH_fish = 40
	else:
		npH_fish = 0


	return npH_fish



def do(do_val):
	if (do_val>=6):
		nDO_FISH = 100
	elif (6>=do_val>=5.1):
		nDO_FISH = 80
	elif (5>=do_val>=4.1):
		nDO_FISH = 60
	elif (4>=do_val>=3):
		nDO_FISH = 40
	else:
		nDO_FISH = 0


	
	return nDO_FISH




def bod(bod_val):
	if (3>=bod_val>=0):
		nBOD_FISH = 100
	elif (6>=bod_val>=3):
		nBOD_FISH = 80
	elif (80>=bod_val>=6):
		nBOD_FISH = 60
	elif (125>=bod_val>=80):
		nBOD_FISH = 40
	else:
		nBOD_FISH = 0


	return nBOD_FISH


def totalcoliform(coli_val):
	if (5>=coli_val>=0):
		n_Totalcoli_FISH = 100
	elif (50>=coli_val>=5):
		n_Totalcoli_FISH = 80
	elif (500>=coli_val>=50):
		n_Totalcoli_FISH = 60
	elif (10000>=coli_val>=500):
		n_Totalcoli_FISH = 40
	else:
		n_Totalcoli_FISH = 0

	return n_Totalcoli_FISH



def conductivity(con_val):
	if (75>=con_val>=0):
		n_CONDUCTIVITY_FISH = 100
	elif (150>=con_val>=75):
		n_CONDUCTIVITY_FISH = 80
	elif (225>=con_val>=150):
		n_CONDUCTIVITY_FISH = 60
	elif (300>=con_val>=225):
		n_CONDUCTIVITY_FISH = 40
	else:
		n_CONDUCTIVITY_FISH = 0

	return n_CONDUCTIVITY_FISH




def nitrate(nit_val):
	if (20>=nit_val>=0):
		n_Nitrate_fish = 100
	elif (50>=nit_val>=20):
		n_Nitrate_fish = 80
	elif (100>=nit_val>=50):
		n_Nitrate_fish = 60
	elif (200>=nit_val>=100):
		n_Nitrate_fish = 40
	else:
		n_Nitrate_fish = 0

	return n_Nitrate_fish




wph_fish =  ph(desirable_ph_upper) * 0.165
wdo_fish = do(desirable_do_upper)* 0.281
wbdo_fish= bod(desirable_bod_upper) * 0.234
wec_fish = conductivity(desirable_conductivity_upper)* 0.009
wna_fish = nitrate(desirable_nitrate_upper) * 0.028
wco_fish = totalcoliform(desirable_totalcoli_upper) * 0.281



wqi_fish_upper_desirable =wph_fish+wdo_fish+wbdo_fish+wec_fish+wna_fish+wco_fish




wph_fish =  ph(desirable_ph_lower) * 0.165
wdo_fish = do(desirable_do_lower)* 0.281
wbdo_fish= bod(desirable_bod_lower) * 0.234
wec_fish = conductivity(desirable_conductivity_lower)* 0.009
wna_fish = nitrate(desirable_nitrate_lower) * 0.028
wco_fish = totalcoliform(desirable_totalcoli_lower) * 0.281

wqi_fish_lower_desirable =wph_fish+wdo_fish+wbdo_fish+wec_fish+wna_fish+wco_fish



print("UPPER DESIRABLE WQI - ",wqi_fish_upper_desirable)

print("LOWER DESIRABLE WQI - ",wqi_fish_lower_desirable)




final_Desirable_wqi_fish = wqi_fish_upper_desirable				### WQI 100-final_desirable_Wqi_value is desirable wateer quality for fishes 	##########




####################	TO FIND ACCEPTABLE RANGE OF WQI	###################

wph_fish =  ph(acceptable_ph_lower) * 0.165
wdo_fish = do(acceptable_do_lower)* 0.281
wbdo_fish= bod(acceptable_bod_lower) * 0.234
wec_fish = conductivity(acceptable_conductivity_lower)* 0.009
wna_fish = nitrate(acceptable_nitrate_lower) * 0.028
wco_fish = totalcoliform(acceptable_totalcoli_lower) * 0.281

wqi_fish_lower_acceptable =wph_fish+wdo_fish+wbdo_fish+wec_fish+wna_fish+wco_fish





wph_fish =  ph(acceptable_ph_upper) * 0.165
wdo_fish = do(acceptable_do_upper)* 0.281
wbdo_fish= bod(acceptable_bod_upper) * 0.234
wec_fish = conductivity(acceptable_conductivity_upper)* 0.009
wna_fish = nitrate(acceptable_nitrate_upper) * 0.028
wco_fish = totalcoliform(acceptable_totalcoli_upper) * 0.281

wqi_fish_upper_acceptable =wph_fish+wdo_fish+wbdo_fish+wec_fish+wna_fish+wco_fish



print("UPPER ACCEPTABLE WQI - ",wqi_fish_upper_acceptable)

print("LOWER ACCEPTABLE WQI - ",wqi_fish_lower_acceptable)




final_acceptable_wqi_fish = wqi_fish_upper_acceptable				### WQI final_desirable_Wqi_value is desirable-final_acceptable_Wqi_value is desirable water quality for fishes 	##########

