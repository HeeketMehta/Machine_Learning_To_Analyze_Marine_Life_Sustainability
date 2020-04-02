import pandas as pd
import numpy as np

################################################################# PROCESSING THE FILE AND CONVERTING DTYPES ###################################################
df = pd.read_csv(r"waterData1.csv",encoding="ISO-8859-1")

df['Temp'] = pd.to_numeric(df['Temp'], errors = 'coerce')
df['B.O.D. (mg/l)'] = pd.to_numeric(df['B.O.D. (mg/l)'], errors = 'coerce')
df['NITRATENaN N+ NITRITENaNN (mg/l)'] = pd.to_numeric(df['NITRATENaN N+ NITRITENaNN (mg/l)'], errors = 'coerce')
df['TOTAL COLIFORM (MPN/100ml)Mean'] = pd.to_numeric(df['TOTAL COLIFORM (MPN/100ml)Mean'], errors = 'coerce')
df['FECAL COLIFORM (MPN/100ml)'] = pd.to_numeric(df['FECAL COLIFORM (MPN/100ml)'], errors = 'coerce')


# print(df.dtypes)


df.fillna(0, inplace = True)



# print(df.dtypes)
df.drop(df.index[262], inplace=True)
df.drop(df.index[433], inplace=True)
df.drop(df.index[1914], inplace=True)

df.drop(['STATION CODE'], axis=1, inplace = True)


# print(df.columns)




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
	# print("SUM OF ", attr, "is equal to ",sum_avg)

	print("Mean OF ",attr," is  ",mean_attr)



	# print(mean1)
	for i in df[attr]:
		if i == 0.0 :
			df[attr].replace(0, round(mean_attr,2), inplace = True)
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






# 	for i in df[attr]:
# 		if i == 0.0 :
# 			df[attr].replace(0, round(mean_attr,2), inplace = True)
# 		else:
# 			pass



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

###########################################################################    FOR CLEANING FECAL COLIFORM (MPN/100ml)    ####################################################



clean_data_with_median(df, 'FECAL COLIFORM (MPN/100ml)')


##########################################################################################################################################################

###########################################################################    FOR CLEANING B.O.D. (mg/l)    ####################################################



clean_data_with_mean(df, 'B.O.D. (mg/l)')


##########################################################################################################################################################

###########################################################################    FOR CLEANING TOTAL COLIFORM (MPN/100ml)Mean    ####################################################



clean_data_with_median(df, 'TOTAL COLIFORM (MPN/100ml)Mean')


##########################################################################################################################################################

df.to_csv('ayushi.csv')



########################################################################################################################################################################