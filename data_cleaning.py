import pandas as pd
import numpy as np














################################################################# PROCESSING THE FILE AND CONVERTING DTYPES ###################################################
df = pd.read_csv(r"datasets/waterData1.csv",encoding="ISO-8859-1")



###########	CONVERTING OBJECT DTYPE INTO FLOAT64 	############

df['Temp'] = pd.to_numeric(df['Temp'], errors = 'coerce')
df['B.O.D. (mg/l)'] = pd.to_numeric(df['B.O.D. (mg/l)'], errors = 'coerce')
df['NITRATENaN N+ NITRITENaNN (mg/l)'] = pd.to_numeric(df['NITRATENaN N+ NITRITENaNN (mg/l)'], errors = 'coerce')
df['TOTAL COLIFORM (MPN/100ml)Mean'] = pd.to_numeric(df['TOTAL COLIFORM (MPN/100ml)Mean'], errors = 'coerce')
df['FECAL COLIFORM (MPN/100ml)'] = pd.to_numeric(df['FECAL COLIFORM (MPN/100ml)'], errors = 'coerce')


# print(df.dtypes)


df.fillna(0, inplace = True)   # REPLACING ALL NAN VALUES WITH 0



# print(df.dtypes)
df.drop(df.index[262], inplace=True)  ####	DROPPING ROWS WITH ALL NAN VALUES ######
df.drop(df.index[433], inplace=True)
df.drop(df.index[1914], inplace=True)

df.drop(['STATION CODE'], axis=1, inplace = True)		####  DROPPING STATION CODE AS IT IS NOT RELEVANT INFO #######


# print(df.columns)
df.drop(['FECAL COLIFORM (MPN/100ml)'], axis=1, inplace = True)        ####  DROPPING FECAL COLI AS IT IS INCLUDED IN THE TOTAL COLI FIELD  #######



################################################	    DATA CLEANING AND MINING 		############################################################




#################################################################################################################

def clean_data_with_mean(df, attr):
	list_of_all_attr = []
	sum_avg = 0
	c = 0
	for i in df[attr]:
		list_of_all_attr.append(i)
		if i == 0.0 :
			pass
		else :
			sum_avg = sum_avg + i
			c = c + 1


	mean_attr = sum_avg/c

	print("Mean OF ",attr," is  ",mean_attr)



	# print(mean1)
	for i in df[attr]:
		if i == 0.0 :
			df[attr].replace(0, round(mean_attr,2), inplace = True)  ### REPLACING ALL ZEROES WITH THE MEAN VALUES #######
		else:
			pass





def clean_data_with_median(df, attr):
	list_of_all_attr = []
	n = len(df[attr])
	
	median_index = int(n/2)
	for i in df[attr]:
		list_of_all_attr.append(i)

	list_of_all_attr.sort()

	# print(median_index)
	median_value = list_of_all_attr[median_index]

	print("MEDIAN OF ",attr," is  =  ",median_value)






	for i in df[attr]:
		if i == 0.0 :
			df[attr].replace(0, round(median_value,2), inplace = True)	### REPLACING ALL ZEROES WITH THE MEDIAN VALUES #######
		else:
			pass



# print(df.dtypes)


########################################################################### FOR CLEANING TEMPERATURE ####################################################



clean_data_with_mean(df, 'Temp')

##########################################################################################################################################################



###########################################################################    FOR CLEANING D.O. (mg/l)    ####################################################



clean_data_with_mean(df, 'D.O. (mg/l)')


##########################################################################################################################################################




###########################################################################    FOR CLEANING PH    ####################################################


clean_data_with_median(df, 'PH')


##########################################################################################################################################################



###########################################################################    FOR CLEANING CONDUCTIVITY (µmhos/cm)    ####################################################



clean_data_with_median(df, 'CONDUCTIVITY (µmhos/cm)')


##########################################################################################################################################################

###########################################################################    FOR CLEANING NITRATENaN N+ NITRITENaNN (mg/l)    ####################################################



clean_data_with_mean(df, 'NITRATENaN N+ NITRITENaNN (mg/l)')


##########################################################################################################################################################





###########################################################################    FOR CLEANING B.O.D. (mg/l)    ####################################################



clean_data_with_mean(df, 'B.O.D. (mg/l)')


##########################################################################################################################################################

###########################################################################    FOR CLEANING TOTAL COLIFORM (MPN/100ml)Mean    ####################################################



