import pandas as pd
import numpy as np

################################################################# PROCESSING THE FILE AND CONVERTING DTYPES ###################################################
df = pd.read_csv(r"datasets/waterData1.csv",encoding="ISO-8859-1")

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
df.drop(['FECAL COLIFORM (MPN/100ml)'], axis=1, inplace = True)



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






	for i in df[attr]:
		if i == 0.0 :
			df[attr].replace(0, round(median_value,2), inplace = True)
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





df.to_csv('datasets/cleaned_data_final.csv')