clean_data_with_median(df, 'TOTAL COLIFORM (MPN/100ml)Mean')


##########################################################################################################################################################


########################################################################################################################################################################













#############################################	 NORMALIZATION 	#############################################

#####finding wqi acc to wqi grading paper ###############







#calulation of Ph
df['npH']=df.PH.apply(lambda x: (100 if (8.5>=x>=7)  
									else(80 if  (8.6>=x>=8.5) or (6.9>=x>=6.8) 
									else(60 if (8.8>=x>=8.6) or (6.8>=x>=6.7) 
									else(40 if (9>=x>=8.8) or (6.7>=x>=6.5)
									else 0)))))



df['nD.O. (mg/l)']=df['D.O. (mg/l)'].apply(lambda x:(100 if (x>=6)
									else(80 if  (6>=x>=5.1) 
									else(60 if (5>=x>=4.1)
									else(40 if (4>=x>=3) 
									else 0)))))



#calculation of total coliform
df['nTOTAL COLIFORM (MPN/100ml)Mean']=df['TOTAL COLIFORM (MPN/100ml)Mean'].apply(lambda x:(100 if (5>=x>=0)  
								else(80 if  (50>=x>=5) 
								else(60 if (500>=x>=50)
								else(40 if (10000>=x>=500) 
								else 0)))))




df['nB.O.D. (mg/l)']=df['B.O.D. (mg/l)'].apply(lambda x:(100 if (3>=x>=0)  
									else(80 if  (6>=x>=3) 
									else(60 if (80>=x>=6)
									else(40 if (125>=x>=80) 
									else 0)))))


df['nCONDUCTIVITY (µmhos/cm)']=df['CONDUCTIVITY (µmhos/cm)'].apply(lambda x:(100 if (75>=x>=0)  
									else(80 if  (150>=x>=75) 
									else(60 if (225>=x>=150)
									else(40 if (300>=x>=225) 
									else 0)))))





df['nNITRATENaN N+ NITRITENaNN (mg/l)']=df['NITRATENaN N+ NITRITENaNN (mg/l)'].apply(lambda x:(100 if (20>=x>=0)  
										else(80 if  (50>=x>=20) 
										else(60 if (100>=x>=50)
										else(40 if (200>=x>=100) 
										else 0)))))




df['wph']=df.npH * 0.165
df['wdo']=df['nD.O. (mg/l)'] * 0.281
df['wbdo']=df['nB.O.D. (mg/l)'] * 0.234
df['wec']=df['nCONDUCTIVITY (µmhos/cm)']* 0.009
df['wna']=df['nNITRATENaN N+ NITRITENaNN (mg/l)'] * 0.028
df['wco']=df['nTOTAL COLIFORM (MPN/100ml)Mean'] * 0.281



df['wqi']=df.wph+df.wdo+df.wbdo+df.wec+df.wna+df.wco 

print()
print("LEGEND FOR THE WQI IS - ")
print("1 - excellent quality")
print("2 - good quality")
print("3 - poor quality")
print("4 - very poor quality")
print("5 - unsuitable quality")







df['new_WQI']=df['wqi'].apply(lambda x:(1 if (100>=x>90)  
										else(2 if  (90>=x>70) 
										else(3 if (70>=x>50)
										else(4 if (50>=x>25) 
										else 5)))))






















#####################################			FOR FISH ANALYSIS BASED ON WQI TO ADD A NEW WQI TARGET 		#########################

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



# print("UPPER DESIRABLE WQI - ",wqi_fish_upper_desirable)

# print("LOWER DESIRABLE WQI - ",wqi_fish_lower_desirable)




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



# print("UPPER ACCEPTABLE WQI - ",wqi_fish_upper_acceptable)

# print("LOWER ACCEPTABLE WQI - ",wqi_fish_lower_acceptable)




final_acceptable_wqi_fish = wqi_fish_upper_acceptable				### WQI final_desirable_Wqi_value is desirable-final_acceptable_Wqi_value is desirable water quality for fishes 	##########







df['new_WQI_fishes']=df['wqi'].apply(lambda x:(1 if (100>=x>final_Desirable_wqi_fish)  
										else(2 if  (final_Desirable_wqi_fish>=x>final_acceptable_wqi_fish) 
										else 3)))







df.to_csv('datasets/cleaned_data_final.csv')

